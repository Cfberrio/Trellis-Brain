# Workflow 01 — Plan de Implementación

> **Para ejecutores agénticos:** SUB-SKILL REQUERIDA: usar `superpowers:subagent-driven-development` (recomendada) o `superpowers:executing-plans` para implementar tarea por tarea. Los pasos usan checkbox (`- [ ]`) para tracking.

**Goal:** Sincronizar el estado del booking de D'Space a un pipeline de GHL (crear contacto + oportunidad, mover de etapa en etapa) y automatizar las transiciones de estado por tiempo, con Supabase como fuente de verdad.

**Architecture:** Supabase es dueño del estado (`bookings.event_status`). Un trigger en `bookings` notifica a GHL en cada cambio relevante vía `pg_net` → edge function `sync-to-ghl` → POST al **inbound webhook** de GHL (un workflow de GHL crea/mueve la oportunidad). Las transiciones por tiempo (`in_progress`, `post_event`, `closed`) viven en `scheduled_jobs` y las ejecuta una función SQL disparada por `pg_cron` cada 5 min. El admin-confirm (`pending→confirmed`) ya existe en el dashboard; solo se engancha al trigger.

**Tech Stack:** Supabase (Postgres 15, plpgsql, `pg_cron`, `pg_net`), Deno Edge Functions (TypeScript), GoHighLevel (pipeline + inbound webhook workflow). Repo: `/Users/cberrio04/Documents/D-space`. Project ref: `okplwpfchbogamvhebyc`.

**Specs base:** [[Workflow-01-Pipeline-y-Estados]] · [[00-GHL-Custom-Fields-y-Values]] · [[00-Comms-Matrix]] · hub [[Arquitectura-Estados-y-Automatizacion]].

---

## Mapa de archivos

| Archivo | Crea/Modifica | Responsabilidad |
|---|---|---|
| `supabase/migrations/<ts>_wf1_extensions.sql` | Crear | Habilita `pg_cron` + `pg_net` |
| `supabase/migrations/<ts>_wf1_automation_config.sql` | Crear | Tabla `automation_config` (URL función + secreto) |
| `supabase/migrations/<ts>_wf1_ghl_notify.sql` | Crear | Trigger `notify_ghl_booking_change` (booking → pg_net → edge) |
| `supabase/migrations/<ts>_wf1_state_scheduler.sql` | Crear | `schedule_booking_state_jobs()` + trigger on confirmed |
| `supabase/migrations/<ts>_wf1_state_dispatcher.sql` | Crear | `run_due_state_jobs()` + `cron.schedule` cada 5 min |
| `supabase/functions/sync-to-ghl/index.ts` | Crear | Lee booking, arma payload, POST al inbound webhook GHL |
| `supabase/config.toml` | Modificar | `verify_jwt = false` para `sync-to-ghl` |

> `<ts>` = timestamp UTC actual al crear el archivo (formato existente `YYYYMMDDHHMMSS_...`). Las migraciones se aplican por el flujo de Lovable/Supabase.

---

## Fase A — Setup manual en GHL (sub-account D'Space)

Hacer en la UI de GHL **antes** del código. Detalle de campos en [[00-GHL-Custom-Fields-y-Values]].

- [ ] **A1.** Crear pipeline "D'Space Bookings" con etapas: Under Review · Confirmed · Pre-Event Ready · In Progress · Post-Event · Closed (Won) · Cancelled (Lost).
- [ ] **A2.** Crear los custom fields de contacto (§3 del doc de fundación): `reservation_number`, `booking_status`, `payment_status`, `event_date`, `event_start`, `event_end`, `guest_count`, `total_amount`, `deposit_amount`, `balance_amount`, `amount_paid`, `balance_payment_url`, `balance_link_expires_at`, `guest_reminder_step`, `access_instructions`, `service_tier`, `space_name`.
- [ ] **A3.** Crear el workflow GHL "WF1 — Pipeline y Estados":
  - Trigger: **Inbound Webhook**.
  - Paso 1: **Upsert Contact** (por email/phone) y setear los custom fields desde el payload.
  - Paso 2: **Create/Update Opportunity** en pipeline "D'Space Bookings". Mapear etapa desde `{{inboundWebhookRequest.event_status}}`: `pending→Under Review`, `confirmed→Confirmed`, `pre_event_ready→Pre-Event Ready`, `in_progress→In Progress`, `post_event→Post-Event`, `closed→Closed (Won)`, `cancelled→Cancelled (Lost)`. Buscar la oportunidad por `reservation_number` para no duplicar.
- [ ] **A4.** Guardar el workflow, **copiar el Inbound Webhook URL**. Mandarlo enviar un POST de prueba para que GHL mapee el sample payload (usar el JSON de §2 de [[Workflow-01-Pipeline-y-Estados]]).
- [ ] **A5.** Anotar el URL → se usa como secret `GHL_WF1_WEBHOOK_URL` en Fase D.

**Verificación A:** mandar manualmente (Postman/curl) el sample payload al webhook URL → aparece un contacto + una oportunidad en "Under Review" en el pipeline.

---

## Fase B — Extensiones Supabase

### Task B1: Habilitar pg_cron + pg_net

**Files:** Create `supabase/migrations/<ts>_wf1_extensions.sql`

- [ ] **Paso 1: Escribir la migración**

```sql
-- WF1: extensiones para automatización.
-- pg_cron: corre las transiciones de estado por tiempo cada 5 min.
-- pg_net: permite que un trigger llame a una edge function vía HTTP.
create extension if not exists pg_cron;
create extension if not exists pg_net;
```

- [ ] **Paso 2: Aplicar** (vía Lovable/Supabase). Si `create extension` está restringido, habilitar `pg_cron` y `pg_net` en Dashboard → Database → Extensions.

- [ ] **Paso 3: Verificar**

```sql
select extname from pg_extension where extname in ('pg_cron','pg_net');
-- Esperado: 2 filas (pg_cron, pg_net)
```

- [ ] **Paso 4: Commit**

```bash
git add supabase/migrations/*_wf1_extensions.sql
git commit -m "feat(wf1): enable pg_cron and pg_net extensions"
```

---

## Fase C — Notificación a GHL (trigger → edge)

### Task C1: Tabla de config

**Files:** Create `supabase/migrations/<ts>_wf1_automation_config.sql`

- [ ] **Paso 1: Escribir la migración**

```sql
-- WF1: config de automatización (URL de la edge function + secreto compartido).
-- Por-venue: al duplicar, cambiar estos valores.
create table if not exists automation_config (
  key   text primary key,
  value text not null
);

insert into automation_config (key, value) values
  ('sync_to_ghl_url', 'https://okplwpfchbogamvhebyc.supabase.co/functions/v1/sync-to-ghl'),
  ('automation_secret', 'CHANGE_ME_RANDOM_64_HEX')   -- generar y reemplazar
on conflict (key) do nothing;

alter table automation_config enable row level security;  -- sin políticas: solo service_role / definer
```

- [ ] **Paso 2:** Reemplazar `CHANGE_ME_RANDOM_64_HEX` por un secreto aleatorio (ej. `openssl rand -hex 32`). Guardar el mismo valor para el env `AUTOMATION_SECRET` (Task D2).

- [ ] **Paso 3: Verificar**

```sql
select key from automation_config order by key;
-- Esperado: automation_secret, sync_to_ghl_url
```

- [ ] **Paso 4: Commit**

```bash
git add supabase/migrations/*_wf1_automation_config.sql
git commit -m "feat(wf1): automation_config table for sync url + secret"
```

### Task C2: Trigger que notifica a GHL

**Files:** Create `supabase/migrations/<ts>_wf1_ghl_notify.sql`

- [ ] **Paso 1: Escribir la migración**

```sql
-- WF1: en cada cambio relevante del booking, notificar a GHL (vía edge function).
-- Dispara en: INSERT con depósito pagado (entra "under review"), cambio de event_status,
-- o cambio de payment_status a deposit_paid/fully_paid.
create or replace function notify_ghl_booking_change()
returns trigger
language plpgsql
security definer
as $$
declare
  v_url    text;
  v_secret text;
  v_fire   boolean := false;
begin
  if (tg_op = 'INSERT') then
    v_fire := (new.payment_status = 'deposit_paid');
  elsif (tg_op = 'UPDATE') then
    v_fire := (new.event_status is distinct from old.event_status)
           or (new.payment_status is distinct from old.payment_status
               and new.payment_status in ('deposit_paid','fully_paid'));
  end if;

  if not v_fire then
    return new;
  end if;

  select value into v_url    from automation_config where key = 'sync_to_ghl_url';
  select value into v_secret from automation_config where key = 'automation_secret';

  perform net.http_post(
    url     := v_url,
    headers := jsonb_build_object(
                 'Content-Type', 'application/json',
                 'x-automation-secret', v_secret),
    body    := jsonb_build_object('booking_id', new.id)
  );

  return new;
end;
$$;

drop trigger if exists trg_notify_ghl_booking on bookings;
create trigger trg_notify_ghl_booking
  after insert or update on bookings
  for each row execute function notify_ghl_booking_change();
```

- [ ] **Paso 2: Verificar** (después de desplegar la función en Fase D — el trigger ya queda activo; aquí solo confirmar que existe)

```sql
select tgname from pg_trigger where tgname = 'trg_notify_ghl_booking';
-- Esperado: 1 fila
```

- [ ] **Paso 3: Commit**

```bash
git add supabase/migrations/*_wf1_ghl_notify.sql
git commit -m "feat(wf1): trigger notify GHL on booking state/payment change"
```

---

## Fase D — Edge function sync-to-ghl

### Task D1: La función

**Files:** Create `supabase/functions/sync-to-ghl/index.ts`

- [ ] **Paso 1: Escribir la función**

```ts
// sync-to-ghl — recibe { booking_id }, arma el payload del booking y lo
// envía al Inbound Webhook de GHL (WF1). GHL crea/mueve la oportunidad.
// Llamada por el trigger de la DB (pg_net) con header x-automation-secret.
// Env (Lovable Cloud secrets):
//   GHL_WF1_WEBHOOK_URL  — inbound webhook URL del workflow WF1
//   AUTOMATION_SECRET    — debe igualar automation_config.automation_secret
//   SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY — auto-inyectados en el runtime
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, content-type, x-automation-secret",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...cors, "Content-Type": "application/json" },
  });
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return json({ error: "method_not_allowed" }, 405);

  if (req.headers.get("x-automation-secret") !== Deno.env.get("AUTOMATION_SECRET")) {
    return json({ error: "unauthorized" }, 401);
  }

  const webhookUrl = Deno.env.get("GHL_WF1_WEBHOOK_URL");
  if (!webhookUrl) return json({ error: "server_misconfigured" }, 500);

  let body: { booking_id?: string };
  try { body = await req.json(); } catch { return json({ error: "invalid_json" }, 400); }
  if (!body.booking_id) return json({ error: "booking_id_required" }, 400);

  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
  );

  const { data: b, error } = await supabase
    .from("bookings")
    .select(
      "id, reservation_number, event_status, payment_status, event_date, total_amount, deposit_amount, balance_amount, amount_paid, number_of_guests, service_tier, customers ( full_name, email, phone )",
    )
    .eq("id", body.booking_id)
    .single();
  if (error || !b) return json({ error: "booking_not_found", detail: error }, 404);

  const { data: spaces } = await supabase
    .from("booking_spaces")
    .select("space_id, start_time, end_time")
    .eq("booking_id", body.booking_id);

  const starts = (spaces ?? []).map((s) => s.start_time).sort();
  const ends = (spaces ?? []).map((s) => s.end_time).sort();
  // Hora local de Orlando con offset DST-correcto (EST -05:00 / EDT -04:00),
  // resuelto por fecha vía America/New_York. Devuelve "YYYY-MM-DDThh:mm:ss±hh:mm".
  const orlandoOffset = (date: string, time: string): string => {
    const probe = new Date(`${date}T${time}Z`);
    const parts = new Intl.DateTimeFormat("en-US", {
      timeZone: "America/New_York", hour12: false,
      year: "numeric", month: "2-digit", day: "2-digit",
      hour: "2-digit", minute: "2-digit", second: "2-digit",
    }).formatToParts(probe).reduce<Record<string, string>>(
      (m, p) => (p.type !== "literal" ? ((m[p.type] = p.value), m) : m), {});
    const asUTC = Date.UTC(+parts.year, +parts.month - 1, +parts.day, +parts.hour, +parts.minute, +parts.second);
    const offMin = Math.round((asUTC - probe.getTime()) / 60000);
    const sign = offMin <= 0 ? "-" : "+";
    const abs = Math.abs(offMin);
    const hh = String(Math.floor(abs / 60)).padStart(2, "0");
    const mm = String(abs % 60).padStart(2, "0");
    return `${sign}${hh}:${mm}`;
  };
  const eventStart = starts.length ? `${b.event_date}T${starts[0]}${orlandoOffset(b.event_date, starts[0])}` : null;
  const eventEnd = ends.length ? `${b.event_date}T${ends[ends.length - 1]}${orlandoOffset(b.event_date, ends[ends.length - 1])}` : null;

  const customer = (b as Record<string, any>).customers ?? {};
  const fullName = (customer.full_name ?? "").trim();
  const [firstName, ...rest] = fullName.split(/\s+/);

  const payload = {
    reservation_number: b.reservation_number,
    event_status: b.event_status,
    payment_status: b.payment_status,
    email: customer.email,
    phone: customer.phone,
    first_name: firstName || undefined,
    last_name: rest.join(" ") || undefined,
    event_date: b.event_date,
    event_start: eventStart,
    event_end: eventEnd,
    total_amount: b.total_amount,
    deposit_amount: b.deposit_amount,
    balance_amount: b.balance_amount,
    amount_paid: b.amount_paid,
    guest_count: b.number_of_guests,
    service_tier: b.service_tier,
    space_name: (spaces ?? []).map((s) => s.space_id).join(", "),
  };

  const res = await fetch(webhookUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const detail = await res.text().catch(() => "");
    console.error("[sync-to-ghl] GHL webhook error", res.status, detail);
    return json({ error: "ghl_webhook_failed", status: res.status, detail }, 502);
  }

  console.info("[sync-to-ghl] synced", b.reservation_number, "→", b.event_status);
  return json({ ok: true });
});
```

- [ ] **Paso 2: Registrar en config.toml**

Modify `supabase/config.toml` — agregar:

```toml
# Llamada por el trigger de la DB (pg_net), no por un usuario: sin JWT.
# Se protege con el header x-automation-secret.
[functions.sync-to-ghl]
verify_jwt = false
```

- [ ] **Paso 3: Set secrets** (Lovable Cloud → secrets):

```
GHL_WF1_WEBHOOK_URL = <URL del paso A5>
AUTOMATION_SECRET   = <mismo valor que automation_config.automation_secret>
```

- [ ] **Paso 4: Desplegar** la función (flujo Lovable/Supabase).

- [ ] **Paso 5: Verificar (invoke directo)**

```bash
curl -i -X POST "https://okplwpfchbogamvhebyc.supabase.co/functions/v1/sync-to-ghl" \
  -H "Content-Type: application/json" \
  -H "x-automation-secret: <secret>" \
  -d '{"booking_id":"<un booking real>"}'
# Esperado: 200 {"ok":true} y la oportunidad aparece/mueve en GHL.
# Sin el header correcto: 401.
```

- [ ] **Paso 6: Commit**

```bash
git add supabase/functions/sync-to-ghl/index.ts supabase/config.toml
git commit -m "feat(wf1): sync-to-ghl edge function posts booking to GHL inbound webhook"
```

---

## Fase E — Transiciones por tiempo

### Task E1: Scheduler (agenda los jobs al confirmar)

**Files:** Create `supabase/migrations/<ts>_wf1_state_scheduler.sql`

- [ ] **Paso 1: Escribir la migración**

```sql
-- WF1: al confirmar un booking, agenda las transiciones por tiempo.
-- Ancla en hora Orlando (DST-correcto vía nombre de zona).
create or replace function schedule_booking_state_jobs(p_booking_id uuid)
returns void
language plpgsql
security definer
as $$
declare
  v_start timestamptz;
  v_end   timestamptz;
begin
  select (b.event_date + min(bs.start_time)) at time zone 'America/New_York',
         (b.event_date + max(bs.end_time))   at time zone 'America/New_York'
    into v_start, v_end
  from bookings b
  join booking_spaces bs on bs.booking_id = b.id
  where b.id = p_booking_id
  group by b.event_date;

  if v_start is null then
    return;  -- sin spaces: nada que agendar
  end if;

  insert into scheduled_jobs (booking_id, job_type, run_at, payload)
  select p_booking_id, j.job_type, j.run_at, '{}'::jsonb
  from (values
    ('set_in_progress', v_start),
    ('set_post_event',  v_end),
    ('set_closed',      v_end + interval '24 hours')   -- backstop 24h tras el fin (o antes si Guest Report — futuro). Ver [[Logica-de-Estados]]
  ) as j(job_type, run_at)
  where not exists (
    select 1 from scheduled_jobs s
    where s.booking_id = p_booking_id and s.job_type = j.job_type
  );
end;
$$;

create or replace function on_booking_confirmed()
returns trigger language plpgsql security definer as $$
begin
  if (new.event_status = 'confirmed' and old.event_status is distinct from 'confirmed') then
    perform schedule_booking_state_jobs(new.id);
  end if;
  return new;
end;
$$;

drop trigger if exists trg_booking_confirmed on bookings;
create trigger trg_booking_confirmed
  after update of event_status on bookings
  for each row execute function on_booking_confirmed();
```

- [ ] **Paso 2: Verificar** (confirmar un booking de prueba y ver 3 jobs)

```sql
-- tras mover un booking a 'confirmed':
select job_type, run_at, status from scheduled_jobs
where booking_id = '<booking>' order by run_at;
-- Esperado: set_in_progress, set_post_event, set_closed (pending)
```

- [ ] **Paso 3: Commit**

```bash
git add supabase/migrations/*_wf1_state_scheduler.sql
git commit -m "feat(wf1): schedule time-based state jobs on booking confirm"
```

### Task E2: Dispatcher + cron

**Files:** Create `supabase/migrations/<ts>_wf1_state_dispatcher.sql`

- [ ] **Paso 1: Escribir la migración**

```sql
-- WF1: ejecuta los jobs de estado vencidos. Cada update fija un guard
-- por el estado previo esperado (0 filas si no coincide = no transiciona).
create or replace function run_due_state_jobs()
returns void
language plpgsql
security definer
as $$
declare
  r record;
begin
  for r in
    select * from scheduled_jobs
    where status = 'pending' and run_at <= now() and attempts < 3
      and job_type in ('set_in_progress','set_post_event','set_closed')
    order by run_at
    limit 50
  loop
    begin
      update scheduled_jobs set attempts = attempts + 1 where id = r.id;

      if r.job_type = 'set_in_progress' then
        update bookings set event_status = 'in_progress'
          where id = r.booking_id and event_status = 'pre_event_ready';
      elsif r.job_type = 'set_post_event' then
        update bookings set event_status = 'post_event'
          where id = r.booking_id and event_status = 'in_progress';
      elsif r.job_type = 'set_closed' then
        update bookings set event_status = 'closed'
          where id = r.booking_id and event_status = 'post_event';
      end if;

      update scheduled_jobs set status = 'completed', completed_at = now() where id = r.id;
    exception when others then
      update scheduled_jobs set status = 'failed', last_error = sqlerrm where id = r.id;
    end;
  end loop;
end;
$$;

-- Cron cada 5 min (única forma real de agendar; NO usar config.toml).
select cron.schedule('process-state-jobs-5min', '*/5 * * * *', $$ select run_due_state_jobs(); $$);
```

- [ ] **Paso 2: Verificar (forzar un job)**

```sql
-- adelantar un job a pasado y correr el dispatcher a mano:
update scheduled_jobs set run_at = now() - interval '1 min'
where booking_id = '<booking pre_event_ready>' and job_type = 'set_in_progress';
select run_due_state_jobs();
select event_status from bookings where id = '<booking>';   -- Esperado: in_progress
select status from scheduled_jobs where booking_id='<booking>' and job_type='set_in_progress'; -- completed
-- y la oportunidad GHL se movió a In Progress (vía trigger notify).
select jobname, schedule from cron.job where jobname = 'process-state-jobs-5min'; -- 1 fila
```

- [ ] **Paso 3: Commit**

```bash
git add supabase/migrations/*_wf1_state_dispatcher.sql
git commit -m "feat(wf1): state job dispatcher + pg_cron every 5 min"
```

---

## Fase F — Wiring admin-confirm + prueba end-to-end

### Task F1: Confirmar que el admin-confirm escribe event_status='confirmed'

**Files:** Modify (si hace falta) la acción de confirmar del dashboard admin (ya existe — gate `pending→confirmed`).

- [ ] **Paso 1:** Localizar la mutación de confirmar (buscar en `src/lib/admin/` el update a `event_status='confirmed'`). Confirmar que escribe ese valor. **No requiere cambio de código** si ya lo hace — el trigger `trg_notify_ghl_booking` + `trg_booking_confirmed` se enganchan solos.
- [ ] **Paso 2: Verificar** que existe y apunta a `event_status='confirmed'`.

### Task F2: Prueba end-to-end

- [ ] **Paso 1:** Crear un booking de prueba con depósito (usar `create_booking` con `p_simulate_payment = true`) → `payment_status='deposit_paid'`, `event_status='pending'`.
- [ ] **Paso 2:** Verificar en GHL: contacto + oportunidad en **Under Review**.
- [ ] **Paso 3:** Confirmar el booking desde el dashboard → GHL oportunidad → **Confirmed**; aparecen 3 jobs en `scheduled_jobs`.
- [ ] **Paso 4:** Pasar a `pre_event_ready` (esto lo hará automático la edge function de **Stripe** al cobrar el balance: `payment_status='fully_paid'` + `event_status='pre_event_ready'`). Mientras Stripe no esté conectado, simularlo a mano con un UPDATE → GHL → **Pre-Event Ready**.
- [ ] **Paso 5:** Forzar `set_in_progress` (Task E2) → GHL → **In Progress**. Repetir para `set_post_event` y `set_closed`.
- [ ] **Paso 6: Commit** (si hubo ajuste de wiring)

```bash
git commit -am "test(wf1): end-to-end state sync verified"
```

---

## Items abiertos (resolver durante ejecución)

- Nombres de `job_type` definidos: `set_in_progress`, `set_post_event`, `set_closed`. (Confirmar OK.)
- `set_closed` a `end + 24h` (backstop). Futuro: cerrar antes si el cliente llena el **Guest Report**. Ver [[Logica-de-Estados]].
- **`confirmed → pre_event_ready` = responsabilidad de Stripe (futuro).** La cadena por tiempo arranca en `pre_event_ready`. Hoy nada lo dispara → la edge function de Stripe (al cobrar el balance) seteará `fully_paid` + `pre_event_ready`. Hasta conectar Stripe, los bookings se quedan en `confirmed` y la cadena no avanza sola (esperado).
- Edge case: el evento empieza sin pagar el balance (sigue `confirmed`). `set_in_progress` (guard `pre_event_ready`) corre una vez a la hora de inicio, no matchea (0 filas) y se marca `completed` → ese job queda quemado. Si el balance se paga después, ya no auto-avanza; resolver con admin. Comportamiento aceptado en v1.
- **Bookings internal/external** (creados ya `confirmed` por INSERT) NO entran en la cadena de tiempo: `trg_booking_confirmed` es `after update` a propósito. Correcto/por diseño.
- Hardening: el header `x-automation-secret` protege `sync-to-ghl`. Considerar rotación del secreto.
- DST: `event_start/event_end` del payload ahora usan offset DST-correcto (`America/New_York`) calculado por fecha en la edge function. Ya no hay caveat.

---

## Self-review (cobertura vs spec)

- Crear contacto + oportunidad → Fase A (workflow GHL) + `sync-to-ghl` (D1). ✓
- Mover de estado en estado → trigger notify (C2) + dispatcher (E2) + mapeo de etapas (A3). ✓
- Entra en `pending`/Under Review → trigger fire on INSERT con `deposit_paid` (C2). ✓
- Admin-confirm `pending→confirmed` → F1 + trigger. ✓
- Transiciones por tiempo → scheduler (E1) + dispatcher + cron (E2). ✓
- Fuente de verdad Supabase, GHL espejo → sí (estado se computa en DB; GHL recibe). ✓
- Sin lógica atada a staff/reportes → sí (solo tiempo + pago + admin-confirm). ✓

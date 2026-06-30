# Workflow 01 · Pipeline y Estados

> **Propósito:** mantener el pipeline de GHL espejeando el estado real del booking, y crear contacto + oportunidad. Es el workflow central: recibe cada cambio de estado vía **inbound webhook** y mueve la oportunidad de etapa en etapa dentro de un mismo pipeline.
>
> Depende de: [[00-GHL-Custom-Fields-y-Values]]. Hub: [[Arquitectura-Estados-y-Automatizacion]].

**Estado:** spec. Fuente de verdad = Supabase/pg_cron. GHL = espejo.

---

## 1. Máquina de estados (enums reales)

Eje `event_status`: `pending → confirmed → pre_event_ready → in_progress → post_event → closed` (+ `cancelled`).
Eje `payment_status`: `pending → deposit_paid → fully_paid`.

| # | Transición (event_status) | Disparador | Tipo | Dónde se computa |
|---|---|---|---|---|
| 1 | `pending → confirmed` | Admin confirma (checklist + aceptar) | **Humano** | Website (admin) |
| 2 | `confirmed → pre_event_ready` | Balance pagado → `payment_status = fully_paid` | **Pago** | Trigger DB on `booking_payments` |
| 3 | `pre_event_ready → in_progress` | Hora de inicio del evento | **Tiempo** | pg_cron + `scheduled_jobs` |
| 4 | `in_progress → post_event` | Hora de fin del evento | **Tiempo** | pg_cron |
| 5 | `post_event → closed` | ~2–3 días después del fin | **Tiempo** | pg_cron |

- `cancelled` desde cualquier estado (admin) → oportunidad GHL status = lost.
- **NADA de lógica atada a funciones** (ni aceptación de staff, ni reportes). Solo tiempo + el paso humano + el evento de pago.
- Anclajes de tiempo: inicio = `event_date` + menor `booking_spaces.start_time` (daily → 10 AM Orlando default). Fin = `event_date` + mayor `end_time`.

---

## 2. Flujo outbound (Supabase → GHL)

```
event_status cambia (trigger DB / cron / admin)
        │
        ▼
  edge function "sync-to-ghl" (MUST-BUILD)
        │  POST → inbound webhook URL de WF1
        ▼
  GHL Workflow 01 (trigger: Inbound Webhook):
    1. Upsert Contact (por email/phone) + setear custom fields
    2. ¿Existe oportunidad para este reservation_number?
         no → Create Opportunity (pipeline "D'Space Bookings", etapa mapeada)
         sí → Update Opportunity → mover a etapa mapeada
    3. (los comms de pago 01/03 NO van aquí — los manda Supabase con PDF)
```

> La señal de estado viaja en el payload **y** se persiste en el custom field `booking_status`. GHL no calcula el estado; solo lo refleja.

### Payload mínimo (POST a WF1)

```json
{
  "reservation_number": "...",
  "event_status": "confirmed",
  "payment_status": "deposit_paid",
  "email": "...", "phone": "...", "first_name": "...", "last_name": "...",
  "event_date": "2026-07-15",
  "event_start": "2026-07-15T18:00:00-05:00",
  "event_end": "2026-07-15T23:00:00-05:00",
  "total_amount": 0, "deposit_amount": 0, "balance_amount": 0, "amount_paid": 0,
  "guest_count": 0, "service_tier": "attended", "space_name": "..."
}
```

### Mapeo etapa (event_status → etapa GHL)

Ver tabla en [[00-GHL-Custom-Fields-y-Values]] §2.

---

## 3. Bidireccional (limitado)

Único movimiento manual permitido en GHL = el paso **admin-confirm**. Dos opciones (elegir en el chat de este WF):
- **(A) Website:** admin confirma en el dashboard → website escribe `confirmed` → outbound a GHL. (Más simple, recomendado.)
- **(B) GHL:** admin arrastra la card a *Confirmed* → trigger "Pipeline Stage Changed" → **Custom Webhook (Premium)** → endpoint Supabase `ghl-update-booking-status` (MUST-BUILD) valida y escribe `confirmed`.

El resto del pipeline = **lectura**. No permitir movidas manuales libres (race conditions vs pg_cron).

---

## 4. MUST-BUILD (Supabase)

- [ ] Extensión `pg_cron` + `cron.schedule()` para el dispatcher.
- [ ] Dispatcher `process-scheduled-jobs` (cada 5 min): lee `scheduled_jobs` pending con `run_at <= now()`, ejecuta por `job_type`, marca completed/failed (attempts < 3).
- [ ] Trigger DB: al pasar a `pre_event_ready` (o al crear el booking confirmado) → agenda los jobs de tiempo (`set_in_progress`, `set_post_event`, `set_closed`) anclados a inicio/fin/+2-3d.
- [ ] Trigger DB on `booking_payments` (balance succeeded) → `payment_status = fully_paid` → `event_status = confirmed→pre_event_ready`.
- [ ] Edge function `sync-to-ghl`: arma payload + POST al inbound webhook de WF1. Reutiliza `GHL_PRIVATE_INTEGRATION_TOKEN` / `GHL_LOCATION_ID` si hace upsert por API en vez de (o además de) webhook.
- [ ] (Opción B) endpoint `ghl-update-booking-status`.

`scheduled_jobs` ya existe (id, booking_id, job_type texto, run_at, status, attempts, last_error, payload jsonb, completed_at; índice `(status, run_at)`).

---

## 5. Items abiertos (resolver en el chat de WF1)

- Orden depósito vs confirm: ¿el booking entra `pending` + `deposit_paid` (under review) y luego admin confirma? ¿O admin confirma antes del depósito? El comms 01 ("50% received + under review") sugiere depósito primero.
- ¿La oportunidad se crea al crear el booking (`pending`) o al confirmar? Propuesta: crear en `pending` (Under Review) para verla desde el inicio.
- Confirmar nombres exactos de los `job_type` de tiempo.
- Opción A vs B para el admin-confirm.

---

## Actualización — decisiones (16-jun-2026)

Resuelve items abiertos de §5:

- **Ciclo de vida:** el booking **nace `pending` en el backend** (Supabase), con depósito 50% = "under review". **GHL NO se entera todavía.**
- El **admin aprueba manualmente** en el backend → `pending → confirmed`. **Ese evento** dispara el inbound webhook a GHL.
- En ese primer webhook, GHL **crea el contacto + la oportunidad directamente en la etapa `Confirmed`**; de ahí en adelante cada cambio de estado mueve la oportunidad.
- `pending` vive **solo en backend** → no hay etapa GHL para `pending`; la oportunidad arranca en `Confirmed`. (Etapa "Under Review" del pipeline = opcional/no usada.)
- Admin-confirm = **Opción A** (aprueba en backend → Supabase manda la señal a GHL).

Sigue abierto: nombres exactos de los `job_type` de tiempo (`set_in_progress` / `set_post_event` / `set_closed`).

---

## Actualización 2 — entra en PENDING (16-jun-2026)

**Corrige la actualización anterior.** La oportunidad GHL **SÍ se crea en `pending` (etapa Under Review)**, no en Confirmed. Decisión: la visibilidad del embudo importa.

Flujo final:
- Booking entra `pending` + depósito 50% pagado (`deposit_paid`) → **primer webhook a GHL** → crea contacto + oportunidad en etapa **Under Review**.
- Admin aprueba en backend → `pending → confirmed` → webhook → mueve a **Confirmed**.
- Balance pagado → `fully_paid` + `pre_event_ready` → webhook → **Pre-Event Ready**.
- Tiempo → `in_progress` → `post_event` → `closed` (cada uno → webhook mueve etapa).

→ La etapa **Under Review SÍ se usa**. Plan de implementación: [[Workflow-01-Plan-Implementacion]].

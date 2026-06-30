# D'Space — Arquitectura de Estados y Automatización (Supabase + GHL)

> Documento de referencia y **lógica general del venue**. Define cómo cambian los estados de un booking, qué vive en la base de datos (Supabase) vs. en GoHighLevel (GHL), cómo entran/salen los webhooks, y cómo se duplica un venue. Es la guía para construir, mantener y replicar D'Space y futuros venues.
>
> Hermano de: el doc de OEV "Arquitectura de Webhooks y Cron Jobs". La **lógica es similar pero NO igual** — D'Space cambia el motor de transición a **tiempo** (no acción humana) y empuja todo lo visual/comms a GHL.

**Fecha:** 2026-06-16 · **Estado:** dirección aprobada, pendiente implementación.

---

## 0. Decisión en una línea

**Supabase/pg_cron es la fuente de verdad de los estados. GHL es el espejo visual (pipelines) + el motor de comunicación (SMS/email) + CRM.** Los webhooks conectan los dos: Supabase empuja cada cambio a GHL; GHL solo empuja de vuelta el único paso humano (admin confirma).

Por qué pg_cron es la verdad y no GHL:

1. **Anti doble-booking.** El guard `EXCLUDE` (multi-espacio) vive en Postgres. GHL no puede prevenir reservas chocadas. Si GHL fuera dueño del estado → reservas pisadas.
2. **Pagos / fees / PDF** ya viven en el website + Supabase (Stripe entra ahí). GHL no calcula fees ni genera el recibo.
3. **pg_cron es gratis, auditable e idempotente** (`scheduled_jobs`, health-check). Las acciones de webhook de GHL son **Premium y cobran por ejecución**.

GHL se usa al máximo donde brilla: pipelines visuales, SMS/email nativo, CRM de contactos, y **snapshots** para duplicar venues.

---

## 1. Modelo de estados (motor = TIEMPO)

Cambio clave vs. OEV: la transición principal **NO es acción humana, es tiempo**. Solo hay UNA interacción humana (admin confirma). La asignación/aceptación de staff es una función aparte y **NO bloquea** la lógica.

| # | Transición | Disparador | Tipo |
|---|------------|-----------|------|
| 1 | `pending → confirmed` | Admin confirma la reservación (checklist + aceptar) | **Humano** (único) |
| 2 | `confirmed → prevent` | Segundo pago (balance) realizado | **Pago** (Stripe→website) |
| 3 | `prevent → in_progress` | Hora de inicio del booking | **Tiempo** (pg_cron) |
| 4 | `in_progress → post_event` | Hora de fin del booking | **Tiempo** (pg_cron) |
| 5 | `post_event → archive` | ~2–3 días después del fin (llene reporte o no) | **Tiempo** (pg_cron) |

**Reglas duras:**

- La lógica de estados **no se ata a funciones** (ni a aceptación de staff, ni a llenado de reportes). Solo tiempo + el paso humano de confirmación + el evento de pago.
- **Staff:** admin asigna staff → al staff le llega un request que acepta. Esto es una función independiente; el booking avanza **aunque el staff no confirme**.
- **Reportes (host report) y feedback:** se piden por tiempo (correos), pero **no bloquean** el avance de estado. Si a los 2–3 días no hay reporte, igual pasa a `archive`.

---

## 2. Qué vive dónde

| Responsabilidad | Vive en | Detalle |
|---|---|---|
| Estado canónico del booking (`lifecycle_status`) | **Supabase** | fuente de verdad |
| Transiciones por tiempo | **Supabase** `pg_cron` + `scheduled_jobs` | motor cada 5 min |
| Guard anti doble-booking (`EXCLUDE`) | **Supabase/Postgres** | imposible en GHL |
| Pagos, link de balance, verificación, fees, PDF | **Website + Supabase + Stripe** | Stripe NO entra a GHL |
| Confirmación del admin (paso humano) | **Website (admin)** | dispara `pending→confirmed` |
| Pipeline visual (ver estados) | **GHL** | espejo de lectura |
| SMS / Email (reminders, post-event, confirmaciones) | **GHL** | comms 100% |
| Contactos / CRM | **GHL** | sync desde Supabase |
| Cadencia de comms por tiempo | **GHL Wait** | solo comms, NUNCA estado canónico |

---

## 3. Flujo de webhooks

### 3.1 Outbound — Supabase → GHL (en cada cambio de estado)

```
Supabase cambia lifecycle_status
        │
        ▼
  outbound webhook  → GHL Inbound Webhook Trigger (URL único por venue)
        │
        ▼
  GHL workflow:
     ├─ Create/Update Opportunity → mueve la oportunidad a la etapa del pipeline
     └─ Send SMS / Send Email (según el estado)
```

- El payload lleva `booking_id`, `lifecycle_status` nuevo, datos del contacto y del evento.
- En GHL, el workflow mapea esos datos y mueve la etapa + dispara comms.

### 3.2 Inbound — GHL → Supabase (SOLO el paso humano)

```
Admin mueve la card a "Confirmed" en el pipeline GHL  (o confirma en el website)
        │
        ▼
  GHL Trigger "Pipeline Stage Changed"
        │
        ▼
  GHL Custom Webhook (Premium) → endpoint Supabase (ghl-update-booking-status)
        │
        ▼
  Supabase valida enum + escribe lifecycle_status + log
```

> **Limitar el bidireccional al paso admin-confirm.** El resto del pipeline en GHL es **lectura**. Si se permiten movidas manuales libres en GHL, se crean race conditions contra pg_cron.

### 3.3 Pago (inbound al website, NO a GHL)

```
Cliente paga balance → Stripe webhook → Website/Supabase
        │  (deriva fee, persiste, genera PDF, idempotencia)
        ▼
  Supabase: confirmed → prevent  → (luego outbound webhook a GHL para mover etapa + email)
```

---

## 4. Capacidades de GHL confirmadas (investigación docs, 2026-06-16)

| Capacidad | Estado | Nota |
|---|---|---|
| **Inbound Webhook Trigger** | ✅ | URL único por workflow; POST/GET/PUT; mapea JSON. **Premium** |
| **Custom Webhook Action** (GHL→externo) | ✅ | POST/GET/PUT/DELETE, auth, headers; retry backoff exponencial. **Premium** |
| **Wait Action — por tiempo** | ✅ | fecha fija o dinámica (custom field); antes/en/después de appointment, **service booking**, **invoice due date**; recurrente; maneja "fecha ya pasó" |
| **Create/Update Opportunity** | ✅ | mueve a pipeline + stage específico; status open/won/lost |
| **Triggers de pipeline** | ✅ | Opportunity Created, Status Changed, **Pipeline Stage Changed**, Stale (X días sin cambio) |
| **Send SMS / Send Email** | ✅ | nativo |

**⚠️ Costo:** Inbound Webhook + Custom Webhook son **acciones Premium**. 100 ejecuciones gratis por sub-account, luego cobran/rebilling. Cada cambio de estado vía webhook consume una ejecución → con volumen, presupuéstalo.

**Por qué NO usar GHL Wait para el estado canónico:** aunque puede esperar hasta una fecha y mover la etapa, sería una segunda fuente de verdad (race conditions vs pg_cron), opaca para auditar, y cuesta ejecuciones. GHL Wait se usa **solo para la cadencia de comms** (secuencias de recordatorios).

---

## 5. Mapa de duplicación de un venue

Meta: clonar un venue completo rápido (escalabilidad). Combina dos lados.

### Lado GHL — Snapshot (ya tienes el sub-account duplicado)

**Snapshot incluye:** Workflows, Triggers, Pipelines, Funnels, Calendars, Forms, Emails, Custom Fields, **Custom Values**, Services, y más.
**NO incluye:** Contacts, Appointments, Conversations, **Stripe connections, integraciones**.
Reusable a N sub-accounts; tiene "Refresh/Update" y "Load into existing sub-account" para empujar cambios.

### Lado Supabase — clonar schema/migrations por venue.

### Checklist al duplicar un venue

1. Cargar snapshot GHL al nuevo sub-account. ✅ (ya hecho una vez)
2. Clonar el backend Supabase (migrations + edge functions + crons) para el venue.
3. **Re-mapear webhook URLs:** el inbound webhook URL de GHL **se regenera por location**. Guardar `venue → webhook_url` en el website/Supabase. NO es un URL global.
4. **Setear Custom Values** location-específicos en GHL: URL del edge function de Supabase, `venue_id`, backend token, etc.
5. **Reconectar Stripe** del venue en el website (no viaja en snapshot — pero como los pagos viven en el website, solo es el ruteo Stripe por venue).
6. Verificar que el `EXCLUDE` guard y los crons quedaron activos en la DB del venue.

---

## 6. Gotchas

- **Webhook URL único por workflow/location** → re-mapear por venue (ver §5.3).
- **Premium executions cuestan** → cada cambio de estado = 1 ejecución de webhook + comms.
- **Bidireccional solo para admin-confirm** → no permitir movidas manuales libres en el pipeline GHL.
- **`config.toml` NO corre crons** (lección heredada de OEV) → todo cron real va en una migración con `cron.schedule()`.
- **Idempotencia** en todo: correr dos veces no debe duplicar.

---

## 7. Pendientes de implementación

- [ ] Definir/escribir las 5 transiciones en `pg_cron` + `scheduled_jobs` (motor por tiempo).
- [ ] Endpoint outbound: Supabase → GHL en cada cambio de estado.
- [ ] Workflow GHL: Inbound Webhook → Create/Update Opportunity + comms.
- [ ] Workflow GHL: Pipeline Stage Changed (solo admin-confirm) → Custom Webhook → `ghl-update-booking-status`.
- [ ] Mapeo `venue → webhook_url` en website/Supabase.
- [ ] Función staff assignment + accept (independiente del estado).
- [ ] Secuencias de comms (reminders, balance, post-event, feedback) en GHL.
- [ ] Captura de foto de licencia al firmar.
- [ ] Probar duplicación end-to-end (snapshot + clonar Supabase + re-mapear).

---

## 8. Workflows — specs detallados

Cada workflow tiene su propio doc (para abrir un chat dedicado por cada uno). Fundación primero:

- **Fundación:** [[00-GHL-Custom-Fields-y-Values]] — campos/values a crear en GHL (está en blanco). Crear ESTO primero.
- **Fundación:** [[00-Comms-Matrix]] — los 8 pasos: qué/cuándo/canal/sender.
- [[Workflow-01-Pipeline-y-Estados]] — inbound webhook → contacto + oportunidad + mueve estados (máquina de 5 transiciones).
- [[Workflow-02-Remaining-Balance]] — cobro del balance (short/long notice).
- [[Workflow-03-Reminders]] — recordatorios al huésped (30d/7d/1d/1h + review).

**Decisiones (16-jun-2026):** layout = fundación + 1 por workflow · WF3 = recordatorios al huésped (no host report) · PDFs (pasos 01/03) los manda Supabase, resto GHL · mejoras = nombres de jobs claros + smart catch-up (DST no se corrige en v1).

**Schema real confirmado:** `event_status` (pending→confirmed→pre_event_ready→in_progress→post_event→closed) × `payment_status` (pending→deposit_paid→fully_paid). `scheduled_jobs` ya existe; pg_cron NO; solo `ghl-lead` cableado; sin Stripe live / sin email / sin sync saliente → todo eso es MUST-BUILD.

### Planes de implementación

- [[Workflow-01-Plan-Implementacion]] — plan tarea-por-tarea (GHL setup + pg_cron/pg_net + trigger + dispatcher + `sync-to-ghl`). Listo para ejecutar.
- [[Workflow-01-GHL-Setup-Guia]] — guía manual paso a paso de Fase A (custom fields, pipeline, workflow nodo-por-nodo). Grounded en docs GHL.

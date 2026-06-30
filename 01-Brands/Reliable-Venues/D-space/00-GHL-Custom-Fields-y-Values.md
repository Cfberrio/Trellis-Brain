# 00 · GHL Custom Fields y Values — Fundación

> **GHL está en blanco.** No hay custom fields ni custom values creados. Este doc es la **fundación**: define todo lo que hay que crear en GHL **primero**. Sin estos campos, ningún workflow (WF1/WF2/WF3) funciona.
>
> Hub: [[Arquitectura-Estados-y-Automatizacion]]. Lo crea el **dueño/admin en la UI de GHL** (sub-account de D'Space).

**Estado:** spec, pendiente crear en GHL.

---

## 1. Contexto técnico (schema real D'Space)

- Eje de estado: `bookings.event_status` = `pending → confirmed → pre_event_ready → in_progress → post_event → closed` (+ `cancelled`).
- Eje de pago: `bookings.payment_status` = `pending → deposit_paid → fully_paid` (+ `failed`, `refunded`, `invoiced`).
- Mapeo nombres del meeting → enums reales: **prevent = `pre_event_ready`**, **archive = `closed`**.
- Link de balance vive en `booking_payments.payment_url` (+ `link_expires_at`), kind `balance`. NO hay columna en `bookings`.
- Fecha: `bookings.event_date` (un día, Lun–Jue). Horas por espacio en `booking_spaces.start_time/end_time`.
- Integración GHL existente: solo `ghl-lead` (popup → contacto). Tokens ya configurados: `GHL_PRIVATE_INTEGRATION_TOKEN`, `GHL_LOCATION_ID`.

---

## 2. Pipeline + etapas (crear en GHL)

Un pipeline "D'Space Bookings" con etapas que **espejean** `event_status`:

| Etapa GHL | event_status | Notas |
|---|---|---|
| Under Review | `pending` | depósito recibido, espera confirmación admin |
| Confirmed | `confirmed` | admin confirmó |
| Pre-Event Ready | `pre_event_ready` | balance pagado (`fully_paid`) |
| In Progress | `in_progress` | evento en curso |
| Post-Event | `post_event` | evento terminó |
| Closed (Won) | `closed` | archivado |
| Cancelled (Lost) | `cancelled` | status oportunidad = lost |

> El movimiento de etapa lo maneja **WF1** vía inbound webhook. El pipeline es **espejo de lectura**; única movida manual permitida = paso admin-confirm (ver [[Workflow-01-Pipeline-y-Estados]]).

---

## 3. Custom Fields en CONTACTO (crear en GHL)

Campos que GHL necesita para mostrar el booking y para los comms/Wait steps. Keys propuestas en `snake_case` (se referencian como `{{ contact.<key> }}`).

| Campo (label) | key | Tipo | Lo usa |
|---|---|---|---|
| Reservation Number | `reservation_number` | Text | todos |
| Booking Status | `booking_status` | Text (espejo event_status) | WF1 |
| Payment Status | `payment_status` | Text | WF1, WF2 |
| Event Date | `event_date` | Date | WF2, WF3 |
| Event Start | `event_start` | Date/Time | WF3 (Wait 1d/1h) |
| Event End | `event_end` | Date/Time | WF3 (review 24h post) |
| Guest Count | `guest_count` | Number | comms |
| Total Amount | `total_amount` | Monetary | comms |
| Deposit Amount | `deposit_amount` | Monetary | comms |
| Balance Amount | `balance_amount` | Monetary | WF2 |
| Amount Paid | `amount_paid` | Monetary | comms |
| Balance Payment URL | `balance_payment_url` | Text/URL | **WF2** (señal de cobro) |
| Balance Link Expires | `balance_link_expires_at` | Date/Time | WF2 |
| Guest Reminder Step | `guest_reminder_step` | Text | **WF3** (señal de recordatorio) |
| Access Instructions | `access_instructions` | Large Text | comms paso 03/06 |
| Service Tier | `service_tier` | Text (self_serve/attended) | comms |
| Space / Venue | `space_name` | Text | comms |

> **`space_name` es multi-valor:** un booking puede tener varios espacios. La edge function `sync-to-ghl` envía los nombres legibles unidos por coma (ej. `"Main Conference, Breakout Room"`) — string, no array. Espacios (enum `space_id` → label): `main`→Main Conference · `mezzanine`→Mezzanine · `meeting`→Meeting Room · `breakout`→Breakout Room. Plantillas de comms: tratar `{{space_name}}` como texto que puede listar varios.

Estándar GHL (no crear): `email`, `phone`, `first_name`, `last_name`.

> **Señales clave:** `balance_payment_url` (WF2) y `guest_reminder_step` (WF3) son los campos que GHL **escucha** para disparar el outreach real. Cuando Supabase los actualiza vía sync, el workflow GHL correspondiente manda el email/SMS.

---

## 4. Custom Values a nivel LOCATION (crear en GHL)

Valores fijos del sub-account (se referencian como `{{ custom_values.<key> }}`):

| Valor | key | Ejemplo |
|---|---|---|
| Venue Name | `venue_name` | D'Space |
| Venue Address | `venue_address` | … |
| Support Phone | `support_phone` | … |
| Supabase Function Base URL | `supabase_fn_base` | https://<proj>.functions.supabase.co |
| Backend Token (GHL→Supabase) | `backend_token` | (secreto, para Custom Webhook de vuelta) |

> Al duplicar a otro venue: estos custom values + los webhook URLs son lo que se re-setea por sub-account (ver mapa de duplicación en el hub).

---

## 5. Webhook URLs (capturar después)

Cada workflow con trigger "Inbound Webhook" genera un **URL único**. Tras crear WF1/WF2/WF3 en GHL, capturar sus URLs y guardarlos en el lado website/Supabase como mapa `venue → { wf1_url, ... }`. **Se regeneran por location** al desplegar snapshot a un venue nuevo.

---

## 6. Orden de creación (checklist)

- [ ] Crear pipeline "D'Space Bookings" + 7 etapas (§2).
- [ ] Crear los custom fields de contacto (§3).
- [ ] Crear los custom values de location (§4).
- [ ] Crear los 3 workflows (WF1/WF2/WF3) — specs en sus docs.
- [ ] Capturar los inbound webhook URLs → guardarlos en website/Supabase.

---

## Actualización — pipeline (16-jun-2026)

`pending` vive **solo en el backend** (decisión WF1). La oportunidad GHL se **crea en la etapa `Confirmed`** (primer webhook = al aprobar el admin). → La etapa **"Under Review" es opcional/no usada**; puedes omitirla del pipeline GHL. El resto del mapeo (§2) igual.

---

## Corrección — Under Review SÍ se usa (16-jun-2026)

Revierte la nota anterior. La oportunidad **se crea en `pending` (Under Review)** al entrar el booking con depósito pagado. **Crear la etapa Under Review** en el pipeline. El primer webhook (booking `pending` + `deposit_paid`) crea contacto + oportunidad ahí.

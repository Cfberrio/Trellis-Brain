# Workflow 01 — Guía de Setup en GHL (Fase A, manual)

> Paso a paso para construir TODO lo de WF1 en la UI de GHL (sub-account D'Space). Grounded en docs oficiales de GHL (16-jun-2026). Plan técnico: [[Workflow-01-Plan-Implementacion]]. Campos: [[00-GHL-Custom-Fields-y-Values]].

---

## 0. Prerrequisito — habilitar Premium Triggers & Actions

El **Inbound Webhook trigger** y el **Custom Webhook action** son **LC Premium**. Habilitar en **Agency view → Settings → Premium Triggers & Actions** (o vía SaaS Configurator). Da 100 ejecuciones gratis por sub-account, luego cobra (rebilling opcional). Sin esto, el trigger Inbound Webhook no aparece.

---

## 1. Custom Fields (Settings → Custom Fields → Add Field)

Crear en el sub-account. Folder sugerido: "Booking". Keys en snake_case (GHL las genera; ajustar si difiere).

| Label | Tipo de campo GHL | Key |
|---|---|---|
| Reservation Number | Single Line | `reservation_number` |
| Booking Status | Single Line | `booking_status` |
| Payment Status | Single Line | `payment_status` |
| Event Date | Date Picker | `event_date` |
| Event Start | Single Line | `event_start` |
| Event End | Single Line | `event_end` |
| Guest Count | Number | `guest_count` |
| Total Amount | Monetary | `total_amount` |
| Deposit Amount | Monetary | `deposit_amount` |
| Balance Amount | Monetary | `balance_amount` |
| Amount Paid | Monetary | `amount_paid` |
| Balance Payment URL | Single Line | `balance_payment_url` |
| Balance Link Expires | Date Picker | `balance_link_expires_at` |
| Guest Reminder Step | Single Line | `guest_reminder_step` |
| Access Instructions | Multi Line | `access_instructions` |
| Service Tier | Single Line | `service_tier` |
| Space / Venue | Single Line | `space_name` |

> `event_start`/`event_end` = **Single Line**. La edge function manda ISO con offset DST-correcto de Orlando (`2026-08-15T18:00:00-04:00` en verano EDT, `-05:00` en invierno EST). WF3 lee este string para los Wait steps. (Date Picker trunca a fecha → no sirve.)

---

## 2. Pipeline + Etapas (Settings → Pipelines → Add Pipeline)

Nombre: **D'Space Bookings**. Etapas en orden:

1. **Under Review** (← `pending` + depósito pagado)
2. **Confirmed** (← `confirmed`)
3. **Pre-Event Ready** (← `pre_event_ready`)
4. **In Progress** (← `in_progress`)
5. **Post-Event** (← `post_event`)
6. **Closed (Won)** (← `closed`)
7. **Cancelled (Lost)** (← `cancelled`)

Guardar. (Anotar Pipeline ID y Stage IDs si más adelante se usan en automatizaciones avanzadas.)

---

## 3. Workflow "WF1 — Pipeline y Estados" (Automation → Workflows → Create)

### Nodo 1 — Trigger: Inbound Webhook
1. Add Trigger → **Inbound Webhook**.
2. Copiar el **Webhook URL** generado.
3. Mandar un POST de prueba a ese URL con el sample payload (abajo). Click **Test Trigger / Fetch Sample**.
4. Seleccionar el request recibido como **mapping reference** (sample data). Guardar el trigger.

**Sample payload (mandar por Postman/curl para el mapeo):**
```json
{
  "reservation_number": "DS-1001",
  "event_status": "pending",
  "payment_status": "deposit_paid",
  "email": "test@dspace.com",
  "phone": "+14075550123",
  "first_name": "Test",
  "last_name": "Guest",
  "event_date": "2026-08-15",
  "event_start": "2026-08-15T18:00:00-04:00",
  "event_end": "2026-08-15T23:00:00-04:00",
  "total_amount": 4000,
  "deposit_amount": 2000,
  "balance_amount": 2000,
  "amount_paid": 2000,
  "guest_count": 80,
  "service_tier": "attended",
  "space_name": "Main Conference, Breakout Room"
}
```
> Reglas GHL: JSON only · keys snake_case sin espacios · **email o phone obligatorio** (matchea/crea el contacto) · arrays no usables en custom values.
> **Multi-space:** un booking puede tener varios espacios. La edge function une los nombres legibles por coma en `space_name` (string, NO array → respeta la regla GHL). Espacios reales (enum `space_id` → label): `main`→Main Conference · `mezzanine`→Mezzanine · `meeting`→Meeting Room · `breakout`→Breakout Room. `event_start` = inicio más temprano de todos los espacios; `event_end` = fin más tardío (mismo día).

> **Cómo se referencian los valores del webhook (CLAVE):** GHL NO resuelve tokens escritos a mano. En cada campo, click el ícono **`{}` (Add Custom Value)** → grupo **"Inbound Webhook"** → eliges la key. Los campos solo aparecen DESPUÉS de guardar el sample (paso 4 del Nodo 1). Por eso el sample va primero.

### Nodo 2 — Action: Create/Update Contact
Un solo nodo de contacto. Mapear con el picker `{}` → Inbound Webhook → key.

**Campos estándar:**
| Campo del contacto | ← key del webhook |
|---|---|
| Email | `email` |
| Phone | `phone` |
| First Name | `first_name` |
| Last Name | `last_name` |

**Custom fields** (botón "Add Field" por cada uno):
| Custom field | ← key del webhook |
|---|---|
| Booking Status | `event_status` ⬅️ **lo leen las branches** |
| Payment Status | `payment_status` |
| Reservation Number | `reservation_number` |
| Event Date | `event_date` |
| Event Start | `event_start` |
| Event End | `event_end` |
| Guest Count | `guest_count` |
| Total Amount | `total_amount` |
| Deposit Amount | `deposit_amount` |
| Balance Amount | `balance_amount` |
| Amount Paid | `amount_paid` |
| Service Tier | `service_tier` |
| Space / Venue | `space_name` |

> 17 mapeos. `balance_payment_url`, `balance_link_expires_at`, `guest_reminder_step`, `access_instructions` se setean en WF2/WF3 — aquí NO. **No hace falta nodo extra de update antes de las branches:** este nodo ya escribió `Booking Status` en el contacto y las acciones corren en orden.

### Nodo 3 — Action: If/Else (7 branches sobre el CONTACT field)
Add Action → **If/Else**. **Importante:** cada branch evalúa el **contact custom field "Booking Status"** (no el webhook crudo) — el Nodo 2 ya lo seteó y los contact fields evalúan confiable en el picker.

Por branch: **Field** (picker → Contact Fields → **Booking Status**) · **Operator** `is equal to` · **Value** (string a mano, minúscula):

| Branch | Value |
|---|---|
| B1 | `pending` |
| B2 | `confirmed` |
| B3 | `pre_event_ready` |
| B4 | `in_progress` |
| B5 | `post_event` |
| B6 | `closed` |
| B7 | `cancelled` |

> La branch **None** se crea sola y no se borra → déjala VACÍA (B1–B7 cubren los 7 estados). Cada branch DEBE tener su value (error común: value vacío).

### Nodo 4 — En CADA branch: Create/Update Opportunity
**Idéntico en las 7**, solo cambian Stage + Status:
- **In Pipeline:** D'Space Bookings
- **Opportunity Name:** picker → **Contact → Reservation Number** (NO `contact.name`)
- **Opportunity Source:** `Website booking`
- **Opportunity Value:** picker → **Contact → Total Amount**
- **Allow Duplicate Opportunities:** **OFF** (dedup por Contact ID → actualiza la misma opp y la mueve)
- **Allow opportunity to move to any previous stage:** **ON**

| Branch | Stage | Status |
|---|---|---|
| pending | Under Review | Open |
| confirmed | Confirmed | Open |
| pre_event_ready | Pre-Event Ready | Open |
| in_progress | In Progress | Open |
| post_event | Post-Event | Open |
| closed | Closed (Won) | **Won** |
| cancelled | Cancelled (Lost) | **Lost** |

### Nodo 5 — Guardar y Publicar
- Workflow Settings: **Allow Re-Entry = ON** (re-entra en cada cambio de estado → la opp se mueve; sin esto entra 1 vez y nunca avanza).
- Save → **Publish**.
- El **Inbound Webhook URL** = secret `GHL_WF1_WEBHOOK_URL` para la edge function (Fase D del plan).

> **AI Workflow Builder:** arma la estructura pero falla el nivel-campo (mapeos a Email repetidos, branches sin value, Name en `contact.name`, todo Status=Open). Tras generar con AI, hay que arreglar a mano todo el Nodo 2–4 como arriba. Más confiable construir manual.

---

## 4. Prueba (end-to-end del lado GHL)
1. Mandar el sample payload (`pending`) → aparece contacto + oportunidad en **Under Review**.
2. Mandar el mismo `reservation_number` con `event_status=confirmed` → la **misma** oportunidad se mueve a **Confirmed** (no se duplica).
3. Repetir con `pre_event_ready`, `in_progress`, `post_event`, `closed` (won), `cancelled` (lost).

---

## 5. Notas / limitaciones
- **Matching por contacto:** Create/Update Opportunity (Allow Duplicate OFF) actualiza la oportunidad del contacto en ese pipeline. Si un cliente repite (2 bookings), el 2do podría actualizar la oportunidad del 1ro. Para v1 es aceptable; para precisión futura: Find Opportunity por un custom field de oportunidad = `reservation_number` y luego Update/Create.
- **Premium executions:** cada webbook entrante = 1 ejecución (presupuestar).
- **Si el webhook URL se filtra:** GHL no permite regenerarlo; hay que borrar el trigger y crear uno nuevo (URL nuevo → actualizar el secret).
- **Re-mapeo:** si cambia la estructura del payload, re-seleccionar el Mapping Reference en el trigger.
- **`pre_event_ready` lo dispara Stripe (futuro):** cuando se conecte Stripe, su edge function detecta el pago del 50% restante → setea `payment_status='fully_paid'` + `event_status='pre_event_ready'` en Supabase → el trigger notify manda la señal y la oportunidad pasa a **Pre-Event Ready**. Hasta entonces ese salto no es automático (admin puede moverlo manual).
- **Bookings internal/external:** nacen ya `confirmed` (creados por staff). NO entran en la cadena de transiciones por tiempo; se manejan independientes del webhook. Solo los bookings de website (nacen `pending` con depósito) recorren la cadena completa.

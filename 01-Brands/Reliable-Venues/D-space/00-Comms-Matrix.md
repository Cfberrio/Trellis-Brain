# 00 · Comms Matrix — Qué se envía, cuándo, por quién

> Matriz compartida de toda la comunicación al cliente. Referencia para WF1/WF2/WF3. Hub: [[Arquitectura-Estados-y-Automatizacion]].
>
> **Regla de envío:** los **2 correos con PDF (recibos) los manda Supabase** directo (GHL no genera PDFs). **Todo lo demás (SMS + emails sin PDF) lo manda GHL** vía workflow, leyendo la señal del custom field.

**Estado:** spec.

---

## Matriz

| # | Paso | Email | SMS | PDF | Disparador | Estado/Señal | Sender | Workflow |
|---|------|:---:|:---:|:---:|---|---|---|---|
| 01 | 50% Received + Booking Under Review | ✅ | — | ✅ | Depósito recibido | `payment_status → deposit_paid` | **Supabase** (PDF) | WF1 mueve a *Under Review* |
| 02 | Remaining 50% Due | ✅ | ✅ | — | 15 días antes del evento (o inmediato si short notice) | `balance_payment_url` actualizado | **GHL** | [[Workflow-02-Remaining-Balance]] |
| 03 | Fully Paid + Access Instructions | ✅ | — | ✅ | Pago final (balance) recibido | `payment_status → fully_paid` (→ `pre_event_ready`) | **Supabase** (PDF) | WF1 mueve a *Pre-Event Ready* |
| 04 | 30-Day Check-in | ✅ | — | — | 30 días antes del evento | `guest_reminder_step = check_in_30d` | **GHL** | [[Workflow-03-Reminders]] |
| 05 | 7-Day Check-in | — | ✅ | — | 7 días antes | `guest_reminder_step = check_in_7d` | **GHL** | WF3 |
| 06 | 1-Day Access Reminder | — | ✅ | — | 1 día antes | `guest_reminder_step = access_1d` | **GHL** | WF3 |
| 07 | 1-Hour Reminder | — | ✅ | — | 1 hora antes del inicio | `guest_reminder_step = reminder_1h` | **GHL** | WF3 |
| 08 | Review Reminder | — | ✅ | — | 24h después del fin (skip si hay review) | `guest_reminder_step = review` | **GHL** | WF3 |

---

## Notas

- **PDF receipts (01, 03):** edge function de Supabase (Resend o similar + generación PDF). **MUST-BUILD** — hoy D'Space no tiene email ni PDF. `booking_policies` ya tiene flags (`send_deposit_emails`, `send_balance_emails`, …) pero nada cableado.
- **02 (balance due):** GHL manda email+SMS usando `balance_payment_url`. La cadencia (short/long notice) la decide el scheduler de Supabase — ver WF2.
- **04–08 (recordatorios huésped):** GHL manda según `guest_reminder_step`. Cadencia + smart catch-up en WF3. **No es host report** — son check-in/acceso al huésped.
- **Política:** respetar `booking_policies` (flow `WEBSITE_FULL_FLOW` vs `INTERNAL_BLOCK_FLOW`). Si la política no requiere pago/recordatorios, no enviar.
- **Caveat horario:** los anclajes de hora ("9 AM", "1h antes") usan zona Orlando. Offset DST **no** se corrige en v1 (decisión) — anotar que en verano el horario puede correrse ~1h.

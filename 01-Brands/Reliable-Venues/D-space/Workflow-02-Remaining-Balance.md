# Workflow 02 · Remaining Balance (cobro del 50% restante)

> **Propósito:** lograr que el cliente pague el balance (2do 50%) antes del evento. Comms paso **02** (email + SMS). Basado en la lógica probada de OEV, adaptada al schema de D'Space + nombres claros.
>
> Depende de: [[00-GHL-Custom-Fields-y-Values]], [[00-Comms-Matrix]]. Hub: [[Arquitectura-Estados-y-Automatizacion]].

**Estado:** spec.

---

## 1. Concepto

El link de pago lo crea **el website/Supabase** (Stripe). Cada recordatorio **regenera un link fresco** (el anterior expira en 24h), lo persiste, y hace `sync-to-ghl` actualizando el custom field `balance_payment_url`. **GHL detecta el cambio y manda el email + SMS** (paso 02). La edge function NO manda el comms al cliente — solo crea el link y sincroniza.

Ancla de cálculo: `bookings.event_date` (no existe `balance_due_date`). Umbral **15 días naturales** hasta el evento define short vs long notice.

```
diffDays = floor((medianoche Orlando del event_date) - (medianoche hoy)) / 1 día
diffDays <= 15  → SHORT NOTICE
diffDays >  15  → LONG NOTICE
```

---

## 2. Cadencia

### SHORT NOTICE (≤15 días) — máx 2 contactos
- **Link inmediato** (síncrono, ya): llama `create-balance-payment-link`. Si falla → 500, no agenda follow-up. Cuenta como "contacto 1".
- **`balance_reminder_followup`** a **+48h** desde ahora → job en `scheduled_jobs`.
- Cadencia: ahora → +48h. Fin.

### LONG NOTICE (>15 días) — 3 contactos diferidos, anclados al evento
```
base    = event_date 09:00 Orlando
t15     = base − 15 días   → job  balance_reminder_t15   (T-15d, 9 AM)
t13     = t15 + 48h        → job  balance_reminder_t13   (T-13d, 9 AM)
t11     = t13 + 48h        → job  balance_reminder_t11   (T-11d, 9 AM)
```
Los 3 se insertan `pending`. Después de T-11d no hay más recordatorios automáticos.

> **Nombres claros (mejora vs OEV):** OEV usaba `balance_retry_1/2/3` (confuso, mezclaba "recordatorio" con "reintento técnico"). Aquí: `balance_reminder_t15/t13/t11` (long) y `balance_reminder_followup` (short). El link inmediato de short notice no es un job — es la llamada síncrona.

---

## 3. Qué hace cada job cuando le toca

Dispatcher `process-scheduled-jobs` (cada 5 min) procesa `balance_reminder_*`:

1. Incrementa `attempts` (reintento técnico, máx 3 — distinto del "recordatorio").
2. Relee `payment_status`:
   - `fully_paid` → job `completed`, log `balance_skipped_already_paid`. No genera link.
   - `!= deposit_paid` → job `failed`.
   - `deposit_paid` → sigue.
3. Llama `create-balance-payment-link` (sin flag de email — el comms lo hace GHL).
4. La función: crea sesión Stripe Checkout nueva (expira 24h) con línea de balance + fee 3.5%; persiste `payment_url` + `link_expires_at` en `booking_payments`; `sync-to-ghl` actualiza `balance_payment_url` → **GHL manda email+SMS (paso 02)**.
5. Éxito → job `completed`, log `balance_reminder_executed`.

**Dos conceptos de "intento" (no confundir):**
| Recordatorio (nombre del job) | `attempts` (campo) |
|---|---|
| Contactos en días distintos (cadencia) | Reintentos técnicos si la ejecución falla |
| 2 (short) o 3 (long) | máx 3 por job |

---

## 4. Cómo se detiene la cadena

- Cliente paga → Stripe webhook (kind `balance`) marca `fully_paid` y **cancela** los `balance_reminder_*` pendientes en `scheduled_jobs`. Dispara WF1: `pre_event_ready` + comms 03 (PDF, Supabase).
- Doble red: si un job corre antes de la cancelación pero ya está pagado → dispatcher lo marca `completed/skipped` (paso 2).
- Idempotencia: el dedup de agendado incluye estado `completed` → nunca re-agenda aunque el booking re-dispare.

---

## 5. MUST-BUILD (Supabase)

- [ ] Stripe webhook (no existe) — marca pagos, idempotencia (`stripe_event_log`), cancela jobs al pagar balance.
- [ ] `create-balance-payment-link` edge function (no existe).
- [ ] Scheduler: al `payment_status → deposit_paid`, agenda short/long notice.
- [ ] Manejo de `balance_reminder_*` en el dispatcher.
- [ ] `sync-to-ghl` actualiza `balance_payment_url` (compartido con WF1).

---

## 6. Items abiertos (resolver en el chat de WF2)

- ¿Stripe Connect transfiere un % (OEV: 20% del balance a cuenta conectada)? En D'Space el service fee es 20% — confirmar a dónde va y si se transfiere en el balance link.
- Líneas exactas del checkout (balance + fee 3.5%; ¿cleaning/addons?).
- Caveat DST: anclas "9 AM" usan offset Orlando fijo; en verano puede correrse ~1h (no se corrige en v1, por decisión).
- Texto/plantilla del email+SMS del paso 02 (se arma en GHL).

---

## Actualización — decisiones (16-jun-2026)

- **Split confirmado:** pago total = **50% depósito** (al reservar) + **50% remaining balance**. Este workflow cobra el **balance (50%)**. Sin cambios a la cadencia short/long notice.

---

## Estado: DIFERIDO (16-jun-2026)

WF2 se construye **después** (decisión). Prioridad: WF1 + WF3. El spec queda listo para retomar — incluye items abiertos (Stripe Connect 20%, líneas del checkout).

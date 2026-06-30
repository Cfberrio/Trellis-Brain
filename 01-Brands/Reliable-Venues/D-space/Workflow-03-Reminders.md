# Workflow 03 · Reminders (recordatorios al huésped)

> **Propósito:** recordatorios de **check-in / acceso al huésped** antes y después del evento. **NO es host report** (D'Space no usa formulario de detalles). Comms pasos **04–08**. Mecánica análoga a balance: agenda jobs en `scheduled_jobs`, los manda el cron, y el contacto real lo dispara **GHL**.
>
> Depende de: [[00-GHL-Custom-Fields-y-Values]], [[00-Comms-Matrix]]. Hub: [[Arquitectura-Estados-y-Automatizacion]].

**Estado:** spec.

---

## 1. Cadencia (4 puntos antes + review)

Ancla = inicio del evento en Orlando (`event_date` + menor `booking_spaces.start_time`; daily → 10 AM default). El review ancla al **fin** (+24h).

| Job (`job_type`) | Cuándo | `guest_reminder_step` | Canal (GHL) | Paso |
|---|---|---|---|---|
| `reminder_check_in_30d` | evento − 30 días | `check_in_30d` | Email | 04 |
| `reminder_check_in_7d` | evento − 7 días | `check_in_7d` | SMS | 05 |
| `reminder_access_1d` | evento − 1 día | `access_1d` | SMS | 06 |
| `reminder_1h` | evento − 1 hora | `reminder_1h` | SMS | 07 |
| `reminder_review` | fin + 24 h | `review` | SMS | 08 (skip si hay review) |

> Nombres literales (mejora vs OEV, que usaba `during`/`post` engañosos).

---

## 2. Qué hace cada job cuando le toca

Dispatcher (cada 5 min) procesa `reminder_*`:
1. Actualiza `bookings.guest_reminder_step` al valor correspondiente.
2. Llama `sync-to-ghl` (CRÍTICO, inmediato) → actualiza el custom field `guest_reminder_step`.
3. **GHL detecta el cambio y manda el email/SMS** según el paso.

La edge function NO manda el comms — cambia el campo señal + sincroniza. `guest_reminder_step` es lo que GHL escucha.

---

## 3. Smart catch-up (mejora conservada de OEV)

No agenda siempre los 4. Según cuánto falte al evento **al momento de agendar** (cuando el booking llega a `confirmed`/`pre_event_ready`), setea el paso actual **ya** y agenda solo los futuros. Evita spam de varios recordatorios de golpe.

| Tiempo al evento al agendar | Paso inmediato (set ya) | Jobs futuros que crea |
|---|---|---|
| > 30 días | ninguno | los 4 (30d, 7d, 1d, 1h) |
| 30d – 7d | `check_in_30d` | 7d, 1d, 1h |
| 7d – 1d | `check_in_7d` | 1d, 1h |
| 1d – 1h | `access_1d` | 1h |
| ≤ 1h | `reminder_1h` | ninguno |

El review (`reminder_review`, fin+24h) se agenda siempre aparte.

---

## 4. Review detection (paso 08)

Skip el SMS de review si ya hay review. **OPEN — definir en el chat de WF3:** ¿dónde se detecta?
- Propuesta default: link de review = trigger link de GHL; si el contacto lo clickeó (o un campo `reviewed = true`), el job `reminder_review` se marca `skipped`. 
- Alternativa: campo en DB que el website/GHL setea.

---

## 5. MUST-BUILD (Supabase)

- [ ] Campo señal `guest_reminder_step` (en `bookings` + custom field GHL).
- [ ] Scheduler: al `confirmed` (o `pre_event_ready`) agenda los `reminder_*` con smart catch-up.
- [ ] Manejo de `reminder_*` en el dispatcher.
- [ ] `sync-to-ghl` (compartido) actualiza `guest_reminder_step`.
- [ ] GHL Workflow 03: trigger por cambio de `guest_reminder_step` → IF/ELSE por valor → manda email/SMS del paso.

---

## 6. Items abiertos (resolver en el chat de WF3)

- Mecánica de review detection (§4).
- ¿El scheduler agenda al `confirmed` o al `pre_event_ready` (balance pagado)? Propuesta: al `pre_event_ready` para no recordar acceso a quien no ha pagado.
- Textos de cada email/SMS (se arman en GHL).
- Caveat DST (igual que WF2).

---

## Actualización — decisiones (16-jun-2026)

**Review (paso 08) resuelto:**
- Corre a **`end_time` + 24 h**.
- **Guard:** solo manda si `event_status = post_event` (a esa altura el booking ya está en `post_event`; `closed` es +2–3 días). Si no está en `post_event` (ej. cancelado), se salta.

Sigue abierto: detección "skip si ya hay review" (trigger link GHL vs campo DB) — si se omite, manda siempre a `end_time`+24h. Y si el scheduler de recordatorios pre-evento agenda al `confirmed` o al `pre_event_ready`.

---

## Actualización 2 — scheduling (16-jun-2026)

Recordatorios pre-evento (30d/7d/1d/1h) se **agendan al `confirmed`** (resuelto). El smart catch-up computa el tiempo-al-evento desde ese momento. Nota: el check-in 30d puede caer antes de pagar el balance (balance vence ~15d antes) — ok, son check-in/acceso, no cobro.

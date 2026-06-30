# Lógica de Estados — D'Space Bookings (WF1)

> Fuente de verdad: **Supabase** (`bookings.event_status`). GHL es **espejo** (la oportunidad se mueve de etapa sola en cada cambio). Hub: [[Arquitectura-Estados-y-Automatizacion]]. Setup GHL: [[Workflow-01-GHL-Setup-Guia]]. Plan: [[Workflow-01-Plan-Implementacion]].

**Cadena:** `pending → confirmed → pre_event_ready → in_progress → post_event → closed` · (`cancelled` aparte).

---

## Transiciones (qué dispara cada salto)

### 1. pending → confirmed
- **Disparo:** admin aprueba en el dashboard ("Approve & Confirm").
- **Tipo:** Manual.
- **Efecto extra:** al confirmar se **agendan 3 jobs por tiempo** (`set_in_progress`, `set_post_event`, `set_closed`) anclados a la fecha/hora del evento (hora Orlando, DST-correcto).

### 2. confirmed → pre_event_ready
- **Disparo:** el cliente **paga el 50% restante** (balance) → Stripe pone `payment_status=fully_paid` + `event_status=pre_event_ready`.
- **Tipo:** Auto (vía edge function de Stripe — **futuro**, cuando se conecte Stripe).
- **Hoy:** no pasa solo; admin puede moverlo a mano. Sin pre_event_ready, la cadena por tiempo no avanza.

### 3. pre_event_ready → in_progress
- **Disparo:** llegó la **hora de inicio** del evento (start más temprano de los espacios).
- **Tipo:** Auto por tiempo (cron cada 5 min).
- **Candado:** solo si el booking está en `pre_event_ready`. Si no (ej. balance sin pagar) → no pasa; el job corre una vez y se descarta.

### 4. in_progress → post_event
- **Disparo:** llegó la **hora de fin** del evento (end más tardío de los espacios).
- **Tipo:** Auto por tiempo (cron).
- **Candado:** solo si está en `in_progress`.

### 5. post_event → closed  ⬅️ ACTUALIZADO
- **Disparo:** **24 horas** tras el fin del evento **O** el cliente llena el **Guest Report** (lo que ocurra primero).
- **Tipo:** Auto por tiempo (cron) + (futuro) trigger por Guest Report.
- **Candado:** solo si está en `post_event`.
- **Hoy en código:** solo la parte de **24h** (`set_closed = fin + 24h`). El "O Guest Report" queda documentado para cuando exista esa feature.

### cancelled (aparte)
- **Disparo:** admin, a mano, en cualquier momento.

---

## Guest Report (futuro — sin referencia en el schema aún)
Reporte post-evento que llena el cliente: estado en que dejó el venue, **fotos de baños / instalaciones**, daños o inconvenientes. Sirve para control de daños y resolver problemas.

**Cómo enganchará con la lógica:** cuando el cliente envíe el Guest Report → cierra el booking de inmediato (`post_event → closed`), sin esperar las 24h. Implementación futura: un trigger sobre la tabla del reporte que haga `update bookings set event_status='closed' where id=... and event_status='post_event'`, o un job que adelante `set_closed`. Custom field GHL relacionado: `guest_reminder_step` / nuevo campo de reporte (definir al construir la feature).

---

## Resumen ultra-simple

| Salto | Disparo | Tipo |
|---|---|---|
| pending → confirmed | admin aprueba | Manual |
| confirmed → pre_event_ready | cliente paga balance (Stripe) | Auto (futuro) |
| pre_event_ready → in_progress | llega hora inicio evento | Auto (tiempo) |
| in_progress → post_event | llega hora fin evento | Auto (tiempo) |
| post_event → closed | **24h tras fin** O **Guest Report** | Auto (tiempo) + futuro |
| → cancelled | admin a mano | Manual |

**Claves:**
- Saltos 3-4-5 = por reloj (cron cada 5 min revisa qué venció), cada uno con candado por el estado previo.
- Cada cambio de estado dispara `sync-to-ghl` → la oportunidad GHL se mueve de etapa sola.
- Bookings `internal`/`external` (creados por staff, nacen `confirmed`) NO entran en la cadena por tiempo (por diseño).

---

## Estado de implementación
- [x] Saltos 1, 3, 4, 5 (24h) en código + desplegados.
- [ ] Salto 2 (Stripe) — pendiente conexión Stripe (WF2).
- [ ] "O Guest Report" en salto 5 — pendiente feature Guest Report.

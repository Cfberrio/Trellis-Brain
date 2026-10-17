---
brain_note_id: "note:e40ddc97-5399-4230-bc2f-35445b5e16d4"
canonical_key: "booking-states-logic"
brand_id: "trellis_core"
---
# Booking States and Reservation Logic

## Canonical Statement

- **process**: Reservations operate on two independent axes: the Event Axis (operative cycle) and the Money Axis (payment status). A payment never moves the event axis, and an event action never moves the money axis.
- **rule**: A 'Lead' is a calculated state defined as Event=pending AND Money=pending. Leads do not block the calendar.
- **rule**: Calendar blocking only occurs when payment status is deposit_paid, fully_paid, or invoiced, and the event is not cancelled.
- **rule**: Booking constraints: Reservations only allowed Monday-Thursday; minimum hours apply (Main/Mezzanine 4h); capacity limits (Main 100, Mezzanine 50, Meeting 6, Breakout 7).
- **decision**: D'Space requires an 80% deposit for online bookings. The balance must be paid before the event to move to the 'lista_pre_evento' state.

## Evidence Log

- 2026-10-17T00:45:35.920Z — `clickup_doc_page:8cqnrff-19757/8cqnrff-26217`
  - `e1` (source_body): Cada reserva vive en **dos líneas a la vez**, independientes: - **Eje del evento (operativo):** ¿en qué punto del ciclo está el evento? - **Eje del dinero (pago):** ¿cuánto ha pagado el cliente? Nunca se mezclan en un solo estado.
  - `e2` (source_body): **LEAD** = evento `pendiente` **Y** pago `pendiente`. Es interés sin dinero todavía. No bloquea el calendario.
  - `e3` (source_body): **"Bloquea calendario"** = pago ∈ {depósito_pagado, pagado_completo, facturado} **y** evento ≠ cancelada.
  - `e4` (source_body): Solo **Lunes–Jueves**. Cumplir **horas mínimas** (Main y Mezzanine = 4h). Tope **por espacio** (Main 100, Mezzanine 50, Meeting 6, Breakout 7).
  - `e5` (source_body): D'Space cobra **depósito del 80%** y el balance vence **antes** del evento. -> lista_pre_evento: Balance pagado + staff asignado + vendor de bar resuelto.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-19757/8cqnrff-26217`
- Source hash: `05973d16c3dcf4b4743de8bc2f2567b33a53724284a45c183f8843aa4482893b`
- Observed at: 2026-10-17T00:45:35.920Z
- Agent run: `4b3cdd71-e337-46ff-827d-9acee27e59ab`
- Validation run: `cb6f1387-17cc-456d-b58c-7a36c1af4892`

---
brain_note_id: "note:336f8b97-b5ef-426b-bfd5-dec7f159f4e5"
canonical_key: "venue-booking-state-logic"
brand_id: "trellis_core"
---
# Venue Booking State Logic

## Canonical Statement

- **rule**: Booking logic transitions are driven by time and payments, not human actions, with the sole exception of the initial admin confirmation.
- **definition**: Booking states exist on two independent axes: event_status (pending, confirmed, pre_event_ready, in_progress, post_event, closed) and payment_status (pending, deposit_paid, fully_paid).
- **process**: The transition from 'confirmed' to 'pre_event_ready' is triggered automatically when payment_status reaches 'fully_paid'.
- **rule**: Staff assignment and post-event reports are informative and do not block the automated lifecycle transitions or archiving.

## Evidence Log

- 2026-10-17T00:46:07.677Z — `clickup_doc_page:8cqnrff-19757/8cqnrff-28537`
  - `e1` (source_body): Principio raíz: la lógica avanza por TIEMPO, no por acciones humanas. Única intervención humana en el flujo = el admin confirma la reserva. Lo demás es automático.
  - `e2` (source_body): El estado de una reserva vive en dos ejes independientes. event_status: pending → confirmed → pre_event_ready → in_progress → post_event → closed. payment_status: pending → deposit_paid → fully_paid.
  - `e3` (source_body): confirmed → pre_event_ready | Cliente hace el 2º pago → payment_status = fully_paid | Pago
  - `e4` (source_body): Asignación de staff: el admin asigna staff → al staff le llega un request → acepta/rechaza. Acepte o no, el booking sigue su curso. Es informativo, no un gate.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-19757/8cqnrff-28537`
- Source hash: `b3ff2709715f8ad2e7264f21499d5d149d3fd13a728aa9721e321f56b4862479`
- Observed at: 2026-10-17T00:46:07.677Z
- Agent run: `9d949863-62fe-402f-b5b6-6eb610dc7947`
- Validation run: `d0f56ae7-1eba-499c-aec3-766ce58a1b8e`

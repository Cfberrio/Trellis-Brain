---
brain_note_id: "note:2ea9aa21-f85b-4102-8734-177b51cfee25"
canonical_key: "booking-lifecycle-states"
brand_id: "orlando_event_venue"
---
# OEV Booking Lifecycle and Payment States

## Canonical Statement

- **process**: The OEV booking lifecycle consists of 7 states: pending (new website submission), confirmed (admin approved), pre_event_ready (checklist/staff ready), in_progress (event occurring), post_event (24h post-event + report), closed_review_complete (final state), and cancelled.
- **rule**: A booking cannot automatically transition to 'in_progress' unless the payment status is 'fully_paid', staff is assigned, and the event start time is reached.
- **process**: Transition to 'in_progress' automatically triggers staff assignment completion, payroll generation, and GHL synchronization.
- **fact**: Payment statuses are tracked independently as pending, deposit_paid (50%), fully_paid (100%), invoiced (internal/external), or refunded.

## Evidence Log

- 2026-10-09T00:37:50.766Z — `clickup_doc_page:8cqnrff-10597/8cqnrff-9197`
  - `e1` (source_body): Los 7 Estados del Lifecycle: 1. pending, 2. confirmed, 3. pre_event_ready, 4. in_progress, 5. post_event, 6. closed_review_complete, 7. cancelled.
  - `e2` (source_body): El booking NO puede pasar a in_progress automáticamente si el pago no está en fully_paid. Esto protege al venue de eventos sin pago completo.
  - `e3` (source_body): Efectos automáticos importantes: Se marcan las asignaciones del staff como 'completadas', Se genera automáticamente el payroll, Se sincroniza el estado con GHL.
  - `e4` (source_body): Payment Status (Estado de Pago): pending, deposit_paid (50%), fully_paid (100%), invoiced, refunded.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-10597/8cqnrff-9197`
- Source hash: `8ce6ae05d2367fd16c6308a30c77aa8d5492419c9846b32bcb6bc0fe7bc511ac`
- Observed at: 2026-10-09T00:37:50.766Z
- Agent run: `5d480dca-3c87-4b6b-a69a-583ab9282fd0`
- Validation run: `3d22ca82-d021-493d-9c42-738ebd12da66`

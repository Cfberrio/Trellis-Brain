---
brain_note_id: "note:783c1d4f-0fbb-42a0-aba6-7928a80bf6be"
canonical_key: "booking-status-transition-automation"
brand_id: "orlando_event_venue"
---
# Booking Status Transition Automation

## Canonical Statement

- **rule**: A booking automatically transitions to 'in_progress' only if it is 'pre_event_ready', fully paid, has staff assigned, and the event start time is reached.
- **rule**: Transition to 'post_event' occurs automatically 24 hours after the event ends, provided the Guest Report is completed.
- **process**: When a booking moves to 'in_progress', the system automatically marks Custodial and Production staff assignments as 'completed' and generates payroll items.

## Evidence Log

- 2026-09-21T14:51:03.427Z — `clickup_doc_page:8cqnrff-10597/8cqnrff-9197`
  - `e2` (source_body): in_progress — Evento en Curso... El sistema lo hace automáticamente cuando se cumplen TODAS estas condiciones: 1. El booking está en pre_event_ready 2. El pago está completo (fully_paid) 3. Hay al menos un miembro del staff asignado 4. Es la hora de inicio del evento
  - `e3` (source_body): post_event — Post-Evento... El sistema lo hace automáticamente cuando se cumplen TODAS estas condiciones: 1. El booking está en in_progress 2. Han pasado 24 horas desde que terminó el evento 3. El Guest Report fue completado
  - `e4` (source_body): Efectos automáticos importantes: Se marcan las asignaciones del staff (Custodial y Production) como "completadas". Se genera automáticamente el payroll.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-10597/8cqnrff-9197`
- Source hash: `8ce6ae05d2367fd16c6308a30c77aa8d5492419c9846b32bcb6bc0fe7bc511ac`
- Observed at: 2026-09-21T14:51:03.427Z
- Decision: `608b88d4-0905-445e-8cff-f8b80545e07a`
- Upstream agent run: `33236509-f3b7-41a4-b633-f21ddc70f9be`
- Validation run: `40251680-d1a0-4b2d-92f8-84ab528ab67c`

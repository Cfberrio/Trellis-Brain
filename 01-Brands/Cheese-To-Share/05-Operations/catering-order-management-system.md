---
brain_note_id: "note:62a1a1a2-8de9-4cad-aae4-0678f79c5ac3"
canonical_key: "catering-order-management-system"
brand_id: "cheese_to_share"
---
# Catering Order Management System

## Canonical Statement

- **process**: Catering orders follow a specific lifecycle: Abandoned (checkout opened, no payment), Paid (50% deposit received), Assigned (staff allocated), Balance Paid (full payment), Completed (event occurred), and Cancelled.
- **rule**: Catering bookings require a minimum of 25 guests and at least 7 days of anticipation.
- **decision**: The payment model for catering is a 50% deposit at checkout via Stripe, with the remaining 50% collected 15 days before the event (or immediately if the event is sooner).
- **rule**: Order status and communication are managed through a single-column state philosophy to avoid confusion; time-based triggers (reminders) are handled by GoHighLevel and Resend.

## Evidence Log

- 2026-10-16T16:54:34.863Z — `clickup_doc_page:8cqnrff-17657/8cqnrff-21817`
  - `e1` (source_body): Estados de la orden (los únicos): Abandoned, Paid, Assigned, Balance Paid, Completed, Cancelled. Filosofía: menos estados, más claridad.
  - `e2` (source_body): Paga el 50% de depósito vía Stripe en la misma página. Mínimo 7 días de anticipación, mínimo 25 invitados.
  - `e3` (source_body): Al hacer checkout: se cobra el 50%. 15 días antes del evento (o de inmediato si el evento es muy próximo): se genera y envía un link al cliente para pagar el otro 50%.
  - `e4` (source_body): Una sola columna de estado. Una orden está en un solo lugar a la vez. Lo que es tiempo, se programa por tiempo. Recordatorios y disparadores van por reloj.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-17657/8cqnrff-21817`
- Source hash: `1b74c6263778a20598183db17ba5555c66187e44f633b0cd6c8e68027034c9af`
- Observed at: 2026-10-16T16:54:34.863Z
- Agent run: `5271708a-4a9e-4fa7-9638-0903f186b6b6`
- Validation run: `93b3a11b-ae2b-4db9-aa11-e0df3a5961a8`

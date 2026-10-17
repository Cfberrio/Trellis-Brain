---
brain_note_id: "note:0e7566eb-bda6-43ef-8dc6-befe453b9cdc"
canonical_key: "cts-bot-order-context-logic"
brand_id: "cheese_to_share"
---
# CTS Bot — Order Context and Support Logic

## Canonical Statement

- **process**: The CTS bot uses ORDER_CONTEXT to access catering order data from the website's orders table, identifying customers by email or the last 7 digits of their phone number.
- **rule**: The bot can cite existing order balances and due dates but is prohibited from providing new price quotes; new quotes must be finalized by Luis.
- **rule**: Bot responses regarding order status must use customer-friendly language (e.g., 'Your date is confirmed!') instead of internal database enums.
- **rule**: Requests for refunds, cancellations, or date changes must be flagged for human intervention; the bot cannot modify existing orders.

## Evidence Log

- 2026-10-17T22:43:04.374Z — `clickup_doc_page:8cqnrff-22017/8cqnrff-30317`
  - `e1` (source_body): El bot CTS ahora ve ORDER_CONTEXT: las órdenes de catering del cliente que escribe, buscadas en la tabla orders por email (fallback: últimos 7 dígitos del teléfono). ... Lo que sigue prohibido es dar totales NUEVOS como finales — quotes nuevos los firma Luis.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22017/8cqnrff-30317`
- Source hash: `38eb4e23abcb11d289666d08e790ef3af2aff436d8c0e7e8905c4f13afbc8c1f`
- Observed at: 2026-10-17T22:43:04.374Z
- Agent run: `2ef49525-0d08-4a2f-a531-b80e0620520e`
- Validation run: `9f4aaa5d-470e-49bb-a216-eed32ca40de4`

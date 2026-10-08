---
brain_note_id: "note:6983757f-55e9-4a44-af73-900865c33418"
canonical_key: "payment-gateway-reconciliation"
brand_id: "st_joseph"
---
# Payment Gateway and Reconciliation Process

## Canonical Statement

- **decision**: Stripe (Checkout + webhook) is the selected payment gateway, with amounts set on the server.
- **rule**: Adult Formation and OCIA events are free; other events use specific pricing.
- **process**: Automatic registration-payment matching is handled via Stripe webhooks; Gift Central rows are auto-matched by email, name, and amount.
- **rule**: Imported paid-event registrations are set to 'To reconcile' status and do not trigger reminder emails until a payment is matched.
- **fact**: Emmaus servers are currently treated as 'No charge' pending a parish decision on payment requirements.

## Evidence Log

- 2026-10-07T20:17:28.940Z — `clickup:86e3etj7p`
  - `e1` (source_body): Gateway decided: Stripe (Checkout + webhook, amount set on the server)... Event-specific pricing; Adult Formation and OCIA are free... Automatic registration ↔ payment matching (Stripe webhook; Gift Central rows auto-matched by email, name and amount)... "To reconcile" status: imported lists...

## Provenance

- Source: `clickup` `86e3etj7p`
- Source hash: `516a8d17d2dde22949f586a73aa22e29c77f455014aa4310a0a4a7fb55eab5f5`
- Observed at: 2026-10-07T20:17:28.940Z
- Agent run: `cfb7a1b1-1977-4794-8b11-02a100bb7ebf`
- Validation run: `7c5350ab-0b3e-4f85-8a4f-b67bcabc44eb`

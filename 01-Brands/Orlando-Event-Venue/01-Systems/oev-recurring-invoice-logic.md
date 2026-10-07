---
brain_note_id: "note:53d006bd-c7d7-4e13-87b0-a88f3775aa9e"
canonical_key: "recurring-invoice-logic"
brand_id: "orlando_event_venue"
---
# OEV Recurring Invoice Logic

## Canonical Statement

- **rule**: Monthly recurring invoices are anchored to a specific calendar day (1st–28th or 'Last day of month') rather than a 30-day cycle.
- **process**: Admins can choose between 'Send first invoice now' or 'Wait until the chosen day' when creating a recurring schedule to prevent double-billing.
- **rule**: All invoice scheduling math is performed in America/New_York time at 3:00 PM ET to prevent date drift from UTC.
- **process**: Existing recurring invoices can be updated via the 'Change send day' action, which recalculates future sends without duplicating invoices in the current month.

## Evidence Log

- 2026-10-06T22:03:14.444Z — `clickup:86e3kmgh5`
  - `e1` (source_body): Monthly = same calendar day each month, not every 30 days. Fix the scheduler logic... Keep the send time at 3:00 PM ET and keep all date math in America/New_York so the day doesn't drift because of UTC.
  - `e2` (source_child): New 'Send on day' picker: 1st–28th, plus 'Last day of month'. New choice when creating: 'Send first invoice now' or 'Wait until the chosen day'. New 'Change send day' button in Actions.

## Provenance

- Source: `clickup` `86e3kmgh5`
- Source hash: `d99765d95856cf1d870ce6cee16309ebd9ab30b25731a5b224b3ee4f7d9ead3e`
- Observed at: 2026-10-06T22:03:14.444Z
- Agent run: `1d1ab015-dda2-457a-9e0b-a9506460e689`
- Validation run: `d646a72a-646e-41e2-8487-d44689dcce95`

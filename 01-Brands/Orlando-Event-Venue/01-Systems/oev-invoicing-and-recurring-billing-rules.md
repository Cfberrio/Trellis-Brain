---
brain_note_id: "note:096a79cc-13af-4155-aae4-c613a97968db"
canonical_key: "oev-invoicing-rules"
brand_id: "orlando_event_venue"
---
# OEV Invoicing and Recurring Billing Rules

## Canonical Statement

- **process**: Monthly recurring invoices in the OEV admin system are scheduled by calendar day (e.g., the 2nd of every month) rather than every 30 days.
- **rule**: Admins can select a specific send day from the 1st to the 28th, or choose 'Last day of month' to handle varying month lengths without skipping.
- **rule**: All invoice scheduling and date math are locked to America/New_York (3:00 PM ET) to prevent UTC day drift.
- **process**: When creating or editing recurring invoices, admins can choose to 'Send first invoice now' or 'Wait until the chosen day' to prevent double-billing.

## Evidence Log

- 2026-10-06T16:11:23.340Z — `clickup:86e3kmgh5`
  - `e1` (source_body): Monthly = same calendar day each month, not every 30 days. Fix the scheduler logic and the helper text... Keep the send time at 3:00 PM ET and keep all date math in America/New_York so the day doesn't drift because of UTC.
  - `e2` (source_child): What changed: Monthly now goes out on the same calendar day at 3:00 PM ET instead of every 30 days. New 'Send on day' picker: 1st–28th, plus 'Last day of month'. New choice when creating: 'Send first invoice now' or 'Wait until the chosen day'.

## Provenance

- Source: `clickup` `86e3kmgh5`
- Source hash: `873cdf92f17c471c27315c3c78f76ad90e3940d55517fefe0e03eedc9a089262`
- Observed at: 2026-10-06T16:11:23.340Z
- Agent run: `aa27b6de-24ed-460f-a8c2-342a4979d249`
- Validation run: `3a2b35ed-c7cf-47d5-ad0a-4237450c7f62`

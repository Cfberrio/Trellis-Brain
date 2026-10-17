---
brain_note_id: "note:c122098a-a5f9-439d-b11d-2a58aca25a23"
canonical_key: "dspace-ghl-booking-architecture"
brand_id: "trellis_core"
---
# DSpace Booking System Architecture

## Canonical Statement

- **process**: The D'Space booking system uses a two-pipeline architecture in GoHighLevel to separate sales (Booking) from fulfillment (Operations).
- **rule**: All bookings require an admin approval gate; a deposit places a tentative hold on the calendar, but confirmation is only sent after admin review.
- **process**: The system is built as a reusable 'Venue Booking' GHL snapshot for rapid deployment to other venues, featuring Stripe Connect for automated 80/20 revenue splits.
- **rule**: Staff access is restricted to the Operations pipeline and assigned events/tasks only, with no visibility into revenue or booking approvals.

## Evidence Log

- 2026-10-17T07:17:11.722Z — `clickup_doc_page:8cqnrff-20217/8cqnrff-27117`
  - `e1` (source_body): Two pipelines so sales and fulfillment never tangle (improvement over the single-pipeline other-venue build). Pipeline 1 — Booking (sales)... Pipeline 2 — Operations (fulfillment).
  - `e2` (source_body): The approval gate is the admin's core control — nothing confirms without it. On each deposit-paid booking the admin reviews against the per-space calendars... and approves or declines.
  - `e3` (source_body): Packaged as a reusable "Venue Booking" snapshot — deploy to the next venue in hours, not weeks... Stripe Connect at agency level → automated 80/20 split, payout straight to her bank.
  - `e4` (source_body): Staff restricted to assigned events, tasks, and checklists — no approvals, no revenue visibility.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-20217/8cqnrff-27117`
- Source hash: `9a0985d9760e56a6cbfcc2345bff1a6edd8f2f6ffea9920c6d16f3c561f6ed52`
- Observed at: 2026-10-17T07:17:11.722Z
- Agent run: `602802df-0738-4f2a-89df-334dc1d2b36b`
- Validation run: `abae505a-885a-4bc0-9964-e44a7d3152b3`

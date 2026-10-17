---
brain_note_id: "note:b5521798-c642-4ef9-b22b-5899438d1d84"
canonical_key: "05-operations-sops-catering-booking-sop-evidencia"
brand_id: "cheese_to_share"
---
# Catering Booking SOP — Evidencia

## Canonical Statement

- **process**: The catering booking flow follows a 6-step questionnaire including contact info, event details (date, time, guest count, type, address), styling notes, policy acceptance, and a 50% deposit payment.
- **rule**: Catering delivery is charged at $2.50 per mile from 3801 Avalon Park Blvd after the first 7 miles.
- **rule**: Catering Cancellation Policy: 14+ days for full refund; 7-14 days incurs a 10% fee; 48 hours to 7 days forfeits the 50% deposit; under 48 hours requires 100% payment.
- **rule**: A 50% deposit is required to confirm a booking; the final balance is due 14 days before the event. Guest counts must be locked 7 days prior.
- **rule**: Outside food cannot be added to a Cheese To Share grazing table without prior written approval to protect presentation standards.

## Evidence Log

- 2026-10-16T16:57:59.758Z — `clickup_doc_page:8cqnrff-17917/8cqnrff-22177`
  - `e1` (source_body): Booking Deposit — 50% to Confirm... Cancellation Policy Cancel 14+ days before your event for a FREE full refund. Cancel 7–14 days before: 10% fee... Event Address ✅ (calculate price for delivery) $2.50 /mile desde 3801 avalon park blvd despues de mile 7

- 2026-10-17T00:38:55.156Z — `clickup_doc_page:8cqnrff-19037/8cqnrff-24557` (validation `45b7be9b-0359-41d7-834c-ef8e2f4541b7`)
  - `e1` (source_body): Cheese to Share — Post-Booking Communication Sequence. Every email and SMS in this sequence closes with this exact contact info... 14 days before your event — Remaining balance is due... 7 days before your event — Final guest count locks.
- **process**: The catering post-booking sequence consists of six touchpoints: 01 Booking Confirmed (Email), 02 Balance Due (Email/SMS at 14 days out), 03 Balance Paid (Email), 04 Event Week Details (Email at 7 days out), 05 Day Before (SMS), and 06 Review Request (Email/SMS post-event).
- **rule**: All catering communications must use the canonical contact block: Cheese To Share, (407) 494-4263, info@cheesetoshare.us, https://www.cheesetoshare.us/. Email sign-offs use 'Warm regards' with the brand block; SMS sign-offs use 'Luis, Cheese To Share'.
- **rule**: Catering guest counts lock 7 days before the event. Increases are permitted if inventory allows, but decreases after this date do not reduce the total price.
- **rule**: The remaining catering balance is due 14 days before the event date.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-17917/8cqnrff-22177`
- Source hash: `b03c63dcd592750879cec91d7c469347be558ed856a37f5f40f7bb178d197472`
- Observed at: 2026-10-16T16:57:59.758Z
- Decision: `1747111b-aaf6-4d62-9af4-1221f0e35416`
- Upstream agent run: `e3e44a49-943c-49d5-bab9-863241955ea1`
- Validation run: `9f7743c8-34c4-480d-b322-ff926f711ef3`

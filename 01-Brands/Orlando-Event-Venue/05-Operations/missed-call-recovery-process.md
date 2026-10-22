---
brain_note_id: "note:560ac8a0-4515-41e4-b67e-b572802948cc"
canonical_key: "missed-call-recovery-process"
brand_id: "orlando_event_venue"
---
# Missed-Call Recovery Process

## Canonical Statement

- **process**: OEV uses a 4-touch Missed-Call Recovery sequence over 4 days to convert missed inbound calls. The sequence uses automated SMS and email, with a 60-second trigger for the first touch. It is designed to capture event dates and move leads into the standard booking cadence.
- **rule**: The Missed-Call Recovery sequence must be stopped immediately if the contact replies, answers a call, books an event, or is tagged as 'oev-not-a-fit'.

## Evidence Log

- 2026-10-22T01:46:12.139Z — `clickup_doc_page:8cqnrff-4977/8cqnrff-31437`
  - `e1` (source_body): This sequence is 4 touches over 4 days. The moment they reply with a date, they exit this sequence and enter the standard cadence at Day 0.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-4977/8cqnrff-31437`
- Source hash: `6aa66d45c80cd521b493ced137f49a1b5452f2a3dce979df4a180679601305e7`
- Observed at: 2026-10-22T01:46:12.139Z
- Agent run: `51cebff5-87b9-4c91-918e-42204e859158`
- Validation run: `2fba4bb0-17e4-4b94-a1b8-e2cecccf48d7`

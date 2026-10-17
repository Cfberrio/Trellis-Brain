---
brain_note_id: "note:0d890fb4-e730-459d-9c87-109ed91b1db2"
canonical_key: "catering-automation-workflow-logic"
brand_id: "cheese_to_share"
---
# Catering Automation Workflow Logic

## Canonical Statement

- **process**: The catering automation workflow uses an inbound webhook to upsert contacts and find or update opportunities in the 'CTS Catering Orders' pipeline based on the 'order_id'.
- **rule**: Opportunity stages in the catering pipeline are determined by specific flag combinations: 'to_delivered' requires 'is_fully_paid' and 'event_ended' to be true; 'to_balance_paid' requires 'is_staffed' and 'is_fully_paid' to be true.
- **process**: The system handles payment retries using an 'attempt_label' logic, distinguishing between 'short_notice' and 'long_notice' scenarios for balance due reminders.

## Evidence Log

- 2026-10-17T00:41:47.674Z — `clickup_doc_page:8cqnrff-19297/8cqnrff-25217`
  - `e1` (source_body): Find Opportunity by CTS Order ID... Update opportunity... Pipeline CTS Catering Orders Pipeline Stage... Branches → to_delivered 14 is_fully_paid Is true And event_ended Is true... Split - Short Notice vs Long Notice... attempt_label Is balance_retry_1

## Provenance

- Source: `clickup_doc_page` `8cqnrff-19297/8cqnrff-25217`
- Source hash: `23af90c162e289dc9208e9bd154be62acd17e466415506fe5743796f8bdb3e43`
- Observed at: 2026-10-17T00:41:47.674Z
- Agent run: `cbe8dea7-c988-4c1f-b1b7-f2d0d643fcd0`
- Validation run: `c651f612-284e-4b8b-b5eb-d34031fc4dda`

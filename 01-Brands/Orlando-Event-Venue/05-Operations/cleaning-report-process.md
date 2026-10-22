---
brain_note_id: "note:16b8e1f1-130a-47a6-9646-bdfdef772dff"
canonical_key: "cleaning-report-process"
brand_id: "orlando_event_venue"
---
# Cleaning Report Process

## Canonical Statement

- **process**: Cleaning staff must complete a post-event cleaning report in the backend for every reservation. The report requires specific media uploads (front door, main area, tables/chairs, bathrooms, kitchen, and optional deep cleaning) and a checklist confirming tasks like floor cleaning, trash removal, equipment storage, and securing the venue.
- **process**: The cleaning report includes an inventory check. If items are marked as 'low' or 'out', an automated 'inventory_update_needed' event is triggered. Maintenance notes in the report trigger an admin ticket.

## Evidence Log

- 2026-10-22T01:39:56.127Z — `clickup_doc_page:8cqnrff-4637/8cqnrff-2417`
  - `e1` (source_body): The staff member will upload this report to the specific reservation they are assigned to in the backend. ... Trigger an automation if any item is low or out. ... If maintenance notes exist → create admin ticket

## Provenance

- Source: `clickup_doc_page` `8cqnrff-4637/8cqnrff-2417`
- Source hash: `aa904868657b7e1d930b9439d04a51b23e7d37f2afab99ed78a38892722e84b8`
- Observed at: 2026-10-22T01:39:56.127Z
- Agent run: `c3a75861-2134-4550-8013-d69129cdf933`
- Validation run: `1e8d4640-9334-4b38-8266-df25454c7fb5`

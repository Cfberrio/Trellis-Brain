---
brain_note_id: "note:fb491468-3743-4de2-a602-c389be0da1fd"
canonical_key: "discipline-rift-ghl-cost-optimization"
brand_id: "trellis_core"
---
# Discipline-Rift-GHL-Cost-Optimization

## Canonical Statement

- **fact**: The primary driver of GoHighLevel wallet depletion for Discipline Rift is 'premium workflow executions' (inbound webhooks triggering email workflows), accounting for approximately 51% of costs, while SMS/MMS usage accounts for 24%.
- **decision**: To reduce GHL costs, the recommended technical solutions are: 1) Replace inbound webhooks with GHL API contact updates and tagging to trigger workflows (saving $30-40/mo), or 2) Migrate email sending to Gmail SMTP (saving $40-45/mo).

## Evidence Log

- 2026-11-12T03:52:35.660Z — `clickup:86e3xyte7`
  - `e1` (source_child): October answered: the main driver is DR premium workflow executions, not SMS or email sends. ... Breakdown: premium workflow executions $40.76 (51%), SMS/MMS $19.35 (24%)
  - `e2` (source_child): 1. Keep GHL, change how the workflow starts. ... DR stops calling the Inbound Webhook. It updates the contact through the GHL API (free) and adds a tag ... 2. Send these emails from DR directly (Gmail SMTP).

## Provenance

- Source: `clickup` `86e3xyte7`
- Source hash: `d19c29719d96940c78c2e3b74623a0f7ccf4cf1f56a73a23b6f2f53d0d278112`
- Observed at: 2026-11-12T03:52:35.660Z
- Agent run: `55039ccb-57f4-4255-bac1-956dd7dcac9c`
- Validation run: `87f90878-b8f2-4df5-adc6-b163a434edbc`

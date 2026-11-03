---
brain_note_id: "note:beb8f4c4-39f9-4b43-b651-051a10df194f"
canonical_key: "discipline-rift-ghl-email-cost-analysis"
brand_id: "trellis_core"
---
# Discipline Rift - GHL Email Cost Analysis

## Canonical Statement

- **fact**: In October 2026, email-related costs accounted for 61% of the Discipline Rift GHL wallet usage ($48.97 of $79.91).
- **fact**: GHL premium workflow triggers (Inbound Webhook) cost $0.01 per execution, which significantly exceeds the cost of the email delivery itself ($0.000675).
- **fact**: Discipline Rift utilizes both LC Email (billed via GHL wallet) and Gmail SMTP (outside GHL, cost $0) for different communication types.

## Evidence Log

- 2026-11-03T20:13:10.286Z — `clickup:86e3xyte9`
  - `90170268745304` (source_child): Email is 61% of October wallet usage ($48.97 of $79.91), and almost all of it is the $0.01 webhook trigger, not the email itself. ... One workflow email costs $0.010675 ($0.01 trigger + $0.000675 delivery). One campaign email costs $0.000675.

## Provenance

- Source: `clickup` `86e3xyte9`
- Source hash: `7df3551bf891ecdbf93068406784494641555af4d0b8033eae59116e447f27b4`
- Observed at: 2026-11-03T20:13:10.286Z
- Agent run: `9d15aa04-1e24-48f2-a6b0-ffa1ddcd9479`
- Validation run: `20c4927b-769e-4da4-b411-8786b2a2dd8f`

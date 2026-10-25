---
brain_note_id: "note:da4d4bab-7cb3-4ea5-819a-4db20991a0ab"
canonical_key: "instagram-research-automation-process"
brand_id: "cheese_to_share"
---
# Instagram Research Automation Process

## Canonical Statement

- **process**: Instagram research automation for Cheese To Share is scheduled for Sundays at 3:00 AM to avoid resource conflicts with other brand automations.
- **rule**: To prevent cross-brand data contamination, automations must maintain strict separation of brand-specific IDs, templates, and recipients. A validation guardrail should be implemented to verify that the brand context matches the output before sending reports.
- **process**: If an automated report fails to arrive, the operational contingency is to notify the team immediately for manual execution.

## Evidence Log

- 2026-10-25T01:19:16.007Z — `clickup_doc_page:8cqnrff-8597/8cqnrff-6897`
  - `e1` (source_body): Sábado 3:00 AM: corre DR. Domingo 3:00 AM: corre Cheese to Share. ... Asegurar separación estricta por brand: IDs, templates, destinatarios, y cualquier “default” por workflow. Agregar un “guardrail” simple: antes de enviar el email, validar que brand = DR implique subject/from/sheet/reference de DR

## Provenance

- Source: `clickup_doc_page` `8cqnrff-8597/8cqnrff-6897`
- Source hash: `054707fd4cdd0e1155b0d37890a7117e7b0cf9f3eb26209140897a1f0543a1a9`
- Observed at: 2026-10-25T01:19:16.007Z
- Agent run: `ad9cefa2-70a5-49a2-8585-7ff6d2aec2db`
- Validation run: `ddc8285b-85f7-462d-ab4a-0b7171f540f1`

---
brain_note_id: "note:6bfee7fb-7098-4775-a536-801283d8b45f"
canonical_key: "trellis-platform-roadmap-standards"
brand_id: "trellis_core"
---
# Trellis Platform Roadmap and Technical Standards

## Canonical Statement

- **decision**: Trellis branding (logos, palette, typography) is centralized in the code to allow for swaps without refactoring.
- **rule**: Email deliverability must migrate to a verified domain with SPF/DKIM/DMARC or an API like Resend once a Trellis domain is available to handle volume and avoid spam.
- **decision**: The Trellis MVP excludes SMS verification, payment collection, advanced reminders, client portals, and CRM integrations.
- **fact**: The Trellis admin system includes Google-only authentication, onboarding, signer downloads, suspension guards, and automatic expiration.

## Evidence Log

- 2026-10-18T04:53:54.816Z — `clickup_doc_page:8cqnrff-22317/8cqnrff-31037`
  - `e1` (source_body): Branding Trellis — integrar logos, paleta, tipografías e íconos... El branding está centralizado en el código para hacer el swap sin refactor.
  - `e2` (source_body): Cuando exista dominio Trellis, migrar a dominio verificado con SPF/DKIM/DMARC (o a una API HTTP tipo Resend) para volumen y entregabilidad.
  - `e3` (source_body): Fuera de alcance del MVP... verificación SMS/identidad fuerte · cobro de pagos · recordatorios programados avanzados · carpetas · portales de cliente
  - `e4` (source_body): Se agregaron: auth Google-only + onboarding, descarga del firmante, guard de suspensión, anular/cancelar y expiración automática.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22317/8cqnrff-31037`
- Source hash: `1b8fd05fd0085fd165e3bb3bb14e325709d5b4eec2f2062d45037cc48da9b819`
- Observed at: 2026-10-18T04:53:54.816Z
- Agent run: `6756dcab-59d9-4447-901c-6cadf88ca333`
- Validation run: `c71d9f12-8812-44b5-98cb-a844adc9a803`

---
brain_note_id: "note:cbac5a3b-4027-4e06-ab46-8df26e982248"
canonical_key: "codex-adversarial-review-integration"
brand_id: "trellis_core"
---
# Codex-Adversarial-Review-Integration

## Canonical Statement

- **decision**: OpenAI Codex is adopted as a secondary code engine for Trellis repositories, specifically for adversarial review of diffs and mechanical tasks with closed specifications, while Claude Code remains the primary orchestrator and decision-maker.
- **rule**: Codex must not be used for brand voice, cross-brand work, open-ended specifications, or deployments. Its primary value is independent verification of changes before they reach production.
- **process**: Repositories must utilize an AGENTS.md file to provide Codex with context (stack, test/lint commands, prohibitions, and known repo constraints) to ensure independent and safe verification.

## Evidence Log

- 2026-10-26T01:28:52.027Z — `clickup_doc_page:8cqnrff-24517/8cqnrff-37097#brand=trellis_core`
  - `e1` (source_body): Se incorporó OpenAI Codex como segundo motor de código con un rol acotado — revisor adversarial de diffs y ejecutor de trabajo mecánico con especificación cerrada — mientras Claude Code sigue siendo el cerebro que decide, contextualiza y es dueño del cambio.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-24517/8cqnrff-37097#brand=trellis_core`
- Source hash: `aaaee227e1f3dbbb615c520b925b66e883cd06aa188f0c496708855d798b55e0`
- Observed at: 2026-10-26T01:28:52.027Z
- Agent run: `8eb00af9-c900-4241-9a0a-30da7b469ce3`
- Validation run: `4864586e-4094-4760-8e16-00b3c9f4a331`

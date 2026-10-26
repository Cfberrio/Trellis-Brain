---
brain_note_id: "note:6016c4f2-3ecb-4223-883f-52cb199c8c35"
canonical_key: "oev-development-process-codex"
brand_id: "orlando_event_venue"
---
# OEV Development Process - Codex Adversarial Review

## Canonical Statement

- **process**: OEV utilizes OpenAI Codex as an adversarial review engine for code changes. Codex operates based on instructions defined in an AGENTS.md file in the repository, which specifies constraints such as prohibitions on publishing, touching environment variables, or crossing repository boundaries.
- **rule**: Codex is restricted from orchestrating, handling brand voice, or performing deployments; its primary value is independent verification of code changes before they reach production.

## Evidence Log

- 2026-10-26T01:29:50.081Z — `clickup_doc_page:8cqnrff-24517/8cqnrff-37097#brand=orlando_event_venue`
  - `e1` (source_body): Se incorporó OpenAI Codex como segundo motor de código con un rol acotado — revisor adversarial de diffs y ejecutor de trabajo mecánico con especificación cerrada — mientras Claude Code sigue siendo el cerebro que decide, contextualiza y es dueño del cambio.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-24517/8cqnrff-37097#brand=orlando_event_venue`
- Source hash: `aaaee227e1f3dbbb615c520b925b66e883cd06aa188f0c496708855d798b55e0`
- Observed at: 2026-10-26T01:29:50.081Z
- Agent run: `b2a8c286-57bf-48db-a0a2-7f1c9bf06ea8`
- Validation run: `b45b99ad-2f80-4918-8f0d-9b1d811fa9e7`

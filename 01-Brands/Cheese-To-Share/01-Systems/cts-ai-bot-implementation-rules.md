---
brain_note_id: "note:27ac2a0e-f9e7-448e-bfc6-e61344f4936f"
canonical_key: "cts-ai-bot-rules"
brand_id: "cheese_to_share"
---
# CTS AI Bot Implementation Rules

## Canonical Statement

- **process**: AI draft bots for customer communication must operate by posting drafts as internal comments in GHL for human review, never as direct auto-replies, to mitigate risk.
- **rule**: System grounding must use dynamic data (e.g., catering menus, availability) injected from the database rather than static facts in the prompt to ensure accuracy.
- **rule**: The current date and time must be injected into all AI bot calls to enable time-sensitive reasoning (e.g., 'this Saturday', 'next season').
- **rule**: Safety policies (e.g., score gates) must be enforced in code, not relied upon as instructions within the prompt.

## Evidence Log

- 2026-10-21T18:16:41.955Z — `clickup_doc_page:8cqnrff-22037/8cqnrff-30277#brand=cheese_to_share`
  - `e1` (source_body): el bot postea [AI DRAFT — copy/edit/send manually] como InternalComment en GHL; un humano copia/edita/envía.
  - `e2` (source_body): cada llamada inyecta datos vivos: ACTIVE_PROGRAMS... CATERING_MENU (CTS: pillars+items+policies)... La regla que quedó: facts estables y reconciliados por el founder viven en el prompt... datos que cambian viven en la DB y se inyectan
  - `e3` (source_body): inyectar CURRENT_DATETIME (fecha, día de semana, hora, timezone del negocio) en TODAS las llamadas de TODAS las marcas.
  - `e4` (source_body): una política de seguridad que depende de que el modelo se auto-limite no es una política — es una sugerencia. El enforcement va en código

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22037/8cqnrff-30277#brand=cheese_to_share`
- Source hash: `af1301a3168bf1287525031c703b5abe0d7db3e39a5a8a3b99bfe6617309f3cd`
- Observed at: 2026-10-21T18:16:41.955Z
- Agent run: `8296bbc3-50a7-4864-9b5f-22a1c461e0f0`
- Validation run: `1c2b2f18-4222-4d9c-b0bc-a95f8df57756`

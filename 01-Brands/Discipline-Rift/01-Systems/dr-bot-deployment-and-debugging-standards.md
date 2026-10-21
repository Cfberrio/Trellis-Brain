---
brain_note_id: "note:f5776355-3a32-4e87-80e2-5276a80b1536"
canonical_key: "dr-bot-deployment-standards"
brand_id: "discipline_rift"
---
# DR Bot Deployment and Debugging Standards

## Canonical Statement

- **rule**: After every agent-based deployment, the cron job URL must be manually verified to ensure it points to the correct function, as agent-generated function names are not stable contracts.
- **process**: Every pipeline with grounding requires a 'debug_grounding' endpoint that accepts contact identifiers (email/phone) to reproduce the exact grounding context the model sees, without triggering external side effects.

## Evidence Log

- 2026-10-21T18:17:09.191Z — `clickup_doc_page:8cqnrff-22037/8cqnrff-30337#brand=discipline_rift`
  - `e1` (source_body): Regla nueva del método: después de cada deploy vía agente, verificar a qué URL apunta el cron. El nombre de función no es un contrato estable cuando deploya un agente. ... Patrón empaquetable: todo pipeline con grounding necesita un endpoint que muestre el grounding crudo.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22037/8cqnrff-30337#brand=discipline_rift`
- Source hash: `aeab1d244b3e3e6026e94c7cccbe4a58c5fa7f635921a84835b9ba5e13d47523`
- Observed at: 2026-10-21T18:17:09.191Z
- Agent run: `2888187d-f548-430b-b32b-6270f2457f9b`
- Validation run: `90dae952-31d2-471d-98e6-6215be0ab2f7`

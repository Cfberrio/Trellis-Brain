---
brain_note_id: "note:f7e409d1-6c79-42f8-9fc5-5d8c2631cd54"
canonical_key: "oev-grounding-deployment-standards"
brand_id: "orlando_event_venue"
---
# OEV Grounding and Deployment Standards

## Canonical Statement

- **process**: OEV uses a two-layer grounding architecture: a 'catalog layer' for generic data (programs, menu, availability) and a 'contact layer' for personal context (parent, order, booking) injected via email/phone lookup to ensure privacy and token efficiency.
- **rule**: After every agent-led deployment, the system must verify the cron job URL via 'SELECT * FROM cron.job' to ensure the function pointer is correct, as function names are not stable contracts during agent deploys.

## Evidence Log

- 2026-10-21T18:18:19.559Z — `clickup_doc_page:8cqnrff-22037/8cqnrff-30337#brand=orlando_event_venue`
  - `e1` (source_body): Decisión de arquitectura: dos capas de grounding... Capa catálogo (por marca, 1 query por corrida)... Capa contacto (por mensaje, matched email→phone last-7): PARENT_CONTEXT / ORDER_CONTEXT / BOOKING_CONTEXT.
  - `e2` (source_body): Regla nueva del método: después de cada deploy vía agente, verificar a qué URL apunta el cron. El nombre de función no es un contrato estable cuando deploya un agente.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22037/8cqnrff-30337#brand=orlando_event_venue`
- Source hash: `aeab1d244b3e3e6026e94c7cccbe4a58c5fa7f635921a84835b9ba5e13d47523`
- Observed at: 2026-10-21T18:18:19.559Z
- Agent run: `5efbe480-dd20-4c0a-b903-a74e4a09d101`
- Validation run: `c8812807-df2b-4a61-9bc1-4e1e56ddb099`

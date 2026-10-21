---
brain_note_id: "note:aa059616-ca73-4fdb-8d08-dc93caad2abf"
canonical_key: "cts-bot-architecture-rules"
brand_id: "cheese_to_share"
---
# CTS Bot Architecture and Deployment Rules

## Canonical Statement

- **rule**: After every deploy via an agent, the system must verify the cron job URL, as function names are not stable contracts during automated deployments.
- **rule**: Bot grounding must be split into two layers: a 'Catalog' layer for generic data (menus, availability) and a 'Contact' layer for personalized data (orders, booking context) to ensure privacy and efficiency.

## Evidence Log

- 2026-10-21T18:17:42.401Z — `clickup_doc_page:8cqnrff-22037/8cqnrff-30337#brand=cheese_to_share`
  - `e1` (source_body): Regla nueva del método: después de cada deploy vía agente, verificar a qué URL apunta el cron. El nombre de función no es un contrato estable cuando deploya un agente.
  - `e2` (source_body): Decisión de arquitectura: dos capas de grounding. Capa catálogo (por marca, 1 query por corrida)... Capa contacto (por mensaje, matched email→phone last-7)

## Provenance

- Source: `clickup_doc_page` `8cqnrff-22037/8cqnrff-30337#brand=cheese_to_share`
- Source hash: `aeab1d244b3e3e6026e94c7cccbe4a58c5fa7f635921a84835b9ba5e13d47523`
- Observed at: 2026-10-21T18:17:42.401Z
- Agent run: `f56534a9-a0ad-4d08-97e1-a3cea76b0c71`
- Validation run: `c7ad0182-1b1c-47cc-ba3e-393ce1a30fed`

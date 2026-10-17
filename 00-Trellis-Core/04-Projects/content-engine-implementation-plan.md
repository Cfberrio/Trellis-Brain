---
brain_note_id: "note:ea0b7e46-7714-4555-a2f7-2451db355714"
canonical_key: "content-engine-plan"
brand_id: "trellis_core"
---
# Content-Engine-Implementation-Plan

## Canonical Statement

- **process**: The Content Engine workflow follows a weekly cycle: Monday (Idea approval and engine execution), Tuesday (Draft review and feedback), Wednesday-Friday (Production and publication), and Month-end (Metric updates and training bank reconstruction).
- **decision**: The Content Engine training bank will be generated automatically from existing sources (social-metrics and vault DNA notes) rather than manual copy-pasting to maintain a single source of truth.
- **rule**: Content performance (winners) is defined by a 'winner_score' formula: (saved×3 + shares×3 + comments×2 + likes×1) / reach, prioritizing high-intent signals over raw distribution.
- **decision**: The initial implementation phase (v1) focuses exclusively on Instagram data, as it contains the most relevant historical content for the target brands.

## Evidence Log

- 2026-10-17T07:16:32.326Z — `clickup_doc_page:8cqnrff-20197/8cqnrff-31217`
  - `e1` (source_body): El ciclo semanal: Lunes (Ideas del backlog... Correr el engine), Martes (Revisar drafts), Mié–Vie (Producción y publicación), Fin de mes (Correr run_monthly.py. El banco se reconstruye solo).
  - `e2` (source_body): Principio: el banco es un artefacto generado, no un archivo que alguien mantiene a mano... se construye desde las fuentes que ya se actualizan solas.
  - `e3` (source_body): Propuesta — separar mérito de distribución: winner_score = (saved×3 + shares×3 + comments×2 + likes×1) / reach
  - `e4` (source_body): Decisión de alcance v1: solo Instagram. Razones: (a) es donde está el 100% del contenido real de DR y CTS... (c) es el único canal con saved.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-20197/8cqnrff-31217`
- Source hash: `35e762346e65a81bf8b35bc38fdb6300e9c35f2c53fee8d3c4006ec83630dcc9`
- Observed at: 2026-10-17T07:16:32.326Z
- Agent run: `f4312a86-494f-41d3-97de-7faf5adc78b4`
- Validation run: `0300beec-f694-4aec-8ba7-6121ff0dc336`

---
brain_note_id: "note:cc51f7c1-c393-4d29-aa1e-99414f358f5e"
canonical_key: "registration-search-filtering-logic"
brand_id: "discipline_rift"
---
# Registration Search and Filtering Logic

## Canonical Statement

- **decision**: Registration search results must be filtered by unique school ID (or exact name) rather than text 'contains' matching to prevent parents from registering at the wrong campus when school names are nested (e.g., Avalon vs Pinecrest Avalon).
- **rule**: Free-typed school searches must follow a specific ranking order: exact name matches first, followed by 'starts with' matches, with all other 'contains' matches grouped under a 'Similar schools' divider.
- **process**: Registration results must be grouped under a school header (name + address) to ensure parents can distinguish between different campuses before selecting a team.

## Evidence Log

- 2026-10-15T00:39:40.994Z — `clickup:86e3pc59d`
  - `e1` (source_body): Root cause: results are filtered with a text "contains" match. "Pinecrest Avalon Elementary School" contains "Avalon Elementary School", so it passes. Fix: Filter by school, not text... Rank free-typed searches... Group results under a school header.
  - `e2` (source_child): Hecho y LIVE en disciplinerift.com (commit 103d114). Filtro por escuela: al tocar una sugerencia se pasa el id (?schoolId=) y sale solo esa escuela. Texto libre ordenado: nombre exacto → solo esa escuela; "empieza con" primero; el resto bajo un divisor "Similar schools".

## Provenance

- Source: `clickup` `86e3pc59d`
- Source hash: `0f02604925c1ce6e74c25d4505cd0a38d4494b0743a73f5b7835a5efe157bbda`
- Observed at: 2026-10-15T00:39:40.994Z
- Agent run: `985634c8-9563-4782-a2a2-1b411687e6fe`
- Validation run: `a477b853-09b3-4268-a1b2-5356e533dfed`

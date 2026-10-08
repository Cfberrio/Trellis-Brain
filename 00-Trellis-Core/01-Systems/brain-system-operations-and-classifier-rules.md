---
brain_note_id: "note:54c6290e-88fe-49df-b805-fce0a94dd501"
canonical_key: "brain-system-operations"
brand_id: "trellis_core"
---
# Brain System Operations and Classifier Rules

## Canonical Statement

- **decision**: The Brain execution schedule is set to run every 2 hours to prevent GitHub Actions from skipping runs.
- **fact**: Brand classifier v2 includes brand-specific profiles, St. Joseph handling, NO_CONTENT detection, and a trivial chat filter to reduce AI costs.
- **rule**: To prevent write rejections due to file format differences (Windows vs Repo), the Brain now re-reads and retries notes that changed externally instead of failing.
- **process**: Before creating a new note, the Brain checks if the source already has an existing note and updates it to prevent duplicates.

## Evidence Log

- 2026-10-07T20:23:01.864Z — `clickup:86e3kcwj2`
  - `e1` (source_child): Desplegado: worker + /brain con clasificador de marca v2... incluye: clasificador v2 (perfiles por marca, St. Joseph, NO_CONTENT, filtro de chats triviales)
  - `e2` (source_child): Las corridas pasan a cada 2 horas... Windows queda guardando en el mismo formato del repo... Si una nota cambió por fuera, el Brain la vuelve a leer y reintenta... Antes de crear una nota nueva, el Brain mira si esa misma fuente ya tiene una, y la actualiza.

## Provenance

- Source: `clickup` `86e3kcwj2`
- Source hash: `df26e86333197e5746d349479ad0410566a2000b897fb78d923b130713559bbc`
- Observed at: 2026-10-07T20:23:01.864Z
- Agent run: `28580fc4-e240-46d1-80d5-8a23b2ff6dcc`
- Validation run: `e474fdd9-050a-42b7-8af6-d86e08990a68`

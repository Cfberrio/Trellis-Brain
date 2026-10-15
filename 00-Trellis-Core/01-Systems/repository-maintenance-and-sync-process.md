---
brain_note_id: "note:909c7535-828f-4d44-b92d-954e4367c9d3"
canonical_key: "repo-maintenance-sync"
brand_id: "trellis_core"
---
# Repository Maintenance and Sync Process

## Canonical Statement

- **process**: To upload changes to the Trellis Brain repository: Open the Obsidian folder in Cursor, open Claude Code, and request a commit and push using 'git push origin main https://github.com/Cfberrio/Trellis-Brain.git'.
- **process**: To update the local Trellis Brain vault with remote changes: Open the folder in Cursor, open Claude Code, and request a pull using 'git pull origin main https://github.com/Cfberrio/Trellis-Brain.git'.
- **rule**: When encountering errors during repository updates, do not attempt manual fixes; copy the full error and ask Claude Code to explain and fix it step-by-step.

## Evidence Log

- 2026-10-15T21:36:17.038Z — `clickup_doc_page:8cqnrff-15737/8cqnrff-17957`
  - `e1` (source_body): Pídele: Claude, sube los cambios de Trellis Brain al repo. Haz el commit necesario y luego push. Comando: git push origin main https://github.com/Cfberrio/Trellis-Brain.git
  - `e2` (source_body): Pídele: Claude, actualiza Trellis Brain con los últimos cambios del repo. Haz pull y dime si quedó actualizado. Comando: git pull origin main https://github.com/Cfberrio/Trellis-Brain.git
  - `e3` (source_body): Si algo falla: No inventes. No borres cosas. No intentes arreglarlo solo. Copia el error completo y dile a Claude: Claude, me salió este error en Trellis Brain. Explícame qué pasó y arréglalo paso a paso.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-15737/8cqnrff-17957`
- Source hash: `54a04f07ac9158a670fd82d1797a187b43a1a1c77df1a8dff016dcbad51e61b5`
- Observed at: 2026-10-15T21:36:17.038Z
- Agent run: `4f9eca3a-9996-4b6d-b7d8-0dc1ce379ffc`
- Validation run: `7e838fde-f511-4da6-b7f0-6e24eaecd26f`

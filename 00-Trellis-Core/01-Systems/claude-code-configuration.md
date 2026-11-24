---
brain_note_id: "note:971d1a30-9d99-4630-b4a9-b466bb4edaf2"
canonical_key: "claude-code-configuration"
brand_id: "trellis_core"
---
# Claude-Code-Configuration

## Canonical Statement

- **process**: To enable 'Bypass permissions' in Claude Code within Cursor, set 'claudeCode.allowDangerouslySkipPermissions' to true in settings, reload the window, and select 'Bypass permissions' in the Claude panel mode selector.
- **rule**: Use 'Bypass permissions' only in internal repositories (CLAUDE CODE, DR, OEV, CTS) for long tasks; avoid it when tasks involve money, production, client shipments, or .env files.

## Evidence Log

- 2026-11-24T23:10:41.394Z — `clickup_doc_page:8cqnrff-27877/8cqnrff-41437`
  - `e1` (source_body): Usarlo solo en repos nuestros (CLAUDE CODE, DR, OEV, CTS) y en tareas largas donde aprobar 40 veces no aporta. No usarlo cuando la tarea toca dinero, producción, envíos a clientes o .env: ahí conviene que pregunte.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-27877/8cqnrff-41437`
- Source hash: `ad2c8fb3466f8b64aa118c9ae40081ac14e3d03fc4917674b84e68745b1637eb`
- Observed at: 2026-11-24T23:10:41.394Z
- Agent run: `0a7fc8f8-05bf-4700-b8a0-fda642a8a83e`
- Validation run: `fb1ae96a-29a7-4679-872b-91e26d115f13`

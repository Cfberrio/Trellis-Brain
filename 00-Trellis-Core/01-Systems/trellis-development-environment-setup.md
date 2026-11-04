---
brain_note_id: "note:329bfc44-4dbb-422a-84a7-847817dd51cf"
canonical_key: "trellis-development-environment-setup"
brand_id: "trellis_core"
---
# Trellis-Development-Environment-Setup

## Canonical Statement

- **process**: The standard Trellis development environment setup on macOS includes Cursor, Homebrew, Git, GitHub CLI, Node.js, Claude Code (with Remote Control), and Obsidian (with Local REST API and Git plugin).
- **rule**: Claude Code MCP integration with Obsidian should use HTTP on loopback (127.0.0.1) if HTTPS certificate constraints prevent connection.
- **process**: Obsidian Git plugin configuration for Trellis-Core vaults requires specific intervals (5 minutes) for auto-pull/push and must be enabled to ensure synchronization between local files and GitHub.

## Evidence Log

- 2026-11-04T20:30:38.770Z — `clickup_doc_page:8cqnrff-18157/8cqnrff-22717`
  - `e1` (source_body): Mapa del sistema: Mac (Apple Silicon) ├── Cursor: editor + terminal integrada ├── Git + gh: versiones y acceso a repositorios GitHub ├── Node.js/npm/npx: herramientas de desarrollo ├── Claude Code: agente que corre en la terminal └── Obsidian: vault TRELLIS-BRAIN
  - `e2` (source_body): Para ese equipo usamos la alternativa HTTP únicamente en loopback local que documenta el plugin: Obsidian → Settings → Local REST API → Enable HTTP server = ON.
  - `e3` (source_body): Auto commit interval (minutes) 5. Auto push interval (minutes) 5 (¡no 0!). Auto pull interval (minutes) 5 (¡no 0!).

## Provenance

- Source: `clickup_doc_page` `8cqnrff-18157/8cqnrff-22717`
- Source hash: `3f304f12864e5fded643f2529c4f39d9ad05c17033b5b820c4e397b7b45b9329`
- Observed at: 2026-11-04T20:30:38.770Z
- Agent run: `21b078c2-6363-45d7-bbbf-e762c81c7842`
- Validation run: `96c61dbe-a941-418f-b7cf-42bedb858b58`

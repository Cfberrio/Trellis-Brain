---
brain_note_id: "note:78e5d1cf-6391-47ba-9039-ddf994bf8905"
canonical_key: "claude-code-session-setup"
brand_id: "trellis_core"
---
# Claude-Code-Session-Setup

## Canonical Statement

- **process**: Claude Code sessions require a standardized setup including specific hooks, MCPs, and environment variables to ensure consistent performance and token efficiency.
- **rule**: To optimize token usage, sessions should be kept short (new session per task), limited to two concurrent sessions, and use transfer notes instead of long conversation histories.
- **fact**: Headroom is currently disabled on specific machines due to version 0.44 compatibility issues; Composio is classified as an MCP, not a plugin.

## Evidence Log

- 2026-11-18T04:36:21.337Z — `clickup:1dfqjx6v2y9`
  - `e1` (source_body): Buenas prácticas de tokens (del análisis del 12 nov): sesión nueva por tarea, máximo 2 sesiones a la vez, nota de traspaso en vez de retomar conversaciones largas.
  - `e2` (source_child): Headroom en mi Mac está apagado desde el 13 nov porque la versión 0.44 rompe los pedidos de Claude... Composio es un MCP, no un plugin.

## Provenance

- Source: `clickup` `1dfqjx6v2y9`
- Source hash: `734b15cdb8112f38cb98a8833fc942da16f6385eae81455afc0a08397a76017d`
- Observed at: 2026-11-18T04:36:21.337Z
- Agent run: `a1f5e3c5-44dc-4977-a53a-7f7604e769bd`
- Validation run: `28bfb167-4998-43fd-80d3-bb55bf0bb072`

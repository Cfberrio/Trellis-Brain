---
brain_note_id: "note:b5e2097d-6f67-44cd-ad91-397801023bfa"
canonical_key: "claude-interaction-standards"
brand_id: "trellis_core"
---
# Claude Interaction Standards

## Canonical Statement

- **definition**: A Skill is a reusable instruction that Claude executes via slash commands (e.g., /meta, /dr) to define how it thinks, formats, or analyzes for a specific brand or task.
- **definition**: MCP/Connections are systems that allow Claude to read, write, or execute actions in external platforms like Notion, GHL, Obsidian, or ClickUp.
- **definition**: Workflows are processes that combine skills, connections, and sequential steps to complete a complex task (e.g., Website Motion Graphics, Repo Update).
- **rule**: Classification Rule: If it changes how Claude thinks/responds via slash command, it is a Skill. If it connects to an external tool, it is an MCP/Connection. If it combines multiple steps/tools for a task, it is a Workflow.

## Evidence Log

- 2026-10-15T21:38:13.851Z — `clickup_doc_page:8cqnrff-15837/8cqnrff-22837`
  - `e1` (source_body): Una skill es una instrucción reutilizable que Claude puede ejecutar cuando la llamamos con un comando tipo slash... sirve para decirle a Claude: cómo pensar, qué formato usar, qué proceso seguir.
  - `e2` (source_body): MCP / Conexiones... permiten que Claude lea, escriba, consulte o trabaje con plataformas externas.
  - `e3` (source_body): Los workflows son procesos que combinan skills, conexiones y pasos para lograr una tarea completa.
  - `e4` (source_body): Si se ejecuta con un slash y solo cambia cómo Claude piensa o responde: Es una Skill. Si conecta a Claude con una herramienta externa... Es un MCP / Connection. Si combina varias cosas... Es un Workflow.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-15837/8cqnrff-22837`
- Source hash: `a86b47fe77d15feaa76294b7cb19655a3154cfeb36ec3dd390fb2885c976a17b`
- Observed at: 2026-10-15T21:38:13.851Z
- Agent run: `a6a4f9ef-493d-4be4-88ef-812b0c6fc328`
- Validation run: `29858653-4b1d-4592-94ce-806db6a8c2f5`

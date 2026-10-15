---
brain_note_id: "note:01b6e592-ca58-4c8c-a3b5-05b0049e2753"
canonical_key: "claude-code-skills-inventory"
brand_id: "trellis_core"
---
# Claude Code Skills Inventory and Setup

## Canonical Statement

- **fact**: Trellis utilizes approximately 145 Claude Code skills, categorized into marketplace plugins, git-cloned skills, and custom Trellis-specific skills.
- **process**: Marketplace plugins are installed via '/plugin marketplace add' followed by '/plugin install [skill]@[marketplace]'.
- **rule**: Custom Trellis skills (e.g., google-ads-*, ads-meta-*) are not in public repos; they must be accessed via the private Trellis repo and copied to ~/.claude/skills/.
- **rule**: Critical production skills like google-ads-phase* and ads-meta-dr-phase* must not be modified.

## Evidence Log

- 2026-10-15T21:43:04.645Z — `clickup_doc_page:8cqnrff-15837/8cqnrff-34957`
  - `e1` (source_body): Total Skills: ~145 (81 listados + 64 adicionales). Ubicaciones: ~/.claude/skills/ + ~/.agents/skills/
  - `e2` (source_body): Tipo A — Plugins de marketplace... Abrir Claude Code en la máquina nueva y correr, por cada marketplace: /plugin marketplace add... Luego instalar los plugins que se necesiten
  - `e3` (source_body): Tipo C — Skills custom Trellis... No existen en ningún repo público — solo viven en .claude/skills/ de este workspace. ...copiar .claude/skills/ a ~/.claude/skills/
  - `e4` (source_body): No modificar skills críticos (google-ads-*, ads-meta-*). Están en producción.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-15837/8cqnrff-34957`
- Source hash: `20cc5d18376a2f0e46a04e1ef94cfb5a5eab0be5e6a5c31227a7bddbc3b7c436`
- Observed at: 2026-10-15T21:43:04.645Z
- Agent run: `43406c4c-a648-489a-a4bd-5f3ac1a5448b`
- Validation run: `f121b591-b287-4968-acd3-0c5f87726ad6`

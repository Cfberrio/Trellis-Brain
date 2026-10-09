---
brain_note_id: "note:6066bc22-3d41-4b06-860d-ade7288cd5d3"
canonical_key: "obsidian-graph-config-maintenance"
brand_id: "trellis_core"
---
# Obsidian Graph Configuration Maintenance

## Canonical Statement

- **fact**: Obsidian graph view color groups fail to apply if the 'path:' queries in graph.json include a root folder prefix that does not match the current vault root (e.g., including 'Trellis-Brain/' when the vault is opened at the internal root).
- **rule**: When creating or fixing graph color groups, use paths relative to the vault root (e.g., starting with 00-Trellis-Core or 01-Brands) without any external wrapper folder prefixes.
- **process**: To manually edit .obsidian/graph.json, Obsidian must be closed first; otherwise, the application will overwrite manual changes with the version stored in memory upon closing.

## Evidence Log

- 2026-10-09T00:28:05.396Z — `clickup:86e3dhaqa`
  - `e1` (source_child): Causa raíz: no fue la actualización de Obsidian. Los 16 grupos de color en .obsidian/graph.json usaban path:"Trellis-Brain/..." — rutas escritas cuando Obsidian abría la carpeta envoltorio externa. ... Editado con Obsidian cerrado: Obsidian guarda graph.json desde memoria al cerrar.

## Provenance

- Source: `clickup` `86e3dhaqa`
- Source hash: `678766059f2f9438eba9a6732a81250d138ad722890e7b959a6039d2a8ba5863`
- Observed at: 2026-10-09T00:28:05.396Z
- Agent run: `7deb5ff2-d9d6-42ff-86f3-be309a139449`
- Validation run: `3e8c2715-75f0-4395-8f40-27a808acadfb`

---
brain_note_id: "note:c56e0a6d-5c43-4f9b-9bfa-ef5323921bc8"
canonical_key: "03-evidence-obsidian-setup-evidencia"
brand_id: "trellis_core"
---
# Obsidian Setup — Evidencia

## Canonical Statement

- **process**: Obsidian setup for Trellis Brain involves 4 steps: 1. Git pull for latest notes/config. 2. Install/Enable specific plugins (Local REST API, Breadcrumbs, Juggl, Excalidraw, Advanced Canvas, Portals, myBrain). 3. Close Obsidian (Cmd/Ctrl+Q) and run a specific Claude Code prompt to apply configuration from 00-Trellis-Core/Obsidian-Config/INSTALL.md. 4. Verify UI elements like Portals tabs and folder colors.
- **rule**: When applying Obsidian configuration via Claude Code, Obsidian must be completely closed (Cmd+Q/Ctrl+Q). If open, plugins will overwrite the new configuration with their current state, causing the setup to fail silently.
- **definition**: The Trellis Brain Obsidian environment uses Portals for folder-specific views, Advanced Canvas for 'Trellis Role' node coloring and 'Trellis Link' arrow typing, and Juggl for brand-based note coloring.

## Evidence Log

- 2026-10-16T17:03:42.000Z — `clickup_doc_page:8cqnrff-18177/8cqnrff-36737`
  - `e1` (source_body): Son 4 pasos y toma unos 5 minutos. Paso 1 — Bajá el vault git pull. Paso 2 — Instalá los plugins... Paso 3 — Cerrá Obsidian y corré el prompt... Paso 4 — Abrí Obsidian y revisá
  - `e2` (source_body): Primero cerrá Obsidian completo con Cmd+Q... Esto no es opcional. Con Obsidian abierto, los plugins reescriben su propia configuración encima de la nueva y no se aplica nada.
  - `e3` (source_body): Portals — Es el panel de tabs de la izquierda. Cada tab muestra solo su carpeta... Advanced Canvas — Trellis Role pinta el nodo según su función... Juggl — Colorea cada nota según su campo brand.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-18177/8cqnrff-36737`
- Source hash: `68d11efa17a7a41c2b70ad9a0f08f24e08c2ccae92b9ad35bfebfa5650a17d17`
- Observed at: 2026-10-16T17:03:42.000Z
- Decision: `9f08df3f-8ba5-4e37-9ae4-02191e53c8d1`
- Upstream agent run: `81af1a96-b75f-4ea3-a0fb-65baf2e87549`
- Validation run: `3920b6dc-9134-45d8-b1a0-9fa21a42f2e1`

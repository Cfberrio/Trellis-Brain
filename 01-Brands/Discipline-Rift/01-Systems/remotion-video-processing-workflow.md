---
brain_note_id: "note:187c09b7-b1be-4bd2-8b2c-d52c1870b859"
canonical_key: "remotion-video-processing-workflow"
brand_id: "discipline_rift"
---
# Remotion Video Processing Workflow

## Canonical Statement

- **process**: To process videos with Remotion in Cursor, files must be placed in a subfolder within the project's 'Public' directory to be accessible.
- **rule**: Video processing prompts should specify the exact file path, 30 FPS, 1080x1920 resolution for vertical video, and a maximum duration (e.g., 3 minutes).
- **process**: The Remotion workflow follows a sequence: use the Remotion Best Practices skill, provide the prompt with the video path, and execute using 'npm run dev'.
- **fact**: Remotion Studio allows for previewing compositions and exporting specific segments by defining frame ranges.

## Evidence Log

- 2026-10-16T16:53:41.174Z — `clickup_doc_page:8cqnrff-17597/8cqnrff-21557`
  - `e1` (source_body): Remotion solo toma videos desde Public... Vayan a la carpeta del proyecto. Busquen la carpeta Public. Dentro de Public, creen una subcarpeta para organizar su material.
  - `e2` (source_body): Asegúrate de definir: Ubicación del video (path exacto desde Public)... Resolución (ej: 1080x1920 si es vertical)... FPS (ej: 30 FPS)... Duración objetivo: máximo 3 min total.
  - `e3` (source_body): Este flujo se basa en una secuencia clara: 1. Skill (leer/usar el skill) 2. Prompt (pegar el prompt ya ajustado con ruta y requisitos) 3. Ejecutar (correr el proyecto)
  - `e4` (source_body): También puedes exportar solo un fragmento... Puede que tengas que definir el rango por fotogramas (frames).

## Provenance

- Source: `clickup_doc_page` `8cqnrff-17597/8cqnrff-21557`
- Source hash: `732be595606a74b2c07bcd5d959c09548fb2bf5eeeaf12e5a216e2da130de12a`
- Observed at: 2026-10-16T16:53:41.174Z
- Agent run: `b3fdc47b-07e8-4da6-bd25-4d169a7d480d`
- Validation run: `1bb850c8-5aa9-4fac-8ce4-1769953faac0`

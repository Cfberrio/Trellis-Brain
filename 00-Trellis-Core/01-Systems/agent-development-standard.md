---
brain_note_id: "note:02972a62-6ea1-4297-b836-48c9a71ccd6e"
canonical_key: "agent-development-standard"
brand_id: "trellis_core"
---
# Agent Development Standard

## Canonical Statement

- **rule**: Before creating any agent or automation, a meeting must be held with the relevant area expert to understand the real process and avoid assumptions.
- **process**: Agents are not built from scratch; they must use the OpenClaw instruction template/structure as a base for skills and agents.
- **process**: The agent development workflow follows a specific sequence: Area Meeting > Automatic Transcript > Instruction Extraction > OpenClaw Template Application > Technical Review by Kristen > Implementation > Testing.
- **rule**: Instructions for OpenClaw must be concrete and actionable (what, how, order, tone, limits) rather than ambiguous (e.g., 'be more charismatic').

## Evidence Log

- 2026-10-14T17:34:17.253Z — `clickup_doc_page:8cqnrff-12337/8cqnrff-12817`
  - `e1` (source_body): Antes de crear cualquier agente o automatización, debe hacerse una reunión con una persona del área correspondiente. Esa reunión existe para: entender el proceso real, sacar el paso a paso, evitar suposiciones, reducir retrabajo
  - `e2` (source_body): Los agentes no se construyen desde cero. La base para crear agentes debe salir de: el template / estructura de instrucciones de OpenClaw
  - `e3` (source_body): Flujo de trabajo: 1. Reunión con el área... 4. Uso del template base de OpenClaw... 5. Revisión técnica: Kristen revisa las instrucciones... 6. Implementación... 7. Pruebas y ajustes
  - `e4` (source_body): OpenClaw no responde bien a instrucciones ambiguas. No se debe escribir: “sé más carismático”... Se debe escribir: qué hacer, cómo hacerlo, en qué orden, con qué tono, con qué límites, qué resultado se espera

## Provenance

- Source: `clickup_doc_page` `8cqnrff-12337/8cqnrff-12817`
- Source hash: `a2c1b959143b66b7934c673eef69ac093f82e2daf7d3b1dc56fffd0b5ca496c8`
- Observed at: 2026-10-14T17:34:17.253Z
- Agent run: `d032a3bf-f35b-4817-9099-7f427e96205f`
- Validation run: `f5b8d7b6-8b71-4e27-9f01-53c95367e9b8`

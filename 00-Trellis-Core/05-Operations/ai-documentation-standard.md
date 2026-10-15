---
brain_note_id: "note:366b1cdf-1c65-46ef-b8d4-7fe28d7a8359"
canonical_key: "ai-documentation-standard"
brand_id: "trellis_core"
---
# AI Documentation Standard

## Canonical Statement

- **rule**: Every AI functionality, skill, workflow, API, prompt, or automation used or developed must be documented using the standardized 'Problem + Solution + Tool' format.
- **process**: Documentation must include a 1-3 minute video explaining the real problem, the solution found, the tool used, the process start point, usage instructions, results, and brand application.
- **rule**: Documentation must explicitly list the 'Setup Inicial' (initial setup) requirements, including necessary software (Claude Code, Node.js), repository access, API keys, and environment variables.
- **process**: Each Claude skill documentation must specify what it does, when to use it, required inputs, expected outputs, its location in the repository, and the execution command.
- **rule**: Security protocol: Never include actual passwords, tokens, or private API keys in documentation; instead, document the variable names and where to obtain them.

## Evidence Log

- 2026-10-15T17:23:58.382Z — `clickup_doc_page:8cqnrff-15457/8cqnrff-17617`
  - `e1` (source_body): cada vez que usen, prueben o desarrollen una funcionalidad de IA, skill de Claude, workflow, API, prompt o automatización, necesitamos documentarlo con este formato. Usar este formato: Problema + Solución + Herramienta
  - `e2` (source_body): Grabar un video de 1–3 minutos mostrando pantalla. El video debe explicar: 1. Qué problema real tenían 2. Qué solución encontraron 3. Qué herramienta usaron 4. Dónde empieza el proceso 5. Cómo se usa 6. Qué resultado genera 7. Cómo aplica dentro de Trellis o una marca
  - `e3` (source_body): Setup inicial. Antes de explicar cómo correr el skill, documenten qué necesita tener listo una persona antes de usarlo. Responder: ¿Necesita Claude? ¿Necesita Claude Code? ¿Necesita Node.js? ¿Necesita repo clonado? ¿Necesita API keys?
  - `e4` (source_body): Explicación del skill de Claude. Responder: Qué hace el skill, Cuándo se usa, Qué necesita recibir, Qué entrega, Dónde vive, Cómo se ejecuta.
  - `e5` (source_body): Seguridad y accesos. Nunca subir contraseñas, tokens privados o API keys visibles. Sí documentar: Dónde se consiguen, Qué tipo de acceso se necesita, Qué nombre tienen las variables.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-15457/8cqnrff-17617`
- Source hash: `1cdb8c9fb8a2941dbe693309745a0d08fac6fb417ba33242f551de5abb5d4a27`
- Observed at: 2026-10-15T17:23:58.382Z
- Agent run: `46c3b00a-c542-4f91-86df-286bbb2e529d`
- Validation run: `4907abf1-4005-4332-a904-2d18f0465038`

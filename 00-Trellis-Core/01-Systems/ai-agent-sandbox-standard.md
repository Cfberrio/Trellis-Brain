---
brain_note_id: "note:f27fcc3c-4272-4135-bb2d-ea9e90bb97a7"
canonical_key: "ai-agent-sandbox-standard"
brand_id: "trellis_core"
---
# AI-Agent-Sandbox-Standard

## Canonical Statement

- **process**: Trellis agents must operate within a sandbox environment—an isolated, disposable execution layer—to prevent unauthorized access to production systems, credentials, or sensitive data. The sandbox must enforce strict network, file system, and permission controls, with all actions logged and subject to human review before integration.

## Evidence Log

- 2026-11-19T04:16:08.909Z — `clickup:86e3zc343`
  - `e1` (source_body): Evaluar una prueba de concepto de sandbox como capa de ejecución controlada para los agentes... Aislar una tarea de prueba. Utilizar un entorno desechable con una copia de un repositorio y datos sintéticos o anonimizados.
  - `e2` (source_child): Es un cuarto de pruebas con la puerta cerrada. El agente entra, trabaja adentro y no puede tocar nada de afuera. Nosotros vemos por la ventana todo lo que hace, porque cada paso queda en un registro. Cuando termina, se bota el cuarto completo.
  - `e3` (source_child): Hecho: ya tenemos un ambiente de pruebas (sandbox) para todos los agentes que vamos a construir. Lo probé hoy, pasó 18 de 18 controles de seguridad y no cuesta nada.

## Provenance

- Source: `clickup` `86e3zc343`
- Source hash: `289858c1e47e50d283ab65b5453964ed6a5a839e6e6ed257e3a6513e98885b21`
- Observed at: 2026-11-19T04:16:08.909Z
- Agent run: `3acff67a-65b0-4558-a0ab-576fd4881df7`
- Validation run: `7f06ef64-a93c-4f6b-9823-4e02ddcff5c1`

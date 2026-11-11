---
brain_note_id: "note:5cfd20bf-92f8-4189-97fd-942ed0765e53"
canonical_key: "agent-harness-architecture"
brand_id: "trellis_core"
---
# Agent-Harness-Architecture

## Canonical Statement

- **fact**: An agent harness is the code that wraps an LLM, managing context, tool execution loops, state, permissions, and validation until a task is complete or a limit is reached.
- **process**: The standard agent loop pattern involves: 1) Requesting a response from the model, 2) Filtering for function calls, 3) Executing local tools, 4) Returning results with call IDs, 5) Repeating until no tools are called or a step limit is reached.

## Evidence Log

- 2026-11-11T20:19:51.017Z — `clickup:86e3zfzv4`
  - `e1` (source_body): El harness es el código que envuelve al modelo: el modelo elige una acción, el harness ejecuta la herramienta y le devuelve el resultado, en loop hasta terminar... El loop en JavaScript pide una respuesta al modelo, corre en paralelo las function calls locales y le devuelve sus resultados

## Provenance

- Source: `clickup` `86e3zfzv4`
- Source hash: `e9479b8b23d18ada1f40915e0c888c57f649c24c7f35cec1297ea9b4dc046cd2`
- Observed at: 2026-11-11T20:19:51.017Z
- Agent run: `28923811-e60a-4245-ba87-45416643552b`
- Validation run: `34158bc0-37f5-40cf-a850-708c80a75332`

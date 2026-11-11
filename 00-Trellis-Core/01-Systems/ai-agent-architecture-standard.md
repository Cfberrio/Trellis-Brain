---
brain_note_id: "note:2492912c-fb42-4d31-bf55-a033b34843b4"
canonical_key: "ai-agent-architecture-standard"
brand_id: "trellis_core"
---
# AI-Agent-Architecture-Standard

## Canonical Statement

- **rule**: AI agent architecture must follow a strict separation: the AI model proposes actions, but the application code must decide and execute them. Security and guardrails must be enforced at the application layer, not by instructions given to the AI.
- **rule**: Sensitive actions (e.g., deleting records, writing to CRM) require explicit human approval based on the original request, not a summary provided by the AI.

## Evidence Log

- 2026-11-11T20:19:06.251Z — `clickup:86e3zfcv3`
  - `e1` (source_child): Lo que vale del workshop no es la plataforma de OpenAI, es una regla: la IA pide, nuestro código decide y ejecuta, y la seguridad no depende de lo que le digamos a la IA.

## Provenance

- Source: `clickup` `86e3zfcv3`
- Source hash: `46bcc47630f26847b5e6c43a9bcb2ac21c9c50d41febe47e41d44136594f11dc`
- Observed at: 2026-11-11T20:19:06.251Z
- Agent run: `086febb6-7f11-43d1-919c-3afdae9029a1`
- Validation run: `bc4aa520-0aee-44ec-88fa-2aa5e43db8e2`

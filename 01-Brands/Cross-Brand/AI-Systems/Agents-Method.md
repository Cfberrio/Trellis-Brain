---
brand: Cross-Brand
area: systems
subarea: ai
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-12337 page 8cqnrff-12817 (Founder / Methods / Agents — Instrucciones para Agentes)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# AI Agents Method — Build Workflow

## Parent
- [[AI-Systems-Home|AI Systems Home]]

## Related
- [[2026-05-20-Claude-Setup|Claude Setup 2026-05-20]]
- [[../Meetings/2026-05-04-Nuevo-Flujo|2026-05-04 Nuevo Flujo (origin of doc-to-MD pipeline)]]

## Purpose
Standard workflow to create AI agents + automations across Trellis brands. Prevents from-scratch reinvention. Uses **OpenClaw** as base template for skill/agent construction.

## Main Rule
Before creating any agent or automation → **mandatory meeting with someone in the relevant area.**

That meeting exists to:
- Understand the real process
- Extract step-by-step
- Avoid assumptions
- Reduce rework

## Creation Base
Agents are NOT built from scratch. The base for creating agents must come from:
- **OpenClaw template / instruction structure**
- Team logic + experience
- Specific information from the meeting

> **OpenClaw provides the skeleton template for building skills and agents.** Instructions adapt onto that base per real case.

## Workflow (7 Steps)

### 1. Meeting with the area
Every automation starts with a conversation with the person who knows the process.

### 2. Automatic transcript
ClickUp captures the transcript automatically. No additional install needed.

### 3. Extract instructions
Use the transcript to write clear, specific, actionable instructions.

### 4. Use OpenClaw base template
Instructions are NOT organized arbitrarily. They mount on the **OpenClaw skill/agent template** as the base structure:
- Order logic
- Define expected behavior
- Specify actions
- Reduce ambiguity
- Consistent implementation

### 5. Technical review
**Kristen** reviews instructions to verify:
- Clarity
- Implementability
- Real operational logic
- Properly anchored on the base structure

### 6. Implementation
With approved instructions → build the agent.

### 7. Tests + adjustments
First version never defines 100%. Always tests + corrections + fine-tuning.

## Instruction Writing Rules

OpenClaw does NOT respond well to ambiguity.

### ❌ Don't write
- "Sé más carismático"
- "Hazlo mejor"
- "Responde más natural"

### ✅ Do write
- **Qué hacer**
- **Cómo hacerlo**
- **En qué orden**
- **Con qué tono**
- **Con qué límites**
- **Qué resultado se espera**

## Operating Principle
> If an instruction cannot be executed concretely, then it's not ready for implementation.

## What We Assume
Many tasks to automate will be new. Don't build agents from intuition alone. Build them with:
- Real context
- Exact instructions
- OpenClaw base template
- Technical review
- Tests

## Goal
Work fluidly, without frustration, without redoing a skill or agent multiple times due to initial lack of clarity.

## Minimum Deliverable After Each Meeting
- Transcript
- Exact instructions
- Instructions mounted on OpenClaw base template
- Technical review
- Clear implementation route

## Expected Outcome
Over time, this process should allow building an increasingly solid, reusable, useful skeleton for most cases — reducing rebuild time for new skills + agents.

## Cross-Reference
- Doc-to-MD pipeline (PDF → .md via ChatGPT + Obsidian + Claude) origin → see [[../Meetings/2026-05-04-Nuevo-Flujo|2026-05-04 Nuevo Flujo]]
- Team Claude/Obsidian/Cursor setup → see [[2026-05-20-Claude-Setup|2026-05-20 Claude Setup]]
- This skill (ClickUp → Obsidian extraction) is itself an example of this workflow → see [[../Meetings/Founder-Sessions/2026-05-21-Founders-Meet|2026-05-21 Founders Meet]]

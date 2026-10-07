---
brain_note_id: "note:c44f9545-d17f-477a-b830-c649d918f45d"
canonical_key: "brain-ingestion-system"
brand_id: "trellis_core"
---
# Brain Ingestion System

## Canonical Statement

- **rule**: The Trellis Brain follows five core principles: Brand isolation (deterministic routing), Canonical before evidence (search existing knowledge first), Home-first retrieval, Deterministic before agentic (rules handle routing/metadata, AI handles meaning), and Fail closed (unresolved brands or low confidence trigger human review).
- **process**: The ingestion pipeline consists of three systems: ClickUp (operational signals), Lovable Cloud (control plane for reasoning and validation), and Vault Gateway (local service for Obsidian REST API writes).
- **rule**: The Brain Agent is restricted to four permitted actions: IGNORE (no durable knowledge), ADD_EVIDENCE (supports existing knowledge), UPDATE_CANONICAL (modifies existing knowledge via section patch), and CREATE_KNOWLEDGE (new reusable concepts).
- **fact**: The system uses a deterministic brand resolver (Task -> List -> Folder -> Space -> Workspace) to ensure brand isolation without relying on LLM inference for routing.
- **process**: Destination Routing ensures every source ends in a clear destination: a specific brand, 02-Meetings, Transcripts, 90-Unknown (fallback), or excluded.

## Evidence Log

- 2026-10-06T16:10:44.811Z — `clickup:86e38nqdd`
  - `e1` (source_body): 5 Core Principles: Brand isolation: info from one brand can never land in another brand's vault area... Canonical before evidence: always search for existing canonical knowledge... 4 Permitted Agent Actions: IGNORE, ADD_EVIDENCE, UPDATE_CANONICAL, CREATE_KNOWLEDGE.
  - `e2` (source_child): Phase 2D: pure deterministic brand resolver (TASK → LIST → FOLDER → SPACE → WORKSPACE, fail-closed on conflict). No LLM in routing.
  - `e3` (source_child): Se diseñó el nuevo sistema de Destination Routing para que cada fuente termine en un destino claro: una marca, 02-Meetings/, 90-Unknown/, excluida o sin contenido.

## Provenance

- Source: `clickup` `86e38nqdd`
- Source hash: `1f78991d25fb85501fa26fcd0544413fc95dca276c87c548e20c53d7c44b9cc3`
- Observed at: 2026-10-06T16:10:44.811Z
- Agent run: `eb7a4cb2-0d7a-4ae2-84fd-9cda826a9760`
- Validation run: `1782f0d7-c6cf-4010-8f80-a7722b0e0319`

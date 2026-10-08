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

- 2026-10-08T18:56:52.680Z — `clickup:86e38nqdd` (validation `d37e0b08-fd15-459e-8697-207d7e179454`)
  - `e1` (source_body): Architecture (3 systems): ClickUp = source of operational signals (webhooks) Lovable Cloud = control plane (webhook intake, dedup, brand routing, AI reasoning, validation, audit) Vault Gateway = local Mac service that executes reads/writes against Obsidian via Local REST API
  - `e2` (source_child): Phase 2D: pure deterministic brand resolver (TASK → LIST → FOLDER → SPACE → WORKSPACE, fail-closed on conflict). ... Phase 3A: clickup-webhook Edge Function deployed. ... 120 s debounce + 600 s max hold coalescing.
  - `e3` (source_child): Se diseñó el nuevo sistema de Destination Routing para que cada fuente termine en un destino claro: una marca, 02-Meetings/, 90-Unknown/, excluida o sin contenido.
  - `e4` (source_child): Se construyeron los writers para Meetings, Transcripts y Unknown, con protecciones de idempotencia, límites de tamaño, reintentos y rutas determinísticas para evitar notas duplicadas.
- **process**: The Brain Ingestion System architecture consists of ClickUp (operational signals), Lovable Cloud (control plane for reasoning/validation), and Vault Gateway (local Mac service for Obsidian REST API writes).
- **rule**: Brand resolution is strictly deterministic following the hierarchy: TASK → LIST → FOLDER → SPACE → WORKSPACE, failing closed on conflict to ensure brand isolation without LLM inference.
- **process**: Destination Routing ensures every source is routed to a specific brand, 02-Meetings, Transcripts, or 90-Unknown (fallback), with built-in idempotency and size limit protections.
- **fact**: The system implements a 120s debounce and 600s max hold coalescing window for ClickUp webhooks to optimize processing and ensure data consistency.

- 2026-10-08T18:59:46.931Z — `clickup:86e38nqdd` (validation `c97d4b65-7fc8-4ab4-9298-f6a5eb487646`)
  - `e1` (source_child): Trellis Brain ya está funcionando de punta a punta. El sistema ahora recoge automáticamente conocimiento de ClickUp — tareas, comentarios, documentos, meeting notes y chats... corre automáticamente dos veces al día. Cuando una decisión queda validada, puede escribir directamente en Obsidian.
  - `e2` (source_child): Se diseñó el nuevo sistema de Destination Routing para que cada fuente termine en un destino claro: una marca, 02-Meetings/, 90-Unknown/, excluida o sin contenido. Unknown queda como último recurso.
- **fact**: The Brain Ingestion System is fully operational end-to-end, automatically extracting knowledge from ClickUp tasks, comments, documents, meeting notes, and chats.
- **process**: The system runs automatically twice daily, prioritizing new information over historical backlogs, which are processed in the background.
- **rule**: Destination Routing directs sources to specific brand folders, 02-Meetings, Transcripts, or 90-Unknown (fallback) for unidentifiable content.
- **process**: The pipeline includes extraction, classification, deduplication, validation, and a human review queue for contradictions or low-confidence decisions.

## Provenance

- Source: `clickup` `86e38nqdd`
- Source hash: `1f78991d25fb85501fa26fcd0544413fc95dca276c87c548e20c53d7c44b9cc3`
- Observed at: 2026-10-06T16:10:44.811Z
- Agent run: `eb7a4cb2-0d7a-4ae2-84fd-9cda826a9760`
- Validation run: `1782f0d7-c6cf-4010-8f80-a7722b0e0319`

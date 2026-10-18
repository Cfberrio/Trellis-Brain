---
brain_note_id: "note:bd28f348-193d-4865-b54d-82431d6cdd6c"
canonical_key: "development-scraping-standards"
brand_id: "trellis_core"
---
# Development and Scraping Standards

## Canonical Statement

- **decision**: Use Apify for social media content extraction and scraping as it is more cost-effective and token-efficient than direct API/Claude prompting.
- **decision**: Adopt Codex in development flows to ensure consistency and correctness, acknowledging that while it may be slower, it provides higher certainty of output quality.
- **rule**: When executing high-volume tasks, distribute subtasks across multiple Claude sessions to maximize token throughput and evaluate results faster.
- **decision**: Shift prompt strategy from searching for content directly to searching for tools/engines that facilitate content discovery (e.g., 'Instagram search engine' templates).

## Evidence Log

- 2026-10-18T18:55:17.391Z — `clickup_doc_page:8cqnrff-25577/8cqnrff-39097#brand=trellis_core`
  - `e1` (source_body): Luis planteó que debía existir ya un "Jeep/JIT/Git" o plantilla instalable en cloud que funcionara como un "Instagram search engine" con instrucciones claras para scrapear y buscar información reciente
  - `e2` (source_body): Cristian propuso usar Apify para extracción; indicó que consume menos dinero/tokens y ejecuta más barato.
  - `e3` (source_body): Luis asignó un subtask: cambiar el enfoque del prompt para que busque una herramienta que ayude a buscar contenido (y no el contenido en sí).
  - `e4` (source_body): Cristian reportó que Codex hacía que las cosas se demoraran más, pero daba certeza de que no iban a estar mal; lo consideró más eficiente y consistente, no más rápido.
  - `e6` (source_body): Luis instruyó a Cristian a montar todos los subtasks en diferentes sesiones de Claude y "maxear" todos los tokens hoy para evaluar qué resultados arrojaban.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-25577/8cqnrff-39097#brand=trellis_core`
- Source hash: `0937e5ec72c60030774a92608c9ea31c6fcecf8bd8d65ad281069df6fb014770`
- Observed at: 2026-10-18T18:55:17.391Z
- Agent run: `28012584-7a29-4006-a4ba-b2d0303cbd6d`
- Validation run: `1440805c-07fb-4661-8d76-aafbd6febf70`

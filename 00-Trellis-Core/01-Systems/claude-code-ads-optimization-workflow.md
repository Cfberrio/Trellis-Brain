---
brain_note_id: "note:e85960af-ef3b-4d7d-8d7d-eb2c04260ca2"
canonical_key: "claude-code-ads-optimization-workflow"
brand_id: "trellis_core"
---
# Claude Code Ads Optimization Workflow

## Canonical Statement

- **process**: Meta Ads optimization in Claude Code follows a 3-phase workflow: Phase 1 (/ads-meta-dr-phase1-extract) extracts read-only data (campaigns, ad sets, ads, spend) into new CSVs; Phase 2 (/ads-meta-dr-phase2-diagnose) interprets performance and waste; Phase 3 (/ads-meta-dr-phase3-rehab) generates a plan for pausing, testing, or reallocating budget.
- **process**: Google Ads optimization in Claude Code follows a 3-phase workflow: Phase 1 (/google-ads-oeb-phase1-extract) connects to the API to extract keywords, search terms, and landing page data; Phase 2 (/google-ads-oeb-phase2-diagnose) evaluates intent and conversion signals; Phase 3 (/google-ads-oeb-phase3-rehab) restructures campaigns and keywords based on real booking data.
- **rule**: When running Claude Code ad skills, always use the exact phase names and ignore old CSV files, focusing only on the newly generated data for decisions.

## Evidence Log

- 2026-10-17T00:50:11.333Z — `clickup_doc_page:8cqnrff-14777/8cqnrff-16717#brand=trellis_core`
  - `e1` (source_body): Solucioné esto en Claude Code con 3 skills. /ads-meta-dr-phase1-extract ... devuelve CSV nuevos. Ignoremos los viejos. /ads-meta-dr-phase2-diagnose Claude interpreta qué funciona... /ads-meta-dr-phase3-rehab Esto me da decisiones: qué mantener, qué pausar, qué separar, qué testear.
  - `e2` (source_body): /google-ads-oeb-phase1-extract ... extrae campañas, keywords, términos de búsqueda ... /google-ads-oeb-phase2-diagnose Claude revisa términos de búsqueda, conversiones ... /google-ads-oeb-phase3-rehab Esto convierte todo en decisiones: qué campañas ajustar, qué keywords mover.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-14777/8cqnrff-16717#brand=trellis_core`
- Source hash: `09f2491aa931595187cff13766375a4fa7097ce5eba335de95ff9201c2fae715`
- Observed at: 2026-10-17T00:50:11.333Z
- Agent run: `fe673afe-b02e-48a9-8318-a0fd6ce87e91`
- Validation run: `5d7d7876-b5be-42f5-a8a4-26a6fc5b1486`

---
brain_note_id: "note:531d3cc6-74a1-4c86-9add-768fdbe90b70"
canonical_key: "cts-technical-deployment-process"
brand_id: "cheese_to_share"
---
# CTS Technical Deployment and Review Process

## Canonical Statement

- **process**: CTS backend deployment requires a pre-deploy review using a local agent that checks for brand-specific errors (e.g., webhook configurations) before publishing.
- **rule**: The deployment workflow for CTS is defined in the CLAUDE.md file within the brand's directory, which mandates waiting for code synchronization before publishing and verifying on the live site.

## Evidence Log

- 2026-10-26T01:26:48.464Z — `clickup_doc_page:8cqnrff-23537/8cqnrff-35477#brand=cheese_to_share`
  - `e1` (source_body): El orden real para publicar: subir el código, esperar a que Lovable lo copie, apretar publicar, y después entrar a la web a comprobar. ... El agente la lee sola al abrirla — nadie tiene que acordarse.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-23537/8cqnrff-35477#brand=cheese_to_share`
- Source hash: `b2ffbb6e7340b1b297164639d4f22a372255ba700480e337defa606630f2f040`
- Observed at: 2026-10-26T01:26:48.464Z
- Agent run: `5021c1fd-62af-4f13-9c10-939b3e5b30c0`
- Validation run: `1dead032-d96a-4c2e-8fc9-619dcb6670d0`

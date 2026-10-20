---
brain_note_id: "note:fbeed695-32fe-4f3d-98e0-67b4e3f1cf8a"
canonical_key: "meta-ads-integration-process"
brand_id: "trellis_core"
---
# Meta-Ads-Integration-Process

## Canonical Statement

- **process**: The Meta Ads API integration requires setting specific environment variables (META_APP_ID, META_APP_SECRET, META_SYSTEM_USER_TOKEN, META_AD_ACCOUNT_ID, META_GRAPH_VERSION) in the root .env file and using the meta-ads Python CLI within the domains/ads/meta directory.

## Evidence Log

- 2026-10-20T18:13:19.052Z — `clickup_doc_page:8cqnrff-23377/8cqnrff-35837`
  - `e1` (source_body): En el .env de la raíz: META_APP_ID=938823898887883... Instalar el CLI: cd domains/ads/meta; python3 -m venv .venv; ./.venv/bin/pip install meta-ads. Usarlo: cd domains/ads/meta; source ./load-meta.sh

## Provenance

- Source: `clickup_doc_page` `8cqnrff-23377/8cqnrff-35837`
- Source hash: `4b23564a169c2a83c9ef1b38f629b27d8261038b1249d7c7ba027771538e496b`
- Observed at: 2026-10-20T18:13:19.052Z
- Agent run: `7b3812ee-fdff-40d4-8c19-a6f2ea76a669`
- Validation run: `bbcf0628-4bc0-4af0-98fc-20cfd5797d73`

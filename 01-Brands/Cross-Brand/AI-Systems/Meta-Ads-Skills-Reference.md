---
brand: Cross-Brand
area: ai-systems
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-15837 page 8cqnrff-18137 (META ADS)"
owner: Cristian Berrío
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Meta Ads Skills — Reference

## Parent
- [[01-Brands/Cross-Brand/AI-Systems/Claude-Skills-Catalog|Claude Skills Catalog]]

## Related
- [[01-Brands/Cross-Brand/AI-Systems/Google-Ads-Skills-Reference|Google Ads Skills Reference]]
- [[01-Brands/Discipline-Rift/06-DNA/DNA-Home|DR DNA Home]]

## Purpose

Reference for the Meta Ads skill pipeline. Targets **Discipline Rift (DR)** as canonical brand. Phase 1 read-only extraction to CSV.

## Active skill

**`meta-ads-phase1-extract`** (DR Meta Marketing API extraction)

### Description
Extraer el decision pack mínimo de Meta Marketing API para Discipline Rift (DR) y guardar los resultados como CSV en `domains/ads/meta/discipline-rift/data/raw/`.

### Step 0 — Load domain context
Read `domains/ads/meta/discipline-rift/CLAUDE.md` completely. Brand rules, messaging, restrictions, operating context.

For deeper brand context (Avatar, Offers, Objections, Positioning), load relevant Obsidian nodes via MCP `obsidian_get_file_contents`.

### Permanent rules
- Phase 1 is exclusively read-only
- Do NOT mutate campaigns, ad sets, ads, budgets, creatives
- Only use `ads_read` permission. Do NOT use `ads_management`
- Save all CSVs in `domains/ads/meta/discipline-rift/data/raw/`
- If a call fails, show Meta API error — don't improvise
- Do NOT print tokens or full secrets in console
- Extract only data with value for real decisions on creative, placement, targeting, setup

### Variable resolution (priority order)
1. `domains/ads/meta/discipline-rift/.env` — optional local override
2. `.env` at workspace root — default primary source

**Required variables:**
- `META_APP_ID`
- `META_APP_SECRET`
- `META_SYSTEM_USER_TOKEN`
- `META_AD_ACCOUNT_ID`
- `META_GRAPH_VERSION`

### Minimum decision pack — required outputs

#### Performance base
- `meta_campaign_insights_YYYYMMDD_HHMMSS.csv`
- `meta_adset_insights_YYYYMMDD_HHMMSS.csv`
- `meta_ad_insights_YYYYMMDD_HHMMSS.csv`

(Additional decision-pack outputs per the full skill SOP — see ClickUp Doc 8cqnrff-15837 page 8cqnrff-18137 for complete spec.)

## Where these skills live

Active in user's main workspace under `domains/ads/meta/discipline-rift/` per the Trellis repo CLAUDE.md domains scaffold.

## Implementation note

Per workspace CLAUDE.md: `domains/` contains scaffold for future pipelines including Meta Ads for DR. Skills + their associated `data/raw/` paths live under their domain folder, NOT at workspace root (root is reserved for the active Google Ads OEV pipeline).

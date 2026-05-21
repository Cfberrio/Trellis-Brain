---
brand: Cross-Brand
area: ai-systems
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-15837 page 8cqnrff-18117 (GOOGLE ADS)"
owner: Cristian Berrío
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Google Ads Skills — Reference

## Parent
- [[01-Brands/Cross-Brand/AI-Systems/Claude-Skills-Catalog|Claude Skills Catalog]]

## Related
- [[01-Brands/Cross-Brand/AI-Systems/AI-Systems-Home|AI Systems Home]]
- [[01-Brands/Orlando-Event-Venue/06-DNA/DNA-Home|OEV DNA Home]]

## Purpose

Documentation reference for the 3 active Google Ads skills running in the Trellis Claude Code workspace. Skills live in `.claude/skills/` of the main repo. Pipeline targets **OEV** as canonical brand.

## Active skills

| # | Skill | Phase | Purpose |
|---|---|---|---|
| 1 | `google-ads-phase1-extract` | Extract | Read-only extraction of OEV Google Ads data to CSV |
| 2 | `google-ads-phase2-diagnostic` | Diagnose | Analyzes most recent CSV batch + produces diagnostic + restructure proposal |
| 3 | `google-ads-phase3-campaign-rehab` | Rehab | Generates SOP for rehabilitating current campaign based on phase 2 + business feedback |

> Video walkthrough: see ClickUp Doc 8cqnrff-15837 / GOOGLE ADS page for screen recording.

## Skill 1 — google-ads-phase1-extract

**Description:** Monta y ejecuta la fase 1 de extracción read-only de Google Ads para OEV a CSV.

**`disable-model-invocation: true`** (skill is callable only by explicit slash command)

### Step 0 — Load domain context
Before any step: read `domains/ads/google/oev/CLAUDE.md` completely. Brand rules, messaging, restrictions, operating context. Don't infer.

### Permanent rules
- Phase 1 is exclusively read-only
- Do not mutate campaigns, conversions, assets, or settings
- Save all CSVs in `data/raw/`
- If a query fails, reduce complexity before retrying
- Do NOT assume more conversions = better conversions
- OEV prioritizes corporate/workshops. `sit paid` is future north-star conversion

### Required structure
- `scripts/`
- `queries/`
- `data/raw/`
- `prompts/`
- `CLAUDE.md`
- `requirements.txt`
- `.env.example`

### Main script (`scripts/run_gaql.py`)
- Use `GoogleAdsClient.load_from_env()`
- Accept `--query-file`, `--out`, `--customer-id` (optional)
- Execute with `GoogleAdsService.SearchStream`
- Flatten each row to a simple dict
- Export CSV
- Print number of exported rows
- Clear error messages

### Phase 1 queries (8 total)
1. `campaigns_last_30_days.sql`
2. `pmax_asset_groups_last_30_days.sql`
3. `conversion_actions.sql`
4. `campaign_conversions_by_action_last_30_days.sql`
5. `campaign_search_terms_last_30_days.sql`
6. `landing_pages_last_30_days.sql`
7. `geographic_performance_last_30_days.sql`
8. `call_conversions_last_30_days.sql`

### Base metrics (when applicable)
- `impressions`
- `clicks`
- `ctr`
- `average_cpc`
- `cost_micros`
- `conversions`
- `conversions_value`
- `segments.date` (last 30 days)

### Expected resources
| Dataset | Resource |
|---|---|
| Campaigns | `campaign` |
| PMax | `asset_group` |
| Conversions | `conversion_action` |
| Conversions by campaign/action | segmented by `segments.conversion_action` |
| Search terms | `campaign_search_term_view` |
| Landing pages | `expanded_landing_page_view` |
| Geography | `geographic_view` |
| Calls | `call_view` |

### Output at finalization
- Show exact path of created file
- Confirm `.claude/skills/google-ads-phase1-extract/SKILL.md` exists
- Do NOT execute yet

## Skill 2 — google-ads-phase2-diagnostic

**Description:** Analiza el batch más reciente de CSV de Google Ads para OEV y genera un diagnóstico con propuesta de reestructuración.

### Business context
- OEV prioritizes corporate/workshops
- Business should NOT be optimized toward generic cheap leads
- `deposit paid` is future north-star conversion
- Account may have only one campaign — adapt analysis to minimal structure, don't assume multiple complex campaigns
- Personal events / celebrations are secondary path to main positioning

### Permanent rules
- Phase 2 is analysis, not implementation
- Don't propose "intuition" changes without CSV backing
- Prioritize signal quality, search intent, structure quality, post-click fit
- Missing CSV → say clearly + continue with what's available
- Empty CSV → say clearly + don't invent conclusions

### What it does
1. Identify most recent timestamp in `data/raw/`
2. Read CSVs corresponding to that batch
3. Diagnose: structure / search intent / conversion signals / landing page fit / geography + call signals
4. Generate restructure proposal (not implementation)

### Required output sections

**A. Executive Read** — what's really happening, main problem, main opportunity

**B. Search Term Cost Map** — most relevant terms, most expensive, corporate/workshop intent, generic/low-quality, waste patterns

**C. Current Structure Read** — what structure exists today, role of PMax/asset groups, account mix quality

**D. Conversion Signal Audit** — what conversion actions exist, dominant signal today, what's missing to align with `deposit paid`

**E. Landing / Post-Click Read** — pages receiving traffic, traffic-destination alignment, gaps

**F. Restructuring Proposal** — what to keep, what to separate later, dominant focus, recommended next-phase structure (no implementation)

**G. Priority Actions** — 3 to 5 priority actions ordered by impact

### Output file
Path: `output/fase-2/YYYY-MM-DD_phase2_diagnostic.md`

Frontmatter:
```
# Phase 2 Diagnostic — OEV
**Fecha:** YYYY-MM-DD
**Batch analizado:** [timestamp]
**Campaña:** [exact name]

---
```

### Console summary (printed)
- Batch timestamp
- Campaign analyzed
- Main problem (1 line)
- Main opportunity (1 line)
- Section G: Priority Actions
- Generated file path

## Skill 3 — google-ads-phase3-campaign-rehab

**Description:** Usa la data de fase 1, el diagnóstico de fase 2 y el feedback de negocio para generar un SOP manual, ultra específico y de alto valor, de qué cambiar dentro de la campaña actual de Google Ads para OEV.

### Source priority (reduce spend, avoid rebuilding from scratch)
1. Latest file in `output/fase-2/*.md`
2. Latest file in `output/fase-3/*.md` if exists
3. Only if missing critical data → review `data/raw/`

Don't explore the whole project. Don't use Explore unless a key file is missing. Don't re-read all CSVs if a phase 2 output exists.

### Business context (updated)
- OEV is NOT exclusively corporate/workshops
- Corporate/workshops remains strong priority, but **baby showers + personal events still contribute material revenue**
- Account has ONE campaign — this phase improves current campaign, doesn't propose multi-campaign restructure yet
- Main current problem: poor asset quality / ad strength + intent mix + waste from irrelevant searches
- `deposit paid` is future north star, NOT focus of this phase
- Weddings / Disney wedding + truly off-category terms CAN stay as off-target
- **Competitor conquesting is valid** — don't block by default
- Audience strategy can't be only business/professional — must reflect real business mix without polluting signal

### Permanent rules (key delta from phase 2)
- This phase is implementation guidance, not analytical
- Don't repeat diagnostic
- Don't propose many new campaigns yet
- Don't focus on calls / offline conversion architecture
- Prioritize changes that can be made TODAY in current campaign
- Recommendation = exactly WHERE to touch in Google Ads
- Be extremely specific
- Don't execute automatic changes
- Don't treat profitable personal events as automatic garbage
- Don't block competitors by default if strategy wants visibility there

### Required output sections

**A. Qué sí vamos a tocar ahora** — 3 to 5 changes this week

**B. Qué NO vamos a tocar todavía** — short list of postponed changes

**C. Campaign Snapshot Used** — exact campaign name, exact asset group, ad strength, main problem, main opportunity

**D. Revenue Truth**
- Revenue lanes to protect
- What NOT to block by mistake
- What IS clear waste

**E. Asset Group Rehab Plan** — rename, missing assets count (headlines, long headlines, descriptions), images/logos/video gaps, assets to replace, dominant focus. **Hybrid demand**, not corporate-only.

**F. Ready-to-Paste Messaging Pack**
- 15 headlines suggested
- 5 long headlines suggested
- 5 descriptions suggested
- CTA direction
- Business name guidance
- What to avoid

All landed to OEV + hybrid demand (corporate/workshops + private events of value, without becoming a cheap generic venue).

**G. Negative Keywords Pack** — 4-group classification:

1. **BLOCK NOW** — high-certainty irrelevance/waste (e.g., convention center / OCCC)
2. **REVIEW FIRST** — depending on revenue mix or future packages:
   - banquet hall / orlando banquet hall
   - event planner / orlando event planner
   - party house rentals
   - team building activities
3. **DO NOT BLOCK BY DEFAULT**:
   - competitor terms (if strategy wants visibility)
   - personal event demand contributing revenue
   - mixed corporate + private terms
4. **DEPENDS ON STRATEGY** — terms that fit/don't fit depending on revenue mix decision

### Output file
Path: `output/fase-3/YYYY-MM-DD_phase3_campaign_rehab.md`

## Where these skills live

Active in the user's main workspace: `/Users/cberrio04/Documents/CLAUDE CODE/.claude/skills/`
- `google-ads-phase1-extract/SKILL.md`
- `google-ads-phase2-diagnostic/SKILL.md`
- `google-ads-phase3-campaign-rehab/SKILL.md`

Domain context: `/Users/cberrio04/Documents/CLAUDE CODE/domains/ads/google/oev/CLAUDE.md`

## Implementation note

Per Trellis CLAUDE.md rules (`/Users/cberrio04/Documents/CLAUDE CODE/CLAUDE.md`): these 3 skills + their root-level pipeline (`scripts/`, `queries/`, `data/raw/`, `output/fase-2/`, `output/fase-3/`, `prompts/`) are the **active production pipeline** and must not be modified without explicit instruction.

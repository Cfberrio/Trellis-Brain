---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/optimization-goals-and-attribution.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/optimization-goals-and-attribution.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Optimization goals"
meta_topic: Ad set optimization_goal, attribution_spec, bid_strategy and budget minimums
gate_mapping: learning conditions, tracking / signal quality, setup quality
meta_publisher: Meta
meta_source_urls:
  - https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/
retrieval_method: webfetch_full_body
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: partial
---

# Optimization goal, attribution spec, bid strategy, budget minimums

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/optimization-goals-and-attribution.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Source is the Marketing API **Ad Set** reference. Field-level and exact, where Help Centre prose is descriptive.

## What Meta states

### `optimization_goal`

| Value | Meta's definition (quoted) |
|---|---|
| `OFFSITE_CONVERSIONS` | "Optimize for people more likely to make a conversion on the site" |
| `LINK_CLICKS` | "Optimize for people more likely to click in the link of the ad" |
| `LANDING_PAGE_VIEWS` | "Optimize for people who are most likely to click on and load your chosen landing page" |
| `LEAD_GENERATION` | "Optimize for people more likely to fill out a lead generation form" |
| `REACH` | "Optimize to reach the most unique users for each day or interval specified in `frequency_control_specs`" |
| `IMPRESSIONS` | "Show the ads as many times as possible" |
| `VALUE` | "Optimize for maximum total purchase value within the specified attribution window" |

The distinction Meta draws between `LINK_CLICKS` and `LANDING_PAGE_VIEWS` is explicit and narrow: clicking the link, versus clicking **and loading** the page. Those are different populations, and the gap between them is page load.

### `attribution_spec`

Quoted: *"Conversion attribution spec used for attributing conversions for optimization. Supported window lengths differ by optimization goal and campaign objective."*

Fields:

- `event_type` — `CLICK_THROUGH`, `VIEW_THROUGH`, or `ENGAGED_VIDEO_VIEW` (required)
- `window_days` — required
- `weight` — defaults to 100

Note the sentence says attribution is used **for optimization**, not only for reporting. The window is an input to delivery, not just a lens on results.

### `bid_strategy`

- `LOWEST_COST_WITHOUT_CAP` — "Designed to get the most results for your budget based on your ad set `optimization_goal` without limiting your bid amount"
- `LOWEST_COST_WITH_BID_CAP` — "Designed to get the most results for your budget…while limiting actual bid to your specified amount"

### Minimum daily budgets

When `bid_strategy` = `LOWEST_COST_WITHOUT_CAP`:

| Billing basis | Minimum daily budget |
|---|---|
| Impressions | $0.50 |
| Clicks / Likes / Video Views | $2.50 |
| Low-frequency actions | $40 (stated as the same globally) |

Meta adds: *"For ads from countries [listed], the minimum values are 2x"* those amounts.

## What Meta does not state

- **The exact allowed `window_days` values are not on this page.** Meta says they "differ by optimization goal and campaign objective" without enumerating them. Do not assert 1-day / 7-day / 28-day from this source — that came from Help Centre pages that were not fetched first-hand.
- No learning-phase mechanics here. The 50-events-per-week threshold widely cited for exiting the learning phase lives on the Business Help Centre and is **not yet verified first-hand in this knowledge base**. See `learning-phase.md` (pending).
- No statement about which optimization goals are valid for which campaign objectives, beyond the note that valid combinations exist.
- "Low-frequency actions" is not defined on the captured page. Which goals fall in that $40/day bucket is unresolved.

## Why it matters for DR

Gate items: **learning conditions**, **tracking / signal quality**, **setup quality**.

**The $40/day floor is the sharp one.** If a completed registration is a "low-frequency action" for billing purposes, Meta's documented minimum daily budget for that optimization is $40/day per ad set. DR is a local single-market advertiser. Whatever DR's total Meta budget is, the number of ad sets it can run while each clears a $40/day floor is small — and splitting budget below the floor is a setup defect, not a tactical choice. This bounds account structure directly.

Which bucket DR's optimization event falls into is **not established** — "low-frequency actions" is undefined on this page. That is the open question, not an assumption.

**`LINK_CLICKS` vs `LANDING_PAGE_VIEWS` is a signal-quality choice.** Meta's own definitions separate clicking from loading. On a small local account, optimizing to a population that clicks but never loads spends real budget teaching the system the wrong thing. This is squarely a learning-conditions and signal-quality item.

**Attribution feeds optimization, not just reporting.** Meta states the spec is "used for attributing conversions for optimization." A window chosen for reporting convenience is also shaping delivery. For a considered purchase like a season enrolment — where a parent may see the ad and register days later after checking a schedule — window length is a real variable, not a reporting preference.

None of this is a DR recommendation. All three are conditions to check against DR's actual ad sets before anything is proposed.

## Open questions

- Enumerate `window_days` allowed per objective. Needs a versioned API reference or a rendered Help Centre page.
- Define "low-frequency actions" and confirm whether DR's registration event sits in the $40/day bucket.
- Verify the learning-phase event threshold first-hand rather than by search summary.
- Confirm which `optimization_goal` values are valid under the objective DR actually runs.

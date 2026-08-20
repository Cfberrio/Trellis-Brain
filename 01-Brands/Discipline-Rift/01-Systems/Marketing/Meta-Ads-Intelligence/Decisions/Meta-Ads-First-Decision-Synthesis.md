---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: playbook
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/first-decision-synthesis.md"
repo_path: domains/ads/meta/intelligence/output/first-decision-synthesis.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/decision
  - discipline-rift
aliases:
  - "First DR Decision Synthesis"
---

# First DR Decision Synthesis

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-Structure-Full-Method|Método completo de estructura DR]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/DR-Meta-Ads-Playbook|DR Meta Ads Playbook]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1A-Objective-and-Optimization-Event|Wave 1A — objetivo y evento de optimización]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/output/first-decision-synthesis.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Date:** 2026-08-13
**Inputs:** `competitors/patterns.md` (Sprint 1 sweep, 2026-08-13) · `knowledge/official-meta/` (11 files, all first-hand) · `domains/ads/meta/discipline-rift/CLAUDE.md` · DR Phase 2 diagnostics · DR raw account snapshots
**Nothing was modified.** No campaign change, no skill, no ClickUp task.

---

# Executive Decision Summary

| Decision | Verdict | Confidence | Why now |
|---|---|---|---|
| 1 — Quarantine the 2026-05-11 Phase 2 diagnostic and re-extract | **AUDIT FIRST** | HIGH | It describes 4 campaigns and ~$9,246 spend. No raw snapshot contains any of it. Decisions are being made against an account that isn't in the data. |
| 2 — Verify geo configuration **and `location_types`** in Ads Manager | **AUDIT FIRST** | HIGH | No `geo_locations` in any of 4 snapshots. Meta's documented default is `['home','recent']` — in Orlando, `recent` means tourists. |
| 3 — Do not consolidate account structure | **KEEP AS-IS** | HIGH | Account is 1 campaign / 1 ad set / 1 ad. Already maximally consolidated. The consolidation reading from Meta docs does not apply here. |
| 4 — Verify the optimization event actually fires; establish pixel/CAPI reality | **AUDIT FIRST** | HIGH | Optimizing to `LANDING_PAGE_VIEWS`, but no LPV/actions data in any extract. Pixel/CAPI status is unknown, not broken. |
| 5 — Restrict placements | **TEST — gated behind #2 and #4** | LOW | 79% of spend to IG feed at $136 CPM vs FB feed $34. But $82 total spend, and high CPM more likely reflects audience size than a placement defect. |

**Acceptance test result: YES** — external intelligence changed decisions. Detail in the final section.

---

## The account, as the data actually shows it

Every raw snapshot (2026-03-30, 04-17, 04-24, 05-12) agrees:

| | |
|---|---|
| Campaigns | **1** — `DR SPRING 2`, `OUTCOME_TRAFFIC`, **PAUSED** |
| Ad sets | **1** — `New Traffic Ad Set`, ACTIVE, `optimization_goal: LANDING_PAGE_VIEWS`, `billing_event: IMPRESSIONS` |
| Ads | **1** — `DR SPRING` |
| Spend (2026-03-25 → 04-23) | **$82.11** · 1,015 impressions · 256 reach · **10 clicks** · CTR 0.99% · CPC $8.21 · CPM $80.90 |
| Targeting payload | `age_min 18, age_max 65, age_range [28,40]`, `custom_audiences: [DR HISTORIC]`, `targeting_automation.advantage_audience: 1`, relaxed brand-safety |
| `geo_locations` | **absent from the payload in all 4 snapshots** |
| `publisher_platforms` | **absent** — delivery observed across 11 positions |
| Budget fields | empty at ad set level in all snapshots |
| Conversion/action columns | **absent from every insights file** |
| Newest extract (2026-05-12) | **0 insight rows** — consistent with a paused campaign and an empty window |

Latest data is 2026-05-12. Today is 2026-08-13. **Everything below describes an account as it stood ~3 months ago, whose only campaign was paused.**

---

# Decision 1 — Quarantine the 2026-05-11 Phase 2 diagnostic and re-extract before acting on it

## Verdict
**AUDIT FIRST**

## Current DR state

`output/fase-2/2026-05-11_meta_phase2_diagnostic.md` describes:

- 4 campaigns (`DR | Recruiting | Lead Gen — Athletes`, `DR | Franchise | Lead Gen — Owners`, `DR | Recruiting | Retargeting — Warm`, `DR | Awareness | Brand — Youth Sports`)
- ~$9,246 total spend, ~$6,403 in scope
- 7 ad sets with daily budgets $65/$45/$40/$18/$17/$25/$20
- 6 named creatives with CPLs from $20.50 to $30.92
- `LEAD_GENERATION` and `BRAND_AWARENESS` objectives

**None of this appears in any raw snapshot.** `meta_campaign_objects_20260512_103221.csv` — extracted *after* that diagnostic was written — returns exactly one row: `DR SPRING 2 | OUTCOME_TRAFFIC | PAUSED`. Same for 03-30, 04-17, 04-24.

The two earlier diagnostics do reconcile:

- `2026-04-24` cites `$82.11 / 1,015 impressions / 256 reach / 10 clicks / CTR 0.99% / CPC $8.21 / CPM $80.90` — matches `meta_campaign_insights_20260424_174401.csv` exactly.
- `2026-03-30` cites one paused campaign, one ad set, one ad, ~$110 spend, IG feed 81.8% at $162 CPM — consistent with its snapshot.

So the pipeline produced grounded output in March and April, and the May 11 output is unsupported by the data on disk.

## External evidence

### Official Meta
Not applicable — this is a data-integrity question, not a platform question.

### Competitors
Not applicable.

## Why this matters for DR

**Setup quality**, and upstream of everything else. The May 11 diagnostic's five priority actions — fix geo, pause the kids 13–22 ad sets, replace the `CollegeDeadline` creative, audit the landing page, hold budget — reference ad sets and creatives that do not exist in any extract. Acting on them means editing objects that may not exist, or reasoning about an account that isn't this one.

`2026-05-11_meta_phase3_campaign_rehab.md` (25KB) was built on top of it and inherits the same exposure.

Three explanations are consistent with the evidence, and the data cannot distinguish them: the diagnostic was run against a different ad account; the extract is pointed at the wrong account while the diagnostic used another source; or the diagnostic content was not derived from the extract at all. **This synthesis does not claim which.**

## Confidence
**HIGH** — on the discrepancy itself. Four independent snapshots spanning six weeks, including one taken the day after the diagnostic, all return the same single campaign. The cause is unknown; the mismatch is not.

## Concrete next action

1. In Ads Manager, read the ad account ID currently being served, and compare it to the account ID the Phase 1 extract authenticates against (`domains/ads/meta/discipline-rift/.env.example` names the variable; the live value is in `.env`).
2. If they differ — the extract is pointed at the wrong account. Fix the ID and re-run Phase 1.
3. If they match — the May 11 diagnostic did not come from this account's data. Move `2026-05-11_meta_phase2_diagnostic.md` and `2026-05-11_meta_phase3_campaign_rehab.md` to an `archive/` or `quarantine/` subfolder with a note, so neither is cited as current.
4. Either way, run a fresh Phase 1 extract before any campaign decision. The newest data is 3 months old.

## What could change this decision
A second ad account genuinely existing under the same business, holding the four campaigns, and the extract simply never covering it. That would make the diagnostic correct and the *extraction scope* the defect. Ads Manager settles it in minutes.

---

# Decision 2 — Verify geo configuration, and specifically `location_types`

## Verdict
**AUDIT FIRST** — not "fix geo"

## Current DR state

The `targeting` payload in `meta_adset_objects_20260512_103221.csv` is complete and readable, and contains **no `geo_locations` key**:

```json
{"age_max": 65, "age_min": 18, "age_range": [28, 40],
 "custom_audiences": [{"id": "120243159885200652", "name": "DR HISTORIC"}],
 "brand_safety_content_filter_levels": ["FACEBOOK_RELAXED", "AN_RELAXED"],
 "targeting_automation": {"advantage_audience": 1}}
```

Same absence in all four snapshots. The `2026-04-24` diagnostic flagged this correctly and did not overclaim: *"Geo: not visible in extracted targeting payload — risk to validate in Ads Manager."*

**Absence from an extract is not proof of absence in the account.** Geo may be set and simply not serialized into this field, or set at another level.

## External evidence

### Official Meta

From `knowledge/official-meta/geo-location-targeting.md`, sourced first-hand from the Marketing API Basic Targeting reference:

- `location_types` has two documented values: `home` — *"People whose stated location in their Facebook profile 'current city' is in an area"*; `recent` — *"People whose recent location is in a selected area, as determined from mobile device data."*
- **The default is both:** *"If no `location_types` array is provided, it will default to `['home', 'recent']`."*
- City-radius targeting has a documented floor of *"10 to 50 miles"*; `custom_locations` goes to *"0.63 to 50 miles"*.

### Competitors

From `patterns.md`: **2 of 5 independent brand families** name the place inside the creative rather than relying on targeting — Super Soccer Stars (NYC, Jersey City, Hoboken) and Soccer Shots Orlando (*"📍Played right here in your community"*, *"Soccer at Your Child's School!"*). Confidence recorded as medium — it clears the 2-family bar, only just.

Sample limitations: the local sample is **2 advertisers / 2 families / 16 ads**, and 11 of those 16 are a BabyStrong launch outside DR's age band. `sample_status` is `unknown` for all six advertisers. Nothing about competitor targeting is observable — Meta publishes no geo targeting for US commercial ads.

## Why this matters for DR

**Geo accuracy.** DR's offer is delivered at a named school on a named campus across a season. Residency is the qualification, not a preference.

The official-Meta finding sharpens the audit question in a way the Phase 2 diagnostic did not reach. Phase 2 asks *"is geo set to Orlando?"* The documentation says that is only half the question. An ad set correctly targeting Orlando, with `location_types` left unspecified, is **also** reaching people whose *recent* location is Orlando as determined by mobile device data. Orlando is one of the highest tourist-volume metros in the United States. A visiting parent from Ohio satisfies `recent` and cannot enrol a child in an Orange County after-school season.

Competitor evidence adds a weak, independent hedge: the two brand families that name the location inside the creative reduce dependence on targeting alone. Two families is thin, and this is a supporting observation, not a driver.

## Confidence
**HIGH** that the audit is warranted — geo is unverifiable from four consecutive extracts on a business whose entire differentiator is locality.
**LOW** on any specific fix, because the current configuration is genuinely unknown.

## Concrete next action

In Ads Manager, open `DR SPRING 2` → `New Traffic Ad Set` → Audience, and record three things verbatim:

1. The locations listed.
2. **The location-type selector** — whether it reads "People living in this location" or "People living in or recently in this location."
3. Whether `Advantage detailed targeting` / audience expansion is widening beyond the set location.

Then reconcile against the extract: if geo is configured in Ads Manager but absent from `meta_adset_objects_*.csv`, the Phase 1 extract is dropping a field it should capture, and that is a separate pipeline fix.

## What could change this decision
Finding geo already set to Orlando **with** location type restricted to "living in this location." Then this closes with no change, and the finding becomes a Phase 1 extraction gap instead.

---

# Decision 3 — Do not consolidate account structure

## Verdict
**KEEP AS-IS** (structure only — this is not an endorsement of the account)

## Current DR state

1 campaign · 1 ad set · 1 ad. Confirmed identically across all four snapshots.

Fragmentation is zero. There is nothing to combine.

## External evidence

### Official Meta

Three separate first-hand pages point toward consolidation for accounts that are fragmented:

- `learning-limited.md`: *"Combine ad sets and campaigns will help you get the results you need faster."*
- `learning-phase.md`: *"Avoid high ad volumes… By combining similar ad sets, you also combine learnings."*
- `optimization-goals-and-attribution.md`: documented minimum daily budget of **$40/day** for low-frequency actions at `LOWEST_COST_WITHOUT_CAP`.

### Competitors

`patterns.md` records that **3 of 5 families** hold copy constant while varying media/CTA across many ad IDs — KidStrong HQ 11 ads on one message, Skyhawks 9 ads on one message, i9 two sets of 6. The file already flags this as `modification_required: yes`, noting DR's volume is far below these advertisers and *"a 9-variant structure would starve every cell."*

## Why this matters for DR

**Learning conditions**, by *not* acting.

This is the clearest case in the synthesis of the evidence hierarchy doing real work. Reading the Meta knowledge base alone — three pages converging on "fewer, better-funded ad sets" — produces a confident consolidation recommendation. DR's actual account data rejects it outright: the account is already at the floor.

The $40/day figure is also not applicable as stated. It is documented for low-frequency **action** optimization; DR optimizes to `LANDING_PAGE_VIEWS`, which Meta lists in the clicks/views tier ($2.50/day minimum). Carrying the $40 number into a DR recommendation would have been a misapplied fact.

The real structural issue is the opposite of fragmentation: **one creative in one ad set produces no comparative signal at all.** The 2026-04-24 diagnostic reached this independently — *"learning conditions and account structure are too thin to learn anything."* That is a case for adding a second creative later, deliberately, not for consolidating.

## Confidence
**HIGH.** Structure is directly observed, unambiguous, and stable across four snapshots.

## Concrete next action

None on structure. Explicitly record "consolidation: not applicable — 1/1/1" so the recommendation is not regenerated by a future pass over the Meta documentation.

When creative testing does begin, note from `significant-edits.md`: *"Adding a new ad to your ad set"* is a significant edit and resets the learning phase. Adding a second creative is not free; it should be a deliberate reset, timed.

## What could change this decision
A fresh extract (per Decision 1) revealing the account genuinely has multiple campaigns and ad sets. Then fragmentation becomes a live question and this decision is re-opened from scratch.

---

# Decision 4 — Verify the optimization event fires; establish pixel/CAPI reality

## Verdict
**AUDIT FIRST** — explicitly *not* "tracking is broken"

## Current DR state

- `optimization_goal: LANDING_PAGE_VIEWS`, `billing_event: IMPRESSIONS`, campaign objective `OUTCOME_TRAFFIC`.
- **No insights file in any snapshot contains an actions, conversions, or LPV column.** Columns are limited to spend, impressions, reach, clicks, ctr, cpc, cpm, and (in the placement file) platform breakdowns.
- Recorded volume: **10 link clicks over 30 days.** LPV cannot exceed link clicks, so LPV in that window is bounded at ≤10 — roughly **≤2.3 per week**.
- The 2026-04-24 diagnostic reached the same wall: *"the extracted insights pack does not contain LPV / actions data, so signal quality on the optimization event is unverified from CSV alone."*
- **Pixel and Conversions API status: no evidence in any extract.** Neither present nor absent — simply not covered.
- **`fbc` / `fbp` click identifiers: no implementation evidence.** Unknown.

## External evidence

### Official Meta

- `optimization-goals-and-attribution.md`: `LANDING_PAGE_VIEWS` = *"Optimize for people who are most likely to click on and load your chosen landing page"*, distinct from `LINK_CLICKS` = *"click in the link of the ad."* Meta separates clicking from loading.
- `learning-limited.md`: an ad set becomes learning limited when it is *"unlikely to receive **about 50 optimization events** in the week after your last significant edit."* Meta's hedges are load-bearing — "about", the ad set's *selected* optimization event, a window anchored to the last significant edit, and a forward-looking prediction rather than a retrospective count. Meta also states plainly: *"Learning limited isn't a penalty."*
- `event-match-quality.md`: **Email and Click ID are High priority**; first name, last name, city, zip are **Low**. EMQ applies to CAPI website events, scored 0–10, **with no target score published**.
- `pixel-capi-deduplication.md`: deduplication requires identical `event_id` and matching `event_name`. Meta names both failure directions — missing deduplication inflates conversions; inaccurate IDs cause real conversions to be *"wrongly deduplicated."*

### Competitors

Not applicable. Ad Library exposes nothing about any advertiser's tracking implementation, and `patterns.md` explicitly forbids inferring it.

## Why this matters for DR

**Tracking / signal quality**, and **learning conditions**.

At ~2.3 clicks/week upper bound, DR is far below the ~50 optimization events per week that Meta uses to diagnose learning limited. Per the interpretation rules this is context, not a verdict: Meta does not require 50 conversions, and learning limited is not evidence the campaign is bad. What it does mean is concrete — the delivery system has very little to learn from, so *any* performance read at this volume is directional at best. That is a reason to distrust conclusions, not a reason to thrash.

Four of Meta's five named causes of learning limited describe this account by construction: small audience, low budget, infrequent optimization event, too few results. That is the expected state of a $2.70/day local account, not an anomaly.

The tracking question is separate and prior. If LPV is not firing, the ad set is optimizing toward an event Meta cannot observe — and no creative, geo or placement decision downstream is interpretable. Because there is no evidence either way, the honest verdict is audit.

## Confidence
**HIGH** that the audit is warranted — the optimization event is unverifiable from four consecutive extracts.
**LOW** on any diagnosis. Nothing here supports a claim that tracking is broken, that CAPI is missing, or that deduplication is failing. `pixel-capi-deduplication.md` documents the rule to audit against; it is not a finding about DR.

## Concrete next action

In Events Manager, record four facts:

1. Does a pixel exist for this business, and is it receiving events in the last 7 days?
2. Is a Conversions API integration connected — yes/no? (If no, deduplication and EMQ are moot and should not be raised again until it exists.)
3. Is `PageView` / landing-page-view firing on the destination URL used by ad `DR SPRING`?
4. If CAPI exists: the current Event Match Quality score, plus whether `event_id` is present on both browser and server events.

Separately: confirm whether the Phase 1 extract *can* pull actions/LPV columns. If the API returns them and the query omits them, that is a Phase 1 query gap, and it is the cheapest fix in this document.

## What could change this decision
Events Manager showing LPV firing cleanly with a healthy pixel and no CAPI — in which case the optimization event is fine, the deduplication material is shelved until CAPI exists, and the remaining issue is purely volume.

---

# Decision 5 — Restrict placements

## Verdict
**TEST — gated behind Decisions 2 and 4**

## Current DR state

No `publisher_platforms` in the targeting payload. Observed delivery across **11 positions** in `meta_ad_insights_by_placement_20260424_174401.csv`:

| Placement | Spend | % | Impr | Clicks | CPM |
|---|---|---|---|---|---|
| instagram / feed | $64.89 | **79.0%** | 476 | 6 | **$136.32** |
| instagram / stories | $9.46 | 11.5% | 299 | 2 | $31.64 |
| instagram / reels | $4.01 | 4.9% | 120 | 1 | $33.42 |
| facebook / feed | $3.19 | 3.9% | 93 | 1 | **$34.30** |
| facebook / instream_video | $0.27 | 0.3% | 6 | 0 | $45.00 |
| facebook / reels | $0.15 | 0.2% | 7 | 0 | $21.43 |
| facebook / stories | $0.12 | 0.1% | 5 | 0 | $24.00 |
| facebook / notification | $0.01 | — | 1 | 0 | $10.00 |
| facebook / marketplace | $0.01 | — | 1 | 0 | $10.00 |
| audience_network / an_classic | $0.00 | — | 4 | 0 | $0.00 |
| audience_network / rewarded_video | $0.00 | — | 3 | 0 | $0.00 |

IG feed costs **~4x** FB feed per thousand impressions and consumed four fifths of the budget.

## External evidence

### Official Meta

`placements.md`, first-hand from the placement-targeting reference: *"If you do not specify anything for a particular placement field, Facebook considers all possible default positions for that field."* DR's configuration matches this exactly — nothing specified, everything served.

Documented restrictions that constrain any test design: Audience Network cannot be selected alone; Facebook `story` cannot be selected independently of `feed` or Instagram `story`; `notification` cannot be selected independently.

Meta publishes **no performance or cost claim per placement** on that page. Nothing in the documentation says narrowing improves results.

### Competitors

`patterns.md` records **no format consensus** across the five families: Soccer Shots 100% video, KidStrong HQ 82% video, i9 56% DCO catalog, Skyhawks 67% static image. Placement is not observable in Ad Library at all — only creative format. So competitor evidence is **weak and indirect** here, and mainly says the category has not converged.

## Why this matters for DR

**Placement control** and **creative clarity**. One creative is being rendered into 11 positions with different aspect ratios, sound expectations and attention profiles.

But the 2026-04-24 diagnostic already identified the more likely explanation, and it argues against acting: *"Either the audience is very small (custom + Orlando) and IG feed is the only inventory Meta can serve into, or the auction is uncompetitive against the targeted seed. Both point to seed/geo size, not a placement problem per se."*

That reading is strengthened by the targeting payload — a single custom audience (`DR HISTORIC`) with `advantage_audience: 1`. A small seed plus an $80 budget is a plausible cause of both the concentration and the $136 CPM. Restricting placements on that basis would treat a symptom of audience size as a placement defect.

The pennies-and-zero-clicks placements (Audience Network, notification, marketplace, FB reels/stories — **$0.56 combined, 0 clicks**) look like delivery noise. At this spend level, excluding them saves under a dollar. It is not a decision worth making now.

## Confidence
**LOW.**

Total spend is $82.11 with 10 clicks. Six clicks on IG feed and one on FB feed cannot separate placement effect from audience size, creative fit, or chance. The 2026-04-24 diagnostic said the same in its own words — *"volume too small to call decisively."* Meta publishes no per-placement performance claim, and competitor data says nothing about placements. Every evidence tier is weak here.

## Concrete next action

**Do not restrict placements yet.** Sequence:

1. Complete Decision 2 (geo + `location_types`) and Decision 4 (tracking).
2. Re-extract per Decision 1 and get a window with meaningful delivery.
3. *Then*, if IG feed still absorbs ~79% of spend at a ~4x CPM premium with geo confirmed and audience size known, run a manual-placement ad set restricted to Facebook feed + Instagram feed + Instagram stories as a single deliberate change — remembering from `significant-edits.md` that *"any change to targeting"* is a significant edit and resets learning.

## What could change this decision
Confirming a large addressable audience with correct geo. That removes the audience-size explanation and makes the CPM gap a genuine placement signal, moving this from TEST toward ADOPT. Conversely, a very small custom-audience seed largely explains the concentration and this drops to NO ACTION.

---

# Answers to the nine required checks

| # | Question | Answer |
|---|---|---|
| 1 | Optimization event? | `LANDING_PAGE_VIEWS`, `billing_event: IMPRESSIONS`, campaign objective `OUTCOME_TRAFFIC`. Not a conversion or registration event. |
| 2 | Optimization-event volume per ad set? | **Not directly measurable** — no LPV/actions column in any extract. Bounded by link clicks: **10 in 30 days (~2.3/week)**. Meta's ~50-optimization-events-per-week figure is diagnostic context, not a requirement; learning limited is not evidence the campaign is bad. |
| 3 | Fragmentation? | **1 campaign / 1 ad set / 1 ad.** No fragmentation. Budget fields empty at ad set level in all snapshots. Consolidation guidance does not apply. |
| 4 | Edit cadence? | **UNKNOWN.** No edit history, no "last significant edit" field, no change log in any extract. Not inferred. |
| 5 | Location targeting? | **`geo_locations` absent from the targeting payload in all 4 snapshots.** Cannot distinguish "not configured" from "configured but not extracted." Meta's default `location_types` is `['home','recent']`. Audit before any change. |
| 6 | Placements? | **Unspecified** — no `publisher_platforms`. Delivery observed across 11 positions, matching Meta's documented all-default-positions behaviour. |
| 7 | Pixel / CAPI? | **UNKNOWN.** No evidence in any extract. Deduplication cannot be assessed — AUDIT FIRST, not "deduplication is broken." |
| 8 | Click identifiers / high-value match params? | **UNKNOWN.** No implementation evidence for `fbc`, `fbp`, or any `user_data` parameter. Meta ranks Email and Click ID **High** priority; whether DR captures either is unestablished. |
| 9 | DR creative vs competitor observations? | **Cannot be determined from available data.** The only creative field in any extract is `ad_name: "DR SPRING"`. No copy, hook, headline, CTA, or landing-page URL is captured. School/on-campus framing, explicit age range, season dates, program-level destination and CTA intent are therefore **unassessable** — not "missing." |

Check 9 is itself a finding: the Phase 1 extract captures no creative content, so the entire creative half of the competitor sweep currently has nothing on the DR side to compare against.

---

# Questions Still Unresolved

Questions DR data cannot answer, official Meta documentation does not answer, and competitor observation does not answer. These are the only legitimate candidates for later expert research.

---

**question:** At genuinely low volume — single-digit weekly optimization events on a local service business — is it better to optimize to a shallower, more frequent event (landing page view, lead) or to hold a deeper event and accept permanent learning-limited status?
**why it matters:** Directly determines DR's optimization goal. Meta's own fix list says *"Consider choosing an optimization event that occurs more frequently"*, but that trades signal quality for volume, and Meta never quantifies the trade.
**what evidence is missing:** Any comparative outcome data for low-volume local accounts. DR has run one traffic campaign at $82 and has no lead-optimized history.
**could expert research materially help:** **Yes.** This is exactly the kind of pattern practitioners observe across many small accounts and platforms never publish.

---

**question:** For a local service business with a small custom-audience seed, does a ~4x CPM premium on one placement indicate a placement problem or an audience-size problem — and how would you tell them apart before spending to find out?
**why it matters:** Decides whether Decision 5 is ever worth running, and prevents treating a seed-size symptom as a placement defect.
**what evidence is missing:** DR lacks volume to separate the two. Meta publishes no per-placement cost guidance. Ad Library exposes no competitor placement data.
**could expert research materially help:** **Yes** — diagnostic heuristics for separating auction/seed effects from placement effects are practitioner knowledge.

---

**question:** What is a workable creative-testing cadence when every creative change is a significant edit that resets learning, and weekly optimization events are in single digits?
**why it matters:** `significant-edits.md` confirms any creative change and any added ad resets learning. Meta simultaneously warns against trying to avoid the learning phase. At DR's volume these two instructions are in practical tension and Meta does not resolve it.
**what evidence is missing:** DR has one creative and no test history. Competitor variation sets (KidStrong 11 ads, Skyhawks 9) are observable in structure but their results are not — `patterns.md` records *"zero visibility into results."*
**could expert research materially help:** **Yes.** This is one of the most commonly discussed practitioner topics and Meta will not publish a position on it.

---

**question:** For a local, seasonal, considered purchase like a school-season enrolment, what attribution window is appropriate — given Meta states the attribution spec is used *"for attributing conversions for optimization"*, not only reporting?
**why it matters:** A parent may see an ad and register days later after checking a schedule. Window length shapes delivery, not just measurement.
**what evidence is missing:** `optimization-goals-and-attribution.md` records that allowed `window_days` *"differ by optimization goal and campaign objective"* without enumerating them. DR has no conversion history to observe a lag distribution.
**could expert research materially help:** **Partly.** The allowed values are a documentation gap first — retrieve those before asking anyone. The judgment about considered local purchases is genuinely expert territory.

---

**question:** Does naming the delivery location inside the creative measurably reduce mis-qualified clicks on a local offer, relative to relying on geo targeting alone?
**why it matters:** It is the single most DR-applicable competitor observation — Soccer Shots' *"Soccer at Your Child's School! ⚽️🏫"* is the only ad in 99 to put delivery location in the title, and it comes from the closest local delivery-model analog. It maps to creative clarity and offer-message fit.
**what evidence is missing:** Only **1 brand family** does it, from a 4-ad sample, below the 2-family consensus bar. Its performance is unknowable — Ad Library publishes no results. DR has never tested it.
**could expert research materially help:** **Marginally.** This is better answered by DR running it than by asking anyone. Listed because it is the strongest creative lead in the sweep, not because expert input would settle it.

---

# Final Test — Did external intelligence change a decision?

## **YES.**

Two decisions changed relative to what the DR Phase 2 diagnostic alone would have produced, and one changed relative to what the Meta knowledge base alone would have produced.

### 1. Decision 3 — external intelligence was *rejected* by DR data, correctly

Reading `knowledge/official-meta/` on its own produces a confident recommendation: consolidate. Three independent Meta pages converge on it — combine ad sets and campaigns, avoid high ad volumes, and a $40/day minimum for low-frequency actions.

DR's actual account is **1 campaign / 1 ad set / 1 ad**. The recommendation is not merely unnecessary, it is meaningless. The $40/day figure was also inapplicable: it governs low-frequency *action* optimization, and DR optimizes to `LANDING_PAGE_VIEWS`, which Meta places in the $2.50/day tier.

Had the knowledge base been applied without account data, this synthesis would have shipped a confident, well-cited, wrong recommendation. Tier 1 evidence overruled tier 2, which is exactly the hierarchy working as designed. **A prevented wrong recommendation is a real result.**

### 2. Decision 2 — the geo audit question got materially sharper

Phase 2 (2026-04-24) asks: *"Geo: not visible in extracted targeting payload — risk to validate in Ads Manager."* Correct, and it stops there.

Official Meta documentation adds the mechanism Phase 2 could not: `location_types` defaults to `['home','recent']`, where `recent` is *"determined from mobile device data."* In Orlando — a top-tier US tourist metro — that default reaches visitors who cannot enrol a child in an Orange County after-school season.

So the operator now walks into Ads Manager with **two** questions instead of one: is geo set to Orlando, *and* is the location type restricted to "people living in this location". The second question did not exist in any DR diagnostic and could not have — it comes only from platform documentation.

### 3. Decision 1 — reprioritized by inspecting raw data rather than trusting the newest output

The task instructed not to assume the Phase 2 diagnostic is current if newer snapshots contradict it. They do. The 2026-05-11 diagnostic describes four campaigns and ~$9,246 of spend that appear in no extract, while the 2026-05-12 snapshot — taken the day after — shows the same single paused traffic campaign as every prior snapshot.

That reordering is not attributable to competitor or Meta intelligence. It came from the discipline of verifying against raw evidence, which is the same rule the intelligence domain applies to Ad Library data. It is now the highest-priority item in this document, ahead of every campaign-level decision.

### What did *not* change

Competitor intelligence did **not** change any decision in this synthesis.

The Sprint 1 sweep contributed one supporting observation (2 of 5 families naming location in creative, medium confidence) and one lead that cannot be acted on yet (school-as-location hook, 1 family, 4-ad sample). Nothing from `patterns.md` drove a verdict.

The honest reason: **DR's creative content is not in the extract at all.** With only `ad_name: "DR SPRING"` available, the competitor creative corpus has nothing on the DR side to compare against. The competitor sweep is not failing — it is blocked on a Phase 1 extraction gap. Closing that gap is what would let the Sprint 1 evidence pay off, and it is a cheaper fix than any further competitor research.

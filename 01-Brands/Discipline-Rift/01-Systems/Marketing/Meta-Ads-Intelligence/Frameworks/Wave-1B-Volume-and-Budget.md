---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: framework
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/wave-1b-volume-budget-framework.md"
repo_path: domains/ads/meta/intelligence/output/wave-1b-volume-budget-framework.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/framework
  - discipline-rift
aliases:
  - "Wave 1B"
  - "Volume and Budget Framework"
---

# Wave 1B — Volume + Budget Viability Framework for DR

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1A-Objective-and-Optimization-Event|Wave 1A — objetivo y evento de optimización]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2A-Campaign-Architecture|Wave 2A — arquitectura de campaña]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]
- [[01-Brands/Discipline-Rift/00-Brand-Core/KPIs|DR KPIs]]
- [[01-Brands/Discipline-Rift/00-Brand-Core/Constraints|DR Constraints]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/output/wave-1b-volume-budget-framework.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Date:** 2026-08-13
**Questions:** B1 (event volume/learning) · B2 (budget viability) · B3 (low-volume learning)
**Knowledge level:** DR HYPOTHESIS / conditional framework, built on PLATFORM FACT + DR's own historical cost data. Nothing here is proven — no campaign, budget, or setting has changed.
**Inherits from:** `output/wave-1a-event-framework.md` (objective conditional: Sales→Website now, Leads→Website if CAPI/CRM/website-form audit clears — see Stage-1 decision-input check below, which resolves that condition **negative today**: no CAPI/Pixel implementation found in either DR repo. Current-state answer is **Sales → Website**.)

---

## 0. What Stage 1 (DR decision-input check) changed

Read-only inspection of DR's frontend (`DISCIPLINERIFT-FRONTEND`) and automation repo found:

- **Registration + payment complete online, same session** — Supabase writes `parent/student/enrollment` at step 4, Stripe Checkout (hosted redirect) at step 6, `enrollment.isactive=true` + `payment` row on confirm. `Complete registration` and `Purchase`-style events are both technically truthful for this funnel.
- **Supabase is the sole system of record** for registration/payment status — no separate CRM.
- **No Meta Pixel or Conversions API implementation exists in code** — grepped both repos for `fbq`, `facebook pixel`, `Conversions API`, `CAPI`: zero hits. This is a stronger negative than "CAPI health unknown" — base tracking infrastructure for Meta appears absent, not just the qualified-leads layer.
- DR's registration flow is a multi-step checkout, not a lead-capture form — **LIKELY_NO** on "website form" applicability for qualified-leads optimization.

**Consequence for this file:** the Leads→Website / qualified-leads branch is **not buildable today** (CAPI prerequisite unmet). Wave 1B therefore treats **Sales → Website, ladder R0/R1/R3** as the operative case, and carries the Leads branch only as "if built" per Wave 1A's own instruction not to pretend it exists.

---

## 1. B1 — Event volume / learning

### What Meta actually establishes (PLATFORM FACT, already retrieved — `learning-phase.md`, `learning-limited.md`)

- Exit condition is **"deliver stably"**; "about 50 results/optimization events in the week after the last significant edit" is Meta's own description of when that *usually* happens — not a rule, not a cliff, not exact.
- Meta names five learning-limited causes: small audience, low budget, low bid/cost control, high auction overlap, infrequent optimization event, or running too many ads at once. **Four of five plausibly describe DR by construction** (single metro, narrow age band, thin budget, and — under the current `LANDING_PAGE_VIEWS`/Traffic setup — an event chosen for volume, not value).
- Meta's own stated fix for an infrequent event: **"choose an optimization event that occurs more frequently"** — moving up-funnel is platform-sanctioned, not a workaround.
- Below-threshold delivery is explicitly **not a penalty** — "less stable, usually higher CPA" is the cost, not disqualification. Results during learning are "not necessarily indicative of future performance."
- No numeric floor exists for how low is "too low to ever exit" — Meta states none.

### What is still learnable below ~50/week

- **Delivery health** — is the ad set spending, or stalled entirely (learning-limited badge, near-zero impressions)? Binary and readable at any volume.
- **Directional cost trend** — CPM/CPC/cost-per-LPV moving up or down across weeks. Not statistically powered, but a persistent multi-week trend at DR's own historical variance is a real (if weak) signal.
- **Gross targeting/geo sanity** — obvious waste (delivery to clearly wrong geography/age) is visible in raw counts without needing 50/week.
- **Rung viability** — whether an event fires *at all* in a given week (0 vs. >0) is checkable with single-digit counts; whether it fires *enough to be worth building on* is not.

### What is NOT learnable below ~50/week

- Fine-grained creative A/B calls (a 2-vs-3 click difference is noise, not a winner).
- CPA comparisons between rungs precise enough to declare one "better" at DR's current volume (10 link clicks / 30 days, per Wave 1A).
- Whether a rung has genuinely "exited learning" in Meta's stability sense — DR's ad sets are very unlikely to reach it on `Complete registration` or `Purchase` at current spend, meaning **conclusions drawn while learning-limited must be labeled DIRECTIONAL, never SUFFICIENTLY_STRONG.**

### Practitioner layer

No credible new practitioner source was found this run (see §5). The existing Wave 1A ingest already carries the load-bearing dissent here: **Kerhoas — "Many businesses won't hit 50 conversions per week per ad set… that's not a reason to panic or rebuild."** Consistent with Meta's own "not a penalty" framing. No further practitioner discovery needed on this specific point — it would only re-confirm an already-converged view (Meta text + Kerhoas).

### B1 status

**ENOUGH_EVIDENCE** — the volume conditions are characterized as a range/condition (not a threshold), what remains learnable below them is stated, and further practitioner sources are unlikely to move this (the loop of near-identical SEO content-farm pages found this run reinforces the numeric folklore rather than adding evidence — see §5). Closed 2026-08-13.

---

## 2. B2 — Budget viability

### DR's own historical cost data (source hierarchy tier 1 — the strongest evidence available for this question)

From `domains/ads/meta/discipline-rift/data/raw/` (2026-03-18 → 2026-04-23, `DR SPRING 2`, `OUTCOME_TRAFFIC` / `LANDING_PAGE_VIEWS`, single ad set):

| Window | Spend | Impr. | Clicks | Landing page views | CPM | Cost/link-click | Cost/LPV |
|---|---|---|---|---|---|---|---|
| 2026-03-18–04-16 (30d) | $110.29 | 1,153 | 11 (3 outbound) | 9 | $95.65 | $36.76 | $12.25 |
| 2026-03-25–04-23 (30d) | $82.11 | 1,015 | 10 | — (not itemized this export) | $80.90 | $8.21* | — |

*\*Second window's `cost/click` uses all clicks (10), not outbound-only; not directly comparable to the $36.76 outbound-click figure in the first window — flagged, not reconciled.*

**This is thin but real, and it is DR's own funnel** — no registration or purchase event fired in either window (none appears in the `actions` array), so **cost-per-registration is currently unmeasured, not merely uncertain.** LPV and link-click costs are the only DR-native cost anchors available.

### Meta's 10× reference, applied

Meta: *"your daily budget should be at least 10 times the average cost of your performance goal"* — a rule of thumb, not a cliff (already corrected in Wave 1A).

Applying DR's own LPV cost (~$12/LPV) as the reference: **10× ≈ $120/day** to be "budgeted comfortably" for LPV optimization by Meta's own heuristic. DR's actual historical spend (~$2.70–3.70/day across these windows) is roughly **30–45× below** that reference — not "a bit thin," structurally far under Meta's own rule of thumb for the shallowest rung already in use.

No DR cost-per-registration exists to apply the same math to R0/R1. Scenario ranges below fill that gap explicitly as assumptions, not observations.

### Cost / event scenario model

| Rung | Objective | Quality | Rel. frequency | DR cost evidence | Cost assumption (range) | 10× implication | ~50/wk implication | Still learnable below | Major failure mode | DR capability req. | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R3 `Landing page view` | Sales (or current Traffic) | Low | Highest | **Observed:** ~$12.25/LPV (n=9, 1 window) | $8–$18/LPV (DR's own range ± spread) | ~$80–180/day | DR's ~9 LPV/30d ≈ 2/week — far below 50, even at current spend | Delivery health, gross geo/targeting sanity, multi-week cost trend | Optimizing toward clicks that don't convert; buys volume, not intent | None beyond current Pixel base event | Moderate — DR data exists |
| R4 `Link click` | Sales/Traffic | Lower | High | **Observed:** $8.21–$36.76/click (two windows disagree — see caveat above) | wide, unreconciled | not meaningfully computable from conflicting DR data | ~10–11/week — also far below 50 | Delivery health only | Cheapest to buy, least correlated with registration; deprioritized per Wave 1A (§R4) | None | Low — data itself is inconsistent |
| R1 `Complete registration` | Sales or Leads | Very high | Lowest | **None — zero registrations recorded in either extracted window** | No credible external benchmark found (see §5); **no defensible number can be stated** | Cannot be computed — no cost-per-event exists to multiply | Structurally near-zero at current spend | Whether the event fires *at all* in a given month (binary) | Cheap non-payers if registration ≠ paid; R0/R1 distinction (Wave 1A) | Requires conversion tracking to be wired up **and** firing before this can even be measured | **None — this cell cannot be filled responsibly, and that itself is the finding** |
| R0 `Purchase` | Sales only | Highest | Lowest | None | Same as R1 | Same as R1 | Same as R1 | Same as R1 | Same as R1, plus whether registration ever fires as a distinct Purchase event | Same as R1, plus Stripe→Meta event bridge (currently absent — Stage 1) | None |
| R1q `Qualified leads` | Leads only | Highest (CRM-fed) | N/A | N/A | N/A | N/A | N/A | N/A | Degrades to plain lead opt. without real CRM feedback | **CAPI (absent — Stage 1), CRM sync, website-form fit (doubtful — Stage 1)** | Not viable today — infrastructure gate, not a cost question |

### What the honest budget answer is

**No defensible single number exists for cost-per-registration.** Two reasons compound: (1) no comparable external source survived pre-screen (§5 — the entire SEO-farm CPL literature found this run lacks event definition, methodology, or a comparable business context, and is explicitly excluded by `CLAUDE.md`'s source-quality rules); (2) no registration/purchase action appears in the referenced exported Meta `actions` arrays, so registration-level Meta signal is **unmeasured in those extracts** and there is no DR-native anchor either — **this is not proof that paid registrations did not occur** outside what those extracts captured. Manufacturing a number here would be exactly the false precision the numeric-threshold rule prohibits.

What **can** be stated honestly, as conditional formulas:

> **IF** cost-per-registration for DR eventually proves comparable to its own cost-per-LPV order of magnitude (i.e., single-digit-to-low-double-digit dollars, which is speculative — registrations are a much deeper, rarer action than LPVs and typically cost substantially more per the general shape of funnels, though DR has no data establishing the multiple) **AND** the target is Meta's own ~50/week learning reference, **THEN** the implied 10×-heuristic daily budget would be an order of magnitude above DR's current $2.70–3.70/day — plausibly $100s/day, not $10s/day, to seriously pursue R0/R1 delivery stability. This is a shape, not a number DR should budget from.

> **IF** the business instead accepts operating on R3 (LPV) as a deliberate floor while R0/R1 remain unreachable, **THEN** DR's own data (~$12/LPV) makes Meta's 10× reference for that shallower rung (~$120/day) directly computable — and DR is currently ~30–45× under it. Even partial movement toward that reference (say $20–40/day) would materially change what's learnable (§3) without requiring the deep event to exist yet.

### Budget tiers for the business (qualitative — no invented numeric cliffs)

- **At current spend (~$3/day):** buys impressions and a trickle of clicks/LPVs. Not enough for stable delivery on any rung; readable only as delivery-health and gross-waste checks (§3). This is the "impressions, not evidence" floor the research questions asked about.
- **At a spend that clears Meta's 10× reference for the *shallowest* usable rung (LPV, ~$80–180/day per DR's own cost):** directional, multi-week cost trends and rung viability become meaningfully readable; still not enough for registration-level learning.
- **At a spend high enough to generate registration events at all, repeatedly, across weeks (unknown magnitude — no data exists to size this for DR):** the deep-event rungs (R0/R1) become testable, and only then does S1 (ratio monitoring, Wave 1A §D) become runnable on real numbers.

### B2 status

**OPEN, closed as far as external evidence allows.** DR's own cost data is used and stated as the strongest available tier-1 evidence; the interpretability floor is stated as a qualitative/conditional structure, not a number, because no credible source (DR or external) exists to support one for the registration event specifically. Re-open with fresh evidence the moment DR records its first Meta-attributed registration, or if paid conversion tracking is ever wired up (Stage 1 finding: currently absent).

---

## 3. B3 — What low volume can and cannot teach

### Internal baseline

`output/experiments.md` (v1) already frames directional-read methodology and states its experiments are unpowered at current spend — consistent with everything found this run; not re-litigated here.

### Honest boundary, restated with DR's actual (thin) data as the test case

**DIRECTIONAL (defensible at DR's current volume):**
- Delivery failure — an ad set stuck at near-zero spend/impressions relative to budget.
- Extreme creative mismatch — one creative getting materially zero engagement against another over weeks, not days.
- Obvious geo waste — delivery concentrated clearly outside DR's service area.
- Rung viability (binary) — did the chosen event fire at all this month, yes/no.
- Multi-week cost-trend direction (CPM/CPC/CPL rising or falling), read as a trend, never as a point estimate.
- Proxy-event drift, once a ratio exists to monitor (Wave 1A S1) — not yet runnable; needs registration-level truth DR does not currently join to ad exposure (Stage 1: Supabase holds it, but no join to Meta spend exists yet).

**CANNOT BE RESPONSIBLY CLAIMED at DR's current or near-term volume:**
- Any statement of the form "Ad A beats Ad B" from single-digit or low-double-digit event counts (DR's actual data: 9–11 total clicks per 30-day window — this is the literal example the task warned against, not a hypothetical).
- Any CPA comparison between optimization rungs.
- Any claim that a rung has "exited learning" — DR's ad sets, at current volume, are not close to Meta's own ~50/week reference on any deep event.
- Any qualified-vs-unqualified ratio claim — S1 requires registration data joined to spend, which does not exist yet (Stage 1 finding).
- Any statement about whether Sales vs. Leads objective "worked better" — neither has been run with a deep conversion event live.

### Framework for labeling evidence

Every future DR read should carry one of two labels, stated explicitly, per the task's requirement:

- **DIRECTIONAL** — consistent with the categories above; stated with its sample size and window, never presented as concluded.
- **SUFFICIENTLY_STRONG** — reserved for results that clear a stated volume/stability bar (tied to B1's honest characterization, not a manufactured number) and are corroborated across more than one time window.

No DR evidence collected to date qualifies as SUFFICIENTLY_STRONG on any question this domain cares about.

### B3 status

**ENOUGH_EVIDENCE** — the boundary is stated with DR's own data as the worked example, and a two-label framework exists for future experiments to declare which side of the line they're on. Closed 2026-08-13.

---

## 4. Feedback to Wave 1A

**No reopening triggered.** B1/B2/B3 did not find the preferred ladder economically or statistically implausible in a way that overturns A2/A3's structure — they instead confirm and sharpen what A2/A3 already stated conditionally (up-funnel fallback is platform-sanctioned; deep-event viability is presently unmeasured, not proven impossible). What *did* change is operational, not evidential: Stage 1's finding that **no Pixel/CAPI exists at all** resolves Wave 1A's conditional rule to **Sales → Website** as DR's current-state answer, and adds a prerequisite (Pixel/CAPI implementation) beneath everything in this file that was previously implicit.

A2/A3 remain in their prior statuses (`REOPENED` per the correction pass) pending the compliance review (R2) and the "website form" definitional question (R1q) — neither of which Wave 1B evidence touches. Recorded, not resolved here.

---

## 5. Practitioner / benchmark sources — this run

**Searched:** youth-sports/enrichment CPL case studies; low-budget/small-business learning-phase practitioner guidance; named practitioners already in this domain's corpus (Kerhoas, Gardideh, Vigneron) on low-volume learnability.

**Candidates evaluated:** ~25 URLs across two search batches. **Zero shortlisted, zero ingested.**

**Rejected, with reason:**
- Nearly the entire "Meta Ads cost per lead 2026 benchmarks" cluster (amraandelma, adovateagency, adamigo, admanage, get-ryze, enrichlabs, sotrosinfotech, stackmatix, 2pointagency) — **content-farm CPL aggregation with no stated event definition, methodology, sample, or business context.** Explicitly the category `CLAUDE.md` §Source quality prohibits. One even asserted a specific 2025→2026 CPL delta ($21.98→$26.43) with no traceable source — the definition of manufactured precision this domain's numeric-threshold rule exists to block.
- The entire "Meta learning phase 2026 guide" cluster (ads.expert, benly.ai, tribeupacademy, niblin, thesocialoutline, modernmarketinginstitute, adstellar, withblip, growwithsakib, code3) — **near-identical SEO restatements of Meta's own ~50/week figure**, several asserting a fabricated "10 conversions in 3 days" alternate rule with no citation. This directly **conflicts** with Meta's first-party text already in this knowledge base (`learning-phase.md`) and is not corroboration — it is the same unsourced folklore multiplying, which `CLAUDE.md` explicitly warns against ("framework-independence warning" already noted in the Wave 1A run log for the 50/week figure itself).
- **Find Your Club "$0.27 cost-per-lead" youth sports case study** — the one candidate with a specific named vertical. Rejected: no spend total disclosed, no registration/paid outcome tracked (stops at landing-page-view retention), self-published by the service provider selling the strategy (promotional venue), and $0.27 CPL with no denominator disclosed is not independently verifiable. Same failure pattern as the customcreatives.com case Wave 1A already rejected.
- Gumroad product listings ("Meta Ads Made Affordable," etc.) — paid products, no accessible substantive content, promotional.

**Conclusion:** no credible independent evidence exists, this run, to support a numeric cost-per-registration or cost-per-lead figure for a business in DR's context. This absence is itself recorded per the task's explicit instruction ("if comparable cost evidence does not exist, say so") rather than papered over with the rejected material.

---

## 6. Paid retrieval

**$0.00 spent.** No Apify retrieval attempted — native WebSearch was sufficient to determine that no candidate cleared pre-screen; nothing reached the point of needing paid transcript retrieval. Ceilings ($0.05/source, $0.25/batch) not approached.

---

## 7. Business decision — what this hands to management

**At DR's current spend (~$3/day):** Meta is not being asked to find registrants (still `OUTCOME_TRAFFIC`), and even on the shallow LPV rung DR runs ~30–45× under Meta's own 10× reference. What this spend can produce: delivery-health checks and very coarse directional signal only. It cannot produce a registration-cost figure, a winning-creative call, or a validated objective choice — and treating any current number that way would be false precision.

**To get a real read on the shallow rung (LPV/R3):** spend near DR's own computed 10× reference for LPV (~$80–180/day, from DR's own $12.25/LPV) would make multi-week cost trend and rung viability directionally readable within weeks, without requiring the deep event to exist yet.

**To ever test the deep rungs (R0/R1, and eventually R1q if CAPI is built):** no credible number can be given — registration-level Meta signal is **unmeasured in the available extracts** (no registration/purchase action appears in the referenced exported `actions` arrays; this does not prove registrations never occurred), and no external source in DR's context survived screening. The honest next step is not "spend more," it is **get a registration/purchase event firing and observed in the extracts at all**, even sporadically, before any registration-level budget question can be answered with real evidence rather than assumption.

**Decision for management:** the binding constraint right now is not budget sizing — it's that **no Meta Pixel/CAPI implementation code was found in the inspected DR repositories** (Stage 1 finding — this does **not** prove that no live or partner-side integration exists; the live account state was not inspected) and that the last-known campaign ran an objective (`OUTCOME_TRAFFIC`) that structurally never asks Meta to find registrants. Fixing those two things is a prerequisite to every dollar-amount question in this file being answerable with evidence instead of scenario ranges.

---

## What would change this framework

- **DR records its first Meta-attributed `Complete registration` or `Purchase` event** — immediately fills the empty B2 scenario cells with real DR-tier-1 evidence and is the single highest-value data point this whole framework is waiting on.
- **Pixel/CAPI gets implemented** — unlocks R0/R1 measurement and reopens the Leads→Website/R1q branch's feasibility question (still separately gated on CRM sync and the "website form" definition).
- **DR spend materially increases** — the scenario ranges in §2 become testable rather than hypothetical; re-run B1/B2 against real delivery data at the new spend level.
- **A credible comparable-context source surfaces later** (a registration/enrollment business, methodology disclosed, spend and event definition stated) — would fill the B2 cost gap this run could not. Actively watch for; do not manufacture in its absence.

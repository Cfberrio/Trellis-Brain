---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/andrew-foxwell.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/andrew-foxwell.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Andrew Foxwell"
  - "Paul Fairbrother"
---

# Andrew Foxwell (with Paul Fairbrother)

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Courtney-Fritts|Courtney Fritts — mismo cluster de independencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/andrew-foxwell.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** andrew-foxwell
**Watchlist priority:** 1
**Topics:** creative_testing · campaign_structure · scaling · measurement · budgeting · bid_cost_controls
**Sources processed:** 5
**Last updated:** 2026-08-19
**Panel status:** **SOURCE_CONTRIBUTOR** for the *video* corpus (assigned 2026-08-19). All 20 videos are 2024/HISTORICAL and are predominantly **other people's claims** recorded on his community podcast — see the Phase 3 section. His own 2025-2026 articles remain the only basis for a current position attributed to him.
**Independence cluster:** **FOXWELL ECOSYSTEM** — shares a cluster with `courtney-fritts.md` (both publish on foxwelldigital.com). **These are NOT independent confirmations of each other.** Where they agree, that is one ecosystem's position; where they disagree, that disagreement is informative and is recorded below.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.foxwelldigital.com/blog/the-meta-creative-testing-frameworks-top-brands-use-in-2026` | article | 2026-03-13 | 2026-08-14 | **4** | D1, D2, D4 |

**Stated context:** co-authored by Andrew Foxwell (Foxwell Digital) and Paul Fairbrother (Fairbrother Agency). Agency-side paid social, **DTC/ecommerce framing throughout**. The article scopes its two methods by *creative production volume*, and cites volume benchmarks of *"a new batch of creative once a week"* (new advertisers), *"40-50 new ads per month"* (mid-sized) and *"100 ads per month and anything upwards"* (larger brands). **No client spend levels, conversion volumes, or results are disclosed for either method.**

**Retrieval:** WebFetch (native), full body.

---

## Claims — article (2026-03-13)

### creative_testing — Method 1: one creative batch per ad set, with a dedicated ABO budget

```yaml
topic: creative_testing
claim: Build a new ad set for each batch of creative and use ad-set budgets so every batch has a guaranteed dedicated testing budget, ensuring each creative brief receives some spend.
recommended_action: "For each new batch of creative, build a new ad set using ABO so the batch has its own testing budget."
context: "brands with a small creative volume or especially those new to advertising"
business_type: ecommerce
spend_level: null
conversion_volume_context: "scoped by creative output: 'a new batch of creative once a week' for new advertisers"
research_question_ids: [D1, D2]
published_at: 2026-03-13
source_url: https://www.foxwelldigital.com/blog/the-meta-creative-testing-frameworks-top-brands-use-in-2026
author: Andrew Foxwell and Paul Fairbrother
evidence: "for each new batch of creative, we build a new ad set. By using ABO...we ensure each batch has a dedicated budget for testing." / "Each creative brief is guaranteed to get some budget" / Cons: "your ads spend more time in the learning phase" / winning ads "can't compete with other stronger batches" / "things can soon escalate with far too many ad sets"
timestamp: "Method 1"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Agency practice described, with pros and cons stated candidly. No account data, no comparison against Method 2, no results shown for either."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

> "for each new batch of creative, we build a new ad set. By using ABO...we ensure each batch has a dedicated budget for testing."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** **yes** · **implementation_transfers:** **no**
**reason:** **This is the strongest external challenge to DR's D1 answer, and it must be recorded as such.** The authors associate Method 1 specifically with *"brands with a small creative volume or especially those new to advertising"* — a description that fits DR. **The principle — guaranteeing budget to new creative produces cleaner reads than letting it compete — transfers, and it is the same principle behind Meta's own Creative Testing feature (which *provides* delivery to test ads).** The implementation does not transfer: a dedicated ABO testing ad set at DR's budget fragments an already-thin spend across two structures, duplicates a single small Orlando audience against itself, and triggers a C2 architecture reopen. Note also the authors' own stated cons cut against DR specifically: *"your ads spend more time in the learning phase"* is a serious cost on an account that already struggles to accumulate events. `PARTIALLY_SUPPORTED`: Meta documents that ad-set budgets give *"more control in delivery"* and that spend limits exist, so the mechanism is real; Meta endorses no such architecture and separately advises *"avoid high ad volumes"* and combining ad sets.

### creative_testing — Method 2: introduce fresh creative directly into main campaigns

```yaml
topic: creative_testing
claim: Dropping new creative straight into the main campaigns is simpler, keeps campaigns continuously supplied with fresh ads, and surfaces the ads that will actually spend — at the cost of some creatives being effectively wasted and low-spend batches yielding no conclusions.
recommended_action: "Place fresh creative directly into main campaigns rather than maintaining separate testing ad sets."
context: "as soon as creative output starts to scale"
business_type: ecommerce
spend_level: null
conversion_volume_context: "associated with scaled creative output (40-50+ new ads per month)"
research_question_ids: [D1, D2]
published_at: 2026-03-13
source_url: https://www.foxwelldigital.com/blog/the-meta-creative-testing-frameworks-top-brands-use-in-2026
author: Andrew Foxwell and Paul Fairbrother
evidence: "drop fresh creative directly into your main campaigns rather than having separate testing ad sets" / Pros: "Simplicity; media buyers never need to move ads between campaigns" / "your main campaigns are always topped up with fresh ads" / "It finds the ads that will spend the most" / Cons: "Meta will favor the ad and instantly give it a lot of spend...burns through a lot of your budget" / "Some ads are 'wasted'" / "If a batch...gets very little spend, it's hard to generate conclusions"
timestamp: "Method 2"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Described as what 'a lot of successful ad accounts' shift to; no accounts named, no data, no outcome comparison."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

> "If a batch of ads gets very little spend, it's hard to generate conclusions."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** This is DR's chosen method, and the source's stated **con is exactly DR's situation** — *"If a batch gets very little spend, it's hard to generate conclusions."* That is an independent practitioner statement of the same conclusion DR reached from its own arithmetic and from Meta's *"evaluate at ad set level"* instruction. **The authors scope this method to scaled creative output, which DR does not have** — so DR is adopting it for a different reason (budget) than the one they give (creative volume), and that difference is recorded rather than glossed. `PARTIALLY_SUPPORTED`: Meta's creative-test design keeps introduction in-campaign and the consolidation guidance agrees; Meta makes no claim about which method performs better.

### creative_testing — Under natural allocation, a minority of ads take most of the spend

```yaml
topic: creative_testing
claim: When many ads compete under Meta's current delivery system, a small minority absorb the large majority of spend and the rest receive almost none.
recommended_action: null
context: natural delivery with many ads in one structure
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [D4]
published_at: 2026-03-13
source_url: https://www.foxwelldigital.com/blog/the-meta-creative-testing-frameworks-top-brands-use-in-2026
author: Andrew Foxwell and Paul Fairbrother
evidence: "If you give Andromeda 10 ads, most likely two or three will get 80% of the total spend, with the rest being starved of budget."
timestamp: "Method comparison"
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "Pattern asserted from agency observation across accounts. The 2-3 of 10 / 80% figures are illustrative — no dataset, distribution, or account sample is presented."
evidence_strength: weak
platform_validation_status: SUPPORTED
```

> "If you give Andromeda 10 ads, most likely two or three will get 80% of the total spend, with the rest being starved of budget."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** **yes** · **implementation_transfers:** n/a (no action recommended — recorded as `null`, not inferred)
**reason:** `SUPPORTED` — this is the **same phenomenon Meta documents as the breakdown effect**, described from the operator side: *"it's normal for some ad sets or ads to deliver less than others"* and the system allocates for aggregate results, not evenly. **Two independent evidence layers now describe the same mechanism**, one of them first-party. The word *"starved"* is the operator's framing and carries an implicit judgement Meta's framing does not; **the observation transfers, the pejorative does not.** The 2-3-of-10 / 80% figures **must not become a DR threshold** — they are illustrative and unsourced.

### creative_testing — Dedicated testing ad sets carry a learning-phase and account-bloat cost

```yaml
topic: campaign_structure
claim: Running a separate ad set per creative batch keeps ads in the learning phase longer, prevents winners from competing against other batches, and proliferates ad sets.
recommended_action: null
context: Method 1's stated drawbacks
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, D2]
published_at: 2026-03-13
source_url: https://www.foxwelldigital.com/blog/the-meta-creative-testing-frameworks-top-brands-use-in-2026
author: Andrew Foxwell and Paul Fairbrother
evidence: "your ads spend more time in the learning phase" / winning ads "can't compete with other stronger batches" / "things can soon escalate with far too many ad sets"
timestamp: "Method 1 cons"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Drawbacks stated candidly from practice; no measurement of the learning-phase cost presented."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** n/a
**reason:** **The proponents of the dedicated-testing-ad-set method name its costs themselves, and those costs land hardest on DR.** More time in the learning phase is expensive precisely where events are scarce. `PARTIALLY_SUPPORTED`: Meta confirms the learning mechanics (`learning-phase.md`, `significant-edits.md`) and separately advises *"avoid high ad volumes"* and that *"combining similar ad sets… combines learnings"* — it does not quantify the cost of the split.

## Contradictions within this cluster

**Recorded, and it is material.** This source associates Method 1 (dedicated testing ad set) with *"brands with a small creative volume or especially those new to advertising"*. `courtney-fritts.md`, publishing in the same ecosystem, states that **for accounts under $100/day, direct competition or manual bids "might be your only viable options"** — i.e. *not* Method 1.

These are not strictly contradictory: **one scopes by creative volume, the other by budget.** DR is low on both, but its **binding constraint is budget**, and the budget-scoped statement is the one that applies. Recorded rather than resolved in favour of either — see `output/wave-2b-creative-operating-method.md §2`.

## Open questions from this source

- No spend level is attached to either method, so neither is scoped to a budget.
- No results are presented for either method — the article compares designs, not outcomes.
- The "2 or 3 of 10 ads get 80%" figure has no stated sample, period, or account base.
- Whether Method 1's guaranteed-budget benefit can be obtained without a second ad set — Meta's native Creative Testing appears to do exactly that, and this article does not discuss the feature.

---

# Phase 2 ingestion — 2026-08-19

**Run:** `knowledge/research-runs/2026-08-19_phase2-expert-corpus/`. Four additional foxwelldigital.com articles, retrieved by crawl, all with **exact publication dates from page metadata**. Written first-party text — quotable verbatim, no speech recognition involved.

**Independence cluster still applies:** FOXWELL ECOSYSTEM. Nothing below is independent of `courtney-fritts.md`.

## Sources processed (Phase 2)

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.foxwelldigital.com/blog/how-to-create-systematic-growth-frameworks-on-meta-for-confident-scaling` | article | 2026-03-11 | 2026-08-19 | 3 | C1, C2, F1, D3 |
| `https://www.foxwelldigital.com/blog/the-9-most-pressing-topics-for-meta-advertisers-in-q3-2026` | article | 2026-07-03 | 2026-08-19 | 3 | D1, D3, C4 |
| `https://www.foxwelldigital.com/blog/the-incrementality-problem-with-performance-max` | article | 2026-08-14 | 2026-08-19 | 2 | C1, G2 |
| `https://www.foxwelldigital.com/blog/why-your-meta-ads-are-failing-and-its-not-metas-fault` | article | 2025-11-17 | 2026-08-19 | 0 | — |

**Stated context (Phase 2 sources):** agency + paid membership community; DTC/ecommerce framing throughout. The PMax article is **Google Ads**, not Meta — it is ingested only for the two claims whose mechanism is channel-independent, and both are labelled accordingly.

---

## Claims — Phase 2

### scaling — "Harvesting vs growing": blended metrics hide stalled acquisition

```yaml
topic: measurement
claim: An account can look healthy on blended ROAS and MER while new-customer acquisition has silently stalled, because performance is being carried by engaged audiences and retargeting — re-monetizing people who already knew the brand rather than adding new ones.
recommended_action: "Judge scaling on new-customer CPA, first-time-buyer revenue and cold-campaign stability as budgets rise — not on blended ROAS. Diagnose it with the Audience Breakdown, without splitting campaigns or ad sets, and check whether removing retargeting budget collapses overall performance."
context: Scaling diagnostics used across the author's membership community.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [F1, G2]
question_link_origin: prospective
published_at: 2026-03-11
source_url: https://www.foxwelldigital.com/blog/how-to-create-systematic-growth-frameworks-on-meta-for-confident-scaling
author: Andrew Foxwell
timestamp: "Harvesting vs. Growing: The Scaling Illusion"
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "Presented as one of the community's most-used diagnostics across member accounts; no account data, distribution or worked example is shown."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "When the account appears healthy due to engaged-audience performance and retargeting efficiency, harvesting occurs. Blended ROAS appears to be in order. MER is fine. However, cold campaigns are ineffective… look at your retargeting separate from prospecting via Audience Breakdown - you don't even need to separate them out by campaign or ad set."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **The methodological point directly supports F1's deferral and is the most useful sentence here: warm and cold performance can be read through a breakdown rather than through separate structures.** That removes the main argument for building retargeting architecture "so we can measure it" — DR can see the split without paying the fragmentation cost E3 and C1 rejected. The diagnostic itself is not yet runnable: DR has no warm pool worth harvesting and no measured new-customer cost. It becomes live the moment DR sustains delivery across a registration window, and it is the right guard against a real DR failure mode — a second season that looks fine because it is re-reaching last season's parents while reaching no new ones.

---

### campaign_structure — Under-fed campaigns should be consolidated, and small advertisers should let one automated campaign carry the signal

```yaml
topic: campaign_structure
claim: When splitting an account means each resulting campaign gets roughly five conversions a week, none will exit the learning phase; a consolidated automated campaign can outperform the sum of its under-fed parts. He scopes this to advertisers under roughly $10-15K/month in that channel.
recommended_action: Below that spend level, keep the structure consolidated rather than splitting into dedicated campaigns — with one exception he calls non-negotiable, separating branded from non-branded demand.
context: Written about Google Performance Max, as the one scenario where PMax genuinely wins.
business_type: ecommerce
spend_level: "< $10-15K/month in that channel"
conversion_volume_context: "~5 conversions per campaign per week if split"
research_question_ids: [C1, C4]
question_link_origin: prospective
published_at: 2026-08-14
source_url: https://www.foxwelldigital.com/blog/the-incrementality-problem-with-performance-max
author: Andrew Foxwell
timestamp: "When PMax Does Make Sense"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as agency experience with an explicit spend threshold; no data presented. **Channel caveat: this is Google Ads, not Meta.** The mechanism cited — signal starvation from splitting — is channel-independent, but the $10-15K figure is a Google-specific judgement and is not transferable as a number."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "You're a small advertiser (< $10-15K/mo in Google spend) and you don't have enough conversion volume to feed separate campaigns. If splitting into Brand Search, Non-Brand Search, Shopping, YouTube, and Display means each campaign gets 5 conversions per week, you'll never exit the learning phase. PMax consolidates signal across placements and can actually perform better than the sum of its under-fed parts."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** **The clearest statement in the whole corpus of the reasoning behind C1**, and it comes from someone arguing *against* automation everywhere else in the same article — which makes it a concession rather than a preference, and therefore stronger. The principle is exactly DR's: below a volume floor, splitting starves every resulting unit, so consolidation is not a compromise but the only structure that can learn. **The number does not transfer** (different channel, different auction, and DR is an order of magnitude below even his floor), and the domain's numeric-threshold rule forbids adopting $10-15K as a DR figure. His "non-negotiable" exception — separate branded from non-branded — has no Meta analogue and should not be imported.

---

### measurement — The channels that look best in-platform tend to be the least incremental

```yaml
topic: measurement
claim: Across geo holdout and matched-market testing, placements with the highest attributed ROAS (branded search, remarketing display) show the lowest incrementality, while placements that look worst in-platform (YouTube) often show the highest — attributed and incremental ROAS are inversely related along that gradient.
recommended_action: Do not allocate on attributed ROAS; measure incrementality with geo holdouts or matched-market tests before trusting a placement's in-platform numbers.
context: Google Ads placements; directional ranges from the author's own testing, presented with an explicit "your mileage will vary" caveat.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [G2]
question_link_origin: prospective
published_at: 2026-08-14
source_url: https://www.foxwelldigital.com/blog/the-incrementality-problem-with-performance-max
author: Andrew Foxwell
timestamp: "The Incrementality Gradient"
confidence: high
evidence_basis: self_reported_test
evidence_basis_details: "A published table of attributed vs incremental ROAS ranges per placement (e.g. brand search 8-12x attributed vs 0-2x incremental; YouTube 0.5-2x attributed vs 2-5x incremental) drawn from the agency's own geo holdout tests. Ranges are directional and the underlying tests are not published. **Google Ads, not Meta.**"
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "Notice something? The channels that look best in-platform (Brand Search, remarketing Display) have the lowest incrementality. The channels that look worst in-platform (YouTube) often have the highest."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** Independent corroboration of the same direction Common Thread Collective reports on the Meta side — bottom-of-funnel surfaces over-report — reached by a different agency with a different dataset on a different platform. That convergence is worth more than two Meta practitioners agreeing. **The numbers are Google's and transfer to nothing DR does**, and geo holdouts are unavailable to a single-metro advertiser. For DR the usable residue is the ordering principle: whatever surface appears to convert most cheaply deserves the most suspicion, not the most budget.

---

### creative_testing — Concept diversity first, format diversity second

```yaml
topic: creative_testing
claim: Creative diversity means different angles, offers and proof points first, and a mix of static, video, carousel and partnership formats second — the concept layer matters more than the format layer for giving the algorithm real signal.
recommended_action: Brief for distinct concepts before distinct formats; treat format mix as the second axis, not the first.
context: Q3 planning guidance ahead of Q4.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [D1]
question_link_origin: prospective
published_at: 2026-07-03
source_url: https://www.foxwelldigital.com/blog/the-9-most-pressing-topics-for-meta-advertisers-in-q3-2026
author: Andrew Foxwell
timestamp: "Creative diversity"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Stated as a prioritization rule; no evidence presented that concept diversity outperforms format diversity."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "Creative diversity means concept diversity first (different angles, offers, and proof points), then format diversity second (a healthy mix of static, video, carousel, and partnership content so the algorithm has real signal to work with)."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** Gives D1's provisional 2-3 per round the ordering rule it lacks, and it is achievable at DR's production capacity: three ads carrying three genuinely different reasons a parent might enrol beats three formats of one message. **It also conflicts usefully with two other panel members** — Motion's CEO (via Ralph Burns) and Barry Hott both put format/visual diversity first. That disagreement is real, unresolved, and cheap for DR to sidestep by varying both at a batch size of three.

---

### creative_refresh — Older creative with accumulated data often beats fresh creative when competition peaks

```yaml
topic: creative_refresh
claim: Ads with months of recent data behind them frequently outperform newly launched creative during peak-competition periods, because the platform has not yet tested the new assets.
recommended_action: Identify winning concepts before the peak season and carry them into it, rather than launching untested creative when competition is highest.
context: Q3-into-Q4 planning for BFCM.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, D3]
question_link_origin: prospective
published_at: 2026-07-03
source_url: https://www.foxwelldigital.com/blog/the-9-most-pressing-topics-for-meta-advertisers-in-q3-2026
author: Andrew Foxwell
timestamp: "Finding Creative Winners in Q3 to Scale in Q4"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as an observed pattern ('many times out-perform'); no comparison data presented."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "ad creatives with months of recent data behind them many times out-perform recently launched creatives that Meta hasn't tested yet when competition on the platform is at an all-year high."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **DR is a seasonal registration business, so it has the same shape of problem with a different calendar** — its peak is the pre-season enrolment window, not BFCM. The claim argues for a specific sequencing DR can adopt: do creative work *before* the registration window opens, so the window runs on assets that already have delivery history, rather than launching new creative into the highest-stakes weeks. It also cuts directly against the calendar-refresh advice elsewhere in this knowledge base (Tomlinson's 7-14 days), and D2 already removed calendar gates — this is a second reason not to refresh on a clock.

---

### bid_cost_controls — Test bid strategies in the low-stakes period to build pattern recognition

```yaml
topic: bid_cost_controls
claim: Lowest-cost/highest-volume gives Meta the most flexibility but can chase lower-value conversions; cost cap and bid cap return efficiency control at the cost of volume; value optimization matters most where order sizes vary widely. Each behaves differently per account, so the pattern must be learned when the cost of being wrong is low.
recommended_action: Test bid strategies during the lower-volume period on smaller budgets, so the choice for the peak period is based on observed account behaviour rather than habit.
context: Q3 preparation for Q4.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [C4]
question_link_origin: prospective
published_at: 2026-07-03
source_url: https://www.foxwelldigital.com/blog/the-9-most-pressing-topics-for-meta-advertisers-in-q3-2026
author: Andrew Foxwell
timestamp: "Bid strategies"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Characterizes each strategy's tradeoff without presenting comparative results; the recommendation to test in the off-peak is procedural advice."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "Lowest cost/highest volume gives Meta the most flexibility, but it can chase lower-value conversions… Testing each on a smaller, lower-stakes Q3 budget builds the pattern recognition needed to choose correctly once CPMs climb."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** The sequencing logic — learn the account's behaviour in the cheap period, not the expensive one — is sound and matches the seasonal argument above. The content is not usable: DR cannot run bid-strategy comparisons at its volume (Taylor Holiday's study shows the outcome distribution is widest exactly where data is thinnest), and cost controls at DR's budget risk suppressing delivery outright. Record the sequencing principle; ignore the strategy comparison until volume exists.

---

## Contradictions within this author (Phase 2)

- **Automation.** The PMax article argues at length against handing structure to an automated system, then concedes that below a volume floor the automated consolidated campaign is the correct choice. Consistent once read as volume-conditional, but the headline and the exception point opposite ways.
- **Concept vs format.** He puts concept diversity ahead of format diversity here; the earlier ingested article (2026-03-13) and other panel members lead with format/production structure.
- **Retargeting.** The scaling framework says to keep cold and retargeting "apart, if done at all", while the harvesting diagnostic says the split can be read from a breakdown without separating anything. The second is the operationally cheaper claim and the one DR should follow.

## Open questions from this author (Phase 2)

1. The harvesting/growing diagnostic is the highest-value idea in this file and carries no evidence at all. Is there a published example where the retargeting-budget-removal test was actually run?
2. His scaling infrastructure pattern ("one or two large CBO campaigns with a single signal, three to six creatives per ad set") is asserted as what members do. Does it come with any spend floor? At DR's volume "three to six creatives per ad set" collides with the capacity arithmetic behind D1's 2-3.
3. The incrementality gradient table is Google-only. Does the Foxwell side hold equivalent Meta-side test data, and does the same inverse relationship appear there?

---

# Phase 3 — full YouTube corpus review (2026-08-19)

**Run:** `knowledge/research-runs/2026-08-19_phase3-full-video-extraction/`
**Method:** every video read start to finish. No passage sampling.

## Corpus coverage

```yaml
downloaded_videos: 20
fully_reviewed: 20
useful: 7
duplicative: 0
low_value: 8
not_relevant: 5
unavailable: 0
words: 121029
date_range: 2024-05-20 .. 2024-12-05
tier: HISTORICAL (20/20)
```

## ⚠ Two findings that must be read before any claim below

**1. Most of this corpus is not Andrew Foxwell speaking.** It is the **Foxwell Founders Forum podcast**, hosted by **Edwin and Tristram**, interviewing members of his paid community. Foxwell appears only in a recorded intro on most episodes. Guests identified: **Akvile DeFazio** (Akvertise), **Jess Bachman** (creative strategy director, Fireteam), **Phil Kiel** (managing director, Hello Earth), **Brad Ploch** (WRK Marketing), **Will Sartorius** (CEO, Selfmade), **Josh** (Align Growth), plus **Courtney Fritts** and named community members in the BFCM recap.

**Attributing these claims to Foxwell would be the same category of error as the Ben Heath multi-location correction.** Every claim below names its actual speaker. Two videos are genuinely Foxwell-led (`cm6nUWeKyo0`, and he participates in `HHVCv51rflY`).

**2. The entire corpus is 2024 — HISTORICAL, all 20 videos, none inside the recency window.** It predates Andromeda, the creative testing tool, value rules, and the attribution changes that dominate the 2026 material. **Nothing here may be cited as current platform behaviour.** What survives is reasoning and arithmetic, not settings advice.

**Consequence for the panel:** the Foxwell *articles* already on file (2025-2026) remain his current position. This video corpus is a **community record**, not an expert corpus, and it is weighted accordingly.

---

## Claims — Phase 3

### campaign_structure — A budget floor for campaign count, stated as an audit rule

```yaml
topic: campaign_structure
claim: An account running more than three campaigns should be spending more than roughly £1,000-1,500 per day; accounts spending around £200/day with five campaigns and multiple ad sets in each are a common and damaging pattern. When performance drops, reducing the number of live ad sets typically produces the same number of sales attributed across fewer places, which is what makes the result readable.
recommended_action: "Consolidate until each live ad set can accumulate enough conversions to be individually readable; treat campaign count as budget-gated."
context: Troubleshooting method for accounts whose performance has fallen. Drawn from accounts his agency audits.
business_type: agency (ecommerce clients)
objective: conversions
spend_level: "audited accounts at ~£200/day; his stated floor for >3 campaigns is >£1,000-1,500/day"
conversion_volume_context: "illustrated with 20 sales split across 2 ad sets vs 10 ad sets"
research_question_ids: [C1, C2, B1]
question_link_origin: prospective
published_at: 2024-06-17
source_url: https://www.youtube.com/watch?v=AniBeD26uU0
author: Phil Kiel (Hello Earth) — NOT Andrew Foxwell
timestamp: "~28:00-31:00 (approx, word-position derived)"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "MULTI_ACCOUNT_EXPERIENCE from agency audits. The 20-sales illustration is hypothetical, not a measured case. No account named, no before/after figures."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

> "if you've got more than three campaigns you best be spending more than… a [thousand] a day" · "I would much rather have two adsets with 20 sales attributed between them rather than 10 adsets with 20 sales attributed between them because then you can say… there's no statistical significance to say I'm going to put my mortgage on this adset"

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** **The clearest articulation in the corpus of *why* fragmentation hurts a small account — it destroys readability, not just efficiency.** That is precisely DR's situation: at DR's volume, splitting would guarantee that no unit ever accumulates enough conversions to justify a decision. The numbers are `PRACTITIONER_SPECIFIC` (UK, 2024, ecommerce) and are **not** adopted; the reasoning is what transfers, and it converges with Loomer's budget-gated splitting rule from an independent cluster. **⚠ 2024, pre-Andromeda.**

---

### creative_testing — A creative needs 2-3× target CPA in spend before any verdict

```yaml
topic: creative_testing
claim: An ad unit must accumulate at least two to three times the expected CPA in spend before it can be called a winner or a loser; judging a creative on a few dollars of spend is a serious mistake. Relatedly, an account cannot support more creative than its testing budget can actually fund, so budget - not creative appetite - sets how many new creatives per month make sense.
recommended_action: "Set a per-creative spend threshold at roughly 2-3x target CPA before rendering any kill/keep verdict, and size creative production to what the testing budget can fund."
context: Creative agency perspective, explicitly criticising cost-cap-driven testing that declares winners on ~$4 of spend.
business_type: agency (ecommerce clients)
spend_level: "example given at $50 CPA -> $150 minimum spend per ad unit; a client spending >$1M/month receives ~30 new creatives per month"
conversion_volume_context: null
research_question_ids: [D1, D2, D3, B1]
question_link_origin: prospective
published_at: 2024-06-03
source_url: https://www.youtube.com/watch?v=h41Ab-8b5yQ
author: Jess Bachman (Fireteam) — NOT Andrew Foxwell
timestamp: "~14:00-17:00 (approx, word-position derived)"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_METHOD from a creative agency. He has a declared commercial interest - his agency is paid to produce the creative that this rule protects from premature killing, and he says so openly ('it's on our balance sheet'). No test data behind the 2-3x figure."
evidence_strength: weak
context_completeness: HIGH
platform_validation_status: NOT_APPLICABLE
```

> "I want to see at least double or triple the expected CPA in spend on an ad unit so if your CPAs are like $50 I want to see at least 150 bucks on that ad unit before we can say it's a winner or loser" · "you can't have more creative than you can effectively test… your overall budget and your testing budget will dictate how much creative you can have per month"

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **This is the missing quantitative half of DR's `NOT_EVALUABLE` rule.** DR holds that a creative with little spend cannot be judged; this states the condition in a form DR can actually compute — *spend on this creative ÷ target cost per registration* — without importing anyone's dollar figure. It converges with Dara Denney's two-condition kill rule and with Loomer's testing-volume floor, from three independent clusters, which is the strongest convergence in the knowledge base on any creative-evaluation question. The second half (budget sets creative volume, not the reverse) is a direct argument for DR's small batches. **⚠ Declared commercial interest; 2024.**

---

### campaign_structure — Cost controls are gated by spend, and hardest at small budgets

```yaml
topic: campaign_structure
claim: Cost caps are not appropriate below roughly $20k/month and become a legitimate option somewhere north of ~$50k/month; they require existing consistent creative winners and a tolerance for volatile daily delivery. For small spenders the practical obstacle is that finding the correct cap value requires more time and spend than a small account has, especially when other variables are moving.
recommended_action: "Do not attempt cost caps at small spend; they require volume, consistent winners, and stable surrounding conditions to calibrate."
context: Foxwell's Q4 planning discussion, and a post-BFCM recap where a small-spender account is discussed directly.
business_type: agency (ecommerce clients)
spend_level: "explicit brackets - under $20k/month no; north of $50k/month a legitimate trial; one member running fully on cost caps is spending >$500k/month"
conversion_volume_context: null
research_question_ids: [B1, B2, C2]
question_link_origin: prospective
published_at: 2024-09-16
source_url: https://www.youtube.com/watch?v=cm6nUWeKyo0
author: Andrew Foxwell (with Courtney Fritts in the 2024-12-05 recap)
timestamp: "~40:00+ (approx, word-position derived)"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "MULTI_ACCOUNT_EXPERIENCE across the agency and community. Brackets are stated as judgement, not derived. Foxwell also reports cost caps intermittently failing - 'Facebook just forgot about them for the day' - spending a full 10k daily budget by 9am, observed on his own accounts and reported roughly a dozen times in the community."
evidence_strength: weak
context_completeness: HIGH
platform_validation_status: UNVALIDATED
```

> Foxwell: *"if you're spending 20K and under, cost cap? No… if you're spending north of 50k a month, looking at a campaign maybe one that's cost capped is a legitimate idea"* · Fritts: *"with small spenders it's just really hard to be able to find what that sweet spot is… it would take too long and too much spend to find what that exact sweet spot number is"*

**applicability_to_DR:** medium · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** DR is far below every bracket named. The value is **negative and preventive**: it closes off a technique DR might otherwise be sold, and it does so from the two people in the panel with the most exposure to small accounts. ⚠ **Fritts and Foxwell are the same independence cluster** — this is one ecosystem agreeing with itself, not corroboration. The reliability observation (caps intermittently ignored, budget exhausted by morning) is a **2024 platform behaviour report** and must not be assumed current.

---

### campaign_structure — CBO/ABO choice may depend on how tight the geography is

```yaml
topic: campaign_structure
claim: His default recommendation is ABO rather than CBO, but he qualifies it - advertisers operating in a smaller country or a tight geographic area may reasonably use CBO, because delivery behaves differently there than in the US. He states plainly that his advice is shaped by running US-centric accounts.
recommended_action: null
context: Q4 planning discussion, prompted by a German advertiser in his community reporting heavy CBO use.
business_type: agency (US-centric ecommerce)
spend_level: "his stated core bracket is $20k-$100k/month"
conversion_volume_context: null
research_question_ids: [C2, E3]
question_link_origin: prospective
published_at: 2024-09-16
source_url: https://www.youtube.com/watch?v=cm6nUWeKyo0
author: Andrew Foxwell
timestamp: "~17:00-19:00 (approx, word-position derived)"
confidence: medium
evidence_basis: opinion
evidence_basis_details: "OPINION with an explicit self-limitation. No data, no account example. He is reporting a community member's practice and conceding it may be valid in a context unlike his own."
evidence_strength: none
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

> "if you're in a smaller country where you're targeting a smaller set of geographic places maybe not the US certainly a CBO could be part of that… a lot of the advice that I have is because of the accounts we run and because of always being a US Centric Advertiser"

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** Recorded because it is the **only place in the corpus where a practitioner suggests that geographic tightness might change the budget-mode answer** — which is DR's exact condition, at a far smaller scale. It is an aside, not a finding: no mechanism, no data, no threshold. It does **not** justify DR changing budget mode. It flags a variable nobody has tested. The self-limitation is the more valuable part, and it is the same honesty marker Loomer gives about local business.

---

### measurement — Branded-search lift as a proxy for what awareness campaigns actually do

```yaml
topic: measurement
claim: Creating a custom conversion that fires on a page view where the referring domain is Google lets you attribute branded/organic search visits back to Meta campaigns as a column in Ads Manager. Early results suggested awareness campaigns drove these Google visits while traffic and engagement campaigns did not.
recommended_action: "Use a referrer-based custom conversion to observe whether Meta spend is generating downstream branded search, rather than assuming it."
context: A test his agency had been running for one to two weeks at time of recording.
business_type: agency (ecommerce clients)
spend_level: null
conversion_volume_context: null
research_question_ids: [G1, G2]
question_link_origin: prospective
published_at: 2024-06-17
source_url: https://www.youtube.com/watch?v=AniBeD26uU0
author: Phil Kiel (Hello Earth) — NOT Andrew Foxwell
timestamp: "~33:00-38:00 (approx, word-position derived)"
confidence: medium
evidence_basis: experience_claim
evidence_basis_details: "REAL_ACCOUNT_EXAMPLE, explicitly preliminary - 'it's early days, it's been live like a week or two' and 'I'll share more when I've got enough to put my mortgage on it'. Attribution logic is asserted, not validated; the causal ordering depends entirely on Meta's attribution window behaving as assumed."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** DR's measurement design has four layers and its hardest problem is connecting ad delivery to a registration that completes in a business system. **This is a cheap, in-platform way to observe one specific downstream behaviour — a parent seeing an ad and then searching for the program by name** — which is plausibly a real part of DR's path to registration and is currently invisible. Recorded as **a technique to evaluate, not a finding**: the speaker himself declines to stand behind it, and the causal-order argument has an obvious hole he was challenged on during the recording and did not fully close.

---

### measurement — Click-through rate is a poor basis for killing an ad

```yaml
topic: measurement
claim: Turning ads off on the basis of click-through rate is not something his agency does, because he sees no correlation between CTR and performance; the same applies to thumb-stop rate. Where an ad is visibly failing, the reasons are usually apparent from the ad itself without those metrics.
recommended_action: "Do not use CTR or thumb-stop rate as a kill criterion; use them at most for creative iteration."
context: Discussion of which reported metrics mislead.
business_type: agency (DTC ecommerce)
spend_level: null
conversion_volume_context: null
research_question_ids: [D3, D4, G2]
question_link_origin: prospective
published_at: 2024-07-02
source_url: https://www.youtube.com/watch?v=TdZjwDFCgjA
author: Brad Ploch (WRK Marketing) — NOT Andrew Foxwell
timestamp: "~21:00-23:00 (approx, word-position derived)"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "OPERATOR_OBSERVATION. 'I don't see any correlations with performance' - an assertion about his own accounts with no data shown."
evidence_strength: weak
context_completeness: MEDIUM
platform_validation_status: NOT_APPLICABLE
```

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **Directly contradicts the benchmark guidance given by Jess Bachman in the same corpus** (CTR under 1% problematic; thumb-stop 20/30/50% bands) — two guests of the same community, three weeks apart, disagreeing on whether engagement metrics should drive creative decisions. Recorded as an open disagreement, not resolved. For DR the practical value is a **guard against a cheap wrong answer**: at DR's volume, engagement-rate differences between creatives will be noise long before conversion differences are readable, so a CTR-based kill rule would produce confident nonsense.

---

## Real-account evidence in this corpus

| Speaker | What was reported | Grade |
|---|---|---|
| Akvile DeFazio | Two before/after cases of her own: a $50k/month ecommerce client and a $10k/month lead-gen client, where adopting ASC + Advantage+ audiences plus AI tooling cut her **account-management time by 33%** and **17% month-over-month** respectively, "without sacrificing performance… all of their metrics are up beating prior results". **The time saving is quantified; the performance claim is not.** | `REAL_ACCOUNT_EXAMPLE` — weak |
| Phil Kiel | A UK brand with rising CPC and falling conversion rate at home; tested the US where **CPM doubled but CTR went from ~0.8% to ~3%**, so cost per click halved, with conversion rate flat. Attributed to market novelty after five years of UK saturation. | `REAL_ACCOUNT_EXAMPLE` — moderate detail, no CPA or revenue |
| Phil Kiel | Scaling **spend down** during poor performance, observing CPA recover at the lower spend, and using that as the data point to scale back up. Reported as this year's repeated pattern. | `OPERATOR_OBSERVATION` — unquantified |
| Foxwell / community | **Reels-only placement testing worked at ~£20k spend but degraded at higher spend** — the audience is too small to absorb it. | `OPERATOR_OBSERVATION` — unquantified |
| Foxwell | For fashion/apparel at $20k-$100k/month, **30% off is a statistically visible step change; 25% and 20% are not.** Countered in the same corpus by a member who found **BOGO 50 outperformed buy-two-for-30%**, and by the argument that value-add beats discount because it avoids devaluing the brand and anchoring customers to a lower price. | `MULTI_ACCOUNT_EXPERIENCE` — asserted, disputed within the corpus |

**None of the offer findings transfer to DR** — they are apparel-discount economics, and DR sells a season registration.

## Contradictions within this corpus
1. **CTR/thumb-stop as decision metrics** — Bachman gives benchmarks and bands; Ploch says he never kills on them. Same community, three weeks apart. **Preserved.**
2. **Cost caps** — Foxwell is sceptical and brackets them by spend; a member running >$500k/month is fully committed to them; Fritts says small accounts cannot calibrate them. Not contradictory once scoped by spend, which is itself the finding.
3. **Discount depth** — 30% as a threshold vs BOGO-50 outperforming it vs value-add beating discounts entirely. Unresolved in the corpus.

## Changes over time
Not assessable. The corpus spans seven months of 2024 and stops. His **current** position lives in the 2025-2026 articles already on file, and this video corpus must not be read as an update to them.

## Relevance to DR
**Strongest:** Phil Kiel's readability argument for consolidation, and Jess Bachman's 2-3× CPA spend threshold before a creative verdict. Both are reasoning DR can apply at any budget.

**Must not be used for:** anything about current platform behaviour, settings, or features. It is 2024 and pre-Andromeda throughout.

## Platform claims awaiting Meta validation
- Cost caps intermittently ignored, with a full daily budget spent in a few morning hours *(2024 observation)*.
- A custom conversion keyed on referring domain attributes downstream Google visits to Meta campaigns as described.
- Reels-only placement delivery degrading above a spend level for lack of inventory.

## Open questions from this corpus
1. **Does the 2-3× CPA testing threshold have a derivation, or is it a rule of thumb?** It is the single most transferable number here and nobody in the corpus explains where it comes from.
2. **Foxwell's CBO-for-tight-geography aside is untested by anyone.** It is the only hint in 927 documents that budget mode might interact with geographic concentration — DR's exact situation.
3. **Should this corpus be re-slugged?** It is filed under `andrew-foxwell` but is predominantly other people's material. Recorded for a future indexing decision; **no file was renamed in this run.**

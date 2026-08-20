---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/sam-tomlinson.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/sam-tomlinson.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Sam Tomlinson"
---

# Sam Tomlinson

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1B-Volume-and-Budget|Wave 1B — volumen y presupuesto]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/sam-tomlinson.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** sam-tomlinson
**Watchlist priority:** 1
**Topics:** campaign_structure · budgeting · optimization · measurement · targeting · scaling · creative_refresh
**Sources processed:** 4
**Last updated:** 2026-08-19
**Evidence model:** v2 — `evidence_basis` / `evidence_basis_details` / `evidence_strength` on every claim.

**Why this source is in the panel:** he is the only practitioner in this corpus who **writes the arithmetic down**. Where others assert that an account is under-funded, he shows the division that proves it. He is also the only one whose structural advice explicitly names service businesses and geo/service-tier splits rather than assuming a product catalogue. Role: EVP at Warschawski (agency); client verticals and managed spend are **not disclosed** on his site, so operator status is inferred from role plus the operational specificity of the writing — rated `medium-high`, not `high`.

**Source quality note:** unlike the podcast and YouTube material elsewhere in this knowledge base, these are **written, first-party, and quotable verbatim**. Nothing below passed through speech recognition. This is the highest-fidelity evidence in the expert layer.

**Date-precision warning:** his site exposes no machine-readable publication date on most issues. Dates marked `(month)` were derived from the WordPress media path of an in-article image and are **month-precision only**; the one marked `(exact)` came from page metadata. Issue numbers establish order. Do not cite a `(month)` date as a precise publication date without re-verifying.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims |
|---|---|---|---|---|
| `https://www.samtomlinson.me/insights/issue-136-the-ultimate-meta-ads-account-audit-part-ii` | article | 2025-10 (month precision) | 2026-08-19 | 4 |
| `https://www.samtomlinson.me/insights/issue-144-why-your-meta-ads-are-struggling-even-with-great-creative` | article | 2025-12 (month precision) | 2026-08-19 | 4 |
| `https://www.samtomlinson.me/insights/capital-allocation-in-advertising-part-ii` | article | 2025-08 (month precision) | 2026-08-19 | 3 |
| `https://www.samtomlinson.me/insights/issue-148-2026-predictions` | article | 2025-12-28 | 2026-08-19 | 1 |

**Stated context:** agency-side, mixed ecommerce and lead-gen clients. Dollar examples run from $50/day ad sets to $1MM+/month accounts. He states benchmarks for both ecommerce and lead gen separately, which is rare in this corpus.

---

## Claims

### optimization — Under-funding makes learning mathematically impossible, and the arithmetic is checkable before launch

```yaml
topic: optimization
claim: If an ad set's budget cannot buy the conversion volume the learning phase requires at that account's actual cost per conversion, the ad set cannot stabilize — this is arithmetic, not a platform malfunction. Worked example: a $150 target CPA needs roughly $3,750/week to reach 25 conversions, so a $50/day budget makes it impossible.
recommended_action: Before launching, divide the weekly budget by the realistic cost per conversion. If the result is below the volume needed for stable delivery, change the budget, the optimization event, or the structure — do not launch and wait.
context: An account whose architecture was full of ad sets each funded below their own learning requirement.
business_type: unstated
spend_level: "$50/day ad sets against a $150+ target CPA"
conversion_volume_context: "25 conversions per ad set per week used as the working threshold; 50/week cited as Meta's documented figure"
research_question_ids: [B1, B2]
published_at: 2025-12
source_url: https://www.samtomlinson.me/insights/issue-144-why-your-meta-ads-are-struggling-even-with-great-creative
author: Sam Tomlinson
timestamp: "The Learning Phase Math Problem"
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "Named client situation with the arithmetic shown explicitly ($150 CPA × 25 conversions = $3,750/week vs a $50/day cap). The diagnosis is derived, not measured — no before/after performance is presented for fixing it."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "If you fund an ad set in a way that makes that threshold mathematically impossible, the algorithm cannot exit Learning. This is not because the platform is malfunctioning, but rather because the conditions for learning were never met… For a group of ad sets, the target CPA was north of $150, but the budget was $50/day. How in the world do you get to 25 conversions (let alone 50) at $150/conversion (requires $3,750 per week in spend) when your budget is capped at less than 10% of that?"

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **The single most transferable claim found in the entire Phase 2 corpus.** It is the exact test B1/B2 exist to run, expressed as a calculation DR can perform with numbers DR already has — and its conclusion for DR is brutal and useful: at roughly $2.70/day historical spend, no plausible cost per registration produces learnable volume. B2 remains open because DR's registration cost is unmeasured, but this claim means DR does **not** need that number to know the current budget cannot learn; it only needs it to know how far off it is. Note the honest limit: this is a statement about *stable delivery*, not a claim that spend below it is wasted — Meta itself says learning-limited is not a penalty, and B3 already defines what stays readable below the line.

---

### optimization — The stable-delivery threshold is lower in practice than Meta's documented figure

```yaml
topic: optimization
claim: Meta's official documentation names 50 optimization events per ad set per week, but ad sets are observed exiting learning at 15-25; roughly 2 optimization actions per day per ad set is the working floor.
recommended_action: If an ad set cannot reliably reach about 2 optimization actions per day, change the structure — most simply by consolidating budgets into fewer, better-defined ad sets.
context: Account auditing across the author's client base.
business_type: unstated
spend_level: null
conversion_volume_context: "15-25 events/week observed as sufficient in his accounts vs 50 documented"
research_question_ids: [B1, C1]
published_at: 2025-10
source_url: https://www.samtomlinson.me/insights/issue-136-the-ultimate-meta-ads-account-audit-part-ii
author: Sam Tomlinson
timestamp: "Structure / scale section"
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "Explicitly framed as his own observation against Meta's published number ('their official documentation says 50, but I have plenty of ad sets exit learning at 15-25'). No dataset shown. The paired claim that consolidation 'often lowers CPA 10-20%' carries no supporting data either."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "Meta's algorithm needs 25+ optimization actions per ad set per week to exit learning and stabilize delivery (their official documentation says 50, but if I have plenty of ad sets exit learning at 15-25). If you can't reliably get to ~2 optimization actions per day, per ad set, then something must change."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** B1 already characterised the volume condition as a **range anchored to Meta's ~50/week reference**, deliberately refusing to manufacture a threshold. This claim is a practitioner reporting a *lower* practical floor — which is directionally helpful to a low-volume advertiser, and is the first external evidence in this domain that the documented figure may be conservative. **It does not move DR's line**: 15/week is still far above DR's observed delivery, so the decision is unchanged either way, and the domain's numeric-threshold rule forbids adopting 15-25 as a number on one unevidenced practitioner observation. Record as context, not as a threshold.

---

### campaign_structure — Fragmentation has a checkable signature

```yaml
topic: campaign_structure
claim: An account is likely over-fragmented if its top three campaigns account for less than 60% of spend, or if more than a handful of campaigns each produce fewer than 25 optimization events in 30 days.
recommended_action: Run both checks on a 30-day report; where they fail, consolidate rather than adding budget.
context: Account audit methodology.
business_type: unstated
spend_level: null
conversion_volume_context: "<25 optimization events per campaign per 30 days flagged as fragmentation"
research_question_ids: [C1, C4]
published_at: 2025-10
source_url: https://www.samtomlinson.me/insights/issue-136-the-ultimate-meta-ads-account-audit-part-ii
author: Sam Tomlinson
timestamp: "Structure section"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Presented as a diagnostic heuristic within an audit checklist; no derivation of the 60% or 25-event figures and no outcome data behind them."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "if the top three campaigns don't account for at least 60% of spend, or if more than a handful of campaigns each produce fewer than 25 optimization events ('conversions') in 30 days, fragmentation is likely kneecapping performance."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** Supports C1's single-campaign conclusion from a third independent direction — and usefully, the failure mode it names (many campaigns each below a volume floor) is the one C3 rejected separation to avoid. The numeric tests are unusable for DR in both directions: with one campaign the 60% test is trivially passed and carries no information, and the 25-event test would flag DR's entire account permanently. **Adopt the diagnostic as a future revisit trigger** — if DR ever adds campaigns, these two checks are a cheap way to notice fragmentation early — and do not import the numbers as thresholds (numeric-threshold rule).

---

### campaign_structure — Structure should mirror how contribution margin is created, including by geo or service tier

```yaml
topic: campaign_structure
claim: Account structure is an operational map of the business: for a service business that can mean campaigns tied to service offering, geography, or service tier, so that budget flows follow where profit is actually created.
recommended_action: Build structure around the units by which the business makes contribution margin, not around platform conventions.
context: Audit framework; explicitly extends beyond ecommerce catalogues to service businesses.
business_type: agency
spend_level: null
conversion_volume_context: null
research_question_ids: [C1, E3]
published_at: 2025-10
source_url: https://www.samtomlinson.me/insights/issue-136-the-ultimate-meta-ads-account-audit-part-ii
author: Sam Tomlinson
timestamp: "Structure section"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Stated as a structural principle; no account evidence attached to the service-business case specifically."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "for a service business, it may mean campaigns tied to service offering, geo or service tier. Structure is an operational map: it should mirror how profit (or contribution margin) is actually created."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** Notable because it is the **only sentence in the corpus that contemplates geo-based structure for a service business** — DR's exact shape. It appears to point toward splitting by campus, which E3 examined and rejected: multiple locations inside one ad set already delivers per-school geometry at zero fragmentation cost, and per-school ad sets would fragment DR's budget. **These are not actually in conflict** — his own fragmentation diagnostic (above) would reject a per-campus split at DR's event volume — but the tension must be recorded rather than smoothed over, because if DR ever reaches the volume where campuses differ materially in economics, this claim is the argument for revisiting E3.

---

### targeting — "Broad" only works when signal quality and market size are both large

```yaml
topic: targeting
claim: Broad targeting is effective when the algorithm receives clear high-quality signals AND the advertiser has a very large addressable market; where those conditions fail, broad is signal dilution rather than strategy.
recommended_action: Before defaulting to broad, check whether the account actually has both conditions; if the addressable market is narrow, do not treat "the creative is the targeting" as a strategy.
context: A brand where ~80% of revenue came from men aged 35-54 in a sport whose participants are ~78% men aged 28-62.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [E1, E2]
published_at: 2025-12
source_url: https://www.samtomlinson.me/insights/issue-144-why-your-meta-ads-are-struggling-even-with-great-creative
author: Sam Tomlinson
timestamp: "The 'Lazy Broad' Targeting Fallacy"
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "Specific client demographic concentration quoted (80% of revenue from men 35-54; ~78% of the sport's participants men 28-62) as the basis for arguing broad was inappropriate there. No comparative test of broad vs constrained on that account is presented."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "there's a version of broad targeting that is both powerful and appropriate. That's the one where the algorithm is given wide surface area _while it_ is being fed clear, high-quality signals AND the advertiser has a staggeringly large addressable market. When all of those conditions are not true, broad targeting is just signal dilution at scale, masquerading as a 'strategy.'"

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **This is the panel's most direct challenge to DR's current E1 configuration, and it deserves to be recorded as such rather than filed away.** DR fails both of his conditions: signal quality is poor (low event volume, registration truth outside Meta) and the addressable market is small by construction (one metro, parents of 6-12s near specific campuses). By his reasoning DR is exactly the case where broad degrades into dilution. **E1 is not overturned by it** — E1's decision rests on first-party platform facts (Locations is a hard control, detailed targeting is only a suggestion, forcing interests narrows an already-small audience and worsens the first learning-limited cause Meta names), and a practitioner opinion does not outrank platform documentation. But this is a credible, specific, opposing argument from outside DR's existing sources, and the honest position is that DR's audience configuration is **constrained by geography and left broad within it out of necessity, not because breadth is optimal at this scale.**

---

### campaign_structure — Blended targets across products with different margins simultaneously over- and under-spend

```yaml
topic: campaign_structure
claim: Running products with materially different margins and return rates under one blended ROAS/CPA target starves the profitable ones and overspends on the unprofitable ones; the account can look healthy on blended metrics while losing money.
recommended_action: Segment campaigns by margin profile and set separate targets per segment so the algorithm optimizes toward outcomes that match each segment's economics.
context: Sporting-goods brand where 75% of spend went to hard goods needing a 4.0 ROAS to break even while the account was praised for a blended 3.0 ROAS.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [C1]
published_at: 2025-12
source_url: https://www.samtomlinson.me/insights/issue-144-why-your-meta-ads-are-struggling-even-with-great-creative
author: Sam Tomlinson
timestamp: null
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "Client case with per-category economics quoted (blended 3.0 ROAS, 75% of spend to a category requiring 4.0 to break even, ~$65 lost per hard-goods sale). Diagnosis is arithmetic from the account's own numbers; no post-fix result shown."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "The old agency raved about the 3.00 ROAS – but neglected to mention that 75% of spend went to the hard goods (which would require a 4.00 ROAS just to break even)… this setup simultaneously under-spends and over-spends – which means the brand gets the worst of both worlds"

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** **This is the strongest pro-segmentation argument in the corpus and it is worth recording precisely because it cuts against C1's consolidation decision.** The reconciliation is that his trigger is *economic divergence between segments*, not campaign count preference — and DR has no such divergence today (one program type, one price band, one metro). If DR ever runs materially different offers (e.g. a low-margin trial session alongside a full season), this claim, not a general preference for more campaigns, is what would justify a split — and it would have to clear his own fragmentation test at the same time.

---

### measurement — Frequency and unique reach, not CPM alone, explain rising acquisition cost

```yaml
topic: measurement
claim: Cost per 1,000 unique accounts reached (CPMr) is rarely tracked but is what reveals whether an account is reaching new people; when CPMr rises, CAC follows. A bimodal delivery pattern — hammering remarketing pools while scattering in prospecting — can drive 7-day frequency above 2.8 and CPM to $105 against competitors at $25-50, with no change by the advertiser.
recommended_action: Track cost per unique reach alongside CPM and monitor 7-day frequency; treat a rising CPMr as an early warning on CAC rather than waiting for CAC to move.
context: A brand whose CPM tripled versus category peers without any change to targets, bids, budgets or creative cadence.
business_type: ecommerce
spend_level: null
conversion_volume_context: "7-day frequency >2.8; some segments served ~20x per 7 days"
research_question_ids: [G2, F1]
published_at: 2025-12
source_url: https://www.samtomlinson.me/insights/issue-144-why-your-meta-ads-are-struggling-even-with-great-creative
author: Sam Tomlinson
timestamp: null
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "Client figures quoted (frequency 2.8+, CPM >$105, competitor CPMs $25-50, some segments at 20x/7 days) with the explicit note that the advertiser had changed nothing. Causal explanation (bimodal distribution) is the author's interpretation."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "when CPMr rises, CAC soon follows… Their 7-day frequency was above 2.8… Their CPM had climbed above $105… Meta was serving some segments this brand's ads 20x per 7 days… while frantically throwing darts in the dark in prospecting."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** Frequency and audience exhaustion were flagged in Phase 1 as the panel's thinnest coverage; this is the best treatment found. It matters more for DR than for most accounts because **DR's audience is small by construction** — parents of 6-12s near specific campuses in one metro — so saturation arrives at far lower absolute spend than in a national account. The metric (cost per unique reach, plus 7-day frequency) is computable in Ads Manager at any spend level, making this one of the few claims here DR can implement immediately as a monitoring habit. It informs no decision yet; it prevents a future misdiagnosis of rising cost as "creative fatigue".

---

### scaling — Blended CPA hides the incremental cost of the next dollar

```yaml
topic: scaling
claim: A budget increase can look acceptable on blended CPA while the incremental CPA on the added spend is far worse — worked example: raising spend from $1,000 to $1,500/day moved blended CPA from $45 to $51.36, but the incremental CPA on that $500 was $71.60, roughly 60% worse than current.
recommended_action: When evaluating a budget increase, compute the CPA of the incremental spend alone, not the blended CPA after the increase.
context: Google Ads budget recommendation, presented as a general capital-allocation principle across channels.
business_type: unstated
spend_level: "$1,000/day scaling to $1,500/day"
conversion_volume_context: "22.22 → 29.21 conversions/day"
research_question_ids: []
question_link_origin: none
published_at: 2025-08
source_url: https://www.samtomlinson.me/insights/capital-allocation-in-advertising-part-ii
author: Sam Tomlinson
timestamp: "Marginal returns"
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "Live client account example with every figure and the full derivation shown. The arithmetic is verifiable from the numbers given; the platform's projection it relies on is Google's, not measured."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "So while the blended CPA only rises to $51.36, the incremental CPA on that $500 is $71.60, which is 43% over target and ~60% worse than the current $45 CPA. At target efficiency, the extra $500 should buy 10 conversions; it's only delivering ~6.98."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** The principle is exactly right and will matter the first time DR raises budget — the question to ask is what the *extra* dollars bought, not what the average looks like afterwards. It is unusable today for the reason that governs half this file: the calculation needs a measured cost per conversion at two spend levels, and DR has neither. File under "how to evaluate the budget decision B2 is waiting on", not under current practice.

---

### budgeting — Cut quickly, add slowly; adding budget to a loser without a thesis is a well-funded prayer

```yaml
topic: budgeting
claim: Marketers systematically invert good capital discipline — they keep losing campaigns alive on sunk-cost reasoning and scale winners timidly. Adding spend to an underperformer is only defensible when there is a specific, data-grounded thesis for why performance will change (conversion lag, seasonality, a shipped post-click fix, new creative).
recommended_action: Cut underperforming positions quickly and scale good ones methodically; require a written thesis before adding budget to something that is losing.
context: Capital-allocation framing applied to media budgets.
business_type: unstated
spend_level: null
conversion_volume_context: null
research_question_ids: [D3]
published_at: 2025-08
source_url: https://www.samtomlinson.me/insights/capital-allocation-in-advertising-part-ii
author: Sam Tomlinson
timestamp: "Rule #3: Cut Quickly, Add Slowly"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Reasoned from portfolio-management analogy with illustrative dialogue rather than account data. Explicitly names the valid exceptions, which is what keeps it from being an absolutist rule."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "absent a thesis grounded in real, objective, quantifiable data, allocating more capital to a loser is a well-funded prayer."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** The thesis requirement transfers cleanly and is close in spirit to D4's rule that no-spend must be diagnosed before it is acted on. **"Cut quickly" does not transfer and is actively dangerous at DR's volume** — D3's central finding is that DR usually cannot tell a loser from noise, so fast cutting would mostly be cutting at random. Adopt the *thesis* half; reject the *speed* half, and note that his advice presumes readable positions, which DR does not have.

---

### scaling — Diminishing returns exist on every channel; the only question is where the curve bends

```yaml
topic: scaling
claim: Every campaign, platform and tactic has a diminishing-returns curve; the curve may not bend until spend is very high, but its absence at current spend is not evidence it does not exist. Blaming "creative fatigue" or "bad audiences" often misdiagnoses the curve.
recommended_action: Increase budget in steps while monitoring marginal returns, rather than scaling until performance breaks.
context: General capital-allocation principle, with per-channel illustrations at $10k-$1MM+ levels.
business_type: unstated
spend_level: "illustrations at $10k, $50k, $200k, $500k, >$1MM/month"
conversion_volume_context: null
research_question_ids: []
question_link_origin: none
published_at: 2025-08
source_url: https://www.samtomlinson.me/insights/capital-allocation-in-advertising-part-ii
author: Sam Tomlinson
timestamp: "Rule #6: Respect Diminishing Returns"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Argued from principle with hypothetical spend illustrations; no account data presented for the curve shapes named."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "It's entirely possible that you might not see declining marginal performance until you're spending well over $1MM per month. But just because diminishing returns don't hit until your spend is 20x higher does not mean diminishing returns don't exist on Meta."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** Relevant to DR mainly as reassurance in the opposite direction: DR is nowhere near any diminishing-returns bend, so **budget increases in DR's range should not be argued against on efficiency-at-scale grounds.** DR's constraint is the floor (can it learn at all), not the ceiling. Worth recording so that a future "but scaling degrades efficiency" objection is not imported from accounts operating 1,000× higher.

---

### measurement — Attribution answers "who gets credit", incrementality answers "would this have happened anyway"

```yaml
topic: measurement
claim: Finance-grade measurement is shifting from attribution to incrementality, and brands that make the shift typically discover that 20-30% of their "best performing" spend was cannibalizing organic sales.
recommended_action: Judge channels by whether they generate net-new customers, not by whether they registered a click, and expect some top-reported spend to be non-incremental.
context: 2026 predictions piece; distinguishes true holdout testing from platforms marketing "incrementality" as a modeled checkbox feature.
business_type: unstated
spend_level: "notes aMMM has become economical for advertisers under ~$250k/month"
conversion_volume_context: null
research_question_ids: [G2]
published_at: 2025-12-28
source_url: https://www.samtomlinson.me/insights/issue-148-2026-predictions
author: Sam Tomlinson
timestamp: null
confidence: medium
evidence_basis: opinion
evidence_basis_details: "A prediction. The 20-30% cannibalization figure is asserted without a source or dataset; the distinction between modeled and holdout-tested incrementality is definitional rather than evidenced."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "Attribution answers the question, 'Who gets the credit?' Incrementality answers the question, 'Did this actually generate net-new customers/revenue?'… the brands that make this switch will realize that 20-30% of their 'best performing' spend was cannibalizing organic sales"

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** The distinction is one G2 already enforces — Meta-attributed registrations, DR's registration ledger, and registrations *caused* by Meta are three different numbers. The claim adds a warning DR should hold in the opposite direction from ecommerce brands: DR's likely error is **under**-counting (offline/branded-search completion), not cannibalization, because DR has almost no organic demand to cannibalize. **Do not import the 20-30% figure** — it is unsourced, and the domain forbids adopting numbers of that provenance.

---

### creative_refresh — Audit benchmarks: refresh cadence, post-click conversion floors, testing budget share

```yaml
topic: creative_refresh
claim: In his audit framework, a healthy account refreshes creative every 7-14 days, allocates 10-20% of budget to testing (ecommerce), limits concurrent test variants to 2-3 for statistical power, and expects post-click conversion rates of at least 1-2% for ecommerce and 2-3% for lead gen.
recommended_action: Audit against these figures; where an account misses them, treat it as a flag to investigate rather than an automatic fix.
context: Checklist sections of a full account audit.
business_type: agency
spend_level: null
conversion_volume_context: "minimum sample sizes referenced around ~2k impressions"
research_question_ids: [D1, D2]
published_at: 2025-10
source_url: https://www.samtomlinson.me/insights/issue-136-the-ultimate-meta-ads-account-audit-part-ii
author: Sam Tomlinson
timestamp: "Sections 7-8 of the audit checklist"
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Checklist benchmarks presented without derivation or supporting data. Format is a professional heuristic list, not a study."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "Review creative refresh cadence (ideally every 7–14 days)… Check budget allocation to testing (e-com 10–20% of total)… Limit concurrent test variants to 2-3 for stat power… Track **Post-Click CVR** (e-com: ≥ 1-2%; lead gen: ≥ 2-3%)"

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** Mostly a **do-not-import** record. The 7-14 day refresh cadence is a calendar rule of exactly the type D2 deliberately removed, and the testing-budget share is meaningless at DR's absolute spend. Two fragments survive translation: limiting concurrent variants to 2-3 independently echoes D1's provisional 2-3 per round (arrived at by different reasoning — his is statistical power, DR's is delivery capacity), and the post-click conversion floors give DR a **crude external sanity check** on its registration page, which is a genuinely under-examined part of DR's funnel. Neither becomes a threshold.

---

## Contradictions within this author

- **Consolidate vs segment.** He diagnoses fragmentation by low per-campaign event volume (Issue #136) and separately argues for splitting campaigns by margin profile (Issue #144). The resolution he implies but never states outright: segment when the economics genuinely differ **and** each resulting segment can still clear the volume floor. Where both cannot be true, his own framework does not say which wins.
- **Threshold numbers.** He cites 25+/week, then 15-25 as observed, then Meta's 50, within the same passage. Useful honesty about uncertainty, but it means no number in this file should be treated as his position.

## Open questions from this author

1. What are his client verticals and spend levels? His About page discloses neither, which caps how far his operator evidence can be weighted.
2. His service-business structural advice (campaigns by geo/service tier) is one sentence with no worked example. Is there a fuller treatment anywhere? That would be the single highest-value follow-up in this corpus for DR.
3. The "lazy broad" argument implies a constrained-market advertiser should do something other than broad — but he never says what, given that detailed targeting is only a suggestion under current platform mechanics. The prescription is missing.
4. Post-click CVR floors are stated for lead gen but a registration funnel is neither ecommerce nor classic lead gen. Which floor, if either, applies?

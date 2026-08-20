---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/andrew-faris.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/andrew-faris.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Andrew Faris"
---

# Andrew Faris

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Taylor-Holiday|Taylor Holiday — mismo cluster de independencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/andrew-faris.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** andrew-faris
**Watchlist priority:** 1
**Topics:** campaign_structure · measurement · bid_cost_controls · scaling
**Sources processed:** 4
**Last updated:** 2026-08-19
**Evidence model:** v2 — `evidence_basis` / `evidence_basis_details` / `evidence_strength` on every claim.

**Why this source is in the panel:** he is an interviewer who argues with his guests, which produces something rare in this corpus — **stated disagreement between two people who both have account access**. He is also the panel's clearest operator-to-analyst path (media buyer → Head of Strategy at Common Thread Collective → CEO of 4x400), so he reasons about ads as a P&L rather than as a dashboard.

**Attribution note:** this is an interview show. The most operationally valuable claims below are **his guests'** — Phil Kiel on account structure, "Olivia" (measurement vendor, surname not resolvable from captions) on incremental attribution, Taylor Holiday on cost controls. Each claim names its actual speaker. **Faris and Holiday are not independent voices** — Faris is CTC's former head of strategy and the cost-control study is CTC's; their agreement is one discourse, not two confirmations.

**Source quality:** YouTube auto-captions. All publication dates are exact (YouTube-declared). Numbers are as transcribed and must be checked against video before use.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims |
|---|---|---|---|---|
| `https://www.youtube.com/watch?v=aCVhMts9cR8` | youtube (auto captions) | 2026-05-12 | 2026-08-19 | 4 |
| `https://www.youtube.com/watch?v=YCpQiZ0A5Kw` | youtube (auto captions) | 2026-08-10 | 2026-08-19 | 2 |
| `https://www.youtube.com/watch?v=SKEaiB4V728` | youtube (auto captions) | 2026-02-05 | 2026-08-19 | 2 |
| `https://www.youtube.com/watch?v=6LvQ6_k6Zco` | youtube (auto captions) | 2026-08-06 | 2026-08-19 | 1 |

**Stated context:** ecommerce/DTC throughout. Spend levels referenced range from "less than 10 grand a day" as the *small* case up to brands spending $20-40M on a single tactic. No claim below was made with a business of DR's size in mind.

---

## Claims

### campaign_structure — Splitting into many campaigns costs reach through audience overlap

```yaml
topic: campaign_structure
claim: Multiple campaigns targeting overlapping audiences do not add reach proportionally — ten campaigns each reaching 1,000 people may produce only ~7,000 account-level reach, because the campaigns overlap. Consolidating lowers frequency, lowers cost per unique reach, and raises reach at the same spend.
recommended_action: Do not add campaigns or ad sets casually; consolidate overlapping ones, and expect the same budget to reach more distinct people afterwards.
context: Account audits of fragmented ecommerce accounts (example given: 10 campaigns × 5 ad sets at $2,000/day).
business_type: ecommerce
spend_level: "$2,000/day in the worked example"
conversion_volume_context: null
research_question_ids: [C1, C4]
published_at: 2026-05-12
source_url: https://www.youtube.com/watch?v=aCVhMts9cR8
author: Phil Kiel (guest)
timestamp: null
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "Speaker describes auditing accounts and quotes a specific recent case with ~80% account-level audience overlap, plus an illustrative 10-campaign example producing 7,000 rather than 10,000 reach. The 7,000 figure is illustrative arithmetic, not a measured result; the 80% overlap is presented as an observed audit finding."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "If each campaign reaches 1,000 people, and you have 10 campaigns, your account reach will not be 10,000. Your account level reach will be 7,000. And at that point, there's a 3,000 overlap between those campaigns. That's that's low. I audited an account last week where the account overlap is like 80%."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **This supplies the mechanism C1 was missing.** C1 concluded "one campaign" largely on the absence of a reason to split — Meta forces campaign count only through objective immutability, and DR has no second objective. This claim gives a *positive* reason: splitting buys overlap, not reach. It matters more for DR than for the accounts he audits, because **DR's audience is small and geographically bounded**, so any split would overlap almost completely by construction — parents near the same campuses are the same people. It also strengthens E3's union-of-radii-in-one-ad-set decision for the same reason. Note this is an argument about *reach efficiency*, not about learning volume; it stacks with, rather than replaces, the volume argument.

---

### campaign_structure — Genuinely different unit economics do require separate campaigns

```yaml
topic: campaign_structure
claim: Consolidation has a limit: products with materially different order values require different acceptable acquisition costs, and forcing them into one highest-volume ad set does the account a disservice even at identical ROAS.
recommended_action: Consolidate to maximize reach efficiency, but split where products carry genuinely different economics rather than lumping them under one target.
context: Advertising a catalogue of ~20 products with differing AOV ($200 vs $300 used as the example).
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [C1]
published_at: 2026-05-12
source_url: https://www.youtube.com/watch?v=aCVhMts9cR8
author: Andrew Faris
timestamp: null
confidence: high
evidence_basis: opinion
evidence_basis_details: "Argued from unit economics in conversation; no account data attached to this specific point."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "a product with a $200 AOV and a product with a $300 AOV require a really different CAC to be successful. And even if it's the same ROAS, and therefore combining them in a highest volume ad set, you're you're actually going to do real disservice to the ad account."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** Recorded because it is the **boundary condition on the previous claim**, and independently matches Sam Tomlinson's margin-segmentation argument — two unrelated practitioners naming the same exception to consolidation. It does not apply to DR today (one program type, one price band), and it is the specific thing to watch for if DR ever runs materially different offers. Consolidation is the right default *because DR lacks economic divergence*, not because consolidation is universally correct.

---

### measurement — Cost per unique reach matters as a trend, not as a level

```yaml
topic: measurement
claim: A high cost per unique reach is not inherently bad; what matters is whether it is rising over time, because a rising CPMr signals the account is exhausting reachable audience even while short-term ROAS looks fine.
recommended_action: Monitor CPMr as a time series rather than judging its absolute level.
context: Discussion of accounts skewed toward retargeting.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [G2, F1]
published_at: 2026-05-12
source_url: https://www.youtube.com/watch?v=aCVhMts9cR8
author: Phil Kiel (guest) with Andrew Faris
timestamp: null
confidence: medium
evidence_basis: experience_claim
evidence_basis_details: "Stated as a reading rule from audit practice; no time-series data shown."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "high CPMR isn't bad. Where it's important is when it changes over time."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** Independently corroborates Sam Tomlinson's CPMr argument and adds the correction that matters for DR: **do not benchmark the level, watch the direction.** DR's absolute CPMr will look poor against any published figure — a small, tightly bounded metro audience is expensive to reach — and reading that as failure would be a mistake. The direction over a season, however, is meaningful and computable at DR's spend.

---

### retargeting — A retargeting-heavy account can post good ROAS while quietly running out of audience

```yaml
topic: retargeting
claim: When delivery skews to retargeting, both platform-reported and incremental ROAS can look strong in the short term, but the retargeting pools dry up and the falling reach eventually surfaces as a problem the short-term ROAS never showed.
recommended_action: null
context: Diagnosing accounts whose delivery has concentrated on warm audiences.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [F1]
published_at: 2026-05-12
source_url: https://www.youtube.com/watch?v=aCVhMts9cR8
author: Andrew Faris (summarizing and confirming with Phil Kiel)
timestamp: null
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Mechanism reasoned aloud and agreed between host and guest; no account example or data presented for the drying-up dynamic."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "if my ads are dispro- disproportionately retargeting my ROAS actually might be high and in fact my incremental ROAS might be high. But, if I get stuck in that loop for for a long time… those retargeting audiences sort of dry up and you no longer can sort of squeeze any more juice out of that"

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** F1 (retargeting) is DEFERRED for DR on the grounds that no meaningful warm pool exists. This claim supports that deferral from the opposite end — it describes what goes wrong when an account leans on a pool it is depleting, and DR's pool would be depleted almost immediately at 256 reach/30 days historically. Keep as a **future guardrail**: when DR does build a warm pool during a registration window, the seasonal shape means exhaustion will arrive fast, and the strong ROAS it shows on the way there will be the least trustworthy number in the account.

---

### measurement — Incremental attribution now outperforms standard attribution on average, and the asymmetry favours testing it

```yaml
topic: measurement
claim: Comparing brands that tested Meta's incremental attribution, the ratio moved from 0.98x (standard slightly ahead) in the 2024-July 2025 window to roughly 1.26x in the July 2025-July 2026 window, with the top of the range around 38-40% better than standard attribution.
recommended_action: Test incremental attribution aggressively rather than cautiously — move highest-volume spend over rather than constructing a careful 50/50 split — because the downside observed is near par while the upside is large.
context: Vendor study of DTC brands that explicitly tested incremental attribution; sample described by the speaker as not large.
business_type: ecommerce
spend_level: "advice scoped to brands spending less than ~$10,000/day"
conversion_volume_context: "sample explicitly described as limited; only brands that ran the test were included"
research_question_ids: [G1, G2]
published_at: 2026-08-10
source_url: https://www.youtube.com/watch?v=YCpQiZ0A5Kw
author: "Olivia" (measurement vendor guest; surname not resolvable from captions) with Andrew Faris
timestamp: null
confidence: medium
evidence_basis: external_data_cited
evidence_basis_details: "Vendor-run study using a geometric mean of ratios, with the selection bias stated aloud by the speaker (only brands that chose to test are included). **Commercial interest: the guest sells the measurement product whose value the study supports.** The 'test aggressively' recommendation is Faris's inference from the distribution, not a study finding."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "the 2024 through July 2025 data that that that ratio is [0.9]8x which means standard attribution had a slight edge over incremental attribution… you see that number jump to 1.26x… incremental attribution is winning more on average now."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** G1 settled DR's attribution configuration on **platform mechanics** (7-day click is the current ceiling; 1-day view; set at ad set level; attribution informs delivery) rather than on performance claims, and this claim does not disturb that. Incremental attribution optimization is a different lever — it asks Meta to bid toward users predicted to convert *because of* the ad — and it presupposes enough conversion signal for that prediction to mean anything. DR has none. Record as a **watch item for a future volume state**, and note the vendor incentive and self-selected sample before it is ever weighted more heavily.

---

### measurement — Do not repivot measurement on a single test result

```yaml
topic: measurement
claim: A single incrementality test is one noisy data point; the correct response is to replicate it or to weight it against a published aggregate benchmark, not to restructure measurement around it.
recommended_action: Treat one test as evidence to be combined, not as a verdict. Where you cannot run repeated tests, anchor on published aggregate benchmarks and adjust from there.
context: Discussion of how brands mishandle incrementality results; a published Meta benchmark of ~1.2 on 7-day click is cited as the anchor.
business_type: ecommerce
spend_level: null
conversion_volume_context: "cited aggregate described as hundreds of tests"
research_question_ids: [B3, G2]
published_at: 2026-02-05
source_url: https://www.youtube.com/watch?v=SKEaiB4V728
author: Taylor Holiday (guest) with Andrew Faris
timestamp: null
confidence: high
evidence_basis: external_data_cited
evidence_basis_details: "Cites a third-party (Haus) published benchmark of ~1.2 on 7-day click for Meta, alongside a baseball-forecast analogy used to explain regression to the mean. The methodological argument is sound; the specific 1.2 figure is second-hand and unverified here."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "you get a single test result back… my suggestion would be you do not pivot the entirety of your measurement to that single data point… one you try to replicate it but two is what we have is like an index of the mean like an aggregate test."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** This is the discipline B3 already encodes — DIRECTIONAL versus SUFFICIENTLY_STRONG — stated by practitioners who reach it from the opposite direction (too much data rather than too little). For DR the warning is sharper than for them: at single-digit weekly events, **every** DR read is the single noisy data point, so the rule is not "replicate before repivoting" but "expect not to be able to conclude at all". Do not import the 1.2 benchmark as a DR expectation; it is an ecommerce aggregate and Taylor Holiday's own range data shows how wide the spread behind such medians is.

---

### bid_cost_controls — Cost controls bid widely at first and converge as data accumulates, so early results are the least representative

```yaml
topic: bid_cost_controls
claim: Cost-cap and minimum-ROAS bidding explore by bidding far above and below target early — the speaker's understanding is up to 9-10x target — then converge as data accumulates, so the first tranche of spend on an ad set should show a much wider range of outcomes than later tranches. He predicts more conversions and fewer ad sets produce results closer to target.
recommended_action: null
context: Interpreting the distribution in CTC's cost-control study; explicitly framed as hypothesis and a request for follow-up analysis.
business_type: ecommerce
spend_level: "hypothetical isolation of the first $10k of ad set spend"
conversion_volume_context: null
research_question_ids: [B1]
published_at: 2026-08-06
source_url: https://www.youtube.com/watch?v=6LvQ6_k6Zco
author: Andrew Faris
timestamp: null
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Explicitly hedged ('my understanding is', 'I bet you') and offered as a testable follow-up to the study rather than as a finding. No data presented."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "they start by bidding really widely like uh my understanding is they can bid like like 9 to 10 extra target… but then they condense over time as as the more data comes in… more conversions and less ad sets might produce results closer to target."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** If true, it says something DR should care about beyond bidding: **the early period of any funded structure is the period whose results least deserve to be trusted**, and an account that never accumulates data never leaves that regime. That is a mechanism-level restatement of why D3 refuses ad-level winner calls at DR's delivery. It is the author's speculation, not a finding, and must stay labelled as such — but it is a well-posed hypothesis, which is more than most of the corpus offers.

---

### scaling — If the target cannot be met at higher spend, the constraint is the business, not the target

```yaml
topic: scaling
claim: When an account cannot spend more without breaching its efficiency target, the answer is not to lower the target — the target is the constraint, and spending more requires the offer or product to become more compelling.
recommended_action: Hold the efficiency target and treat inability to scale as a signal about the business, not as a reason to relax the target.
context: Argument about brands grinding out modest growth at a fixed target.
business_type: ecommerce
spend_level: "$3M-scale business used as the example"
conversion_volume_context: null
research_question_ids: []
question_link_origin: none
published_at: 2026-02-05
source_url: https://www.youtube.com/watch?v=SKEaiB4V728
author: Taylor Holiday (guest) with Andrew Faris
timestamp: null
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Position argued in debate between the two; no account evidence presented."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "keep the T target where it is. That's the constraint. If you want to spend more money, you have to do something more awesome."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** The stance — refuse to solve a demand problem by relaxing the efficiency bar — is directionally right and worth holding when DR eventually sets a cost-per-registration ceiling. It is also the closest this corpus comes to the position DR's own domain rules already take: if the ads cannot produce registrations at a viable cost, that is information about the offer, the geography, or the price, not a reason to keep buying impressions. **DR has no target to hold yet**, so this is a stance to adopt at the moment B2 closes, not now.

---

## Contradictions within this author

- **Consolidate vs split.** Within the same episode he endorses consolidation for reach efficiency and then argues that differing product economics require more campaigns. He states the tension explicitly and does not resolve it into a rule — the honest reading is that the two forces trade off and the balance is account-specific.
- **Testing posture.** He advocates aggressive, non-careful testing of incremental attribution (move the spend, watch what happens) while elsewhere endorsing the discipline of never repivoting on a single result. The reconciliation implied is that the asymmetry of downside justifies the former, but he does not say so.

## Open questions from this author

1. The audience-overlap mechanism is asserted with one audit figure (80% overlap). Is Meta's audience-overlap tooling still able to measure this, and does the effect hold when campaigns differ by geography rather than by product?
2. The incremental-attribution study includes only brands that opted to test. What does the distribution look like among brands that tried it and reverted?
3. His cost-control convergence hypothesis (wide early bidding, narrowing later) is checkable against CTC's own data set. It has not been checked.
4. Nothing in this source addresses accounts below roughly $10k/day, which he treats as the small case. DR is three orders of magnitude below that floor.

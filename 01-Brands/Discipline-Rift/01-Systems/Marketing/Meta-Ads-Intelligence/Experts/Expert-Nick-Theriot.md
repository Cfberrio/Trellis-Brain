---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/nick-theriot.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/nick-theriot.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Nick Theriot"
---

# Nick Theriot

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/nick-theriot.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** nick-theriot
**Watchlist priority:** 1
**Topics:** campaign_structure · scaling · creative_strategy · targeting · creative_testing · budgeting
**Sources processed:** 4
**Last updated:** 2026-08-19
**Evidence model:** v2 — `evidence_basis` / `evidence_basis_details` / `evidence_strength` backfilled 2026-08-13 from the raw transcript already on file (`data/raw/2026-08-13_nick-theriot_Xo9FANGyo2k_expert-source.json`). No new retrieval. All evidence below is **self-reported by the author** unless stated otherwise; nothing here is independently verified.
**Field notes (2026-08-13):** `validation_status` renamed to `platform_validation_status` — it grades the claim against current first-party Meta documentation only, never against practitioner agreement or DR results. `research_question_ids` backfilled where the mapping to `knowledge/research-questions.md` is obvious; this source predates the backlog, so mappings are retrospective. Existing `UNVALIDATED` values are untriaged — some may become `NOT_APPLICABLE` at the next validation pass.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims |
|---|---|---|---|---|
| `https://www.youtube.com/watch?v=Xo9FANGyo2k` | youtube (18m38s, auto captions) | 2025-04-28 | 2026-08-13 | **7** |

**Stated context:** ecommerce/DTC. He states his agency offer is for accounts doing **at least $100,000/month in revenue**, and mentorship for those below it. References "thousands of creative tests… over the last couple years."

**Disclosed incentive (recorded because he raises it himself):** *"I have zero incentive of you using a CBO… that's not my main mechanism."* He states his revenue comes from agency and mentorship offers, not from CBO advocacy.

---

## Claims — YouTube (2025-04-28)

### campaign_structure — One CBO for both testing and scaling

```yaml
topic: campaign_structure
claim: Testing and scaling both happen inside a single CBO campaign, not in separate test and scale campaigns.
recommended_action: Run one CBO. Test new ads inside it and scale up that same campaign based on performance.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-04-28
source_url: https://www.youtube.com/watch?v=Xo9FANGyo2k
author: Nick Theriot
timestamp: "0:00"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as his standing practice ('what's worked for my students and clients'); no account data or comparison shown. He separately discloses he has no commercial incentive tied to CBO advocacy."
evidence_strength: weak
research_question_ids: [C1, C3]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: PARTIALLY_SUPPORTED   # see Validation 2026-08-13 — Claim 3
```

> "I like to do CBO for my testing and scaling. Not that I create a separate campaign for scaling with a CBO and a separate campaign for testing with CBO. No, just literally one campaign."

**applicability_to_DR:** high · **modification_required:** no
**reason:** **PRINCIPLE AND IMPLEMENTATION BOTH TRANSFER, and it is the cheaper of the two competing structures.** DR already runs a single campaign with a single ad set. This claim says that is a legitimate structure rather than a deficiency — directly contradicting the four-campaign model, and directly relevant to whether DR should ever build one.

---

### creative_testing — ~90% of ads not getting spend is normal

```yaml
topic: creative_testing
claim: Roughly 90% of tested ads receive little or no spend in a CBO, and this is expected rather than a malfunction.
recommended_action: Do not treat low/zero spend on most new ads as a problem to fix. Keep testing to find the minority that do spend.
business_type: ecommerce
spend_level: null
conversion_volume_context: "based on thousands of creative tests and hundreds of winners found"
published_at: 2025-04-28
source_url: https://www.youtube.com/watch?v=Xo9FANGyo2k
author: Nick Theriot
timestamp: "0:30"
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "Grounded in 'the thousands of creative tests I've done over the last couple years and the hundreds of new winning ads we found for accounts' (4:00); aggregate experience only, no dataset or account breakdown shown."
evidence_strength: weak
research_question_ids: [D4]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "sometimes these ads just simply don't get spent. And I would say probably on average about 90% of ads don't get spent. And that's okay because we know that not every ad we create is going to become a winner."

**applicability_to_DR:** low · **modification_required:** yes
**reason:** The reassurance depends on running enough tests that the surviving 10% is a usable number. At DR's volume, 10% of a handful of ads is zero. **The volume assumption invalidates the comfort, not the observation.**

---

### creative_testing — $5/day minimum to nudge a zero-spend ad set, then stop

```yaml
topic: creative_testing
claim: A zero-spend ad set can be nudged with a $5/day minimum spend, but if it still fails to take off at $5-10/day the answer is not more forced budget.
recommended_action: "Add a $5/day ad set minimum on new tests. If it still does not take off, stop forcing spend and diagnose the creative instead."
business_type: ecommerce
spend_level: "$5/day minimum"
conversion_volume_context: null
published_at: 2025-04-28
source_url: https://www.youtube.com/watch?v=Xo9FANGyo2k
author: Nick Theriot
timestamp: "1:00–2:04"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Remedy described as routine practice; no outcome evidence presented for the $5/day nudge or its failure threshold."
evidence_strength: weak
research_question_ids: [D4]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: PARTIALLY_SUPPORTED   # see Validation 2026-08-13 — Claim 5
```

> "if you're in the bucket of people that's like, 'Hey, my ad is literally getting $0 in spend'… then just simply add a $5 a day minimum spend to that particular adset… Now, if you're in the bucket of people that's adding this $5 $10 a day of spend to it for minimum spend and it's still not taking over… then the other thing you can do is what we're going to be talking about in today's video."

**applicability_to_DR:** low · **modification_required:** yes
**reason:** **The scale mismatch here is the sharpest single data point in this run.** Nick's smallest possible intervention — $5/day on one ad set — is roughly **185% of DR's entire current daily ad spend** ($2.70/day). The cheapest tactic in the ecommerce playbook exceeds DR's whole budget.

---

### creative_testing — Non-spend is a creative verdict, not a distribution bug

```yaml
topic: creative_testing
claim: Persistent low spend inside a CBO is Meta's read on the creative, and should be diagnosed in a fixed order rather than overridden with budget.
recommended_action: "Diagnose in this order: hook, then visual, then market-size research, then whether the ad is too educational (view duration), then positioning. Do not force spend."
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-04-28
source_url: https://www.youtube.com/watch?v=Xo9FANGyo2k
author: Nick Theriot
timestamp: "3:36–12:47"
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "Diagnostic order asserted from aggregate experience ('out of the thousands of creative tests… I always noticed one thing'), plus an anecdote of strong hooks taking over an account while carrying 'a horrible cost per purchase'. No data shown."
evidence_strength: weak
research_question_ids: [D4]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: INSUFFICIENT_EVIDENCE   # see Validation 2026-08-13 — Claim 2
```

> "If a CBO ad set is not getting a ton of spin, it's always going to start off with the hook." … "often times when I look at campaigns and we're testing new creatives and just nothing's getting spent, it's not even like, hey, the creative is wrong or the hook is wrong or like the CBO is wrong. It's just the simple way of what we're trying to call out and what we're trying to position is just terrible."

**applicability_to_DR:** high · **modification_required:** no
**reason:** **PRINCIPLE TRANSFERS AND IS SCALE-INDEPENDENT.** It is a diagnostic ordering, not a budget tactic — it costs nothing to adopt. It also reframes DR's situation: low delivery may be a message problem before it is a budget problem.

---

### creative_strategy — Creative creates the audience

```yaml
topic: targeting
claim: The hook and creative determine who Meta serves the ad to; creative performs the targeting function.
recommended_action: Control who you reach through hook and creative messaging rather than through audience settings.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-04-28
source_url: https://www.youtube.com/watch?v=Xo9FANGyo2k
author: Nick Theriot
timestamp: "5:39"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Mechanism asserted flatly ('creative does all the targeting for you'); no evidence presented."
evidence_strength: none
research_question_ids: [E2]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "your hook and your creative is what creates the audience of people that you're going to target. Creative does all the targeting for you if you not aware of that."

**applicability_to_DR:** medium · **modification_required:** yes
**reason:** PRINCIPLE may transfer, but **DR is the case where it most clearly does not transfer wholesale.** Creative cannot enforce residency. A compelling Orlando-parent hook does not stop delivery to a tourist matched on `recent` location. For a local on-campus offer, geo configuration is doing work creative cannot do.

---

### targeting — Narrow hooks suppress spend; no retargeting audiences

```yaml
topic: retargeting
claim: A narrowly-worded hook shrinks the addressable pool and suppresses delivery; retargeting is achieved through messaging rather than retargeting audiences.
recommended_action: "Widen who the hook calls out to increase delivery. Build retargeting-stage messaging into creative instead of building retargeting audiences."
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-04-28
source_url: https://www.youtube.com/watch?v=Xo9FANGyo2k
author: Nick Theriot
timestamp: "5:08–6:40"
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Reasoning by constructed example ('lefthanded brain surgeons in the Arizona desert' vs 'doctors in general across the USA'); the no-retargeting-audiences position is stated in passing. No evidence presented for either."
evidence_strength: none
research_question_ids: [E2, F1]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "if a creative is calling out lefthanded brain surgeons in, you know, the Arizona desert, it's going to be such a small group of people that Facebook will barely spend on it. But if it's just calling out doctors in general across the USA, it has a huge audience." … "I'm not putting a retargeting audience in that adset because again, the creative creates the audience. I'm just building that creative opinion with only messaging that a retargeting audience would resonate with."

**applicability_to_DR:** low · **modification_required:** yes
**reason:** Confidence `medium` — the retargeting position is stated in passing rather than argued. More importantly, **this claim points the opposite way from DR's needs.** DR's qualification problem calls for *narrowing* (age band 6–12, named school, Orlando residency); Nick's advice is to widen the callout to unlock delivery. That tension is real and is exactly what should be tested rather than adopted.

---

### creative_strategy — Long educational video suppresses delivery

```yaml
topic: creative_testing
claim: Ads that are too educational produce low average view duration, which suppresses spend; short hooks routed to an advertorial work better.
recommended_action: "Show 5-20 seconds of what people want, then send traffic to an advertorial or listicle that carries the education, rather than educating inside the ad."
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-04-28
source_url: https://www.youtube.com/watch?v=Xo9FANGyo2k
author: Nick Theriot
timestamp: "10:44–11:45"
confidence: medium
evidence_basis: experience_claim
evidence_basis_details: "Asserted from observed view-duration patterns on uploaded videos, extended by analogy to YouTube's algorithm; no Meta-side data shown."
evidence_strength: weak
research_question_ids: [D4]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "if we upload a video and it's a 6 minutee long video it's like a VSSL and people are like watching a little bit then hopping it off and that view view duration is really low then likelihood is also going to keep that ad spend really low on it… let's do less education on Facebook ads and only show maybe 5, 10, 15, 20 seconds of what people want and then send people to like an advvertorial or listical"

**applicability_to_DR:** medium · **modification_required:** yes
**reason:** PRINCIPLE (front-load the want, move education post-click) may transfer and touches DR's creative-clarity and offer-message-fit gates. IMPLEMENTATION (advertorial/listicle funnel) is an ecommerce pattern; a parent researching a school season may need more information earlier, not less. `medium` confidence — the view-duration→spend mechanism is asserted by analogy to YouTube, not evidenced.

---

## Validation — 2026-08-13

Validated against the existing `knowledge/official-meta/` base only. No new platform research.

### Claim 2 — non-spend is a creative verdict; do not force spend → **INSUFFICIENT_EVIDENCE**

**Expert source:** Nick Theriot, `Xo9FANGyo2k` @ 3:36–12:47
**Official sources checked:** `official-meta/learning-limited.md`, `official-meta/learning-phase.md`

**What Meta establishes.** Meta lists causes of learning limited: *"small audience size, low budget, low bid or cost control, high auction overlap, an infrequent optimization event, or other issues such as running too many ads at the same time."* **Creative quality is not among them.** Meta's stored documentation says nothing about per-ad budget distribution inside a CBO, which is the exact phenomenon Nick is explaining.

**What Meta does NOT establish.** Nothing in the stored base supports — or refutes — the claim that persistent non-spend is Meta's verdict on the creative. The hook → visual → market size → view duration → positioning diagnostic order is entirely Nick's framework.

**Partial tension worth recording.** Meta's own remedies for under-delivery include *"Raise your budget"* and *"Raise your bid or cost control"* — closer to forcing than to Nick's "stop forcing." These are not in direct contradiction, because they address different scopes: Meta is describing an *ad set* diagnosed learning limited, Nick is describing *individual ads* inside a funded CBO. But the instincts point opposite ways, and no stored evidence resolves it.

**Status therefore stays INSUFFICIENT_EVIDENCE, and the framework remains expert opinion.**

**applicability_to_DR:** medium · **modification_required:** no
**reason:** It costs nothing and it is scale-independent — a diagnostic ordering, not a budget tactic. Its value to DR is as a *sequencing discipline* (interrogate the message before buying more delivery), explicitly held as one practitioner's unvalidated framework rather than platform fact.

---

### Claim 3 — one CBO handles both testing and scaling → **PARTIALLY_SUPPORTED**

**Expert source:** Nick Theriot, `Xo9FANGyo2k` @ 0:00
**Official sources:** `official-meta/learning-limited.md`, `official-meta/learning-phase.md`, `official-meta/optimization-goals-and-attribution.md`

**What Meta establishes — consolidation as a direction.** Three independent pages converge:
- *"Combining ad sets and campaigns will help you get the results you need faster, which means you'll see stable results sooner."*
- *"Avoid high ad volumes… By combining similar ad sets, you also combine learnings."*
- Documented minimum daily budgets, which penalise splitting a small budget across many ad sets.

**What Meta does NOT establish.** Meta never says one campaign is sufficient, never addresses separating testing from scaling, and never endorses any specific campaign count. **META SUPPORTS CONSOLIDATION ≠ NICK RECOMMENDS ONE CAMPAIGN.** The first is a documented direction; the second is one practitioner's architecture.

**Assessment at DR's actual volume.** DR runs 1 campaign / 1 ad set / 1 ad at ~$2.70/day, with 10 link clicks in its last measured 30-day window. Four of Meta's five named learning-limited causes already describe this account (small audience, low budget, infrequent optimization event, too few results). Splitting that budget across Sam's four campaigns would worsen every one of them. **For DR specifically, the consolidation direction and Nick's architecture point the same way — and DR is already there.**

**applicability_to_DR:** high · **modification_required:** no
**reason:** Validates DR's existing structure. The actionable content is a **prohibition, not a build**: do not construct a multi-campaign architecture at this volume. Zero cost, zero risk, prevents a well-cited wrong move.

---

### Claim 5 — spending-limit intervention may carry a learning cost → **PARTIALLY_SUPPORTED**

Nick's $5/day minimum (@ 1:00–2:04) falls under the same finding recorded in full in `sam-piliero.md` → Validation → Claim 5. Meta lists *"Ad set spending limit amount"* as conditionally significant, *"depending on the magnitude of the change"*, with no published threshold.

Nick's $5/day is a small absolute change and, on Meta's own $100→$101 illustration, is the kind least likely to be significant — but Meta publishes no threshold, so this cannot be asserted. **At DR's scale the same $5/day is ~185% of total daily spend, i.e. an enormous relative change** — precisely where "magnitude" would matter most, and precisely where Meta gives no guidance.

---

## Contradictions within this author

None internal.

## Open questions from this author

- The claim that view duration drives ad delivery is reasoned by analogy to YouTube's algorithm; no Meta-side evidence is offered.
- The "90% of ads don't get spend" figure is stated from experience with no account-size scoping.
- He never addresses what happens at low absolute volume — every example assumes enough tests for a 10% survival rate to be meaningful.
- The no-retargeting-audiences position is asserted, not defended.

---

# Phase 2 ingestion — 2026-08-19

**Run:** `knowledge/research-runs/2026-08-19_phase2-expert-corpus/`. Three further YouTube sources, all with exact upload dates. Auto-captions — figures are as transcribed and must be checked against video before use.

**What changed since the 2026-08-13 ingestion:** that run captured a single 2025-04-28 video. These three are 2026 and show him **operating at account level on screen** (Ads Manager walkthroughs, client calls), which is a stronger evidence format than the earlier explainer. His stated context is unchanged: ecommerce/DTC agency and paid mentorship, accounts far above DR's spend.

## Sources processed (Phase 2)

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.youtube.com/watch?v=IO0hAgX8Bx8` | youtube (auto captions) | 2026-04-01 | 2026-08-19 | 4 | C1, C3, D3, S1 |
| `https://www.youtube.com/watch?v=E6fLpuNNYnI` | youtube (auto captions) | 2026-05-01 | 2026-08-19 | 2 | D1, D3 |
| `https://www.youtube.com/watch?v=qM7G_PHZUc4` | youtube (auto captions) | 2026-04-24 | 2026-08-19 | 2 | D1, E2 |

**Stated context (Phase 2):** the account walked through on screen spends roughly **$26,000 per 7 days** with 571 purchases at a $46 cost per acquisition. Client calls reference $1,200/day budgets. **DR's historical spend is roughly 1,000× lower than the account he demonstrates on.**

---

## Claims — Phase 2

### campaign_structure — Everything runs in one CBO, including tests that used to have their own campaigns

```yaml
topic: campaign_structure
claim: His agency's account structure puts the overwhelming majority of spend in a single CBO campaign; landing-page tests that were once run as a separate campaign are now run inside the main campaign, and a separately tested bid-cap campaign performed badly and was abandoned.
recommended_action: Run testing and scaling inside one CBO campaign rather than building dedicated test campaigns.
context: Client account selling one product to one core avatar in the USA and Canada.
business_type: ecommerce
spend_level: "$26,000 per 7 days on the demonstrated account; $1,900 spent on the abandoned bid-cap test"
conversion_volume_context: "571 purchases in 7 days at ~$46 CPA"
research_question_ids: [C1, C3]
question_link_origin: prospective
published_at: 2026-04-01
source_url: https://www.youtube.com/watch?v=IO0hAgX8Bx8
author: Nick Theriot
timestamp: null
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "Live Ads Manager screen share with campaign-level spend, purchases and CPA visible, plus the abandoned bid-cap campaign shown with its spend. Single account; no comparison against the alternative structure is presented, and the bid-cap verdict rests on $1,900 of spend which he does not claim is conclusive."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

> "majority of our spend last 7 days, $26,000 in this account was on this one CBO campaign that did 571 purchases at a $46 cost per acquisition… Landing page test, this is where we used to test landing pages in a separate campaign. We don't do it anymore. We just do it in our main campaign."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** Strengthens his earlier one-CBO claim with **account evidence rather than assertion**, and adds a detail C3 will care about: the direction of travel is *toward* consolidation over time — he removed a separate test campaign he used to run. That is the same movement C3 concluded for DR from the opposite direction (nothing to separate yet). The CBO/ABO half does not transfer cleanly: C2 keeps DR's ad set budget as a low-stakes keep decision, and at one ad set the distinction is near-moot. Note the honest asymmetry — his consolidation happens at a spend level where each ad still accumulates real delivery; DR's consolidates a budget that would be thin however it is arranged.

---

### scaling — Increase budget 20% when yesterday beats the target new-customer CPA

```yaml
topic: scaling
claim: Scaling is a mechanical rule: raise campaign budget by 20% when yesterday's new-customer cost per acquisition is at or better than the modelled target; where the account is volatile, use a trailing average instead of yesterday.
recommended_action: Model a target new-customer CPA for the business, then raise budget 20% on days that beat it, switching to a trailing-average read when daily numbers swing.
context: Scaling a consolidated CBO after new winning ads are found.
business_type: ecommerce
spend_level: "demonstrated on the $26k/7-day account"
conversion_volume_context: null
research_question_ids: [S1, S2]
question_link_origin: prospective
published_at: 2026-04-01
source_url: https://www.youtube.com/watch?v=IO0hAgX8Bx8
author: Nick Theriot
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Procedure demonstrated on screen as standing practice. The 20% figure is stated without derivation and no comparison against other increments is shown."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "we do a 20% up if yesterday's target in CPA are better. So, we set a target cost per purchase… If we're seeing a lot of volatility in the account, instead of looking at yesterday, we'll look at the last 7[-]day average."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** S1/S2 are DEFERRED and this does not change that. The transferable fragment is his **volatility caveat**, not his rule: when daily numbers swing, stop reading days. DR's delivery is nothing but swing — single-digit weekly events make "yesterday" pure noise — so the correct DR translation of this claim is that DR is permanently in the condition where his own rule says do not use the daily read. The 20% figure is a practitioner convention with no evidence behind it and is not adopted (numeric-threshold rule).

---

### creative_testing — He could find no evidence that any creative upload volume breaks an account

```yaml
topic: creative_testing
claim: He deliberately challenged the common belief that creative uploads should be capped (e.g. six per week) and could find no evidence that any particular volume breaks performance; he reports seeing accounts on $50/day budgets test 50 new creatives daily and still scale.
recommended_action: Do not cap creative uploads at an arbitrary weekly number; upload on a fixed day for operational cleanliness rather than for algorithmic reasons.
context: Answering a client asking whether uploading ~50 additional ads at once was safe.
business_type: ecommerce
spend_level: "$50/day account cited as the example that tested 50 creatives daily"
conversion_volume_context: null
research_question_ids: [D1, D2]
question_link_origin: prospective
published_at: 2026-05-01
source_url: https://www.youtube.com/watch?v=E6fLpuNNYnI
author: Nick Theriot
timestamp: null
confidence: medium
evidence_basis: experience_claim
evidence_basis_details: "An explicit statement of absence of evidence ('I've just not been able to find one like scientific proof') plus a second-hand example of a $50/day account uploading 50 creatives daily. The second-hand example is unverified and no performance data accompanies it."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "I've challenged that particular belief this year, and I've just not have not been able to find one like scientific proof of, okay, if I upload this many creatives, it's going to break things… I've seen people with like a $50 a day budget test 50 new creatives every single day and still been able to scale."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** **This is the most direct external challenge to D1's provisional 2-3 per round, and it is the closest any panel member comes to DR's budget range** ($50/day). It deserves to be recorded as a challenge rather than filed away. But it does not overturn D1, for a reason the claim itself concedes: he is reporting **absence of proof of harm**, not evidence of benefit. D1's 2-3 was never justified by a fear of breaking delivery — it came from DR's own arithmetic that ~235-270 impressions/week cannot make *any* number of ads individually readable, and from Meta's separate advice against high ad volumes. A 50-creative round at DR's delivery would produce 50 unread ads. **Where he and D1 agree is the operational rule:** upload on one chosen day, in one batch — which is exactly D2's single change window.

---

### creative_testing — Kill an ad at one times target AOV with no sale, but only if it is not the top spender, and give it ~72 hours

```yaml
topic: creative_testing
claim: An ad that has spent roughly one times the target average order value without producing a sale should be killed — conditional on it being a lower-spending ad than the account's top spender, and on it having run about 72 hours (2-3 days) first.
recommended_action: Apply the 1× AOV no-sale kill only to non-top-spending ads, after roughly 72 hours of delivery.
context: Client call reviewing an ad that spent $50 and sold one book.
business_type: ecommerce
spend_level: null
conversion_volume_context: "$50 spend on the ad discussed; AOV-based threshold"
research_question_ids: [D3]
question_link_origin: prospective
published_at: 2026-05-01
source_url: https://www.youtube.com/watch?v=E6fLpuNNYnI
author: Nick Theriot
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as the rule in a document he distributes to mentorship clients, applied live to a specific ad on the call. No data justifying either the 1× AOV threshold or the 72-hour window is presented."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "in the doc that you shared, you said like if it spends one times the AOV that you're aiming for, should kill it. Is that right?" — "That is correct, but only if it's a lower spending ad than our like top spending ad."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** **Conflicts with D3 and the conflict is the record.** D3 concluded that no defensible spend or impression kill threshold exists for DR and explicitly refused to invent one, replacing it with a relative-exposure comparison and a NOT_EVALUABLE default. This is a fixed numeric threshold plus a 72-hour calendar gate — both forms D2 and D3 rejected. Two parts survive translation and are worth keeping: the kill is **relative** (only for ads below the top spender), which is the same comparability instinct D3 encodes, and it is scaled to **order value** rather than to a flat dollar figure, which is at least economically anchored. DR's season price could in principle anchor an equivalent — but with no measured cost per registration, applying it now would be manufacturing precision.

---

### creative_strategy — Spend 80% on iterating what works and 20% on genuinely new ideas

```yaml
topic: creative_testing
claim: His allocation across creative work is 80% doubling down on formats, visuals and messaging already proven to work, and 20% exploring genuinely new ideas.
recommended_action: Split creative effort roughly 80/20 between iteration of proven concepts and exploration of new ones.
context: Answering whether an established format (podcast clips) would tire out.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [D1]
question_link_origin: prospective
published_at: 2026-04-24
source_url: https://www.youtube.com/watch?v=qM7G_PHZUc4
author: Nick Theriot
timestamp: null
confidence: high
evidence_basis: opinion
evidence_basis_details: "Stated as a personal operating heuristic applied across his life and work, not as a tested allocation."
evidence_strength: none
platform_validation_status: UNVALIDATED
```

> "80% of my time is doubling down of what works… And in 20% of my time, money, and energy is going into exploratory new actions and new ideas. So, 80/20 on iterations, variations versus 20% messaging, new messaging."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** The split presumes a **known winner to double down on**, and D3 established that DR cannot currently identify one at ad level. Applying 80/20 before anything is proven would mean iterating on an assumption. Worth recording as the posture DR should adopt *after* a concept demonstrates itself across repeated windows — and as a caution that an 80/20 read of "what works" at DR's volume would most likely be reading noise.

---

### creative_strategy — Let customer research pick the niche, then build all creative around it

```yaml
topic: creative_strategy
claim: A customer survey can reveal an unexpected dominant segment that should then drive all advertising — in his client's case, 350-360 of 700 respondents were nurses buying the shoes for 12-hour pain-free shifts, so the account moved to nurse-specific creative and creators.
recommended_action: Survey existing customers, identify the dominant use case, and rebuild creative and creator sourcing around that segment rather than around the general product benefit.
context: Footwear client; survey of ~700 respondents.
business_type: ecommerce
spend_level: null
conversion_volume_context: "~700 survey responses; ~51% nurses"
research_question_ids: [E2, D1]
question_link_origin: prospective
published_at: 2026-04-24
source_url: https://www.youtube.com/watch?v=qM7G_PHZUc4
author: Nick Theriot
timestamp: null
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "Specific survey with respondent counts and segment breakdown quoted; the strategy change is described but no post-change performance result is presented."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "we ran a customer survey. And out of the 700 people that replied back… 350, 360 of those people were nurses that buy our shoes and they love our shoes because it allows them to go a full 12 hours at work pain-free… Now, I want to niche down to a nurse now. And that's what we're doing in all of our advertising."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **A method DR can run this season without any ad spend, and one that feeds E2 directly.** E2 assigns qualification to the message but the message content is currently an assumption about why parents enrol. Asking existing DR parents produces exactly the input this claim uses. Two DR-specific constraints: the survey must go to **parents, not children**, and the resulting segmentation must stay in the creative brief — E2 already establishes that message qualifies while settings enforce, and a survey finding cannot become a targeting input. Sample size is the honest limit: DR will not get 700 responses, so the result will be directional.

---

## Contradictions within this author (Phase 2 vs earlier ingestion)

- **Creative volume.** The 2025 ingestion recorded his "roughly 90% of ads don't get spend, and that's fine" framing, which presumes running many ads. Here he goes further and says he can find no evidence any upload volume is harmful. Consistent in direction; the newer claim is broader and rests on absence of evidence rather than observation.
- **Thresholds.** He rejects arbitrary creative-volume limits for lack of scientific proof, while distributing a kill rule (1× AOV, 72 hours) with no more proof behind it. He does not acknowledge the asymmetry.

## Open questions from this author (Phase 2)

1. What is the 1× AOV kill threshold derived from? It is the most operationally consequential number he gives and it is unexplained.
2. His bid-cap campaign "did horrible" on $1,900 of spend. Taylor Holiday's study reports bid cap delivering 123% of target on a small sample. **Two practitioners, opposite readings, both on thin data** — worth flagging rather than resolving.
3. He demonstrates on a one-product, one-avatar account. Does the single-CBO structure hold when the business has genuinely different economics per offer, which both Faris and Tomlinson say requires separation?

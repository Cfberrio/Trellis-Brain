---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/sam-piliero.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/sam-piliero.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Sam Piliero"
---

# Sam Piliero

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Dara-Denney|Dara Denney]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Ben-Heath|Ben Heath]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/sam-piliero.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** sam-piliero
**Watchlist priority:** 1
**Topics:** campaign_structure · scaling · creative_testing · targeting · budgeting · retargeting
**Sources processed:** 4 (Phase 1–2) · **60/60 YouTube videos fully reviewed** (Phase 3, 2026-08-19)
**Panel status:** `VETTED_OPERATOR` — see the Phase 3 section at the end of this file for the full-corpus review, coverage table, and the evidence caveats that qualify everything above.
**Last updated:** 2026-08-19
**Evidence model:** v2 — `evidence_basis` / `evidence_basis_details` / `evidence_strength` backfilled 2026-08-13 from the raw transcript already on file (`data/raw/2026-08-13_sam-piliero_FCc0Nl1Ivxw_expert-source.json`). No new retrieval. All evidence below is **self-reported by the author** unless stated otherwise; nothing here is independently verified.
**Field notes (2026-08-13):** `validation_status` renamed to `platform_validation_status` — it grades the claim against current first-party Meta documentation only, never against practitioner agreement or DR results. `research_question_ids` backfilled where the mapping to `knowledge/research-questions.md` is obvious; this source predates the backlog, so mappings are retrospective. Existing `UNVALIDATED` values are untriaged — some may become `NOT_APPLICABLE` at the next validation pass.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims |
|---|---|---|---|---|
| `https://www.instagram.com/p/DbwSuDLMDRZ/` | instagram (`type: "ad"`) | 2026-08-07 | 2026-08-13 | **0** |
| `https://www.youtube.com/watch?v=FCc0Nl1Ivxw` | youtube (18m27s, auto captions) | 2025-12-11 | 2026-08-13 | **9** |

**Stated context for all YouTube claims:** ecommerce/DTC. Case study is a brand taken from $56,000 to $250,000/month net sales in 90 days; Meta spend rose from $26,000 to $79,000 per period at flat 1.9 ROAS. Worked example throughout the video assumes **$1,000/day** total budget.

---

## Claims — YouTube (2025-12-11)

### campaign_structure — Four-campaign separation: prospecting, scale, retargeting, retention

```yaml
topic: campaign_structure
claim: Separate new-customer acquisition, engaged/retargeting, and retention into distinct campaigns rather than mixing them.
recommended_action: Build four campaigns — Prospecting CBO, Scale, Retargeting/Engaged, Retention — each with exclusions preventing overlap.
business_type: ecommerce
spend_level: "$1,000/day worked example"
conversion_volume_context: null
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "2:34"
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "The overall structure is presented at 0:00–0:14 as 'directly responsible for taking this brand from $56,000 in net sales all the way to $250,000 per month' in 90 days (spend $26k→$79k at flat 1.9 ROAS). Described only; no underlying account data shown. The case is tied to the structure as a whole, not to its individual tactics."
evidence_strength: moderate
research_question_ids: [C1]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "You're going to notice a theme here is that we're going to separate out our new customer acquisition, our engaged customer acquisition, and our retention."

**applicability_to_DR:** low · **modification_required:** yes
**reason:** PRINCIPLE (don't let cold and warm compete for the same budget) may transfer. IMPLEMENTATION does not — four campaigns at DR's $2.70/day would put each ad set far below any workable budget, and DR has no purchase-event pool to build retention audiences from.

---

### campaign_structure — Prospecting CBO carries ~80% of total spend

```yaml
topic: campaign_structure
claim: The prospecting CBO is the primary scaling vehicle and generally represents about 80% of total ad spend regardless of account size.
recommended_action: Allocate ~80% of total budget to the prospecting CBO campaign.
business_type: ecommerce
spend_level: "explicitly scale-independent: '$100, $1,000, $10,000'"
conversion_volume_context: null
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "2:34"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated as general practice ('this campaign generally represents 80% of the total ad spend'); no data tied to the ratio, and no evidence offered for the scale-independence claim."
evidence_strength: weak
research_question_ids: [C1]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "whatever your budget is, whether it's $100, $1,000, $10,000, this campaign generally represents 80% of the total ad spend."

**applicability_to_DR:** medium · **modification_required:** yes
**reason:** This is the one claim Sam explicitly scopes as scale-independent, naming $100/day as a valid floor. Even so, $100/day is ~37x DR's current daily spend. The allocation principle may transfer; the claim that it holds at any size is asserted, not evidenced.

---

### creative_testing — Modular creative "packs": each new creative round gets its own ad set

```yaml
topic: creative_testing
claim: Each new round of creative should launch as a new ad set ("pack"), because adding new ads into an existing ad set interferes with what is already learning there.
recommended_action: Create a new broad ad set per creative round, date-labelled; never add new creative into an existing running pack.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "5:40–6:11"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "'That's what I would advise for about 95 plus% of brands' — agency practice asserted; no comparison, test, or data shown for the pack mechanism itself."
evidence_strength: weak
research_question_ids: [D1, D2]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: PARTIALLY_SUPPORTED   # see Validation 2026-08-13 — Claim 1
```

> "Packs are just organization pieces. They're not actually doing anything unique. They're just not interfering at the learning phase. For example, if I were to just throw all my ads into one campaign and one ad set, then what would start to happen in time as I created new ads is that everything in pack number one or my only pack would get interfered with."

**applicability_to_DR:** medium · **modification_required:** yes
**reason:** **PRINCIPLE TRANSFERS AND IS INDEPENDENTLY CHECKABLE** — Meta's own significant-edits documentation lists "Adding a new ad to your ad set" as always significant, i.e. it resets that ad set's learning phase. Sam's mechanism claim is not folklore. IMPLEMENTATION DOES NOT TRANSFER: DR runs one ad set at $2.70/day and cannot fund parallel packs. For DR the usable form is timing — batch creative changes deliberately — not proliferating ad sets.

---

### creative_testing — Ad-set minimum spend at 1x target CPA, judged in 4–7 days

```yaml
topic: creative_testing
claim: New packs should carry an ad-set minimum spend limit set in dollars equal to roughly 1x target CPA; after 4-7 days, an ad set spending exactly the minimum every day is a failure signal.
recommended_action: "Set ad set spending limit minimum = 1x target CPA in dollars. Check at 4-7 days. If it spends only the minimum daily, remove the limit and move on - the ads are not good. If it spends above the minimum, the limit can be removed because it will overspend freely."
business_type: ecommerce
spend_level: "$100/day minimum in the worked example (target CPA $100)"
conversion_volume_context: null
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "11:48–12:48"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Operating procedure described ('what I like to do here…'); no outcome evidence presented for the minimum-spend method or the 4–7 day window."
evidence_strength: weak
research_question_ids: [D3, D4]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: PARTIALLY_SUPPORTED   # see Validation 2026-08-13 — Claim 5
```

> "What I like to do here is set this to a small number, usually equal to one time my target cost per acquisition… It is on you as the media buyer, the operator here to check this after just a period of around 4 to 7 days… What you don't want to see is it's spending the same $100 minimum every day. If that's the case, remove this, move on. Those ads are not good."

**applicability_to_DR:** low · **modification_required:** yes
**reason:** IMPLEMENTATION IMPOSSIBLE — the "small number" is $100/day, roughly 37x DR's entire daily spend. PRINCIPLE (force a minimum read, then judge on whether delivery exceeds the floor) is interesting but untested at DR's scale. **Also carries an unflagged risk:** Meta lists "Ad set spending limit amount" as a change that may or may not be significant depending on magnitude — so routinely setting and removing these limits may reset learning. Sam does not mention this.

---

### scaling — Dedicated scale campaign seeded by duplicated winners

```yaml
topic: scaling
claim: A separate scale campaign should hold duplicates of the best-performing ads, identified by incremental attribution rather than standard attribution.
recommended_action: "Create a scale campaign at no less than 1x CPA daily budget. Sort ads by spend, compare standard vs incremental attribution, duplicate high-spend/high-incremental ads into the scale campaign. Do not pause the originals - running duplicates is fine."
business_type: ecommerce
spend_level: "budget floor = 1x CPA; example $100/day"
conversion_volume_context: "requires enough ads with meaningful spend to rank"
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "6:42–9:48"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Ads Manager walkthrough of the method (duplicate winners by incremental attribution); no results of the method presented."
evidence_strength: weak
research_question_ids: [C3]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "All the scale campaign is is a place reserved for your best of your best ads… click compare attribution and click incremental attribution. What this is going to show me is the purchases that were most likely occurring because of Facebook… This doesn't mean you pause those ads down. In fact, we're completely comfortable having duplicates of those exact ads."

**applicability_to_DR:** low · **modification_required:** yes
**reason:** Requires a population of ads with enough spend to rank by incremental attribution. DR has one ad and no conversion column in its extract. The incremental-attribution comparison itself is worth noting as a reporting technique for later, once DR has volume.

---

### placements — Run all placements

```yaml
topic: placements
claim: Run all placements unless there is a strong data reason or a legal/platform restriction not to.
recommended_action: Leave placements on all/Advantage+ rather than manually restricting.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "5:09–5:40"
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "'99% of the brands that we work with are running all placements. We do find that this works better' — cross-client pattern asserted; no data or comparison shown."
evidence_strength: weak
research_question_ids: []   # placements = settled default, no open question   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: INSUFFICIENT_EVIDENCE   # see Validation 2026-08-13 — Claim 4
```

> "we want to make sure that we're on all placements unless you have some crazy indication of data or you physically can't show up for like legal reasons… 99% of the brands that we work with are running all placements. We do find that this works better unless we find key data points where refinements are necessary."

**applicability_to_DR:** medium · **modification_required:** no
**reason:** Directly relevant — DR currently runs all placements by default, and the first decision synthesis listed placement restriction as a low-confidence TEST. This claim argues against making that change. "We do find that this works better" is asserted from agency experience with no evidence presented; Meta publishes no per-placement performance claim either way.

---

### measurement — Standard attribution: 7-day click / 1-day engaged / 1-day view

```yaml
topic: attribution
claim: Use the standard 7-day click, 1-day engaged, 1-day view attribution setting across prospecting, scale and retargeting.
recommended_action: Set attribution to 7-day click / 1-day engaged / 1-day view; do not vary it per campaign.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "4:07"
confidence: high
evidence_basis: none_presented
evidence_basis_details: "Setting stated in passing during the setup walkthrough; no rationale or evidence presented."
evidence_strength: none
research_question_ids: [G1]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "we're going to be using standard attribution with normal 7-day click, one day engage, one day view."

**applicability_to_DR:** medium · **modification_required:** no
**reason:** PRINCIPLE may transfer, but DR's purchase decision is a seasonal enrolment that a parent may complete days after first exposure. Meta documents that attribution feeds optimization, not only reporting, so window choice is a delivery variable — and Meta does not enumerate allowed windows per objective.

---

### targeting — Interest ad sets test the interest, not new creative

```yaml
topic: targeting
claim: When adding interest-targeted ad sets, populate them with already-proven ads so the interest is the only variable being tested.
recommended_action: Put known-winning ads (the same ones in the scale campaign) into new interest ad sets. Never test a new interest and new creative simultaneously.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "11:18"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Experiment-design reasoning (isolate the interest as the only variable); no performance evidence presented. The claim's force is logical, not empirical."
evidence_strength: none
research_question_ids: [E1]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "You don't want to test both an interest with new ads at the same time. You really just want to test your best ads in the interest because then the interest is the variable."

**applicability_to_DR:** high · **modification_required:** no
**reason:** **PRINCIPLE TRANSFERS CLEANLY AND IS SCALE-INDEPENDENT.** It is a statement about experiment design, not budget. DR's 2026-05-11-era history shows exactly the failure it prevents — the earlier diagnostic could not attribute a CPL difference because targeting and creative changed together. Costs nothing to adopt as a rule.

---

### targeting — Retargeting must stay narrow; reject audience expansion

```yaml
topic: retargeting
claim: Audience expansion toggles can silently make a retargeting ad set broad, which defeats retargeting.
recommended_action: When building retargeting ad sets, uncheck the auto-selected expansion option and confirm the audience definition reads narrow, not broad.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
published_at: 2025-12-11
source_url: https://www.youtube.com/watch?v=FCc0Nl1Ivxw
author: Sam Piliero
timestamp: "14:20"
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Live Ads Manager walkthrough showing the expansion toggle flipping the audience-definition readout broad→narrow — demonstrates the UI mechanism, not any performance outcome."
evidence_strength: weak
research_question_ids: [F1]   # backfilled 2026-08-13; source predates the backlog
platform_validation_status: UNVALIDATED
```

> "This little button uses a suggestion maybe auto selected for you. And if it is, you're going to notice your audience definition is broad. This is not what we want. Broad audiences are not for retargeting… So we're going to unselect this and our audience definition is going to go to narrow."

**applicability_to_DR:** medium · **modification_required:** yes
**reason:** DR runs no retargeting campaign, so the literal advice is inapplicable. But the underlying mechanism is directly relevant: DR's live ad set carries `targeting_automation.advantage_audience: 1` against a `DR HISTORIC` custom audience — the same "expansion silently widens a defined audience" pattern, on a local advertiser where widening also risks geo accuracy.

---

## Instagram source — retained, zero claims

**Preserved deliberately.** The Instagram post that triggered this project is a 47-second paid ad (`type: "ad"`) for a webinar. It names a structure argument — "the structure that everybody's using" vs "the structure that actually works", a "growth loop" vs a "death loop" — and states neither. Zero actionable claims; extracting one would mean inventing withheld content.

Caption context, explicit: *"Most ecommerce brands and advertisers cannot scale their Meta Ads profitably… over 100 ecom businesses."*

The comparison is instructive and worth keeping: **the same author's short-form social produced 0 claims and his long-form YouTube produced 9.** That is a reusable source-selection signal, not a judgement about the author.

Term still undefined: **"the Andromeda era."** Not defined in either source.

## Validation — 2026-08-13

Validated against the existing `knowledge/official-meta/` base only. No new platform research.

### Claim 1 — new creative in an existing ad set disrupts learning → **PARTIALLY_SUPPORTED**

**Expert source:** Sam Piliero, `FCc0Nl1Ivxw` @ 5:40–6:11
**Official source:** `official-meta/significant-edits.md` (Business Help Centre, rendered 2026-08-13)

**What Meta establishes.** The platform mechanism is confirmed twice over. Meta's always-significant list contains both *"Any change to ad creative"* and *"Adding a new ad to your ad set"*. Meta also draws the distinction Sam is relying on: *"Every edit you make… has some effect on delivery, but not every edit causes the ad set to reenter the learning phase. Only a significant edit causes an ad set to reenter the learning phase."*

So: adding creative to a running ad set **does** reset that ad set's learning. Sam's mechanism is not folklore.

**What Meta does NOT establish.** Meta never recommends creating a new ad set as the remedy, and the pack implementation runs into Meta's own guidance pointing the other way — `learning-phase.md`: *"Avoid high ad volumes. When you create many ads and ad sets, the delivery system learns less about each ad and ad set… By combining similar ad sets, you also combine learnings."*

**The split that matters.**
- **PRINCIPLE TRANSFERS:** adding creative to a live ad set resets its learning — SUPPORTED.
- **IMPLEMENTATION DOES NOT:** "therefore launch a new pack ad set every round" is Sam's inference, unendorsed by Meta and in tension with Meta's consolidation guidance.

**applicability_to_DR:** high (principle) / low (implementation) · **modification_required:** yes
**reason:** DR runs one ad set at ~$2.70/day. The usable form is *timing* — batch creative changes into deliberate resets — not proliferating ad sets DR cannot fund.

---

### Claim 4 — run all placements by default → **INSUFFICIENT_EVIDENCE**

**Expert source:** Sam Piliero, `FCc0Nl1Ivxw` @ 5:09–5:40
**Official source:** `official-meta/placements.md`

**What Meta establishes.** Only the default behaviour: *"If you do not specify anything for a particular placement field, Facebook considers all possible default positions for that field."* That describes what happens, not what is advisable.

**What Meta does NOT establish.** Any recommendation. The stored file states plainly that it documents the API surface, not Advantage+ placements guidance, and that **Meta publishes no performance or cost claim per placement**. Sam's *"we do find that this works better"* is agency experience presented as fact, with no evidence shown.

**Collision recorded.** Sam's claim (all placements, don't restrict) points opposite to the earlier low-confidence DR hypothesis in `output/first-decision-synthesis.md` Decision 5 (restrict placements → TEST). **Neither position is backed by official performance evidence.** DR's own placement data — IG feed 79% of spend at $136 CPM vs FB feed $34 — is 10 clicks on $82.11, far too thin to settle it.

This does not mean manual placement restriction can never be useful. It means nothing available today decides it.

**applicability_to_DR:** medium · **modification_required:** no
**reason:** Practical effect is to *lower* the priority of a placement change, not to forbid one. Default stays all placements until DR evidence justifies otherwise.

---

### Claim 5 — spending-limit changes may themselves affect learning → **SUPPORTED** (with Meta's exact qualifier)

**Expert sources:** Sam Piliero `FCc0Nl1Ivxw` @ 11:48–12:48 (minimum = 1x CPA) · Nick Theriot `Xo9FANGyo2k` @ 1:00–2:04 ($5/day minimum)
**Official source:** `official-meta/significant-edits.md`

**What Meta establishes.** *"Ad set spending limit amount"* appears in Meta's conditionally-significant list, introduced by: *"A change to any of the following areas **may or may not be significant, depending on the magnitude of the change**."*

**What Meta does NOT establish — and this qualifier is load-bearing.** Meta publishes **no threshold**. Its own illustration contrasts $100→$101 (*"isn't likely"*) with $100→$1000 (*"may"*), and the stored file records that as an illustration, not a rule. Meta also does not address repeated small edits accumulating.

**This must NOT be read as "every spend-limit edit resets learning."** It is: such a change *can* be significant, magnitude decides, and the magnitude threshold is unpublished.

**Why this is the most valuable item in the run.** Both playbooks lean on spending-limit intervention as the standard remedy for non-delivery — Sam sets and removes a 1x-CPA minimum as routine practice, Nick adds $5/day on new tests. **Neither mentions that the intervention may itself carry a learning cost.** The finding exists only because expert claims were held against the official base; neither layer contains it alone.

**applicability_to_DR:** medium · **modification_required:** yes
**reason:** DR currently sets no ad-set spending limits (budget fields empty in all four snapshots), so there is no live exposure. It is a **guardrail on future action**: if DR ever adopts either expert's minimum-spend remedy, that is an edit with possible learning consequences on an account that already struggles to accumulate optimization events.

---

## Contradictions within this author

None internal. See `nick-theriot.md` for cross-author disagreements.

## Open questions from this author

- No evidence is offered for "all placements works better" — it is agency experience, stated as fact.
- The 80%-to-prospecting rule is asserted as scale-independent down to $100/day, with no reasoning for why the ratio holds at the bottom of that range.
- Ad-set spending-limit churn versus Meta's significant-edit rules is never addressed.
- What is "the M3 method" (referenced as a 22-page guide) and does it scope claims by spend level?

---

# Phase 2 ingestion — 2026-08-19

**Run:** `knowledge/research-runs/2026-08-19_phase2-expert-corpus/`.

**Dedup — one source skipped:** `https://www.youtube.com/watch?v=FCc0Nl1Ivxw` ("The NEW BEST Facebook Ads Campaign Structure for 2026", 2025-12-11) surfaced again in the Phase 2 corpus and was **not re-processed**. It was already ingested on 2026-08-13 and its raw transcript is on file at `data/raw/2026-08-13_sam-piliero_FCc0Nl1Ivxw_expert-source.json`. Its passages were used only to confirm that the two new sources below describe the same system rather than a changed one.

**What is new:** a July 2026 rebuild of the same architecture with **three accounts of different sizes walked through on screen**, and a December 2025 video that **scopes the architecture by spend tier** — which is the thing DR most needed from him and which the earlier ingestion did not capture.

## Sources processed (Phase 2)

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.youtube.com/watch?v=6P5M8yvXx1g` | youtube (auto captions) | 2026-07-26 | 2026-08-19 | 4 | C1, C3, D1, D2, B2 |
| `https://www.youtube.com/watch?v=Fo-p03fwvdA` | youtube (auto captions) | 2025-12-21 | 2026-08-19 | 2 | C4, F1 |
| ~~`https://www.youtube.com/watch?v=FCc0Nl1Ivxw`~~ | — | — | — | **skipped, already indexed 2026-08-13** | — |

**Stated context (Phase 2):** ecommerce/DTC agency (The Moonlight Agency). The **smallest** account he demonstrates spends about **$200/day** ($7,900 over 30 days at a stated 6.94 ROAS); the walkthroughs otherwise assume $1,000/day. He states the prospecting CBO "generally represents 80% of the total ad spend" whatever the budget. **DR's historical spend is roughly 1-2% of his smallest demonstrated account.**

---

## Claims — Phase 2

### campaign_structure — The architecture is explicitly scoped by spend tier, and retargeting is added only above ~$30k

```yaml
topic: campaign_structure
claim: The full four-campaign architecture is staged by account size: prospecting CBO plus a scale campaign for new-customer acquisition, an existing-customer effort for retention, and retargeting added specifically at the $30k+ range — because the overspending in prospecting and scaling that retargeting solves only appears at that scale.
recommended_action: Add retargeting structure when the account reaches the spend level where prospecting/scaling overspend on already-engaged users, not before.
context: A staged account-growth walkthrough; the tier discussed here is beyond $30k, with daily budgets moving between $1,000 and $4,000.
business_type: ecommerce
spend_level: "$30k+ named as the tier where retargeting is added; $1,000-$4,000/day discussed"
conversion_volume_context: null
research_question_ids: [C4, F1]
question_link_origin: prospective
published_at: 2025-12-21
source_url: https://www.youtube.com/watch?v=Fo-p03fwvdA
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Staged architecture described from agency practice with the spend tier named explicitly; no data shown for why $30k is the boundary."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "Once we get beyond 30K… we have the same prospecting CBO system as before… And then finally we have the new addition of retargeting… the reason I add retargeting in here is specifically because we start to see the overspending in prospecting in the scaling campaign happen more so at this 30k plus range than ever."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** **This materially improves how the earlier Piliero ingestion should be read.** C1 and C3 characterised his four-campaign architecture as carrying preconditions DR does not meet, and this claim is the author **stating the scoping himself**: retargeting is a solution to a problem that appears at $30k, and the elaborate structure belongs to accounts operating there. That converts an inference into his own testimony, which is stronger. It also independently supports F1's deferral — the panel's most structure-heavy practitioner does not build retargeting at small scale either. The tier figure is a practitioner convention, not evidence, and is not adopted as a DR threshold.

---

### campaign_structure — Testing must never exceed 20% of total budget

```yaml
topic: budgeting
claim: Ad-set spending minimums for a new creative pack should be set to one times target CPA, but if that figure exceeds 20% of total budget it must be converted to a percentage and capped at 20% — testing with more than a fifth of budget is waste.
recommended_action: Cap all testing at 20% of total budget; spend as much as possible on proven ads and as little as possible on tests.
context: Setting ad-set spending limits when launching a new creative pack inside the prospecting CBO.
business_type: ecommerce
spend_level: "worked at a $1,000/day budget with a $50 target CPA"
conversion_volume_context: null
research_question_ids: [D1, B2]
question_link_origin: prospective
published_at: 2026-07-26
source_url: https://www.youtube.com/watch?v=6P5M8yvXx1g
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Rule stated with an explicit conversion procedure and demonstrated in Ads Manager. The 20% cap is asserted as a principle ('that is a waste of money'); no data behind the number."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "If this number is greater than 20% of your total budget, then change this from a dollar value to a percentage and max this out at 20%. Under no circumstances are we testing with more than 20% of our total budget."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** **The rule's own arithmetic explains why his system cannot run at DR's scale, and that is its value here.** He sets a testing minimum of 1× target CPA and caps it at 20% of budget — which means the system is only coherent when the daily budget is at least five times the target CPA. DR's cost per registration is unmeasured (B2), but on any plausible value DR's historical ~$2.70/day fails that condition by a wide margin. This is the clearest quantitative demonstration in the corpus that the pack architecture presupposes a budget floor DR does not clear. The 20% figure itself is not adopted.

---

### creative_testing — Run the forced-spend minimum for exactly 7 days, then remove it

```yaml
topic: creative_testing
claim: The ad-set spending minimum on a new pack should run for 7 days and then be removed; removing it stops forcing spend without resetting learnings — a winner keeps spending because it is already above the threshold, a loser stops draining budget.
recommended_action: Set the minimum for 7 days, then unselect and publish; check the pack at 4-7 days and if it is spending exactly the minimum every day, remove it and move on.
context: Managing new creative packs inside the prospecting CBO.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [D2, D3]
question_link_origin: prospective
published_at: 2026-07-26
source_url: https://www.youtube.com/watch?v=6P5M8yvXx1g
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Procedure demonstrated on screen. **The claim that removing the minimum 'is not going to reset your learnings' is a platform-mechanism assertion made without documentation** and is the part most in need of validation."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "you're only running this minimum for 7 days. After that 7-day period, you go back into here and yes, you make a change to an existing adset. You unselect this and you publish… It's not going to reset your learnings."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** **Flag the platform assertion, not the tactic.** `official-meta/significant-edits.md` places changes to a live ad set on Meta's always-significant list, and he is asserting a specific exemption for removing a spending minimum. That is exactly checkable and should go to the validation pass — if he is wrong, his own system carries an unflagged learning reset every 7 days, which is the same unflagged cost already found in the 2026-08-13 ingestion (Claim 5). The diagnostic underneath is the useful residue: **an ad set that spends exactly its minimum every day and no more is telling you the ads are not wanted** — a relative signal, compatible with D3, and readable without a threshold.

---

### campaign_structure — The scale campaign is one broad ad set holding about five known winners

```yaml
topic: campaign_structure
claim: Above the prospecting campaign sits a scale campaign — a single broad ad set containing roughly five of the account's very best ads, whose only function is to force more spend against ads already proven.
recommended_action: Keep the scale campaign to about five ads you know intimately; it does nothing except concentrate budget on proven winners.
context: The top of his account architecture, demonstrated across three accounts of different sizes.
business_type: ecommerce
spend_level: "smallest demonstrated account ~$200/day ($7,900/30 days at a stated 6.94 ROAS)"
conversion_volume_context: null
research_question_ids: [C3, S2]
question_link_origin: prospective
published_at: 2026-07-26
source_url: https://www.youtube.com/watch?v=6P5M8yvXx1g
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: self_reported_case_study
evidence_basis_details: "Three client accounts shown on screen with 30-day spend and ROAS figures; the structure is visible but no comparison against running without a scale campaign is presented, so the attribution of results to the structure is the author's."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "at the top of our account, we have a scale campaign. The scale campaign is a broad single ad set smash of all our winners together… Generally, we're looking at like 5ish total ads in the scale campaign, nothing more… all this does is force more spend against these ads, nothing else."

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** no · **implementation_transfers:** no
**reason:** C3 rejected testing/scaling campaign separation for DR because **there is nothing to separate — no winner pool exists**, and this claim states the precondition even more plainly than the earlier ingestion did: the scale campaign holds ads "you should literally know these ads so well, like the back of your hand." D3 established that DR cannot identify a winner at ad level at current delivery. **The precondition is the finding**: this architecture is not wrong for DR, it is unbuildable, and it stays unbuildable until repeated windows produce a stable ordering.

---

### retargeting — Retargeting audiences and creative are defined by intent recency, and widened for smaller businesses

```yaml
topic: retargeting
claim: The retargeting campaign runs Facebook/Instagram engagers, 30-60 day site visitors and 90-day-plus add-to-carts or checkout initiators, with creative weighted toward objections, offers and sales; smaller businesses should widen these windows so the audiences have anyone in them at all.
recommended_action: Set retargeting windows by business size — narrower for large accounts, broader for small ones — and use objection-handling and offer creative in that campaign.
context: The retargeting campaign in his architecture.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [F1]
question_link_origin: prospective
published_at: 2026-07-26
source_url: https://www.youtube.com/watch?v=6P5M8yvXx1g
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Standing configuration described; no data on window-length performance."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "we normally like to run Facebook and Instagram engagers, 30 to 60day site visitors, and 90-day plus add to carts or initiate checkouts. You could flex these dates based on how big your business is… If you're a smaller business, you might want to go a little bit broader so you actually have some audiences in here."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** F1 is deferred, and this claim is useful mainly for the sentence about small businesses: **the smaller the account, the longer the window has to be for the pool to contain anyone.** That is the mechanism behind F1's deferral, stated by a practitioner who builds retargeting for a living. It also collides with Jon Loomer's position that a separate remarketing campaign is redundant because Meta already allocates a fifth of budget to warm users unprompted. **Two structure-literate practitioners, opposite conclusions, neither with data** — recorded as an open conflict for whenever F1 reopens.

---

### measurement — Audience segment reporting must be configured before it can tell you anything

```yaml
topic: measurement
claim: Audience segment reporting has to be set up in advertiser settings before it works, defining an engaged audience (e.g. 30-day site visitors, 90-day add to cart) and existing customers (pixel purchasers plus the all-time customer list from email/CRM).
recommended_action: Configure engaged-audience and existing-customer definitions in advertiser settings as part of account setup, not after a problem appears.
context: Campaign settings walkthrough from a blank ad account.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [G2, F1]
question_link_origin: prospective
published_at: 2026-07-26
source_url: https://www.youtube.com/watch?v=6P5M8yvXx1g
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Setup step demonstrated in the interface; no performance claim attached."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

> "our audience segment reporting… You need to set these up in your advertiser settings. These are going to define your engage and existing customers."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **Independently confirms the setup step Jon Loomer's remarketing diagnostic depends on**, from a different practitioner, and it is a configuration DR can complete before spending anything. It converts both his and Loomer's warm-versus-cold diagnostics from theory into something DR could actually read during its next registration window — the single cheapest measurement improvement identified in this Phase 2 run. Two DR caveats carry over from the Loomer file: the reporting is tied to a Sales objective, which A1 has not settled, and DR's "existing customer" list is a parent list, which must be handled under the same child-data constraints A3/E2 already impose.

---

## Contradictions within this author (Phase 2 vs earlier ingestion)

- **None on substance.** The July 2026 walkthrough describes the same pack architecture as the December 2025 source already on file; the system is stable across eight months, which is itself a mild signal of conviction.
- **New scoping, not a new position.** The earlier ingestion carried his architecture without a stated spend floor, and C1/C3 had to infer that its preconditions excluded DR. He now states the tiering himself. The inference was correct; it is no longer an inference.

## Open questions from this author (Phase 2)

1. **Does removing an ad-set spending minimum reset learning?** He asserts it does not. `significant-edits.md` says changes to a live ad set are always significant. This is the highest-value validation item in the file.
2. His smallest demonstrated account is ~$200/day. What does his system look like below that — or does he consider it inapplicable? The pack arithmetic (1× CPA minimum, 20% cap) implies a floor of roughly 5× target CPA per day, which he never states as a floor.
3. He and Jon Loomer disagree directly on whether a separate retargeting campaign is worth building when Meta already serves warm users automatically. Neither presents data. Any future F1 reopen should treat this as the live question.

---

# Phase 3 — Full video corpus review (2026-08-19)

**Panel status:** `VETTED_OPERATOR` — 60/60 videos read start to finish, chronologically, no passage sampling. Agency operator (The Moonlighters) with a stable, repeatedly demonstrated system, a documented history of publicly reversing his own positions when data changed, and two on-record Meta employees interviewed on his own channel. Evidence is still overwhelmingly **self-reported**; account screenshots are shown but never exported, and no third party has audited any figure in this corpus.

## Coverage

| Status | Videos |
|---|---|
| `FULLY_REVIEWED_USEFUL` | 45 |
| `FULLY_REVIEWED_DUPLICATIVE` | 9 |
| `FULLY_REVIEWED_LOW_VALUE` | 6 |
| `FULLY_REVIEWED_NOT_RELEVANT` | 0 |
| `TRANSCRIPT_INCOMPLETE` | 0 |
| `TRANSCRIPT_UNAVAILABLE` | 0 |
| **Total** | **60** |

`LOW_VALUE` = software tutorials whose subject is a third-party tool rather than Meta (`gtvTGN6kKPk` Nano Banana, `zKymHum4gWY` Arcads, `LRk2Vijbsy4` SuperScale, `CPc4lB33RvU` + `0Z6Rgo6iiUA` Claude/Meta MCP, `5Vz3XToNMSI` "7 levels" framing with no operational content). `NOT_RELEVANT` is zero: every video in this corpus is about Meta advertising.

**Corpus tier:** 60/60 `CURRENT`. Published 2025-11-16 → 2026-08-14 — **entirely post-Andromeda**. This is the only expert corpus in the panel with no HISTORICAL content at all, and the only one that spans the Andromeda→GEM→Lattice period continuously at roughly two videos per week. For questions about *current* platform behaviour this corpus outranks every other expert file on recency grounds alone.

**Corpus caveat — commercial framing.** Every video ends in an agency pitch (`themoonlighters.com/apply`) and/or a paid-community pitch (`school.com/facebook`), and several late videos carry affiliate placements (Arcads, SuperScale, a virtual-try-on app he co-owns). His stated client count also drifts: "nearly 100 brands" (Nov 2025 – Jul 2026) → "over 80 brands" (2026-08-14). Nothing here is disqualifying, but self-reported scale figures in this file should be read as marketing copy, not as audited counts.

---

## Corpus-level findings — things only a full read produces

### ⚠ F-1. He reversed his headline creative-volume position over nine months. Passage sampling would have produced a flat contradiction.

This is the defining trajectory of the corpus and it is only visible chronologically:

| Date | Video | Position |
|---|---|---|
| 2025-11-19 | `cWTzsftTb_Y` | *"more ads are still better than less ads"* — opens by attacking the run-fewer-ads camp; shows AG1 at 4,991 active ads, Nike at 18,787 |
| 2025-11-23 | `upfQQuyL3uI` | Formalises the **rule of 10,000**: one new ad per week per $10,000/month of spend |
| 2026-01-28 | `se8B4xOJHco` | Restates it harder: *"People who make creative, of course, want to sell you more creative"* — accuses the low-volume camp of self-interest |
| 2026-04-12 | `LYBrcvGP5AE` | Adds a **floor of two ads/week**, and an explicit small-budget accommodation (four ads every two weeks) |
| 2026-05-15 | `yp6BtzVPWBE` | Item 18 of 21: *"Quality beats quantity in ads every single time"* — first crack |
| 2026-06-04 | `nZmTmIVApmY` | Meta's Matt Steiner tells him, on his own channel, that *"creating an extremely large number of them probably isn't going to help you more than having a reasonable diversity of ads"* |
| 2026-07-05 | `TIs3ID-9a3o` | Shows a client account improved by **cutting** active ads 165 → 62 |
| 2026-08-14 | `f1PGNuLWQHE` | *"I'm just going to put an end to that. **Volume of creative does not matter.** Quality of creative at scale does matter."* |

He never announces the reversal as a reversal. Any density-based extraction would have surfaced both the November and the August passages and recorded them as an unresolved internal contradiction. Read in sequence it is a position that moved under evidence — including evidence handed to him by Meta in an interview he conducted himself.

**DR consequence:** the rule of 10,000 must **not** be carried into DR as a live rule. Its author has retired it. What survives is his floor — two genuinely different ads per week, or four every two weeks if production is the constraint — which is a rate DR can actually sustain.

### ⚠ F-2. He reversed his flexible-ads position twice in five months, and the second reversal was Meta's, not his.

`sqyA27k_aQ4` (2025-12-28): flexible ads are "built for this algorithm," the way to keep near-identical iterations alive as one unit. → `ecBotbrHkvg` (2026-02-16): *"just 30 days ago, this was an incredible setting… this setting is no longer the optimal way to run your ads"* — bad crops, duplicate images inside auto-generated carousels. → `T9T7u_bCE4Y` (2026-04-26): Meta deprecates the flexible format; its behaviour moves into the Advantage+ **Flex media** enhancement, which is **on by default**.

**DR consequence:** any DR ad built today inherits Flex media unless it is explicitly turned off. His resulting rule of thumb, stated twice (`TIs3ID-9a3o`, `6P5M8yvXx1g`), is the most portable creative-controls guidance in the corpus: **allow enhancements that add things around the creative; block every enhancement that alters the creative itself** (visual touch-ups, music, generated backgrounds, animation, product touch-ups).

### ⚠ F-3. He replaced his own campaign method mid-corpus — M3 → M4 — and the change is specifically about small new ad sets not getting spend.

`VB4viinqh-Y` (2026-03-09) and `C9QN6etdeTQ` (2026-03-12) retire the method he had taught for two years. He names and rejects three testing approaches including **his own prior one**: *"testing in the classic CBO structure without any control… this is a structure that I myself have taught for the last 2 years, and things change, I let everyone know."*

The stated cause is post-Andromeda delivery: new ad sets launched into a mature CBO now receive *"literally zero spend or just a few pennies."* M4 = M3 plus two changes: (a) a **7-day ad-set minimum budget on every new pack**, then removed; (b) packs grouped by **avatar + concept** rather than by upload batch.

This is the second mid-corpus method change found in this run (Jon Loomer's creative-testing-tool → push-delivery shift is the first). Both were invisible to Phase 2 and both were caused by the same thing — Andromeda changing how new creative gets exposure.

### ⚠ F-4. A named Meta engineer states on the record that low spend structurally causes volatility.

`nZmTmIVApmY` (2026-06-04), Matt Steiner, who describes his own remit as *"monetization infrastructure, ranking, and foundational AI at Meta"* — i.e. the systems in question. Asked directly whether delivery volatility is a feature rather than a bug:

> "Volatility and associated price optimization are the opposite end of the spectrum of low volatility and higher prices. So you kind of have to decide which matters more to you, lowest prices or low volatility, because they're on opposite ends of the spectrum."

Piliero then restates it in advertiser terms — *"when you're spending less or when your average order values or cost per acquisitions are significantly higher, you then therefore have to just accept that you have to deal with volatility"* — and Steiner agrees.

**This is the single most consequential passage in the corpus for DR.** DR's erratic day-to-day results at its spend level are, per the person who owns the ranking systems, the *expected* behaviour of a thin bidder in a real-time auction — not evidence of a broken structure, a bad pixel, or a wrong setting. It reframes an entire class of DR diagnostic instinct. It remains `PLATFORM_VALIDATION_STATUS: UNVALIDATED` — it is a vendor statement in a promotional interview, not documentation — but it is the strongest-provenance mechanical statement anywhere in the panel.

### F-5. The corpus contains real small-account evidence, which Phase 2's open question #2 assumed it did not.

Phase 2 recorded "his smallest demonstrated account is ~$200/day; what does his system look like below that?" as an open question. The full corpus answers it three ways:

- `6P5M8yvXx1g` (2026-07-26) shows three accounts side by side, the smallest at **$7,900/30 days (~$260/day) at 6.94 ROAS**, explicitly to demonstrate the system is not scale-gated.
- `TIs3ID-9a3o` (2026-07-05) walks a **$14,000/30-day (~$470/day)** fashion account from 0.63 → 1.4 ROAS in 30 days, with no new creative, no sale, and **fewer** ads.
- The `$100/day` advertiser is addressed directly and repeatedly, with its own arithmetic (see C-1 below).

Open question #2 is **resolved** — his system does have a stated small-budget form.

---

## Claims — Phase 3

### C-1 · budgeting — The 20%-of-budget cap on ad-set minimums is the small-account form of his testing rule

```yaml
topic: budgeting
claim: A new ad set's forced daily minimum should be 1× target CPA, but never more than 20% of total daily budget; on a $100/day account that means $20, not the CPA.
recommended_action: When launching a new pack, set an ad-set daily minimum of min(1 × target CPA, 20% of total daily budget), for exactly 7 days, then remove it.
context: Stated as a hard rule in the definitive M4 walkthrough and repeated verbatim in four other videos.
business_type: ecommerce
spend_level: "explicitly scaled: worked from $100/day up to $1,000+/day"
conversion_volume_context: null
research_question_ids: [C1, C3, B2]
question_link_origin: prospective
published_at: 2026-07-26
source_url: https://www.youtube.com/watch?v=6P5M8yvXx1g
corroborating_sources:
  - https://www.youtube.com/watch?v=Uus6i9Gn6m0   # 2026-05-01
  - https://www.youtube.com/watch?v=LRk2Vijbsy4   # 2026-05-26
  - https://www.youtube.com/watch?v=NxaYt0ta00U   # 2026-06-26
  - https://www.youtube.com/watch?v=TIs3ID-9a3o   # 2026-07-05
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: operator_method
evidence_basis_details: "Stated as agency standard operating procedure across five videos spanning May–July 2026 with identical arithmetic. No before/after data is attached to the 20% cap specifically — the supporting case studies (TIs3ID-9a3o, LQMY3SGPO1w) change several things at once, of which this is one."
evidence_strength: moderate
context_completeness: complete
platform_validation_status: UNVALIDATED
```

> "If you have a budget that cannot absorb that full target CPA amount, like if you have a smaller budget, you only want the maximum threshold for testing… is 20%. If you had a brand that you were spending $1,000 a day on, the most you could ever put your average daily minimum is 200. If you were spending 100, the most you could ever put here is 20. So 20% of your total budget is the maximum… across all of the ad sets combined."

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** yes
**reason:** This is the rule Phase 2 could not find and had to infer around. The principle — cap total forced testing spend as a share of budget rather than as a fixed dollar figure — is budget-neutral and therefore survives translation to DR intact. The arithmetic is stated for exactly DR's order of magnitude. **The one caveat he himself attaches** (`FYUR8ZL4_xY`, 2026-03-15): *"If you're only spending a little bit of money, then you might not have the flexibility to do this. This is going to be most applicable and most effective for businesses that are spending a lot."* The rule scales down mathematically; he is not certain it scales down behaviourally. Record as `DR_HYPOTHESIS`, not as a rule.

---

### C-2 · targeting — Geographic expansion runs as one extra ad set inside the existing CBO, never as a new campaign

```yaml
topic: targeting
claim: To add a new geography, duplicate an existing ad set inside the same prospecting CBO, swap only the location, and populate it exclusively with already-proven winning ads — so location is the only variable and the CBO decides whether it deserves budget.
recommended_action: Add geographies as additional ad sets in the existing prospecting CBO carrying proven creative only; do not build a separate campaign and do not force budget beyond the standard 7-day minimum.
context: Six-month progression shown for one account, July 2025 → December 2025.
business_type: ecommerce (multi-country shipping)
spend_level: "$8,000/month rising to $141,000/month over the period shown"
conversion_volume_context: "10–12 countries at start, 36+ at end"
research_question_ids: [E3, C1, B2]
question_link_origin: prospective
published_at: 2026-03-01
source_url: https://www.youtube.com/watch?v=S3bybSKk4Ok
corroborating_sources:
  - https://www.youtube.com/watch?v=uuHBybzdQp8   # 2025-11-30, same protocol for country/placement/landing page
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: real_account_example
evidence_basis_details: "Ads Manager country breakdown shown at two points six months apart: July 2025 $8,000 spend → $22,000 revenue at 2.60 ROAS across ~10–12 countries; December 2025 $141,000 spend → $294,000 revenue at 2.07 ROAS across 36+ countries. Black Friday explicitly excluded from the comparison window. Account identity withheld. Numbers read from screen, not exported."
evidence_strength: moderate
context_completeness: complete
platform_validation_status: UNVALIDATED
```

> "One that doesn't force any amount of spend to any new country and only spends when the country is better than your baseline… we've seen new markets outscale existing markets in just a few months."

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **This claim replaces the Ben Heath multi-location passage that Phase 2 recorded as DR's closest structural analogue.** The Heath passage came from an awareness campaign with the optimizer deliberately disabled (see the ⚠ CORRECTION block in `ben-heath.md`). This is a conversion campaign, in a live account, with a six-month before/after and an explicit statement that ROAS was traded (2.60 → 2.07) for 17× the spend. It is a strictly better source for the same question. `implementation_transfers: partial` because DR expands across US metros, not countries — the mechanic is identical but CPM heterogeneity between US metros is far smaller than between countries, which likely weakens the effect rather than reversing it.

---

### C-3 · measurement — Geo targeting shares pixel signal; no separate pixel or account is needed per location

```yaml
topic: measurement
claim: Expanding into new geographies does not require new pixels or new data sets; signal is shared to the location automatically and existing-market performance is not degraded by the addition.
recommended_action: Do not create per-location pixels, data sets, or ad accounts when expanding geographically.
context: Stated as an aside while introducing the geo-expansion protocol.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [E3, G1]
question_link_origin: prospective
published_at: 2026-03-01
source_url: https://www.youtube.com/watch?v=S3bybSKk4Ok
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Asserted flatly, with no supporting data, test, or documentation reference. He does not say how he knows it. Consistent with — but not evidence for — the shared-standard-event model he describes separately in H_jfsgGJc4c."
evidence_strength: weak
context_completeness: partial
platform_validation_status: UNVALIDATED
```

> "You don't need new pixels. You don't need to do anything fancy here. Whenever you're geotargeting or expanding countries in Facebook, the signals are always shared to that location."

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** no
**reason:** If true, it removes an entire category of proposed DR complexity (per-market pixels/accounts for new cities) at zero cost. It is exactly the kind of platform-mechanics assertion this project refuses to promote on a practitioner's word alone. **Highest-priority item for the platform-validation queue** — it is cheap to check against Meta documentation and it gates a structural decision.

---

### C-4 · targeting — The language setting is the failure mode of geographic expansion

```yaml
topic: targeting
claim: Leaving the language setting on "All languages" while targeting geographies that speak other languages causes ads to be served to people who cannot read them; the fix is to select every variant of the ad's actual language.
recommended_action: On any ad set targeting a multilingual geography, set Languages explicitly to the language(s) the creative is written in — for English, select English (All), English (UK) and English (US).
context: Presented as "the one setting that can make or break this entire thing" within the geo-expansion protocol.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [E3, D2]
question_link_origin: prospective
published_at: 2026-03-01
source_url: https://www.youtube.com/watch?v=S3bybSKk4Ok
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Stated with high emphasis and no data. Note he takes the opposite position in TIs3ID-9a3o (2026-07-05) for translation-capable businesses: 'translating to all is going to expand your reach significantly.' The two are reconcilable — one is about serving untranslated creative, the other about deliberately translating it — but he never reconciles them out loud."
evidence_strength: weak
context_completeness: partial
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** medium · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** DR advertises in English in US metros with large Spanish-speaking populations. The claim implies a checkable question DR can answer from its own delivery data rather than from his: is DR currently serving English-only creative to Spanish-preference users, and does that show up in its placement/geo breakdown? Cheap to inspect, no spend required.

---

### C-5 · creative_testing — A new round of creative always goes into a new ad set, never into an existing one

```yaml
topic: creative_testing
claim: Adding new ads into an ad set that is already running interferes with the existing ads' delivery; new creative must always launch as a new ad set.
recommended_action: Never inject new ads into an existing pack. Every new round of creative gets a new ad set inside the same prospecting CBO.
context: Stated as the load-bearing rule of the pack system in the definitive walkthrough.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [C1, B2]
question_link_origin: prospective
published_at: 2026-07-05
source_url: https://www.youtube.com/watch?v=TIs3ID-9a3o
corroborating_sources:
  - https://www.youtube.com/watch?v=Z4YWKO8T_3M   # 2026-07-11, audit showing the failure mode
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: real_account_example
evidence_basis_details: "The rule is asserted throughout the corpus as method. Z4YWKO8T_3M supplies the only failure evidence: an audited account that spent 6% LESS month over month, added new ads into an existing consolidated campaign, and saw one ad go from $11 to $2,000 in 30-day spend, 'effectively hogging the entire budget of the entire account' and tanking overall ROAS. One account, no control, described not exported."
evidence_strength: moderate
context_completeness: complete
platform_validation_status: UNVALIDATED
```

> "Every time we launch new ads, we launch them into a new pack or a new ad set. We never inject new ads into old packs. Let that sit with you. That is critical."

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** yes
**reason:** Costs DR nothing, requires no additional budget, and is the one M4 component with no spend precondition attached. Converges with Jon Loomer's independent observation that every structural change solves a problem or creates one. This is the cheapest structural discipline available to DR from the entire panel.

---

### C-6 · creative_testing — Kill an ad only after 2× target CPA in spend with zero purchases

```yaml
topic: creative_testing
claim: The default is not to pause ads at all; the one clean kill condition is an ad that has spent twice the target CPA and driven no purchases. If the account overall is hitting its KPI, pause nothing.
recommended_action: Pause an ad only when (a) the account is missing its KPI AND (b) that ad has spent ≥2× target CPA with zero purchases, or (c) it is attracting demonstrably wrong customers.
context: Post-launch checklist, item 6 of 11.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [B2, B3]
question_link_origin: prospective
published_at: 2026-04-24
source_url: https://www.youtube.com/watch?v=zo9evN1pVaM
corroborating_sources:
  - https://www.youtube.com/watch?v=r3_Ly3Y9cHk   # 2026-04-19, "we don't want to pause our ads ever"
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: operator_method
evidence_basis_details: "Stated as a rule of thumb, twice, five days apart. No test, no data. The supporting argument is the supportive-ad mechanism (C-7), which does have a documented test behind it."
evidence_strength: weak
context_completeness: complete
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** yes
**reason:** ⭐ **Third independent arrival at the same threshold from three unrelated clusters.** Dara Denney's two-condition kill rule (missing CPA goal AND meaningful spend), Jess Bachman's 2–3× target CPA spend-before-verdict floor in the Foxwell corpus, and now Piliero's 2× target CPA with zero purchases. Denney, Bachman and Piliero share no employer, no community, and no funding relationship. **DR can compute this threshold from DR's own target CPA without adopting anyone's number.** This is the strongest cross-cluster convergence produced by the entire Phase 3 run so far and it should be promoted directly to `DR_HYPOTHESIS` for the next test window.

---

### C-7 · creative_testing — High-spending under-target ads can be supportive; pausing them degraded the whole campaign

```yaml
topic: creative_testing
claim: An ad that takes a large share of spend at a worse-than-average CPA may be functioning as an introduction ad for the campaign; removing it can degrade every other ad in the campaign.
recommended_action: Before pausing a top-spending ad that misses target, treat it as possibly supportive; prefer a maximum spend cap over a pause.
context: One campaign, $27,000 spend over 30 days, one ad taking $14,000 of it at $45 CPP against a $43 average.
business_type: ecommerce
spend_level: "$27,000/30 days in the campaign shown"
conversion_volume_context: null
research_question_ids: [B2, B3, C4]
question_link_origin: prospective
published_at: 2025-11-19
source_url: https://www.youtube.com/watch?v=cWTzsftTb_Y
author: Sam Piliero
timestamp: null
confidence: medium
evidence_basis: real_account_test
evidence_basis_details: "A deliberate pause/unpause with an observed outcome — the closest thing to a designed test in this corpus. Paused for ~3 days: 'day one after pausing this ad down, everything was great. Day two, results tanked. Day three tank. Day four tank. Day five, we launch it back on and things start to recover again.' N=1, no holdout, no control period, day-level reporting only, and the causal reading is his own: 'we can't prove that it's the first impression… I BELIEVE it is a supportive ad for that exact reason.' He states his own uncertainty explicitly."
evidence_strength: moderate
context_completeness: complete
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** medium · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** ⚠ **This cuts against DR's instinct and against several DR-adjacent heuristics.** DR's natural move when one ad eats budget at a poor CPA is to pause it. He tested exactly that and reports it made everything worse. But the test is N=1 at 100× DR's spend, and the effect he describes (an introduction ad feeding an ecosystem) requires an ecosystem — a campaign with enough concurrent ads for a halo to exist. DR may simply not have one. Record as a **caution against reflexive pausing**, not as a rule. The safer transfer is his own alternative: cap the ad set's share (C-8) rather than pause.

---

### C-8 · campaign_structure — Cap a runaway ad set's budget share instead of pausing it

```yaml
topic: campaign_structure
claim: When one ad set takes a dominant share of CBO spend at borderline performance, set a percentage maximum roughly 20 points below its current share rather than pausing it, forcing redistribution without destroying the ad set's learnings.
recommended_action: Use ad-set spending-limit MAXIMUM (percentage mode) as the kill switch of last resort; if an ad set is taking 80% of spend, cap at ~60%.
context: Client prospecting campaign, $196,000 spend / $326,000 revenue over 30 days, 31 ad sets, one taking 45% of spend.
business_type: ecommerce (subscription)
spend_level: "$196,000/30 days"
conversion_volume_context: null
research_question_ids: [C1, C4, B2]
question_link_origin: prospective
published_at: 2026-06-26
source_url: https://www.youtube.com/watch?v=NxaYt0ta00U
author: Sam Piliero
timestamp: null
confidence: medium
evidence_basis: operator_method
evidence_basis_details: "Demonstrated in a live account with real spend figures on screen, but presented hypothetically — he explicitly says 'let's say hypothetically this wasn't working as well.' No outcome is shown for having applied the cap. He also states there is no science to the percentage: 'There's no perfect science to the percentage threshold.'"
evidence_strength: weak
context_completeness: complete
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** medium · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** Directly addresses the concentration problem DR reports. The percentage-mode maximum is budget-agnostic, so it works at any spend. But at DR's level the campaign may contain too few ad sets for redistribution to have anywhere useful to go — capping the only ad set that spends does not produce a second one that performs. Useful once DR runs ≥3 concurrent packs; not before.

---

### C-9 · scaling — Graduated budget increases keyed to distance above target, checked across five windows

```yaml
topic: scaling
claim: Budget increase size should be a function of how far above target the account is — 5–10% when barely above, 20–30% when comfortably above, 50%+ when at roughly double target — and the decision should be checked across 30/14/7/3-day and yesterday windows, not one.
recommended_action: Before increasing budget, read ROAS at 30, 14, 7 and 3 days plus yesterday; scale only if the recent windows are also above target, and size the increase by the margin.
context: Live account at 8.46 ROAS on 30 days but 7.30 at 14 days and 6.94 at 7 days against an 8× target — used as an example of when NOT to scale.
business_type: ecommerce
spend_level: "$43,000/30 days in the account shown"
conversion_volume_context: null
research_question_ids: [C3, B3]
question_link_origin: prospective
published_at: 2026-08-03
source_url: https://www.youtube.com/watch?v=h1RGGrhU00I
corroborating_sources:
  - https://www.youtube.com/watch?v=Z4YWKO8T_3M   # 2026-07-11, same increments, "vertical scaling"
  - https://www.youtube.com/watch?v=yp6BtzVPWBE   # 2026-05-15, 20–30% every 3–5 days evergreen
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: operator_method
evidence_basis_details: "Consistent across three videos over three months. The multi-window check is demonstrated live and — usefully — demonstrated arriving at a DON'T-SCALE verdict, which is rarer and more credible than a highlight reel. No outcome data for the increments themselves."
evidence_strength: moderate
context_completeness: complete
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** The percentages are `PRACTITIONER_SPECIFIC` and carry ecommerce assumptions. **The multi-window check transfers cleanly and costs nothing** — and it is the more valuable half. DR's decision failure mode is reading one window and acting; requiring 30/14/7/3/yesterday agreement before a budget move is implementable today at any spend. The increments themselves should stay as `DR_HYPOTHESIS` at most, because at DR's conversion volume a 7-day window may contain too few conversions to read at all — which is exactly what Steiner's volatility statement (F-4) predicts.

---

### C-10 · scaling — Aggressive scaling test: +188% spend held ROAS flat over 12 days

```yaml
topic: scaling
claim: Tripling spend over a short window does not necessarily degrade efficiency; the perceived learning-phase penalty is largely new top-of-funnel impressions taking longer to convert.
recommended_action: null   # he does not prescribe tripling; he presents it as counter-evidence to stair-stepping
context: One brand, two consecutive 12-day evergreen periods.
business_type: ecommerce
spend_level: "$37,000 → ~$108,000 per 12-day period"
conversion_volume_context: null
research_question_ids: [C3, B3]
question_link_origin: prospective
published_at: 2026-01-28
source_url: https://www.youtube.com/watch?v=se8B4xOJHco
author: Sam Piliero
timestamp: null
confidence: medium
evidence_basis: real_account_example
evidence_basis_details: "Spend +188%, revenue +187.7%, ROAS change −0.01 from a 1.49 base, across two consecutive 12-day windows. ⚠ ASR DEFECT: the captions render the post-scale spend as '$19,000' while simultaneously describing a '$71,000 increase' from $37,000 — arithmetically the figure must be ~$108,000. The percentages are internally consistent and are the reliable part; the absolute dollar figure must NOT be quoted from this transcript. No control group; the comparison is period-over-period in a single account."
evidence_strength: moderate
context_completeness: partial
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** low · **principle_transfers:** partial · **implementation_transfers:** no
**reason:** ⚠ The strongest single data point in the corpus against learning-phase caution — and the least transferable. It is one account, at ~$3,000/day, in a business already at scale, with a 1.49 ROAS target that tolerates enormous variance. Steiner's volatility statement (F-4) implies the *opposite* prediction at DR's spend: less budget means more auction-driven variance, so a 3× jump at DR's level would be far noisier than at his. The principle that survives is narrow: **a ROAS dip immediately after a budget increase is not by itself evidence the increase was wrong** — impressions higher in the funnel take longer to convert. Nothing about the magnitude transfers.

---

### C-11 · measurement — Incremental attribution for creative selection, standard attribution for delivery

```yaml
topic: measurement
claim: Run 7-day click / 1-day engaged / 1-day view as the delivery attribution setting to maximise signal, but evaluate which creative to scale using the incremental attribution column.
recommended_action: Keep standard attribution on the ad set; add the incremental attribution comparison column and rank creative by incremental ROAS and incremental spend when deciding what to iterate on.
context: The most consistently repeated operational instruction in the corpus — present in over twenty of the sixty videos.
business_type: ecommerce
spend_level: "stated as applicable at every size, including 'a couple thousand dollars'"
conversion_volume_context: null
research_question_ids: [G1, G2, B2]
question_link_origin: prospective
published_at: 2026-03-06
source_url: https://www.youtube.com/watch?v=H2DpNyRpapE
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: operator_method
evidence_basis_details: "Method claim repeated across the corpus without variation. The supporting statistic is NOT his: in this video Josh, a Meta Director of Signal Growth, states on camera that incremental attribution drives 'a 24% increase in incremental conversions versus our standard attribution model,' built from 'thousands of conversion lift tests.' That figure is a vendor claim in a promotional interview — no methodology, sample, or confidence interval is published. It must be attributed to Meta, never to Piliero, and never repeated as an independent finding."
evidence_strength: moderate
context_completeness: complete
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** The split — optimise on the widest window, *judge creative* on the narrowest — is free, reversible, and requires no budget. It converges with Jon Loomer's independent use of incremental attribution. ⚠ **The DR caveat is conversion volume:** the incremental column is a model output, and at DR's conversion counts the incremental figure may be too sparse to rank anything. Meta's own guidance in this same interview is to prove it with a conversion lift test — which is available only to advertisers spending hundreds of thousands per month, i.e. not DR. DR can *look at* the column; DR cannot yet *decide* on it.

---

### C-12 · measurement — Leading-indicator ladder for accounts with too few purchases to read

```yaml
topic: measurement
claim: When purchase volume is too low to evaluate creative, read cost-per-link-click → cost-per-add-to-cart → cost-per-initiated-checkout → cost-per-purchase as a ladder; the lower the upstream cost, the better the eventual purchase economics.
recommended_action: Add cost per link click, cost per add to cart and cost per initiated checkout as columns alongside cost per purchase, and use them as proxies during periods with insufficient purchase data.
context: Presented as the way to tell whether scaled spend is moving down-funnel before purchases arrive.
business_type: ecommerce
spend_level: null
conversion_volume_context: "explicitly framed for periods when purchase data is too thin to judge"
research_question_ids: [G2, B2, B3]
question_link_origin: prospective
published_at: 2026-07-11
source_url: https://www.youtube.com/watch?v=Z4YWKO8T_3M
corroborating_sources:
  - https://www.youtube.com/watch?v=zo9evN1pVaM   # 2026-04-24, same ladder, "proxy metric"
author: Sam Piliero
timestamp: null
confidence: medium
evidence_basis: operator_method
evidence_basis_details: "Demonstrated in an account with the columns visible and the correlation asserted from the screen: 'the lower on average our cost per checkout initiated is, the better our return on ad spend is.' The correlation is stated, not measured — no coefficient, no sample, no counter-examples shown."
evidence_strength: weak
context_completeness: complete
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** ⭐ **This is the most directly useful measurement idea in the corpus for DR's actual constraint.** DR's core evaluation problem is that registrations are too infrequent to read at ad level within a decision window. A proxy ladder is precisely the right shape of answer. ⚠ **But it is his weakest-evidenced claim of the useful set** — an asserted correlation with no data — and DR's funnel is not an ecommerce cart funnel, so DR would have to define its own intermediate events (form start, form complete, schedule view) rather than inherit add-to-cart. Treat as a **method to design a DR test around**, not as a finding.

---

### C-13 · creative_strategy — Avatar × template = concept, and concepts are what the retrieval system matches

```yaml
topic: creative_strategy
claim: Post-Andromeda, an ad's targeting is determined by which avatar it calls out combined with the template/angle it uses; the resulting "concept" is what the retrieval system matches to an audience, and different concepts should be allowed to run concurrently at different scale/efficiency points.
recommended_action: Name and group ad sets by avatar and concept; keep every concept running that clears the target efficiency metric, regardless of how little it can spend.
context: Framework introduced Feb 2026 and used as the organising principle of every subsequent video.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [D1, D2, D4, A2]
question_link_origin: prospective
published_at: 2026-02-13
source_url: https://www.youtube.com/watch?v=zBbLFPBUSXM
corroborating_sources:
  - https://www.youtube.com/watch?v=LQMY3SGPO1w   # 2026-05-21, real-account outcome
  - https://www.youtube.com/watch?v=nZmTmIVApmY   # 2026-06-04, Meta's own description of retrieval
author: Sam Piliero
timestamp: null
confidence: high
evidence_basis: real_account_example
evidence_basis_details: "The framework itself is a model, not a finding. The one real-account outcome attached: LQMY3SGPO1w reports +83% purchases at <1% spend increase over 3 weeks in an evergreen April period, with cost per purchase down 45%, attributed to going deep on avatars identified via post-share concentration. Single account, single change claimed, no control, figures read from screen. The mechanism half — that retrieval matches ads to people at the individual ad level — is independently corroborated by Matt Steiner in nZmTmIVApmY, which is the strongest support any creative claim in this panel has."
evidence_strength: moderate
context_completeness: complete
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** The organising principle — build creative around a named person with a named problem, and let several such concepts coexist at different scale points — costs nothing and is the single most repeated idea in the current-tier panel. DR has obvious distinct avatars (the parent chasing structure, the parent chasing skill development, the parent solving childcare logistics). ⚠ Two DR frictions: (1) DR's avatars are **parents buying for children**, so the person called out in the ad and the person the product serves differ, which none of his examples cover; (2) running many concepts concurrently requires enough budget for each to clear a delivery floor — the same precondition that gates C-1.

---

### C-14 · campaign_structure — At small scale the whole system is two campaigns, and one real account improved by shrinking

```yaml
topic: campaign_structure
claim: The core structure is only two campaigns — prospecting CBO and retention — with retargeting and scale campaigns added later and conditionally; a small account improved materially by consolidating rather than expanding.
recommended_action: Build prospecting CBO + retention only. Add a retargeting campaign only when the audience-segment breakdown shows engaged spend approaching prospecting spend.
context: Fashion brand, $14,000 spend over 30 days.
business_type: ecommerce (fashion)
spend_level: "$14,000/30 days ≈ $470/day"
conversion_volume_context: null
research_question_ids: [C1, F1]
question_link_origin: prospective
published_at: 2026-07-05
source_url: https://www.youtube.com/watch?v=TIs3ID-9a3o
corroborating_sources:
  - https://www.youtube.com/watch?v=FYUR8ZL4_xY   # 2026-03-15, "retargeting campaign is now optional"
author: Sam Piliero
timestamp: null
confidence: medium
evidence_basis: real_account_example
evidence_basis_details: "0.63 → 1.40 ROAS month over month (+121%), with active ads cut 165 → 62. He states explicitly that no sale ran, no new products launched, and no new ads were made — the change was structure plus breakdown-driven reallocation. ⚠ CONFOUNDED: he names at least three simultaneous changes (M4 structure, ad consolidation, and reallocation across placement/age/gender/day-of-week breakdowns). The 121% cannot be attributed to any one of them. Prior-period baseline is given twice and inconsistently — '0.63' in one sentence, 'a 0.7 or 0.6' in another."
evidence_strength: moderate
context_completeness: partial
platform_validation_status: UNVALIDATED
```

> "This is a condensing down of the account, and I know that goes against what almost everybody says all the time, that we need more ads, we need more ads, we need more ads."

**applicability_to_DR:** high · **principle_transfers:** yes · **implementation_transfers:** partial
**reason:** ⭐ **Closest account in the entire panel to DR's situation** — small, previously unprofitable, improved by *simplifying*. It is direct counter-evidence to the "more campaigns, more ads" default that DR has been pulled toward, from the same practitioner who spent the previous six months arguing for volume. `implementation_transfers: partial` only because it is ecommerce with a purchase-event pool DR does not have; the retention campaign half of the two-campaign core is not currently buildable for DR. **For DR, the core is one campaign, not two** — and that is a narrowing he himself sanctions for businesses without an existing-customer base (`Fo-p03fwvdA`, the under-$3,000/month tier).

---

## Real-account evidence in this corpus

Six items rise above method assertion. All are self-reported, none are exported or third-party verified.

| Video | Date | What was shown | Design | Strength |
|---|---|---|---|---|
| `cWTzsftTb_Y` | 2025-11-19 | Pause/unpause of a supportive ad; results tanked days 2–4, recovered on relaunch | Deliberate intervention, N=1, no control | moderate |
| `se8B4xOJHco` | 2026-01-28 | +188% spend, +187.7% revenue, ROAS −0.01 over 12 days | Period-over-period, N=1 | moderate |
| `S3bybSKk4Ok` | 2026-03-01 | Geo expansion: $8k→$141k/mo, 2.60→2.07 ROAS, 10→36+ countries over 6 months | Longitudinal, N=1, BFCM excluded | moderate |
| `6P9F943jkUY` | 2026-03-20 | Placement CPM shift across ~100 brands / ~$70M spend: IG Reels CPM −9% while Feed +24.3%, IG Stories +12.1%, FB Reels +25.5% | Aggregated multi-account, no methodology published | moderate |
| `LQMY3SGPO1w` | 2026-05-21 | +83% purchases at <1% spend increase, CPP −45%, over 3 weeks | Single change claimed, N=1, no control | moderate |
| `TIs3ID-9a3o` | 2026-07-05 | 0.63→1.40 ROAS with ads cut 165→62 at $14k/mo | N=1, confounded (≥3 changes) | moderate |

Nothing in this corpus reaches `strong`. The ceiling is a single-account before/after with the operator's own causal reading.

---

## Contradictions

**Within this author (all preserved, none resolved):**

1. **Creative volume.** Nov 2025 "more ads are better" → Aug 2026 "volume of creative does not matter." Resolved by him *in favour of quality*; recorded as evolution, not as a live contradiction. See F-1.
2. **Flexible ads.** Dec 2025 bullish → Feb 2026 reversed → Apr 2026 deprecated by Meta. See F-2.
3. **Testing method.** M3 (launch and let the CBO decide) → M4 (force a 7-day minimum on every new pack). He names the reversal explicitly. See F-3.
4. **Languages setting.** `S3bybSKk4Ok`: never leave it on All Languages. `TIs3ID-9a3o`: translate to all to expand reach. Reconcilable in principle, never reconciled by him.
5. **Retargeting campaigns.** Dec 2025: a required part of the four-campaign structure. Mar 2026 onward: optional, gated on an audience-segment trigger. His Phase 2 disagreement with Jon Loomer has therefore narrowed from the Loomer side without either party citing the other.

**Against Meta, inside his own video:** `nZmTmIVApmY` — Matt Steiner tells him that creating an extremely large number of creative variations *"probably isn't going to help you more than having a reasonable diversity of ads."* Piliero does not push back and does not reconcile it with the rule of 10,000 he was still publishing at the time. He adopts the position seven weeks later without attribution.

**Against other panel members:**

- **vs Jon Loomer — customer lifecycle strategy.** Loomer debunks it (the only `moderate`-strength claim in his file, and it is a debunk). Piliero uses the field routinely — but only as the exclusion UI, never as an optimisation lever. **Not a real disagreement**; they are describing different uses of the same control.
- **vs Andrew Foxwell corpus / Brad Ploch — CTR as a kill metric.** Ploch: never kill on CTR, no correlation with performance. Piliero: CTR-all is a warning signal for engagement-driven overspend (`cWTzsftTb_Y`) and the CPC/CTR ladder is a leading indicator (C-12). Live, unresolved, neither presents data.
- **vs Dara Denney — dedicated testing campaigns.** Denney describes a funded dedicated testing campaign ($1,000/day, $100–200/ad set/day). Piliero explicitly rejects dedicated testing budgets as "creating cost centers." **This is a genuine method disagreement between two `VETTED_OPERATOR` sources at different scales**, and it should be carried into any DR testing-structure decision rather than silently resolved.

---

## Open questions from this author (Phase 3)

1. **UNRESOLVED — does removing an ad-set spending minimum reset learning?** Phase 2 flagged this as the file's highest-value validation item. The full corpus supplies more assertions but no evidence: *"It's not going to reset your learnings. It's not going to do anything crazy"* (`6P5M8yvXx1g`, 2026-07-26) and *"You don't worry about the learning phase or resetting anything"* (`TIs3ID-9a3o`, 2026-07-05), plus similar phrasing in `Uus6i9Gn6m0` and `L83waCBHBwU`. Asserted at least four times across five months, **never once with data**. Meta's own `significant-edits` documentation says edits to a live ad set are significant. Per the brief, this is **not resolved here** — it goes to the platform-validation queue as the top item. It matters because the entire M4 method depends on it being true.
2. **RESOLVED (Phase 2 #2) — his smallest demonstrated account.** ~$260/day at 6.94 ROAS, plus a $470/day turnaround, plus explicit $100/day arithmetic. His system does have a stated small-budget form. See F-5.
3. **NARROWED (Phase 2 #3) — Loomer vs Piliero on retargeting campaigns.** Piliero has moved to "optional, trigger-gated." The remaining disagreement is about the trigger, not about the principle.
4. **NEW — does the 20% testing cap behave the same at $10/day as at $1,000/day?** He asserts the arithmetic scales and then warns in the same corpus that the mechanism "might not have the flexibility" at small budgets. He never resolves it. At DR's scale a 20% cap may be below any delivery floor, in which case the rule is arithmetically valid and operationally void.
5. **NEW — is post-share concentration a usable proxy for DR?** `LQMY3SGPO1w` and `H_jfsgGJc4c` both make shares the primary pre-conversion signal. DR's category (youth sports programmes, parent audiences, local) is plausibly high-share. Cheap to check in DR's own breakdowns; no spend required.
6. **NEW — how much of the ~$70M placement CPM dataset is portable?** `6P9F943jkUY` is the only aggregated multi-account dataset in the entire panel. If Instagram Reels CPMs really fell ~9% while every other placement rose 12–25%, that is a materially different placement economics picture than DR is likely assuming. No methodology is published and the accounts are all ecommerce. Worth one DR-side check against DR's own placement breakdown before anything is concluded.

## What must NOT be carried into DR from this file

- **The rule of 10,000** — retired by its own author.
- **Cost caps, bid caps, target ROAS** — he states repeatedly and unambiguously that these are not applicable below roughly $100,000/month.
- **The 24% incremental-attribution figure** — a Meta marketing claim, not an independent finding; attribute to Meta or do not use it.
- **Any absolute dollar figure from `se8B4xOJHco`** — the captions are arithmetically broken (see C-10).
- **The four-campaign structure** — superseded by his own two-campaign core, and DR cannot build the retention half.

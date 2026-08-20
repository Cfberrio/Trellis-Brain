---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: framework
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/wave-2a-campaign-architecture-framework.md"
repo_path: domains/ads/meta/intelligence/output/wave-2a-campaign-architecture-framework.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/framework
  - discipline-rift
aliases:
  - "Wave 2A"
  - "Campaign Architecture Framework"
---

# Wave 2A — Campaign Architecture Framework for DR

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1B-Volume-and-Budget|Wave 1B — volumen y presupuesto]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Wave 2B — método creativo]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-Structure-Full-Method|Método completo de estructura DR]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/output/wave-2a-campaign-architecture-framework.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Date:** 2026-08-14 (task dated 2026-08-13; run executed across the date boundary — capture dates in evidence files are the authority)
**Questions:** C1 (campaign count) · C2 (budget placement) · C3 (testing/scaling separation) · C4 (revisit triggers)
**Knowledge level:** **DR HYPOTHESIS.** Built from PLATFORM FACT + EXTERNAL PRACTITIONER CLAIM + DR context facts. **Nothing here is proven for DR.** No campaign, ad set, ad, budget, targeting, placement, Pixel or CAPI setting has been changed or created.
**Inherits:** `wave-1a-event-framework.md` (conditional objective) · `wave-1b-volume-budget-framework.md` (volume/budget reality, Stage-1 DR system check)
**Hands to:** Wave 2B (D1–D4 creative operating method) — see §11 input contract

---

## 0. Executive answer

**The most defensible initial CAMPAIGN-LEVEL architecture for DR today is a single campaign, with budget kept where it already sits (ad set level), and no separate testing and scaling campaigns.**

**Scope boundary, stated up front:** this wave answers *campaign-level* structure. It does **not** decide how new creative should be introduced at the ad-set level — whether into the existing ad set or via another ad set. That is **D1, which remains OPEN**, and Wave 2A deliberately does not pre-answer it.

The most valuable output of this wave is again a **prohibition rather than a build** — at campaign level. Every *campaign-level* elaboration available (second campaign, scale campaign, retargeting campaign, campaign-level budget allocation) either requires a condition DR does not meet or divides signal DR does not have.

```text
Campaign count:                          1
Campaign role(s):                        single acquisition campaign — no role split
Ad-set current state:                    1 ad set (last-known structure — a starting state, not a cap)
Budget strategy:                         keep ad set budget for now (no change justified today)
Testing/scaling structural relationship: no separate testing and scaling CAMPAIGNS
Ad-set-level creative introduction:      NOT DECIDED HERE — owned by D1 (Wave 2B)
Current confidence:                      C1 HIGH · C2 MEDIUM (low-stakes) · C3 HIGH · C4 MEDIUM
Knowledge level:                         DR HYPOTHESIS
```

**One honest qualifier on C2.** At one ad set, the budget-placement decision is **largely inert** — Meta's own criteria for choosing between the two modes are all comparisons *between* ad sets, and there is no second ad set to compare. The recommendation is a tiebreak on optionality, not a performance claim, and it should not absorb further analysis until a second ad set actually exists.

---

## 1. DR constraints inherited from Wave 1

Only the constraints that materially bind architecture:

| Constraint | Source | Architectural consequence |
|---|---|---|
| Very thin historical delivery — **metric-specific, not interchangeable**: ~9 **landing page views** in one referenced 30-day window; ~10–11 **clicks** across the reported historical windows (all-clicks vs outbound-clicks differ between extracts) | DR extracts, Wave 1B §2 | Any structural split divides an already-thin signal. **Do not collapse LPVs, clicks, registrations and purchases into one "event" count** |
| No defensible registration CPA exists — **registration-level Meta signal is unmeasured in the available extracts** (no registration/purchase action appears in the referenced exported `actions` arrays). This is **not** proof that paid registrations did not occur | Wave 1B §2 | Cannot size, justify, or trigger any structure by CPA |
| Historical spend ~$2.70–3.70/day — **context, not a confirmed current budget** | Wave 1B; DR extracts through 2026-05-12, campaign PAUSED | Architecture must not assume today's budget is either that figure or a larger one |
| Objective is campaign-level and **cannot be changed after publish** | `campaign-objectives-and-optimization-events.md` | Campaign count is forced upward only by needing two objectives at once |
| **Wave 1A objective/event selection remains conditional and unresolved** (A1 RESEARCHING · A2 REOPENED · A3 REOPENED). Wave 2A does **not** settle it | Wave 1A §B | Architecture is checked for invariance across the currently legitimate branches — see §10 |
| Optimization-event ladder is deliberately mobile (R0/R1/R3) | Wave 1A §C | A future second ad set may legitimately need a *different* performance goal |
| ~50 events/week is a hedged reference, not a cliff; 10× is a heuristic | `learning-limited.md`, `learning-phase.md`, Wave 1B §1–2 | No architecture trigger may be built on either number |
| Geo-constrained (Orlando), parent purchaser, child participant 6–12, paid season registration, seasonal windows | DR domain CLAUDE.md | Geography must be enforced by settings; seasonality creates a real future budget-isolation motive |

---

## 2. C1 — Campaign count

### C1 CURRENT RECOMMENDATION
**One campaign.** Do not create a second.

### Platform facts
- Meta's consolidation direction is documented across three pages already on file: *"Combining ad sets and campaigns will help you get the results you need faster, which means you'll see stable results sooner"*; *"Avoid high ad volumes… By combining similar ad sets, you also combine learnings"*; plus documented minimum daily budgets that penalise splitting a small budget.
- **Meta never states that one campaign is sufficient, and names no correct campaign count.** Recorded explicitly in `campaign-budget-and-consolidation.md §What Meta does not state`. Consolidation-as-direction and one-campaign-as-rule are different statements and are not merged here.
- The objective is set at campaign level and *"You cannot change your published campaign objective"* — so **needing two objectives simultaneously is the one platform-forced reason to hold two campaigns.** DR needs one.
- Four of Meta's five named learning-limited causes (small audience, low budget, infrequent optimization event, too many ads) already describe DR by construction. Splitting budget worsens several at once.

### Practitioner evidence
- **Nick Theriot** — one campaign for testing and scaling (`experience_claim`, weak, ecommerce, `PARTIALLY_SUPPORTED`). Reused; not re-ingested; not counted as new evidence.
- **Sam Piliero** — four-campaign separation (`self_reported_case_study`, moderate, ecommerce, $1,000/day worked example). Reused; not re-ingested.
- **No new independent practitioner evidence was ingested for C1.** Discovery produced only SEO/content-farm material (§9) asserting campaign counts ("2–4 active campaigns", "consolidate if you can't fund 50 conversions per ad set") with no methodology, no author accountability, and in one case a fabricated numeric rule. Rejected under `CLAUDE.md §Source quality` and the numeric-threshold rule.

### Conflict
Sam vs Nick remains **unresolved as a general question and is not resolved here.** It is resolved *for DR* by context, not by vote: Sam's architecture is scoped to a $1,000/day account with a mature winner pool and a retention audience; Nick's is scoped to accounts with enough test volume for a 10% survival rate to mean something. **DR matches neither environment.** What decides DR is its own volume against Meta's own consolidation guidance — both practitioners' *environments* are 30–370× DR's spend.

### DR transferability
- **Similarities to both sources:** none material at the structural level. Both are ecommerce with volume DR does not have.
- **Differences:** single metro, single service line, single objective, one ad, seasonal registration windows, no purchase-event pool, no winner pool.
- **Principle transfers** (fragmenting a thin signal degrades learning): yes.
- **Implementation transfers** (Sam's four campaigns): no. (Nick's one campaign): yes — but note DR arrives there from Meta's consolidation logic plus its own volume, *not* by adopting Nick's authority.

### C1 ALTERNATIVE(S) REJECTED FOR NOW
| Alternative | Where it is rational | Why it does not transfer today | What would make it relevant |
|---|---|---|---|
| Four-campaign separation (prospecting / scale / retargeting / retention) | High-spend ecommerce with a winner pool and a purchase-based retention audience | Every cell would be starved; DR has no retention or retargeting pool to build from | Sustained volume plus a real warm pool — F1, currently DEFERRED |
| Two campaigns to run two objectives in parallel (e.g. Sales vs Leads head-to-head) | Accounts with enough volume to power two simultaneous reads | Halves an already-insufficient signal; Wave 1B shows DR cannot power one read, let alone two | Volume sufficient for two interpretable reads — no defensible number exists |
| One campaign per school / per sport | Businesses whose segments need genuinely different settings and budgets | Multiplies structures against a fixed thin budget; school-level geo is an ad-set/targeting question (E3), not a campaign question | E3 evidence that per-school geo cannot be enforced within one ad set |

### KEY UNCERTAINTY
Whether DR's seasonal registration windows will eventually create a legitimate need to isolate a stable in-season campaign from experimentation. That is a real motive (see C3) and it is currently **hypothesis, not evidence**.

### REVISIT TRIGGER(S)
See §5 registry — triggers T1, T7, T8.

### STATUS
**ENOUGH_EVIDENCE** — for the current decision. Meta's mechanics are understood first-hand, the practitioner conflict is characterised rather than voted on, and no additional credible source is likely to change "one campaign" for an account at DR's volume with one objective and one service line. Reopens on the §5 triggers.

---

## 3. C2 — Budget placement (Advantage+ campaign budget vs ad set budgets)

### C2 CURRENT RECOMMENDATION
**Keep the ad set budget for now.** This is a **KEEP / no-unnecessary-change decision**, not a performance finding.

It does **not** mean: ABO wins · ABO performs better · small budgets should use ABO · Meta recommends ABO for DR. **Meta publishes no performance claim for either mode**, and nothing here establishes one.

The reasoning is simply: DR has one ad set, campaign-level allocation has no second ad set to allocate toward, and **no demonstrated benefit justifies changing the budget mode today.**

### Current Meta mechanics (retrieved first-hand 2026-08-14 — `campaign-budget-and-consolidation.md`)

**What Advantage+ campaign budget actually does:**
> *"automatically manages your campaign budget across ad sets… This budget continuously distributes in real time to ad sets with the best opportunities."*

Its entire documented function is **allocation between ad sets**. Meta opens the page with: *"Advantage+ campaign budget is best suited for campaigns with at least 2 ad sets."*

**What ad set budget actually does:** Meta's own stated goals, verbatim — *"You want to control the amount spent on each ad set. The value of your ad sets differs greatly… You have a large difference in audience size between your ad sets. You have mixed optimization goals or bid strategies."* Benefit: *"More control in delivery."*

**What Meta supports:** a fit list for each mode, based entirely on relationships *between* ad sets.
**What Meta does NOT claim:** that either mode performs better. No performance comparison is published, and Meta appends its own disclaimer that opportunity score *"does not reflect your actual or future performance."* **Any "CBO beats ABO" or "ABO is better for testing" claim is not sourced from Meta.**

### SINGLE-AD-SET INTERPRETATION (DR today)

Separating the dimensions, as required:

| Dimension | With exactly one ad set | Verdict |
|---|---|---|
| **Allocation effect** | Nothing to allocate between; A+CB's documented function has no object to act on | **MOOT** |
| **Control effect** | A campaign budget with one ad set and an ad set budget are the same dollar reaching the same place | **MOOT** |
| **Configuration effect** | A+CB's uniformity constraints (common budget type, bid strategy, delivery; common performance goal under Highest Volume) bind nothing when there is one ad set | **MOOT today, real later** |
| **Future architecture effect** | The constraints bite the moment ad set #2 exists — especially if #2 needs a different performance goal, which Wave 1A's mobile ladder makes plausible | **MATERIAL** |
| **Operational simplicity** | A+CB is marginally simpler to manage; at one ad set the difference is negligible | **NEGLIGIBLE** |
| **Readability** | A+CB pushes evaluation to campaign level; at one ad set both levels are the same number | **MOOT today, cost later** |

**So the honest answer to "is this decision materially important today?" is NO** — on the two dimensions that normally decide it (allocation, control), one ad set makes them identical. It matters only through the future-architecture dimension.

**Why "keep" is the defensible call:**
1. **The primary reason is the absence of a reason to change.** A+CB's only documented benefit is cross-ad-set allocation, and Meta itself scopes the mode to campaigns *"with at least 2 ad sets"* — a condition DR does not meet. Changing modes today would buy nothing documented.
2. **Whether switching budget mode is a significant edit is not established** (`campaign-budget-and-consolidation.md §What Meta does not state`). An unknown-cost change with no documented benefit is not worth making.
3. *Secondary, contextual only:* keeping ad set budget also preserves the option of a future second ad set on a different performance goal, which Wave 1A's mobile ladder makes plausible. The claim that A+CB prohibits that under Highest Volume bidding is **practitioner-sourced (Loomer, `PARTIALLY_SUPPORTED`, weak evidence)** — Meta corroborates the direction via *"mixed optimization goals or bid strategies"*, but the hard eligibility requirement was not retrieved first-hand. **This is supporting context, not the reason for today's decision.**
4. *Secondary:* Meta routes hard per-ad-set budget requirements toward ad set budgets rather than campaign-budget spend limits — relevant only once a second ad set exists.

**No evidence claims either mode will deliver better for DR.** Points 3 and 4 describe future optionality; point 1 is the decision.

### MULTI-AD-SET INTERPRETATION (what changes when ad set #2 exists)

| Factor | Favors Advantage+ campaign budget | Favors ad set budgets |
|---|---|---|
| Automatic allocation | Yes — its documented purpose | — |
| Intentional budget isolation | — | Yes; Meta names per-ad-set control as the reason |
| Similar audience sizes | Required for sensible A+CB behavior (Meta: large size differences → use ad set budgets) | Handles dissimilar sizes |
| Mixed performance goals / bid strategies | Blocked (practitioner-sourced; Meta-corroborated in direction) | Yes — Meta's own stated criterion |
| Readability at low volume | Worse — pushes reads to campaign level | Better — preserves per-ad-set reads |
| Fragmentation risk | Lower (one budget) | Higher if budgets are set below workable levels |

**Decision rule when ad set #2 arrives:** if both ad sets share the same performance goal, bid strategy and roughly similar audience sizes, A+CB becomes the better-fitting mode by Meta's own criteria. If they differ on any of those — or if DR needs a guaranteed floor for one of them — ad set budgets fit better. **Do not pre-commit; the answer depends on what ad set #2 is for.**

**Do not treat this as a permanent CBO-vs-ABO binary.** Meta already names a **third** mode, `ad set budget sharing`, which this run did not capture. When T2 actually fires, re-evaluate **all then-current Meta budget options** rather than the two discussed here — the feature set on the day of the decision governs, not this file's snapshot. Do not research that mode now; it is inert while one ad set exists.

### Practitioner evidence
- **Jon Loomer**, *Advantage Campaign Budget Best Practices* (2023-06-28, updated 2025-03-01) — **newly ingested this run, 5 claims, all C2.** Evidence quality is low throughout: 3 `experience_claim`/weak, 2 `opinion`/none. No spend, client, or volume context disclosed anywhere. Validation outcomes: 3 `PARTIALLY_SUPPORTED`, 1 `INSUFFICIENT_EVIDENCE` (an unsourced "two-hour re-adjustment period" — quarantined, do not cite), 1 `NOT_APPLICABLE`.
- **Critically: neither Loomer article addresses the single-ad-set case at all.** Every claim assumes multiple ad sets. The source that most directly covers C2 does not reach DR's actual configuration — recorded as a gap, not papered over.
- Sam and Nick both *assume* CBO inside their structures without arguing for it against ABO; neither is evidence on this axis.

### DR transferability
Loomer's principle (match budget mode to whether ad sets need to differ) **transfers cleanly and is scale-independent** — it is a fit rule, not a budget tactic. His implementations are scoped to multi-ad-set campaigns and therefore **do not reach DR today**. `principle_transfers: yes` / `implementation_transfers: partial`.

### UNCERTAINTY
1. Whether switching modes on a live campaign resets learning — **unknown, and it is the uncertainty that most affects how cheap this decision is to revisit.**
2. Whether the A+CB eligibility constraints are exactly as Loomer states — first-party retrieval failed to cover it this run.
3. `ad set budget sharing` — a third mode Meta names and this run did not capture.

### REVISIT TRIGGER(S)
§5 registry — triggers T2, T3, T4, T6.

### STATUS
**ENOUGH_EVIDENCE (conditional).** Sufficient to parameterize Wave 2B: Meta's decision criteria are now first-hand, the single-ad-set case is resolved as largely inert, and the multi-ad-set rule is stated conditionally. It is **not** saturated as a general question — the three uncertainties above are real and two are cheap first-party retrievals when they become decision-relevant.

---

## 4. C3 — Testing / scaling separation

### C3 CURRENT RECOMMENDATION
**No separate testing and scaling CAMPAIGNS.**

> **Scope limit — read this before using C3 anywhere.** C3 answers the **campaign-level** question only. It does **not** establish that all creative testing must happen inside the existing ad set. Whether new creative should enter the existing ad set or a new one is **D1, which remains OPEN**, and Meta's significant-edit mechanics make that a genuine question rather than a formality. Wave 2A must not be cited as having settled it.

### RECOMMENDATION FOR DR NOW — why
DR fails every precondition a *campaign* separation would serve:
- **No winner pool.** One ad exists. A scale campaign is a container for proven winners; DR has nothing to put in it.
- **Very thin delivery to divide.** ~9 landing page views in one referenced 30-day window and ~10–11 clicks across the reported windows. A second campaign divides that.
- **No differentiated operational need today.** The campaign is paused; there is no live in-season delivery requiring protection from experimentation.
- **No measured downstream signal to protect.** Registration-level Meta signal is unmeasured in the available extracts — which is a reason a split cannot be evaluated, not a finding that registrations never happened.

### EXISTING SAM/NICK CONFLICT
Direct and unresolved in general: Sam runs a dedicated scale campaign seeded by duplicated winners ranked on incremental attribution; Nick rejects the split outright. Both ecommerce, both weakly evidenced on this specific axis (`experience_claim`, weak). **Not resolved by preference or by vote.** Sam's method has an explicit precondition — enough ads with meaningful spend to rank — that DR does not meet, so his recommendation is not applicable rather than wrong. That is the honest resolution: **the conflict is real but currently inert for DR.**

### NEW INDEPENDENT EVIDENCE
**None.** No credible independent practitioner source on testing/scaling separation scoped to low-volume or local accounts survived pre-screen (§9). Recorded as honest absence.

### PLATFORM MECHANICS THAT MATTER
- Consolidation guidance (three pages) points against splitting at low volume.
- `significant-edits.md`: *"Any change to ad creative"* and *"Adding a new ad to your ad set"* are always-significant edits that reset that ad set's learning. **This is the mechanism that will eventually create a genuine separation motive** — experimentation inside a structure carrying live seasonal demand is not free.
- Also from `significant-edits.md`: under Advantage+ campaign budget, adding a new ad set does **not** reset existing ad sets. Relevant later; not a reason to separate now.
- Meta says nothing about testing-vs-scaling structure. **Silence, not endorsement, in either direction.**

### WHAT IS BUSINESS-LOGIC VS PLATFORM-FACT
- **PLATFORM FACT:** creative changes/additions reset ad-set learning; consolidation combines learnings; Meta publishes no separation guidance.
- **BUSINESS LOGIC (DR HYPOTHESIS):** that DR's seasonal registration window creates a future need to protect in-season delivery from experiments. Derived from the platform fact plus DR's seasonality — **not stated by Meta and not tested by DR.** Labeled as hypothesis wherever it appears.

### CONDITIONS THAT COULD MAKE SEPARATION USEFUL LATER
1. A genuine winner pool exists — more than one ad with repeatable results at meaningful spend.
2. Event volume high enough that splitting does not starve either structure (**no defensible numeric threshold found**; observable proxy is whether the existing structure delivers stably in Meta's sense).
3. An in-season window where resetting learning would cost real registrations, while creative testing still needs to continue — the strongest DR-specific motive.
4. A second objective becomes necessary (forces separation via C1 regardless).
5. A budget-control requirement that campaign-level allocation cannot express.

### WHAT DOES NOT YET JUSTIFY SEPARATION
- A practitioner running one ("Sam does it").
- Wanting to "test properly" while holding one ad and single-digit weekly events.
- Learning-limited status — Meta: *"Learning limited isn't a penalty."*
- Any spend figure copied from an ecommerce playbook.
- Reaching or missing ~50 events/week or the 10× budget reference — **neither is an architecture trigger.**

### STATUS
**ENOUGH_EVIDENCE** — the decision for DR now is well-supported (all preconditions fail), the general conflict is characterised rather than falsely settled, and the future conditions are stated observably. Reopens on §5 triggers T5, T6, T7.

---

## 5. C4 — Architecture trigger registry

| Current decision | Keep while… | Reopen when… | Observable evidence | Evidence basis |
|---|---|---|---|---|
| **T1 · C1: one campaign** | DR runs one objective, one service line, one metro | DR genuinely needs **two campaign objectives running at once** | A second objective is required by a business decision (e.g. running Leads→Website alongside Sales→Website) — objective is campaign-level and immutable after publish | **PLATFORM FACT** (`campaign-objectives-and-optimization-events.md`) |
| **T2 · C2: ad set budget** | Campaign contains exactly one ad set | A **second ad set exists** | Ad set count ≥ 2 in Ads Manager | **PLATFORM FACT** — Meta: A+CB *"best suited for campaigns with at least 2 ad sets"* |
| **T3 · C2: ad set budget** | Ad sets (if >1) would share performance goal and bid strategy | Two ad sets need **different performance goals or bid strategies** | The intended configuration of ad set #2 differs on either field | **PLATFORM FACT** (Meta lists *"mixed optimization goals or bid strategies"* as an ad-set-budget criterion) + **PRACTITIONER** (Loomer, `PARTIALLY_SUPPORTED`) |
| **T4 · C2** | Ad set audiences are comparable in size | Ad sets differ **greatly in audience size** | Ads Manager audience-size estimates diverge materially | **PLATFORM FACT** — Meta names this as an ad-set-budget criterion |
| **T5 · C3: no separation** | One ad, no repeatable performers | A **winner pool exists** — several ads with repeatable results at meaningful spend | Multiple ads accumulating spend with consistent relative performance across more than one window | **PRACTITIONER** (Sam's own stated precondition) + **DR CONTEXT**. **No numeric threshold found or invented** |
| **T6 · C2 + C3** | Nothing in-flight is worth protecting | An **in-season window** exists where a learning reset would cost real registrations while testing must continue | An active registration window with live delivery producing registrations | **PLATFORM FACT** (significant edits reset learning) + **DR HYPOTHESIS** (seasonality creates the motive) |
| **T7 · C1 + C3 — CAPACITY TO SUPPORT INDEPENDENT STRUCTURES** | Splitting the account would leave one or both proposed structures without enough sustained budget or signal to produce useful independent reads | DR has sustained budget, delivery and downstream signal such that each proposed structure could **operate and be evaluated independently without obviously starving the other** | Sustained delivery across multiple windows · enough event flow to compare structures honestly · enough budget to fund each proposed structure · evidence that the consolidated structure has a genuine constraint separation would solve | **DR CONTEXT** + **PLATFORM FACT** as supporting context only. **Learning-phase status and ~50 events/week are NOT the trigger** — they may inform the picture, never decide it. No event/week or dollar/day threshold is set |
| **T8 · C1 — MATERIAL MULTI-MARKET DIVERGENCE** | New locations can be represented cleanly inside the existing campaign architecture | Expansion beyond the current market creates a **materially independent campaign-level requirement** — e.g. separate budget control, a separate season/calendar, a materially different offer, a separate objective, or delivery constraints that cannot be expressed in the existing structure | The specific divergent requirement, named, and why the current architecture cannot carry it | **DR CONTEXT FACT**. **Launching another city or school does NOT by itself create another campaign** — geo/targeting implementation belongs to E3 |

**Explicitly NOT triggers:** hitting or missing ~50 optimization events/week; exiting the learning phase or losing the "Learning limited" badge; hitting or missing Meta's 10× budget heuristic; reaching any dollar/day figure quoted by any practitioner. **None of these is a sufficient architecture gate on its own** — Meta itself hedges the first two (*"Learning limited isn't a penalty"*, exit is *"as soon as they can deliver stably"*) and the third is explicitly a rule of thumb. They may serve as supporting context inside T7; they never decide it.

**When NOT to revisit architecture:** if none of T1–T8 is observable, architecture is settled and the answer is to work on message, offer-fit, tracking and geo accuracy instead. This registry exists to stop monthly relitigation.

---

## 6. Evidence matrix

| Recommendation | PLATFORM FACT | EXTERNAL PRACTITIONER CLAIM | DR CONTEXT FACT | DR HYPOTHESIS |
|---|---|---|---|---|
| One campaign | Consolidation guidance ×3 pages; objective is campaign-level and immutable; learning-limited causes | Nick (one campaign, weak); Sam (four campaigns, moderate) — **conflicting, unresolved** | 1/1/1 today; ~$2.70–3.70/day historical; single objective, single metro | That one campaign remains right as DR grows — untested |
| Ad set budget | A+CB *"best suited for… at least 2 ad sets"*; Meta's ad-set-budget criteria; **no performance claim for either mode** | Loomer (5 claims, weak/none; 3 PARTIALLY_SUPPORTED, 1 INSUFFICIENT_EVIDENCE, 1 NOT_APPLICABLE) | One ad set exists | That preserving per-ad-set optionality will matter — untested |
| No testing/scaling split | Significant-edit mechanics; consolidation; **Meta silent on separation** | Sam yes / Nick no — conflicting, both ecommerce, both weak on this axis | One ad, no winner pool, no live delivery | That seasonality will later justify separation — untested |
| Trigger registry | T1–T4 anchored in first-party text | T5 anchored in a practitioner's own precondition | T7, T8 anchored in DR context and structure facts | T6's seasonal motive |

**Nothing in this table crosses levels.** No practitioner agreement was promoted to platform fact; no platform mechanism was promoted to a DR operating rule; no DR context fact was treated as proof that an architecture works.

---

## 7. Principle vs implementation

| # | External idea | Principle | Transfers? | Implementation | Transfers? | Why |
|---|---|---|---|---|---|---|
| 1 | Sam: four-campaign separation | Don't let cold, warm and retention compete for one budget | **partial** — sound where multiple genuine audiences exist | Build four campaigns with exclusions | **no** | Assumes $1,000/day and a retention pool; four cells at DR's spend starve all four |
| 2 | Nick: one CBO for testing + scaling | Fragmenting a thin signal degrades learning | **yes** | Run exactly one CBO campaign | **partial** | DR lands on one campaign for the same reason, but via Meta's consolidation guidance and its own volume — **not** on Nick's authority, and the CBO half is separately rejected (§3) |
| 3 | Sam: dedicated scale campaign of duplicated winners | Protect proven performers from experimentation | **yes** (as a future motive) | Duplicate winners ranked on incremental attribution into a scale campaign | **no** | Requires many ads with rankable spend; DR has one ad |
| 4 | Loomer: match budget mode to whether ad sets must differ | Budget mode is a **fit** decision, not a performance decision | **yes**, scale-independent | Use A+CB with multiple similarly-sized ad sets, hands-off | **partial** | The implementation presumes ≥2 ad sets; DR has one, and the source never addresses that case |
| 5 | Loomer: judge results at campaign level | Campaign-level allocation makes ad-set-level reads less meaningful | **partial** | Stop looking at ad-set results entirely | **no** | Meta frames campaign-level measurement as a *fit criterion*, not a prescription; at DR's volume per-ad-set readability is worth preserving |

---

## 8. What we explicitly rejected

**Four-campaign architecture (Sam).** *What it is:* prospecting CBO (~80% of spend) + scale + retargeting + retention, with exclusions. *Where it is rational:* high-spend ecommerce with a mature winner pool and purchase-based audiences. *Why it does not transfer:* DR has no purchase-event pool, no winner pool, and a budget that would leave every cell below workable levels. *What could change it:* sustained volume plus a real warm pool (F1, DEFERRED).

**Dedicated scale campaign.** *What it is:* a container for duplicated proven winners. *Rational:* when you can rank ads by incremental attribution. *Doesn't transfer:* one ad exists; nothing to promote. *Could change:* trigger T5.

**Advantage+ campaign budget for DR today.** *What it is:* Meta's automatic cross-ad-set allocation. *Rational:* campaigns with ≥2 similarly-sized ad sets sharing one configuration — Meta's own stated fit. *Doesn't transfer:* DR has one ad set, so the mechanism has nothing to allocate; and it would constrain a future second ad set that may need a different performance goal. *Could change:* triggers T2/T3/T4 — and note this rejection is **weak-form**, since the decision is largely inert today (§3).

**Per-school or per-sport campaigns.** *Rational:* where segments need genuinely different budgets and settings. *Doesn't transfer:* multiplies structures against one thin budget; per-school geography is an ad-set/targeting question (E3), not a campaign one. *Could change:* E3 evidence, or trigger T8.

**Hybrid "always-on ABO testing campaign alongside a CBO scaling campaign."** Surfaced repeatedly in discovery. *Rational:* possibly at volume. *Doesn't transfer:* it is C1 + C3 rejected simultaneously, and every source proposing it was content-farm material with no methodology (§9). *Could change:* triggers T5 + T7 together, with credible evidence.

---

## 9. Practitioner discovery outcome (summary — full log in the research run file)

**Search themes:** low-budget Meta campaign structure; local-service campaign structure at low conversion volume; one vs multiple campaigns for local business; CBO vs ABO at low spend; testing/scaling in one vs separate campaigns; Advantage+ campaign budget with a single ad set; named-practitioner case studies with disclosed spend.

**Candidates evaluated:** ~30. **Shortlisted: 1. Ingested: 1** (Loomer, above). **Reused without re-ingest: 2** (Sam, Nick).

**Main rejection cluster — the "2026 Meta campaign structure guide" content farms** (adnabu, mbadv, creative-brackets, adlibrary, hyperfx, adcontrolcenter, adsuploader, rebootiq, tryvizup, adstellar, admanage, 1clickreport, get-ryze, stackmatix): near-identical SEO restatements with confident numeric prescriptions ("2–4 active campaigns", "8–15 creative variants per ad set", "1–3 ad sets per campaign", "consolidate if you can't fund 50 conversions per ad set per 7 days"). **No methodology, no account context, no author accountability, and numbers that trace to nothing.** These are exactly the manufactured thresholds the numeric-threshold rule prohibits, and their apparent agreement is folklore multiplying, not corroboration.

**Case-study cluster rejected** (socialbaddie, adligator HVAC, cropink, webtonic, leapengine, mariapeaglerdigital, mta.digital): promotional venues, no disclosed structure, unverifiable single-account before/after figures, and in the closest-looking case (a local service provider at ₱350/day) an objective-switching tactic with no registration-level outcome. Same failure pattern already rejected in Waves 1A and 1B.

**Deliberately not chased:** a Perpetual Traffic/Foxwell creative-diversity thread (Wave 2B territory), and everything touching D1–D4, E, F, G, S.

---

## 10. Unknowns

### Unknown but acceptable — does not prevent the architecture hypothesis
- Whether switching budget mode later is a significant edit. *(Handled by choosing the branch-safe mode now.)*
- The exact first-party A+CB eligibility requirements. *(Direction corroborated by Meta's own criteria; hard form is practitioner-sourced and labeled.)*
- `ad set budget sharing` — Meta's uncaptured third mode.
- Origin of Loomer's "two-hour re-adjustment period". *(Quarantined; cited nowhere.)*
- DR's current live budget. *(Architecture is deliberately budget-shape-independent at this volume.)*
- Whether Pixel/CAPI gets built. *(Affects Wave 1A's objective branch, not campaign count or budget placement — see below.)*

### Unknown that would reopen architecture
- **A second campaign objective becoming necessary** (T1) — the only unknown that forces campaign count upward.
- **What ad set #2 is actually for** (T2/T3/T4) — decides the multi-ad-set budget mode; unanswerable until it exists.
- **Whether volume ever supports a split** (T7) — currently no; no numeric threshold defensible.
- **Whether seasonality creates a real protection need** (T6) — DR HYPOTHESIS, testable only in-season.

### Objective/event dependency — INVARIANT or DEPENDENT?

**Wave 2A does NOT settle the objective.** Wave 1A objective/event selection remains conditional and unresolved (A1 RESEARCHING · A2 REOPENED · A3 REOPENED). What this wave establishes is that **the architecture holds across the currently legitimate branches**, so Wave 2B does not need to resolve the objective question before researching creative operations.

**C1: INVARIANT.** Under any legitimate Wave 1A branch, DR runs exactly one objective at a time, so one campaign either way. The branches differ in *which* objective, not *how many*.

**C3: INVARIANT.** No campaign-separation precondition is met under any branch.

**C2: INVARIANT.** Keeping the ad set budget is compatible with every legitimate branch and with a mobile optimization-event ladder. **It was chosen partly because it survives Wave 1A remaining unresolved**, which is the correct posture while A2/A3 are REOPENED.

**What this wave must not be cited for:** it does **not** establish that the objective is Sales → Website, and it does **not** establish that live Pixel/CAPI is absent. The earlier repo inspection found no Pixel/CAPI *implementation code in the inspected DR repositories* — that is not proof about the live account, a partner integration, or a platform-side tag. Any downstream use of a specific objective must come from current authoritative account state, not from this file.

---

## 11. INPUT CONTRACT FOR WAVE 2B

D1–D4 may assume exactly the following, and must not research creative operations across other architectures:

```yaml
wave_2b_input_contract:

  knowledge_level: DR_HYPOTHESIS

  campaign_count_assumption:
    current_recommendation: 1
    meaning: >-
      Wave 2B should not research separate testing and scaling campaigns.
      A second campaign requires a C1 revisit trigger.

  ad_set_current_state:
    last_known_structure: 1
    meaning: >-
      DR's current/last-known architecture contains one ad set.
      This is a starting state, NOT a restriction on D1.

  d1_scope:
    same_vs_new_ad_set: OPEN
    instruction: >-
      D1 is explicitly authorized to research whether new creatives should be introduced
      into the existing ad set or through a new ad set. Wave 2A does not pre-answer this.
      If D1 finds that a second ad set is justified, surface the architecture implication
      and reopen C2 as required rather than suppressing the finding.

  budget_strategy_assumption:
    recommendation_now: keep_ad_set_budget
    confidence: conditional_low_stakes
    reason: >-
      With one ad set, the documented allocation advantage of campaign-level budgeting
      has no second ad set to act on, and no demonstrated performance benefit justifies
      changing modes today.
    reopen_when: >-
      A legitimate second ad set enters the proposed structure.
    future_note: >-
      Reevaluate all then-current Meta budget options, including campaign budget,
      ad-set budgets, and any current budget-sharing features. Do not assume today's
      feature set or a permanent CBO-vs-ABO binary.
    standing_guardrail: >-
      Ad-set spending-limit churn is a conditionally-significant edit and is not a
      delivery remedy (playbook Decision 6).

  testing_scaling_separation_assumption:
    separate_campaigns_now: false
    meaning: >-
      Testing and scaling do not require separate campaigns at DR's current state.
      This says nothing about whether creative introduction should use the existing
      or another ad set; that belongs to D1.

  objective_event_dependency:
    architecture: invariant_across_current_wave_1a_branches
    objective_selection: unresolved_conditional
    instruction: >-
      Wave 2B does not need to solve the objective/event question, but it must not
      falsely state that Wave 2A proved Sales -> Website or that live Pixel/CAPI
      is absent.

  historical_volume_context:
    landing_page_views: >-
      Approximately 9 LPVs in one referenced historical 30-day window.
    clicks: >-
      Approximately 10-11 clicks in the reported historical windows, with metric
      definitions differing across extracts.
    registration_signal: >-
      No registration/purchase action appears in the referenced exported Meta actions
      arrays. Registration-level Meta signal and cost-per-registration are therefore
      unmeasured in those extracts. This is NOT proof that registrations never occurred.
    instruction: >-
      Do not collapse LPVs, clicks, registrations, and purchases into one generic
      "event" count.

  tracking_epistemic_guardrail:
    known: >-
      No Pixel/CAPI implementation code was found in the previously inspected DR repos.
    unknown: >-
      Actual live/partner Meta integration state was not proven by that repo grep.
    instruction: >-
      Do not turn repo-code absence into proof that live Pixel/CAPI does not exist.

  low_volume_evidence_rule:
    required_labels:
      - DIRECTIONAL
      - SUFFICIENTLY_STRONG
    instruction: >-
      D1-D4 must not declare winners, kill rules, spend-distribution rules, or
      creative superiority from tiny samples.

  architecture_revisit_triggers:
    - T1
    - T2
    - T3
    - T4
    - T5
    - T6
    - T7_REVISED
    - T8_REVISED

  remaining_architecture_uncertainties:
    blocking_wave_2b: []
    non_blocking:
      - budget-mode switch learning/edit consequences not fully established
      - exact first-party A+ campaign-budget eligibility constraints not fully captured
      - current/future budget-sharing mechanics become relevant only if multiple ad sets exist
      - whether DR seasonality eventually creates a real separation need remains a DR hypothesis
```

**Nothing blocks Wave 2B.** Every remaining uncertainty concerns multi-ad-set futures or the objective question, neither of which Wave 2B must resolve to research creative operating method.

---

## 12. What Wave 2A does NOT prove

- **The architecture has not been proven by DR results.** No DR experiment has tested campaign count, budget placement, or separation.
- **External evidence does not prove this architecture will outperform alternatives for DR.** Meta publishes no performance comparison between budget modes and no campaign-count guidance; the two practitioners who address structure disagree, are both ecommerce, and are both weakly evidenced on these axes.
- **No architecture here becomes a DR PROVEN OPERATING RULE** until live DR evidence justifies that promotion — and Wave 1B establishes that DR currently cannot generate evidence strong enough to promote anything.
- **The C2 recommendation is a keep/no-unnecessary-change decision, not a performance finding**, and is explicitly labeled low-stakes while one ad set exists.
- **It does not settle the ad-set-level creative-introduction method.** D1 remains OPEN and is authorized to research same-ad-set vs new-ad-set introduction on its own evidence.
- **It does not establish DR's objective, nor the presence or absence of live Pixel/CAPI.**
- Most of this wave's value is negative and campaign-level: it prevents building four campaigns, a dedicated scale campaign, and a hybrid two-campaign ABO/CBO structure at an account that cannot fund or read any of them.

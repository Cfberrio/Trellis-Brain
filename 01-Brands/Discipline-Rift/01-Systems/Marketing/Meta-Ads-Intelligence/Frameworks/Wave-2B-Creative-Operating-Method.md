---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: framework
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/wave-2b-creative-operating-method.md"
repo_path: domains/ads/meta/intelligence/output/wave-2b-creative-operating-method.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/framework
  - discipline-rift
aliases:
  - "Wave 2B"
  - "Creative Operating Method"
---

# Wave 2B — Creative Operating Method for DR

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2A-Campaign-Architecture|Wave 2A — arquitectura de campaña]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-3-Audience-and-Measurement|Wave 3 — audiencia, geo, atribución y medición]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Ad-Scripting-Playbook|DR Ad Scripting Playbook]]
- [[01-Brands/Discipline-Rift/02-Communication/Marketing-Language-Library|DR Marketing Language Library]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Competitors/Competitor-Patterns|Patrones entre anunciantes]]
- [[01-Brands/Discipline-Rift/06-DNA/Message|DR Message DNA]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/output/wave-2b-creative-operating-method.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Date:** 2026-08-14 · **Questions:** D1 · D2 · D3 · D4
**Knowledge level:** **DR HYPOTHESIS.** Built from PLATFORM FACT + EXTERNAL PRACTITIONER CLAIM + DR context facts. **Nothing here is proven for DR.** No campaign, ad set, ad, budget, targeting, Pixel or CAPI setting was changed or created.
**Inherits:** `wave-2a-campaign-architecture-framework.md §11` input contract (unmodified)
**Hands to:** external audit → then Wave 3

---

## 0. EXECUTIVE ANSWER

```text
Creative introduction location:  The existing ad set. Do not build a second ad set to test creative.
Creatives per round:             Start with 2-3. This is a PROVISIONAL LOW-COMPLEXITY STARTING
                                 HYPOTHESIS, deliberately conservative — NOT a proven optimum.
                                 DR's delivery cannot currently discriminate between reasonable
                                 small batch sizes. Re-derive from live DR data.
Introduction method:             All creatives for a round go live in ONE edit session (one learning
                                 reset, not N). Creative is the only thing that changes that session.
Cadence / review condition:      No fixed calendar and NO universal day-count gate. Review once the
                                 period has been technically clean and enough delivery has accumulated
                                 to classify under the D3 ladder. Elapsed time is context, not evidence.
                                 Next round is gated on the current round becoming decidable.
Kill rule:                       Four separate kill types (technical / policy / dominated / downstream).
                                 "Not enough evidence" is an allowed and expected verdict, not a failure.
Keep rule:                       Keep by default while an ad is NOT_EVALUABLE. Absence of evidence is
                                 not evidence of weakness.
No-spend rule:                   Run the 5-branch diagnostic BEFORE any creative judgement. Unequal
                                 delivery between ads is documented-normal Meta behaviour, not a verdict.
                                 Never manipulate natural delivery to force an ad to spend — but
                                 controlled, funded exposure via a designed test is legitimate when the
                                 question matters and DR can fund an interpretable test.
Controlled-test rule:            Natural in-ad-set competition now. Meta's native Creative Testing when
                                 (and only when) the 20% test slice is a meaningful absolute amount.
                                 A/B testing is REJECTED for DR at current scale — Meta itself states
                                 A/B ad sets are more vulnerable to under-delivery from small audiences
                                 and prescribes broadening the audience, which DR structurally cannot do.
Confidence:                      D1 MEDIUM (lowered 2026-08-14 — credible operators recommend a
                                 dedicated testing ad set for low-creative-volume accounts; see §2)
                                 D2 MEDIUM · D3 MEDIUM-HIGH on the boundary, LOW on any threshold
                                 (none is evidence-established) · D4 HIGH
Knowledge level:                 DR HYPOTHESIS
```

**The single most important finding of this wave:** at DR's current delivery, **the individual ad is not a readable unit.** Meta's own instruction — *"When running multiple ads in 1 ad set, evaluate your results at the ad set level"* — plus DR's own arithmetic (below) means the purpose of running 2–3 creatives is **diversity and delivery health, not picking a winner.** Any method that promises to identify DR's best creative from current-scale data is selling false precision.

---

## 1. Input from Wave 2A (not re-litigated)

One campaign · one ad set is the last-known structure and is a starting state, not a cap · budget stays where it is (ad set level) · no separate testing/scaling campaigns · objective/event selection remains **unresolved and conditional** — this wave does not claim otherwise · no Pixel/CAPI conclusion is drawn from repo inspection · historical delivery is metric-specific and must never be collapsed.

**D1 was explicitly left open by Wave 2A.** It is answered here on its own evidence, and the answer does **not** require a C2 reopen (see §2).

---

## 2. D1 — How many creatives, and where

### D1 CURRENT RECOMMENDATION
**Introduce new creative into the existing ad set. Do not create a second ad set for creative testing at DR's current scale.**

### INTRODUCTION LOCATION — why the existing ad set

**Platform evidence, and it is unusually direct.** Meta's own native creative-introduction feature is built to work *inside the existing campaign*: *"The test is set up in an existing campaign so that high-performing ads can continue to run after the test with delivery system learnings retained. **There's no need to merge them into another campaign where the learnings would reset.**"* Meta names relocating creative as the thing that *causes* a reset. The platform's own answer to "where do new creatives go" is: **here**.

Supporting platform facts already on file: *"Avoid high ad volumes… By combining similar ad sets, you also combine learnings"*; *"Combining ad sets and campaigns will help you get the results you need faster."*

**Against a second ad set for DR specifically:** it fragments a thin budget across two structures, duplicates the same tiny Orlando audience against itself, and would trigger a C2 reopen (T2/T3) for a benefit no evidence establishes. Sam Piliero's "pack ad set per creative round" is the named implementation of this alternative — its principle (don't disturb what's already learning) is real and Meta-confirmed, but its implementation assumes a $1,000/day account that can fund parallel packs.

**C2 REOPEN NOT TRIGGERED.** D1 concludes the existing ad set is correct, so Wave 2A's budget-placement decision stands untouched. Had D1 concluded otherwise, the reopen would have been surfaced rather than absorbed — see §12 Test 9.

### CREATIVES PER ROUND — provisional, not a proven optimum

**No external source establishes a defensible number for DR, and none was adopted.** The content-farm cluster's "8–15 creative variants per ad set" and "test 5 ads at a time" carry no methodology and were rejected (§10). Meta's *"2 to 7 copies"* is a **bound on its creative-testing tool**, not a recommendation for ordinary ad-set operation — Meta's only ordinary-operation statement is the qualitative *"avoid high ad volumes."*

So the number is derived from **DR's own delivery arithmetic**:

| DR's last measured 30-day window | Value |
|---|---|
| Impressions | ~1,015–1,153 |
| Reach | ~256–260 |
| Clicks | ~10–11 (all-clicks; outbound clicks were 3 in the window that itemised them) |
| Landing page views | ~9 (in the one window that itemised them) |

≈ **235–270 impressions per week** for the whole ad set. Split across N active ads:

| N ads | Approx. impressions per ad per week |
|---|---|
| 2 | ~120 |
| 3 | ~80 |
| 5 | ~47 |
| 8 | ~30 |

**Read what this actually says.** At *every* value of N, an individual ad accumulates delivery far below any level at which a click-rate or cost difference between ads is readable. **The batch-size question does not have a "right answer that makes ads comparable" at current delivery — no N achieves that.** What N controls is only how thinly the ad set's own aggregate signal is spread and how much creative diversity exists.

**Therefore: start with 2–3 per round — as a PROVISIONAL LOW-COMPLEXITY STARTING HYPOTHESIS.**

> **Honest statement of what the arithmetic does and does not prove (corrected 2026-08-14).** The arithmetic proves that (a) delivery is very low, (b) more ads thin it further, and (c) **no batch size makes individual ads readably comparable at current delivery.** It does **not** prove that 3 is better than 2, or that 4 is worse. **DR's current delivery cannot discriminate between reasonable small batch sizes**, and no external source supplies a defensible number for DR's context. Earlier wording called this "capacity-derived", which overstated the derivation. It is a deliberately conservative starting point, not an optimum.

Rationale, in order:
1. More than one, because a single ad is a single point of failure and Meta's delivery system needs something to allocate between (and `learning-phase.md` warns against trying to avoid the learning phase entirely).
2. Not many more, because Meta says *"avoid high ad volumes"*, because each additional ad further thins the ad-set aggregate that is currently the only readable unit, and because Foxwell/Fairbrother report from practice that *"If you give Andromeda 10 ads, most likely two or three will get 80% of the total spend, with the rest being starved of budget"* (`multi_account_experience`, weak, illustrative figures that are **not** adopted as a DR threshold).
3. Low complexity is itself a reason at this stage: fewer moving parts means fewer confounds while DR is establishing whether it can observe anything at all.
4. **Re-derive from live DR data.** The standing rule is *"however many ads the ad set's current delivery can carry while the ad set aggregate stays interpretable"* — recomputed, not defended.

### META MECHANICS
Adding a new ad to an ad set is an **always-significant edit** — it resets that ad set's learning (`significant-edits.md`). Meta nonetheless states *"Testing new creative… is essential"* and warns against avoiding the learning phase. **Both are true**: introduction has a real cost and must still happen; the answer is to make it deliberate (§3), not rare.

### PRACTITIONER EVIDENCE — and the genuine challenge to this decision

**The strongest external challenge to "existing ad set" is real and is recorded rather than dismissed.** Foxwell & Fairbrother associate their **Method 1 — a dedicated per-batch testing ad set on ABO, so *"each creative brief is guaranteed to get some budget"*** — with *"brands with a small creative volume or especially those new to advertising."* **That description fits DR.** Confidence on D1 is therefore lowered from MEDIUM-HIGH to **MEDIUM**.

**Why the decision nonetheless holds — context, not vote count:**

1. **The same ecosystem contradicts itself on the axis that binds DR.** Courtney Fritts (also foxwelldigital.com) states that **for accounts under ~$100/day, direct competition or manual bids *"might be your only viable options."*** Foxwell scopes Method 1 by *creative volume*; Fritts scopes by *budget*. DR is low on both, **but its binding constraint is budget**, and DR's historical spend is roughly an order of magnitude below Fritts's boundary. The budget-scoped statement governs. **Both are one ecosystem — this is not 2-vs-1, it is one ecosystem being internally context-dependent**, which is itself the finding.
2. **Method 1's proponents name its costs, and they land hardest on DR:** *"your ads spend more time in the learning phase"*, winners *"can't compete with other stronger batches"*, *"things can soon escalate with far too many ad sets."*
3. **Meta's own creative-introduction feature achieves Method 1's benefit without Method 1's structure.** Guaranteed budget for new creative is exactly what native Creative Testing provides (*"delivery provided to new test ads"*) — **inside the existing campaign, with learnings retained.** The principle Foxwell is reaching for is available without a second ad set; DR simply cannot fund it yet.
4. DR's own arithmetic and the C2 fragmentation cost are unchanged.

**Note the direction of the operator evidence on the underlying problem:** Foxwell's *"if a batch gets very little spend, it's hard to generate conclusions"* is an independent practitioner statement of exactly the conclusion DR reached from Meta's *"evaluate at ad set level"* instruction and its own delivery arithmetic.

**Source summary:**
- **Sam Piliero** — "pack" ad set per creative round (`experience_claim`, weak, ecommerce, $1k/day). Reused, not re-ingested.
- **Nick Theriot** — creative introduced within one consolidated structure (`experience_claim`, weak, ecommerce). Reused.
- **Jon Loomer** — 4 claims on Meta's Creative Testing tool, incl. one `self_reported_test` (`moderate`) — the only source in the corpus that **ran** the mechanism. His *"two to five test ads"* is graded **`OUTDATED`** vs Meta's current *"2 to 7"*.
- **Foxwell & Fairbrother** — 4 claims (`experience_claim` / `multi_account_experience`, all weak), dated 2026-03-13. **FOXWELL ECOSYSTEM.**
- **Courtney Fritts** — 4 claims across 2 articles (`multi_account_experience` / `opinion`, weak-to-none, **both undated**). **FOXWELL ECOSYSTEM — not independent of the above.**

### DR TRANSFERABILITY
DR is one metro, hard residency qualifier, parent purchaser, seasonal, extremely thin delivery, one ad today. The **principle** shared by all three practitioners — don't casually disturb a structure that is learning — transfers. **No practitioner's ad-count or ad-set implementation transfers**, because every one of them assumes delivery volume DR does not have.

### WHAT WE REJECTED
| Option | Verdict | Why |
|---|---|---|
| **A — existing ad set** | **ADOPTED** | Meta's own creative-introduction mechanism works here; consolidation guidance; no fragmentation |
| **B — new ad set per creative round** | REJECTED now | Fragments thin budget; duplicates a small geo audience against itself; triggers C2 reopen for no evidenced benefit |
| **C — native Creative Testing** | **DEFERRED, conditionally adopt** | Best-fitting mechanism on paper (delivery *provided* to test ads, learnings retained, in-campaign). Blocked today because Meta suggests *"no more than 20%"* of existing budget for the test slice — a trivial absolute amount at DR's scale — and because it requires switching to Highest volume bid strategy, itself an always-significant edit. Adopt when the 20% slice is meaningful. |
| **D — A/B testing** | **REJECTED at DR scale** | Meta: A/B ad sets *"may be more vulnerable to under-delivery caused by small audiences. You may need to broaden your audiences more than usual."* DR **cannot broaden** — residency is the qualification. Platform-grounded rejection, not a preference. |
| **E — other native mechanisms** | none adopted | Nothing else retrieved materially solves D1 |

### WHAT WOULD CHANGE THE RULE
Delivery rises enough that a 20% creative-test slice funds real delivery across 2+ test ads → adopt Option C. Delivery rises enough that individual ads accumulate comparable, readable exposure → the ad becomes a readable unit and batch size should be re-derived. A material finding that a second ad set solves a real problem → **surface a C2 reopen (T2/T3), do not build silently.**

### STATUS
**ENOUGH_EVIDENCE (conditional).** Location is settled on first-party mechanics plus consolidation guidance. Batch size is a derived capacity rule with its recomputation trigger stated — no exact universal number is claimed, because none is defensible.

---

## 3. D2 — Introduction procedure and cadence

### D2 CURRENT RECOMMENDATION
**Batch each round into one deliberate change window. Do not drip ads in one at a time. Do not run a creative round and any other change in the same window.**

### BATCHING VS DRIPPING — what is fact and what is inference

**PLATFORM FACT.** *"Adding a new ad to your ad set"* and *"Any change to ad creative"* are both on Meta's always-significant list — each drip is its own learning reset. Separately, from the delivery-troubleshooting page: *"Extensive pausing can interfere with the system's ability to optimize delivery and allocate budget on schedule… **if changes are too frequent then your campaign will be constantly adapting and in flux**."* And Meta explicitly discourages informal toggling: *"We do not recommend testing informally, such as by turning ad sets or campaigns on and off manually. This can lead to inefficient ad delivery and unreliable test results."*

**WHAT META DOES NOT SAY.** Meta never says "batch", never says "don't drip", and prescribes **no cadence at all**. It also warns the other way: *"you shouldn't try to avoid the learning phase completely. Testing new creative and marketing strategies is essential."*

**DR INFERENCE (hypothesis).** Given N new creatives, introducing them in one session costs one reset; introducing them one at a time costs N resets, each restarting a ~7-day window DR's delivery already struggles to fill. **This is arithmetic on top of a platform fact, not a Meta recommendation** — and it is upgraded from Wave 1's pure inference by the "constantly adapting and in flux" sentence, which supports the *principle* without endorsing the tactic.

### CHANGE WINDOW PROCEDURE

**BEFORE a round — five checks, no more:**
1. Campaign and ad set are active, and the ad set is not mid-reset from a recent significant edit.
2. Every existing ad's **Delivery column status** is clean — no *In review*, *Update required*, *Creative limited*, *Creative fatigue*, or error state. (An unresolved technical problem contaminates everything downstream.)
3. The **previous round has reached a decidable evidence state** (§4). If it has not, do not start a new round — that is the gate.
4. Nothing else is scheduled to change in the same window: budget, audience/geo, placements, performance goal, bid strategy, landing page, offer.
5. The offer and landing page are actually live and correct.

**DURING introduction — change creative only:**

| Variable | During a creative round |
|---|---|
| Ad creative | **This is the only thing that changes** |
| Budget | Hold. (Conditionally significant; also confounds any read) |
| Audience / geo / placements | Hold. (Always significant; also confounds) |
| Performance goal | Hold. (Always significant) |
| Bid strategy | Hold. (Always significant — note this is what a future Creative Test would force) |
| Landing page / offer | Hold. (Not a Meta edit, but a total confounder — see Tests 17–18) |

Publish the whole batch in **one** session.

**AFTER introduction — the discipline is inaction:**
- Do not add another ad mid-round.
- Do not toggle ads on/off to "give one a chance" — Meta names this as unreliable.
- Do not change budget in the window, and specifically not late in the day (*"if you double your daily budget at 10pm, the system would only have 2 hours to spend"*).
- Do run the **D4 diagnostic** on any ad showing no/low spend — that is diagnosis, not intervention.

### WHEN TO REVIEW — corrected 2026-08-14

> **Correction.** The earlier version imposed a hard **≥7-day** gate on ordinary natural-delivery review, citing Meta's A/B-test guidance. **That was an invalid transfer**: Meta's 7-day figure governs *controlled A/B tests*, a different mechanism with split audiences and a scheduled measurement window. Meta publishes **no** minimum observation period for ordinary in-ad-set delivery. The hard gate is removed.

**The review condition is evidence-based, not time-based:**

> **Review once the period has been technically clean (no unresolved Delivery-column problem, no non-creative change mid-window) AND enough delivery has accumulated to classify each ad and the ad set under the D3 ladder. Elapsed time is context, not evidence, and not a universal threshold.**

**Time still plays two legitimate roles**, both weaker than a gate:
- **A guard against reacting to hours of data.** Reviewing an ad set the morning after publishing is not a review.
- **A weakly-evidenced practitioner floor.** Courtney Fritts states a creative should *"run for at least 7 days"* before being killed. This is an **EXTERNAL PRACTITIONER CLAIM** — `opinion`, `evidence_strength: none`, **undated**, ecommerce framing, no derivation given. **It is recorded, not adopted as a rule**, and it must never again be presented as a Meta fact.

**What DR should actually do:** treat roughly a week as a sensible earliest-look habit, and treat the *evidence condition* as the thing that authorises a decision. If a week has passed and nothing has accumulated, the answer is NOT_EVALUABLE and the correct action is to keep waiting — not to decide.

Meta's related guidance is retained for its own scope: **when DR eventually runs a controlled test**, Meta recommends *"a minimum of 7-day tests"*, a 30-day maximum, and **extending beyond 7 days when customers take longer than that to convert** — which describes DR's parent decision cycle.

### WHEN A NEW ROUND MAY START
When the current round reaches a decidable state per §4 — i.e. every live ad is classified, technical problems are resolved, and the ad set has produced *some* interpretable aggregate signal. **Time alone never authorises the next round** (Test 1).

### STATUS
**ENOUGH_EVIDENCE (conditional).** The procedure is fully specified and every prohibition traces to a platform fact. The batching *preference* remains a **DR HYPOTHESIS** with a stated falsification path (§13) — Meta does not prescribe cadence and no credible practitioner evidence at DR's scale was found.

---

## 4. D3 — Evidence ladder and kill/keep

### D3 CURRENT RECOMMENDATION
**Classify every ad into an evidence state before deciding anything. "Not enough evidence" is a valid, expected, and at DR's current scale the *most common* verdict.**

### THE EVIDENCE LADDER

| State | Definition | What may be concluded | What may NOT be concluded |
|---|---|---|---|
| **0 — NOT LIVE / TECHNICALLY INVALID** | Rejected, in review, *Update required*, error status, wrong/broken URL, ad set paused, schedule ended, payment/account issue | Nothing about the creative. Fix or remove | Anything about creative quality |
| **1 — LIVE BUT NOT EVALUABLE** | Live, but delivery is negligible or wildly unequal to peers | Delivery health only. **Default state at DR's current scale** | Good, bad, winner, loser — anything |
| **2 — DELIVERY EVIDENCE ONLY** | Enough impressions/spend to observe CPM, reach, and gross click response | **DIRECTIONAL** reads on delivery health and gross mismatch | Any cost-per-outcome comparison; any winner |
| **3 — INTERMEDIATE RESPONSE EVIDENCE** | Observable click / landing-page-view behaviour, ideally repeating rather than appearing once | **DIRECTIONAL** message signal | That it produces registrations. Clicks are not business outcomes (Test 5) |
| **4 — DOWNSTREAM BUSINESS EVIDENCE** | Attributable paid-registration evidence, in enough quantity, across repeated windows | The only state where business-performance conclusions become possible | Anything, if the quantity is single-digit and unrepeated |

**Meta's constraint on the unit of analysis, verbatim:** *"When running multiple ads in 1 ad set, evaluate your results at the ad set level."* At DR's delivery this is not a stylistic preference — it is the reason **State 1 is the honest default for individual ads**, and why the *ad set* is DR's readable unit today.

### IMMEDIATE STOP CONDITIONS (not performance judgements)
- **Technical kill** — State 0 conditions: broken/incorrect destination, error status, ad not actually running as intended.
- **Policy / brand kill** — violates DR's claim rules or banned language (`discipline-rift/CLAUDE.md`): elite/high-performance framing, "tryouts" for a non-tryout offer, confidence/discipline as a guaranteed promise, any unmeasured claim. **This is a hard requirement and needs no data at all.**

### NOT-EVALUABLE CONDITION
An ad is NOT_EVALUABLE — and is **kept, not killed** — when any of these hold:
- Its exposure is not reasonably comparable to the ads it would be compared against (judgement, not a fixed ratio — see §4 confidence-building conditions).
- The ad set as a whole has not accumulated interpretable delivery in the window.
- A D4 diagnostic branch 1 or 2 problem is unresolved.
- The round overlapped a non-creative change (audience, budget, offer, landing page).

**Keeping an unevaluable ad is the correct action.** Killing it is fabricating a verdict.

### DIRECTIONAL KILL/KEEP CONDITIONS — corrected 2026-08-14

> **Correction.** The earlier version required "exposure within the same order of magnitude" and "more than one window". Those are **still thresholds** — non-dollar, but thresholds — and **no evidence establishes either boundary for DR.** They are demoted from qualification rules to **confidence-building conditions**.

**Dominated-performance kill is operator judgement under documented conditions, not a mechanical rule.**

Confidence that an ad is genuinely weak **increases** as more of these hold — and none of them is individually sufficient:

| Confidence-building condition | Why it matters |
|---|---|
| The ad received a **reasonably comparable opportunity** to its peers | Unequal exposure is expected (breakdown effect), so a starved ad tells you nothing |
| The weakness **repeats** rather than appearing once | A single window at DR's exposure cannot separate weak creative from normal allocation |
| **No technical confound** — clean Delivery status throughout | State 0 problems invalidate everything |
| **No non-creative change** occurred in the window | Audience/budget/offer changes confound the read |
| **Downstream evidence agrees**, where any exists | The only evidence that speaks to the business outcome |

**No exact exposure ratio and no exact number of windows is currently evidence-supported for DR, and none is asserted.** Where these conditions hold together, retire the ad as part of the *next* round — and label the decision **DIRECTIONAL**, never SUFFICIENTLY_STRONG.

- **Directional keep** — anything delivering and not dominated. **Default.**
- **When conditions are mixed or ambiguous, the answer is NOT_EVALUABLE and the ad is kept.** Manufacturing determinism here would be the exact failure this ladder exists to prevent.

### DOWNSTREAM QUALITY KILL
Available only at State 4: an ad generates cheap intermediate response but consistently fails to produce paid registrations while peers do, across repeated windows. **Downstream evidence outranks proxy success** whenever both exist (Test 6). Not runnable today — no registration-level Meta signal exists in the available extracts.

### SUFFICIENTLY-STRONG CONDITION
A read is **SUFFICIENTLY_STRONG** only when: it rests on State 3–4 evidence, exposure between compared ads is comparable, **and it repeats rather than appearing once** — Loomer's usable standard, *"results that are so clear that if you ran the test again, you'd get similar results."*

**No DR creative evidence to date meets this bar. At current delivery, none realistically will.**

### TIME RULE
**There is no evidence-established minimum observation period for ordinary natural in-ad-set delivery, and none is imposed.** Meta's 7-day figure governs controlled A/B tests only; transferring it to natural delivery was an error and has been removed (§3). The one external statement bearing on natural delivery — Fritts's *"run for at least 7 days"* — is undated `opinion` with `evidence_strength: none` and is recorded, not adopted.

**Time is context, never evidence.** A week with 2 clicks is State 1, not a tested creative (Test 1). Roughly a week is a sensible earliest-look habit; the **evidence condition** is what authorises a decision.

### SPEND RULE
**No defensible spend threshold exists.** No first-party figure; every practitioner figure found ($100/day minimum-spend limits, $50/day test budgets) comes from accounts 15–40× DR's historical spend. None adopted, none invented.

### IMPRESSION / EXPOSURE RULE
**No defensible absolute number exists, and no exact exposure ratio is evidence-established either.** What is defensible is the **direction**: *ads may only be meaningfully compared when they received reasonably comparable opportunity; the more unequal the exposure, the less any comparison means.* "Reasonably comparable" is deliberately left to operator judgement under the §4 confidence-building conditions rather than fixed at a ratio DR cannot justify. This follows from the breakdown effect — unequal exposure is expected, so unequal exposure cannot itself be the finding.

### WHAT COUNTS AS A "WINNER"
At DR's current delivery: **nothing.** "Winner" is not an available verdict at ad level. Even Meta's own creative test ships without one — *"A confidence level is not included"* — and Meta's A/B results documentation treats *"the test did not find a winner"* as a normal outcome. The strongest permissible statement today is a **DIRECTIONAL ad-set-level** read.

### WHAT MUST NEVER BE CALLED A WINNER
An ad with more spend than another (that is the breakdown effect, §5) · an ad with a better CTR at single/double-digit click counts · an ad that "won" a single window · an ad with strong clicks and no downstream evidence (Test 5) · an A/B or creative-test result that Meta itself declined to declare a winner for · anything at State 0–1.

### STATUS
**ENOUGH_EVIDENCE (conditional).** The ladder, the four kill types, and the not-evaluable default are fully specified and platform-anchored. **Deliberately no numeric thresholds** — the numeric layer is `NO_USEFUL_EVIDENCE_FOUND` and is recorded as such rather than filled.

---

## 5. D4 — The no-spend diagnostic

### THE CORE PLATFORM FACT
Meta documents the misreading by name. **The "breakdown effect"** is *"the misinterpretation that our system shifts impressions and spending into underperforming ad sets, placements or ads. In reality, the system is designed to maximize the number of results for your campaign."* And from delivery troubleshooting: *"it's normal for some ad sets or ads to deliver less than others, as long as your overall campaign is spending budget according to the goals you've set."*

Meta's own worked example: the placement with the **better final average CPA ($1.10) received $50**, while the one with the **worse average CPA ($1.46) received $450** — because the first one's *marginal* cost was rising faster. **The better-looking row correctly got less money.**

**Consequence: unequal spend between DR's ads is the expected state, and is not evidence about creative quality.**

### THE DIAGNOSTIC TREE — run in order, stop at the first hit

**BRANCH 1 — Is the ad eligible to deliver?**
Check: Delivery column status · in review / rejected / *Update required* · ad, ad set and campaign all active · schedule not ended · account or payment restriction · destination URL loads.
→ Any hit: **STOP. State 0. No creative verdict.** Fix it.

**BRANCH 2 — Can the ad set deliver at all?**
Check: budget actually spending (Meta may spend *"up to 75% over or below your daily budget on a given day"*) · any ad-set spending limit · audience size vs Orlando geo constraint · bid/cost control set too low (*"your cost per result goal or bid cap may not be high enough to be competitive"*) · a significant edit inside the last ~7 days · frequent pauses causing *"constantly adapting and in flux"* · *Creative limited* / *Creative fatigue* · audience saturation.
→ Any hit: **STOP. Ad-set-level problem. No per-creative verdict.**

**BRANCH 3 — Is this just allocation?**
Apply the breakdown effect. Meta allocates for the **aggregate** result and instructs evaluation at ad set level when multiple ads share an ad set.
→ **Default answer at DR's scale: YES, this is allocation.** Unequal or zero spend on one of 2–3 ads inside a thin ad set is exactly what the documentation describes. **STOP — no creative verdict.**

**BRANCH 4 — Does the ad have enough exposure to judge?**
Apply §4. If exposure is not reasonably comparable to peers → **NOT_EVALUABLE. Keep. Stop.**

**BRANCH 5 — Comparison genuinely matters and natural delivery will not supply it**
Only now consider a controlled method: **native Creative Testing** (delivery *provided* to test ads — the documented fix for exactly this) when the 20% slice is fundable; **A/B testing** — rejected at DR scale; **or accept the question is unanswerable now and move on.**
Note the tool's limitation: it **cannot test existing ads**, only new duplicates — so it answers "which new creative performs better under equal spend", never "why is my running ad starved."

### THE FORCE-SPEND RULE — corrected 2026-08-14

> **Correction.** The earlier version stated a flat absolute: *"Never force spend."* Credible operators take the opposite operational position — that early algorithmic prediction can starve an ad before it accumulates evidence, and that some deliberate exposure is therefore warranted (Fritts: *"Budget for real learning. Try to spend at least 3× your CPA… before calling it quits"*, noting ads sitting at *"$5–$10 in spend"* are insufficient for evaluation). The absolute was too strong. **It is replaced by a distinction, not reversed.**

**The distinction that matters is HOW exposure is obtained:**

| | Verdict | Why |
|---|---|---|
| **Manual / informal forcing** — toggling ads on and off, budget churn, repeatedly overriding delivery to push spend at one ad | **REJECTED — unchanged** | Meta: *"We do not recommend testing informally, such as by turning ad sets or campaigns on and off manually. This can lead to inefficient ad delivery and unreliable test results."* And frequent changes leave a campaign *"constantly adapting and in flux."* This is the thing Nick Theriot is right to warn against |
| **Controlled, deliberately funded exposure** — native Creative Testing, or another designed and funded test structure | **LEGITIMATE, conditionally** | Meta built a mechanism that *provides* delivery to test ads precisely because natural allocation will not. Using it is not "overriding Meta" — it is using a documented Meta feature |

**The operating rule:**

> **Never manipulate natural delivery merely to force an ad to spend. If an important creative question remains unanswered because natural delivery starves the ad, obtain the answer through a controlled testing mechanism — and only when DR can fund an interpretable test.**

**Conditions that must all hold before controlled exposure is justified:**
1. The creative question actually matters to a business decision.
2. Natural delivery genuinely cannot answer it (Branches 1–4 exhausted).
3. DR can fund a test slice that produces meaningful delivery — not a token 20% of a tiny budget.
4. The method isolates the question rather than adding confounds.
5. The learning cost (including the bid-strategy switch Creative Testing requires) is worth paying for this question.

**Today at DR's budget, condition 3 fails**, so the practical answer remains "leave it alone" — but it now rests on a **funding condition that can change**, not on a principle that forbids controlled testing forever. The Fritts numbers (3× CPA, 3× production cost, "$5–$10 is insufficient") **do not transfer**: DR has no measured cost-per-registration, so the multiplier is uncomputable, and creative production cost is unrelated to statistical readability.

### SITUATION RULES

| Situation | What it CAN mean | What it does NOT prove | Check | Do | Don't | Evidence level |
|---|---|---|---|---|---|---|
| **No spend** | Not eligible (B1); ad set constrained (B2); normal allocation (B3) | That the creative is bad | B1 → B2 → B3 | Fix technical causes; otherwise leave alone | Delete it as "rejected by Meta"; manually manipulate delivery to force spend | NOT_EVALUABLE |
| **Low spend** | Allocation working as designed | Weak creative | B2, B3 | Let the round finish | Toggle on/off to "help" it | NOT_EVALUABLE |
| **Unequal spend** | Expected — breakdown effect | That the high-spend ad is the better business creative | B3 | Evaluate at **ad set level** | Rank ads by spend share | NOT_EVALUABLE at ad level |
| **Enough spend + weak response** | Possible genuine weakness | Confirmed weakness from one window | B1, B4; is exposure comparable? | If repeated across windows → directional dominated-performance kill at next round | Kill mid-window on one window | DIRECTIONAL |
| **Enough spend + strong intermediate response** | Message resonates | That it produces registrations | B4; is downstream measurable at all? | Keep; note as directional | Call it a winner | DIRECTIONAL |
| **Strong intermediate + weak downstream** | Proxy-quality mismatch (the A3 failure mode) | Anything, if downstream counts are tiny | State 4 quantity; repetition | If repeated → downstream quality kill | Override downstream evidence with CTR | DIRECTIONAL → SUFFICIENTLY_STRONG only if repeated |

### VERDICT ON THE NICK THERIOT CLAIM
**PARTIALLY TRANSFERS.**
- **PRINCIPLE — transfers, and is now platform-supported.** Meta's delivery system deliberately allocates unevenly, and treating that as misallocation is the named misinterpretation. "Don't *manually* force spend" is consistent with Meta's own framing — note this covers informal manipulation, not the use of a documented controlled-testing feature (§5 force-spend rule).
- **IMPLEMENTATION — does NOT transfer.** "A no-spend creative should be abandoned" fails against the same page: unequal delivery is *normal*, and Meta documents many non-creative causes. At DR's volume no-spend overwhelmingly means **NOT_EVALUABLE**, not "bad creative". His own claim also assumes enough tests that a 10% survival rate is a usable number — at DR's scale 10% of a handful is zero.
- `platform_validation_status` on the underlying claim remains **INSUFFICIENT_EVIDENCE** (Meta does not state that non-spend is a creative verdict, and does not refute it either). Unchanged by this wave.

### STATUS
**ENOUGH_EVIDENCE.** The diagnostic is fully specified, ordered, and anchored in two first-party pages retrieved this run. This is the wave's strongest question.

---

## 6. FIRST DR RELAUNCH — CREATIVE PLAN

Runnable as written. Assumes Wave 2A architecture and a fresh extract first (playbook Decisions 1, 2, 7 remain prerequisites and are unchanged).

1. **How many creatives launch:** 2–3. Recompute if expected weekly delivery has materially changed since the last extract.
2. **Where:** all of them in the single existing ad set, published in one session.
3. **What happens to the existing creative:** keep it live if it is technically clean and on-brand. It is the only continuity DR has, and killing it removes the baseline.
4. **Held constant through the round:** budget, audience/geo, placements, performance goal, bid strategy, landing page, offer.
5. **First review condition:** the window has been technically clean **AND** enough delivery has accumulated to classify each ad under the D3 ladder. **No fixed day-count gate** — roughly a week is a sensible earliest look, not a threshold.
6. **"Not enough evidence" looks like:** any ad below comparable exposure; any unresolved Delivery-column problem; any window in which something non-creative also changed. Expect **most or all ads to be NOT_EVALUABLE at first review** — that is a correct result, not a failed test.
7. **Triggers intervention:** only Branch 1 or Branch 2 findings (technical or ad-set constraint), or a policy/brand violation. Nothing else.
8. **Triggers the next round:** the current round is fully classified and technically clean — never the calendar alone.
9. **Would make us use a controlled test:** the 20% Creative-Testing slice becomes a meaningful absolute amount, **and** a specific creative question matters enough to pay the bid-strategy switch (an always-significant edit).

---

## 7. RECURRING CREATIVE-ROUND SOP

1. Check the prior round: every ad classified into a State (§4).
2. Resolve every Branch 1 / Branch 2 problem before interpreting anything.
3. Apply kill types: technical → policy → dominated (directional, repeated) → downstream (State 4 only). Otherwise **keep**.
4. Confirm the round is decidable. If not, extend — do not start a new round.
5. Introduce 2–3 new creatives into the existing ad set, in one session, recomputing the count from current delivery.
6. Hold every non-creative variable constant.
7. Avoid all unrelated significant edits during the window.
8. Observe to the review condition (technically clean window AND delivery accumulated to classify). Do not intervene.
9. Run the D4 tree on any no/low-spend ad **before** any creative conclusion.
10. Keep / kill / continue, labelling every read DIRECTIONAL or SUFFICIENTLY_STRONG.
11. Record: date, ads introduced, what was held constant, delivery per ad, states assigned, decisions and reasons.
12. Repeat.

**Step 11 is the one that builds Half 2.** Without it every round starts from zero and DR never accumulates its own evidence — which is the entire point of the project.

---

## 8. CONTROLLED TESTING — when to use what

| Method | Use when | DR today |
|---|---|---|
| **Natural in-ad-set competition** | Default. Cheapest, no extra structure, no learning cost beyond the introduction itself | **This is DR's method now** |
| **Native Creative Testing** | You need comparable spend across *new* creatives, inside the existing campaign, with learnings retained | **DEFERRED.** Adopt when 20% of budget is a meaningful absolute amount across 2+ test ads. Costs a bid-strategy switch (always-significant edit). Ships with **no confidence level** — output is directional by construction |
| **A/B testing** | You need clean isolation and can fund split audiences | **REJECTED at current scale.** Meta: A/B ad sets are *more* vulnerable to under-delivery from small audiences and the remedy is to broaden — DR structurally cannot |
| **No test** | The question cannot be answered at current delivery | **Frequently correct.** Say so rather than manufacturing a verdict |

---

## 8b. Real-operator evidence matrix

**Purpose: show what the actual operating systems in use today are, what evidence each really presents, and why DR borrows some principles and rejects some implementations.** This is not a ranking of experts.

| Operator | Source / date | Business & spend context | Testing method | Creative introduction | No-spend interpretation | Kill/keep logic | Evidence actually shown | `evidence_basis` | `evidence_strength` | Principle → DR | Implementation → DR | Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Sam Piliero** | YouTube 2025-12-11 | Ecommerce/DTC; **$1,000/day** worked example; $56k→$250k/mo case | Isolated "packs" | **New ad set per creative round** | not addressed directly | 4–7 days via min-spend behaviour, 1× CPA (~$100/day) | Case study tied to structure as a whole; no per-tactic data | `self_reported_case_study` / `experience_claim` | moderate / weak | **yes** (don't disturb what's learning) | **no** (cannot fund packs) | SAM |
| **Nick Theriot** | YouTube 2025-04-28 | Ecommerce/DTC; agency floor **$100k/mo revenue** clients | Consolidated | **Into the existing consolidated structure** | **Non-spend is a creative verdict; don't force spend** | diagnose hook→visual→market→duration→positioning | "thousands of tests" asserted; no dataset | `multi_account_experience` | weak | **yes** (system allocates deliberately) | **no** (abandon-on-no-spend) | NICK |
| **Jon Loomer** | jonloomer.com 2025-10-13 (upd. 2026-01-02) | Own info-product account; **$50/day test**, `Complete Registration` (free signup), $3–5 expected CPA | **Meta native Creative Testing** | Duplicated test ads **inside the existing campaign** | Use equal-spend testing rather than fixing allocation | Don't overreact to small samples; want reproducible results | **Actually ran the test**; reports parameters + result ordering | `self_reported_test` | **moderate — strongest in corpus** | **yes** | **partial** (20% slice too small at DR budget) | LOOMER |
| **Andrew Foxwell + Paul Fairbrother** | foxwelldigital.com 2026-03-13 | Agency, DTC/ecommerce; **no spend disclosed**; scoped by creative output (weekly batch → 100+ ads/mo) | Method 1 (dedicated ABO test ad set) **or** Method 2 (into main campaigns) | **Method 1 for low creative volume / new advertisers; Method 2 once output scales** | *"2 or 3 of 10 ads get 80% of spend, rest starved"* | Method 2 con: low-spend batches yield no conclusions | Methods compared by design; **no results for either** | `experience_claim` / `multi_account_experience` | weak | **yes** (guaranteed budget → cleaner reads) | **no** (second ad set unfundable) | FOXWELL |
| **Courtney Fritts** | foxwelldigital.com **undated ×2** | Agency, DTC; claims accounts *"thousands to tens of thousands in daily spend"* | **Context-conditional** — budget, creative volume, data density, maturity, risk | **Under ~$100/day: direct competition may be the only viable option** | Attributes non-spend to hooks/pacing/engagement signals | *"3× CPA or 3× production cost… and at least 7 days"* before killing | **None** — no case studies or metrics | `multi_account_experience` / `opinion` | weak / **none** | **yes** (method must fit context; don't kill unexposed creative) | **no** (numbers uncomputable for DR) | FOXWELL |
| *Dara Denney* | YouTube — **evaluated, deferred** | framed on testing at every budget | — | — | — | — | not retrieved (paid transcript required) | — | — | — | — | *would have been DENNEY* |

### Independence clusters

```text
META FIRST-PARTY   — 11 pages across Waves 2A/2B (outranks all practitioner platform claims)
SAM                — Sam Piliero
NICK               — Nick Theriot
LOOMER             — Jon Loomer (3 sources = ONE voice, not three confirmations)
FOXWELL ECOSYSTEM  — Andrew Foxwell + Paul Fairbrother, and Courtney Fritts
                     (3 sources = ONE ecosystem, not three confirmations)
DENNEY             — evaluated and deferred; would have been the 5th independent cluster
```

**4 practitioner clusters, 5 named operators, 10 practitioner sources.** Where the Foxwell ecosystem's two authors disagree with each other (§2), that internal disagreement is treated as evidence the question is context-dependent — **not as a majority.**

### Where the operators materially disagree

| Question | Positions | How DR resolved it |
|---|---|---|
| Where creative enters | Sam & Foxwell: **separate ad set**. Nick, Fritts, Loomer(via Meta's tool): **existing structure** | **Not by count.** By budget scoping: Fritts puts the viability boundary near $100/day and DR is an order of magnitude below it; Foxwell's own stated Method 1 costs (longer learning, ad-set bloat) land hardest on DR; and Meta's own tool delivers Method 1's benefit *in-campaign* |
| What no-spend means | Nick & Fritts: **a creative verdict**. Meta & Foxwell's observation: **normal allocation** | Split principle from implementation. Allocation is documented first-party; the creative-verdict inference is not, and is `INSUFFICIENT_EVIDENCE` |
| Whether to give starved ads exposure | Nick: **don't force**. Fritts: **fund real learning before killing** | Both are right about different mechanisms — **manual manipulation rejected, controlled funded exposure permitted** (§5) |
| How long before judging | Sam: 4–7 days. Fritts: ≥7 days. Meta: 7 days **for A/B tests only** | **No day-count gate adopted.** Evidence condition replaces it; the practitioner floors are recorded as weak, undated claims |

---

## 9. Principle vs implementation matrix

| Source idea | Principle | Transfers | Implementation | Transfers | Why |
|---|---|---|---|---|---|
| Sam: pack ad set per creative round | Adding creative to a live ad set disturbs its learning | **yes** (Meta-confirmed) | New ad set every round | **no** | Assumes $1k/day; DR cannot fund parallel packs; Meta's own creative-introduction feature stays in-campaign |
| Nick: don't force spend on no-spend ads | The system allocates deliberately; overriding is usually wrong | **yes** (now platform-supported via breakdown effect) | Treat no-spend as a creative verdict | **no** | Meta documents unequal delivery as normal and lists many non-creative causes |
| Sam: judge at 4–7 days via minimum-spend behaviour | Give a creative a bounded window before deciding | **partial** | 4–7 days, $100/day floor | **no** | Assumes ~37× DR's spend; at DR's delivery the window contains almost nothing |
| Loomer: creative test to equalise spend | Equal-spend comparison answers what natural delivery cannot | **yes** | Run creative tests routinely | **partial** | 20% slice is trivial at DR's budget; requires bid-strategy switch |
| Loomer: aim for ~50 events/week in a test | Results should be reproducible before they are trusted | **yes** (as the reproducibility standard) | Target 50 events per ad | **no** | He concedes his own $50/day test missed it; DR is orders of magnitude below. Same single origin as every 50/week citation |
| Foxwell/Fairbrother: dedicated ABO testing ad set per batch | Guaranteeing budget to new creative produces cleaner reads than letting it compete | **yes** | Build a new ad set per creative batch | **no** | Unfundable at DR's budget; triggers C2 reopen; their own stated costs (longer learning, ad-set bloat) hit DR hardest. **Meta's native tool delivers the same benefit in-campaign** |
| Fritts: method must fit account context | No universal best-practice testing method exists | **yes**, scale-independent | Pick from her Method 1–4 taxonomy by budget tier | **partial** | Direction transfers (DR is far below her ~$100/day viability boundary); the taxonomy and the boundary are undated and underived |
| Fritts: 3× CPA / 3× production cost before killing | Don't kill a creative that never accumulated exposure | **yes** | Spend 3× CPA before killing | **no** | DR has **no measured cost-per-registration**, so the multiplier is uncomputable; production cost is unrelated to readability |
| Content farms: "test 5 ads", "8–15 variants", "refresh every 2–4 weeks" | — | — | — | **no** | No methodology, no context, untraceable numbers. Rejected wholesale |

---

## 10. What we rejected

**A/B testing as routine practice.** *Rational:* accounts with large or broadenable audiences needing clean isolation. *Not for DR:* Meta itself says A/B ad sets under-deliver on small audiences and prescribes broadening — impossible for a residency-qualified single-metro offer. *Later:* if DR ever advertises across multiple metros with a genuinely large addressable audience.

**A second ad set for creative testing.** *Rational:* accounts that can fund parallel structures. *Not for DR:* fragments a thin budget, duplicates a small audience against itself, triggers a C2 reopen for no evidenced benefit, and Meta's own tool keeps creative in-campaign. *Later:* a finding that a second ad set solves a real problem → surface C2 T2/T3.

**Native Creative Testing right now.** *Rational:* genuinely the best-designed mechanism for this problem. *Not for DR yet:* the suggested 20% slice is a trivial absolute amount, plus a bid-strategy switch cost. *Later:* when that slice funds real delivery. **Note this rejection is about DR's budget, not about the feature's quality** (Test 10).

**Any fixed calendar refresh cadence** ("every 2–4 weeks"). *Rational:* high-frequency accounts with real fatigue curves. *Not for DR:* at ~256 reach/30 days, fatigue is not DR's binding constraint, and every number found was untraceable. *Later:* if `Creative limited` / `Creative fatigue` ever appears in DR's Delivery column — Meta's own documented fatigue signal, which is observable and free.

**Killing ads on a 4–7 day schedule.** *Rational:* accounts where 4–7 days contains hundreds of events. *Not for DR:* it would contain single-digit clicks. *Later:* only when exposure per ad becomes comparable and material.

---

## 11. Unknown / uncertain

**Does not block the operating method:**
- Whether native Creative Testing is interpretable at low delivery — Meta publishes no volume floor.
- Whether switching bid strategy to enable a creative test carries the always-significant learning cost (it appears to; no page states the interaction).
- The full Delivery-column status vocabulary (only *Creative limited* and *Creative fatigue* captured).
- Whether batching genuinely beats dripping for DR — the core D2 hypothesis, untested.
- Registration-level Meta signal is **unmeasured in the available extracts** — so State 4 is currently unreachable. **This is not proof that registrations never occurred.**

**Would change the method:**
- Delivery rising enough that individual ads become comparable → State 2–3 becomes routinely reachable, batch size re-derives, creative testing becomes fundable.
- A registration/purchase event becoming measurable → State 4 opens and the downstream quality kill becomes runnable. **This remains the single highest-value missing input across all of Wave 1 and 2.**

---

## 12. Stress-test results — 20 scenarios

| # | Scenario | Expected procedure | Classification | Result |
|---|---|---|---|---|
| 1 | 7 days, almost no data | Time is a gate, not evidence; exposure condition unmet | NOT_EVALUABLE — keep | **PASS** — §4 Time rule states this explicitly |
| 2 | New creative gets zero spend | D4 tree Branch 1 → 2 → 3 before any creative claim | NOT_EVALUABLE | **PASS** |
| 3 | 90/10 spend split | Breakdown effect; evaluate at ad set level | NOT_EVALUABLE at ad level | **PASS** — Meta's worked example carries it |
| 4 | 100/0 split | Tree distinguishes B1 technical / B2 constraint / B3 allocation / B4 exposure | Depends on branch; never collapsed | **PASS** |
| 5 | High clicks, no registration signal | State 3 ceiling | DIRECTIONAL only | **PASS** — "winner" explicitly unavailable |
| 6 | Cheap clicks, poor downstream | Downstream outranks proxy | Downstream quality kill if repeated | **PASS** — §4 and §5 both state precedence |
| 7 | Learning Limited shown | Not a penalty; not an architecture or creative trigger | No automatic action | **PASS** |
| 8 | In-season, working, needs new creative | D2 change-window procedure, one deliberate batch | Deliberate round | **PASS** |
| 9 | D1 prefers a second ad set | Surface C2 REOPEN (T2/T3) | Escalation, not silent build | **PASS** — §2 states it; D1 did not conclude this, and the conditional is recorded |
| 10 | Creative Testing exists but unfundable | Defer despite being official | Deferred | **PASS** — §8 and §10 reject on budget, not quality |
| 11 | A/B clean on CTR, no business evidence | CTR is State 3 at best | Not a business winner | **PASS** |
| 12 | Practitioner: "kill after 4 days" | Transfer mechanism, not duration | Rejected as a number | **PASS** — §9 row 3 |
| 13 | Practitioner: "test 5 ads" | Refuse without evidence; derive from capacity | 2–3 derived from DR delivery | **PASS** |
| 14 | Wave 1A objective branch changes | Method keyed to evidence states + delivery diagnostics, not objective name | Survives | **PASS** — State 4 defined by business outcome, not by a Meta event label |
| 15 | Registration absent from extracts | "Unmeasured", never "zero" | Correct language | **PASS** — §11 and §0 |
| 16 | Current live budget unknown | Capacity rule recomputed from current delivery | No hard-coded historical budget | **PASS** — §2 states the recomputation trigger |
| 17 | Creative test + audience change together | Confounded | NOT_EVALUABLE | **PASS** — §3 hold-constant table and §4 |
| 18 | Offer changes mid-round | Confounded | NOT_EVALUABLE | **PASS** — offer is in the hold-constant table |
| 19 | Ad zero spend due to delivery error | Branch 1 halts before creative judgement | State 0 | **PASS** |
| 20 | Breakdown-effect trap | Row-level causal reading blocked; ad-set-level evaluation mandated | No naive conclusion | **PASS** |

### Tests 21–26 — added by the final evidence patch (2026-08-14)

| # | Scenario | Expected | Result |
|---|---|---|---|
| 21 | **Foxwell forced-spend conflict** — clean creative gets almost no natural spend; an experienced operator argues it deserves exposure | Method must distinguish manual interference from controlled, funded exposure — and say neither "always force" nor "never obtain exposure" | **PASS (after correction)** — §5 force-spend rule now draws exactly this line: manual manipulation rejected (Meta's own informal-testing warning), controlled funded exposure permitted under five stated conditions, of which DR currently fails only the funding one |
| 22 | **2 vs 3 false precision** — what evidence proves 3 beats 2? | None exists; the method must not imply such precision | **PASS (after correction)** — relabelled **PROVISIONAL LOW-COMPLEXITY STARTING HYPOTHESIS**; §2 now states explicitly that DR's delivery cannot discriminate between reasonable small batch sizes |
| 23 | **7-day transfer** — what establishes 7 days for ordinary natural delivery? | Only Meta's A/B documentation → invalid transfer, must be removed | **PASS (after correction)** — hard gate removed from §3, §4, §6, §7 and the combined snapshot; replaced by an evidence condition. Fritts's 7-day statement retained only as weak, undated `opinion` |
| 24 | **Two-windows threshold** — what proves exactly two windows suffices? | Nothing; repetition may build confidence without becoming a mechanical rule | **PASS (after correction)** — §4 demotes "more than one window" and "same order of magnitude" from qualification rules to **confidence-building conditions**; dominated-performance kill is now explicitly operator judgement under documented conditions |
| 25 | **Foxwell ecosystem vote** — 3 ecosystem sources vs 1 independent voice | Must not resolve by count | **PASS** — §8b clusters Foxwell + Fairbrother + Fritts as **one** ecosystem; §2 resolves D1 on budget-scoping and Method 1's own stated costs, and explicitly notes the two ecosystem authors disagree with each other |
| 26 | **Method proven at $5k+/day** — DR cannot fund the same test | Principle transfers, implementation rejected/modified | **PASS** — every row of §8b and §9 records `principle_transfers` and `implementation_transfers` separately; Foxwell Method 1, Sam's packs, Fritts's 3× multipliers and Loomer's 50-events target are all principle-yes / implementation-no |

```text
tests_run: 26
tests_passed: 26
tests_failed: 0
warnings: 1
corrections_forced_by_tests: 4   (tests 21, 22, 23, 24 — all changed the final method)
```

**Warning (not a failure) — Test 14.** The method survives an objective-branch change, but **State 4 remains unreachable until registration-level signal is measurable**, which is itself dependent on unresolved Wave 1A/1B tracking questions. The dependency is on *measurement*, not on which objective is chosen. Recorded, not corrected — correcting it is not within Wave 2B's scope.

**One rule was corrected during stress testing.** An earlier draft of §4 allowed a "dominated performance" kill on a single window. Test 1 and Test 3 both broke it — one window at DR's exposure cannot distinguish weak creative from normal allocation. **Corrected to require repetition across more than one window**, which is the form now in §4. This changed the final operating method.

---

## 13. Half 2 validation contract

**H1 — Creative belongs in the existing ad set (D1).**
*Why:* Meta's own creative-introduction mechanism stays in-campaign; consolidation guidance; DR cannot fund fragmentation.
*Current evidence:* PLATFORM FACT + consolidation; no DR data.
*If true, DR should observe:* the ad set continues to accumulate delivery across rounds; introductions do not collapse delivery for more than the reset window.
*If false:* delivery degrades persistently after each introduction, or new ads never receive exposure across several rounds even when technically clean.
*Data needed:* per-ad delivery per round; ad-set delivery trend across rounds.
*Reconsider when:* the false pattern repeats across ≥2 rounds → reopen D1, and surface C2 T2/T3 before building anything.

**H2 — Batching beats dripping (D2).**
*Why:* each addition is an always-significant edit; N drips = N resets; Meta warns frequent changes leave a campaign "in flux".
*Current evidence:* PLATFORM FACT + arithmetic. **The batching preference itself is a DR HYPOTHESIS — Meta prescribes no cadence.**
*If true:* ad-set delivery stabilises faster after a single batched change than after a period of scattered edits.
*If false:* batched rounds show no stability advantage over scattered introductions.
*Data needed:* edit log with dates; delivery stability after each change window.
*Reconsider when:* two batched rounds show no advantage over a comparable scattered period.

**H3 — At current delivery, the individual ad is not a readable unit (D3).**
*Why:* DR's own arithmetic (~80–120 impressions/ad/week) plus Meta's "evaluate at ad set level" instruction.
*If true:* ad-level metrics swing wildly between windows with no stable ordering.
*If false:* ad-level ordering is stable across ≥2 consecutive windows at comparable exposure.
*Data needed:* per-ad impressions, clicks, LPVs per window, across ≥2 windows.
*Reconsider when:* stable ordering appears at comparable exposure → the ad becomes readable, and D3's directional ceiling rises.

**H4 — No-spend is allocation, not a creative verdict (D4).**
*Practitioner split:* Nick Theriot and Courtney Fritts both read non-spend as a creative signal; Meta and Foxwell's own observation describe it as normal allocation. **DR sides with the documented mechanism, not the count.**
*Why:* breakdown effect; "normal for some ads to deliver less than others"; documented non-creative causes.
*If true:* no-spend ads that survive Branches 1–2 later receive delivery when conditions change, and ads Meta starved are not systematically the ones that fail on downstream evidence.
*If false (this is the harmful case):* starved ads, when later force-exposed via a creative test, consistently underperform — meaning Meta's allocation was informative and DR wasted rounds keeping them.
*Data needed:* one creative test, once fundable, comparing previously-starved creatives under equal spend.
*Reconsider when:* that test is affordable and run.

**H5 — Start with 2–3 creatives per round (D1) — PROVISIONAL, NOT PROVEN.**
*Why we believe it:* deliberately conservative complexity-limiting choice. DR's arithmetic shows no batch size makes ads individually readable, so the only things N controls are aggregate-signal thinning and creative diversity.
*Platform evidence:* Meta's qualitative *"avoid high ad volumes"* only. **No Meta number.**
*Practitioner evidence:* Foxwell's *"2 or 3 of 10 ads get 80% of spend"* (weak, illustrative, **not adopted as a threshold**). No source supplies a defensible batch size for DR's context.
*DR context:* ~235–270 impressions/week total across the whole ad set.
*If true:* the ad set retains interpretable aggregate delivery with 2–3 ads live.
*If false:* aggregate signal degrades, or 2–3 proves too few to generate usable diversity.
*Data needed:* ad-set aggregate delivery vs active ad count per round, across rounds.
*Reconsider when:* delivery materially changes — **recompute, do not defend the number.** **The claim is "start small and re-derive", not "2–3 is correct."**

**H6 — Controlled exposure beats leaving a starved creative alone, once fundable (D4) — NEW 2026-08-14.**
*Why we believe it may be true:* credible operators (Fritts explicitly, Foxwell implicitly via Method 1) hold that early algorithmic prediction starves ads before evidence exists; Meta itself built a feature that *provides* delivery to test ads, which concedes natural allocation will not.
*Platform evidence:* native Creative Testing provides delivery and retains learnings — but ships with **no confidence level**.
*Practitioner evidence:* Fritts (`opinion`, none, undated); Foxwell Method 1 (`experience_claim`, weak).
*DR context:* the 20% test slice is currently a trivial absolute amount — condition 3 of §5 fails.
*If true:* when DR eventually funds a creative test, previously-starved creatives will show meaningfully different performance under equal spend than natural allocation implied.
*If false (the harmful case):* the starved creatives underperform under equal spend too — meaning Meta's allocation was already informative and DR wasted rounds keeping them.
*Data needed:* one native Creative Test, once fundable, including previously-starved concepts.
*Reconsider when:* that test becomes affordable. **This is the cleanest single experiment available to DR on this whole question.**

---

## 14. WAVE 2 COMBINED OPERATING SNAPSHOT

The first time Wave 2A and 2B are visible together. **This does not modify `dr-playbook.md`.**

```text
Campaigns:                  1 — no separate testing/scaling campaigns
Current ad-set approach:    1 ad set (last-known state; not a cap). New creative goes HERE
Budget placement:           Keep ad set budget. Low-stakes while one ad set exists.
                            Reopen C2 if a second ad set ever enters
Testing/scaling campaigns:  None
Creative introduction:      Into the existing ad set, one batched change window per round
Creatives per round:        2-3, derived from current delivery capacity; recompute when delivery changes
Review condition:           technically clean window AND enough delivery to classify under the D3
                            ladder. NO fixed day-count gate. Time is context, never evidence
Kill/keep:                  Technical + policy kills are immediate and need no data.
                            Dominated-performance kill requires comparable exposure repeated across
                            >1 window. Downstream quality kill requires State 4 (not yet reachable).
                            Default is KEEP while NOT_EVALUABLE
No-spend:                   Run the 5-branch diagnostic first. Unequal delivery is documented-normal.
                            Never manually manipulate delivery to force spend; controlled funded
                            exposure via a designed test is legitimate when DR can fund it.
                            Never read spend share as creative quality
Architecture reopen:        T1-T6, T7_REVISED, T8_REVISED (Wave 2A §5), plus a D1 finding that a
                            second ad set is justified -> C2 T2/T3
Evidence level:             DR HYPOTHESIS throughout. Nothing here is proven by DR results
```

**What is deliberately absent:** any spend threshold, any impression threshold, any fixed refresh calendar, any winner-declaration rule, any statistical claim. Each was considered and each was rejected for lack of defensible evidence — recorded rather than filled.

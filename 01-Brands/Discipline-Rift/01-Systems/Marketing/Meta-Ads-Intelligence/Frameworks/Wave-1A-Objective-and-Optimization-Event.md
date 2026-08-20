---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: framework
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/wave-1a-event-framework.md"
repo_path: domains/ads/meta/intelligence/output/wave-1a-event-framework.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/framework
  - discipline-rift
aliases:
  - "Wave 1A"
  - "Objective and Optimization Event Framework"
---

# Wave 1A — Objective and Optimization-Event Framework for DR

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1B-Volume-and-Budget|Wave 1B — volumen y presupuesto]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2A-Campaign-Architecture|Wave 2A — arquitectura de campaña]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Decisions/Meta-Ads-First-Decision-Synthesis|Síntesis de la primera decisión]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]
- [[01-Brands/Discipline-Rift/06-DNA/Conversion|DR Conversion DNA]]
- [[01-Brands/Discipline-Rift/06-DNA/Funnel|DR Funnel DNA]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/output/wave-1a-event-framework.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Date:** 2026-08-13 · **Revised:** 2026-08-13 (correction pass, v2)
**Questions:** A1 (objective) · A2 (optimization event) · A3 (quality vs quantity)
**Knowledge level:** **DR HYPOTHESIS / conditional decision framework.** Built from PLATFORM FACT + EXTERNAL PRACTITIONER CLAIM. **Nothing here is proven for DR.** No campaign, ad set, ad, budget, targeting, placement, Pixel or CAPI setting has been changed.
**Hands to:** Wave 1B (B1/B2/B3 — volume and budget viability)

> ### Corrections applied in v2
> An audit found six material interpretation errors in v1. All are corrected here:
> 1. **A platform-side quality lever DOES exist for website funnels** — v1 said it did not. Qualified-leads optimization works with website forms, subject to mandatory CAPI. This reopened the Leads objective and **removed v1's single-winner A1 answer**.
> 2. **R2's child-data gating is not permissible as designed** — Meta's Business Tools Terms prohibit sharing data from/about under-13s, and prohibit event *names and criteria* being based on it. R2 is now compliance-gated.
> 3. **The 10× budget figure is Meta's rule of thumb, not a viability cliff.** v1's "unaffordable regardless of learning status" overstated it.
> 4. **Haus does not evidence that Meta's platform reporting misjudges mid-funnel** — its DTC iROAS is already an incrementality metric. Corrected and downgraded.
> 5. **A published campaign objective cannot be changed at all** — v1 treated it as a significant edit. It requires a new campaign.
> 6. **"Link clicks is strictly worse at identical cost" was unsupported** — no cost-equivalence evidence exists. Replaced with the real reason.

---

## A. Final business outcome

**Paid season registration.** Parent purchases, child participates, ages 6–12, one metro, school/on-campus delivery.

Four things are **not established**, and all four now gate the objective decision below:

1. **Where registration completes** — on-site in one session, or later/offline. Meta documents server (website) events as usable for *"measurement, reporting, or optimization"*; its offline-events sentence names only measurement and audience creation.
2. **Its frequency** — DR has never measured a registration count attributable to Meta. Last measured window: **10 link clicks in 30 days**.
3. **Whether CAPI exists** — unknown in either direction (playbook Decision 7, an audit nobody has run).
4. **Whether a CRM holds registration stages and can sync them back** — unknown.

Items 3 and 4 are no longer background detail. They **decide the objective**.

---

## B. Objective — a conditional decision, not a winner

v1 named Sales as the candidate. That rested on the claim that no quality lever existed for website funnels, which was wrong. With the lever restored, the two objectives trade against each other and **the evidence does not support ranking one above the other before DR ground truth is known.**

This decision is unusually expensive to get wrong: **Meta states *"You cannot change your published campaign objective. You can always stop your campaign and create a new one if you want to change the objective."*** Switching later means abandoning that campaign, not editing it.

### The two candidates

| | **Sales → Website** | **Leads → Website** |
|---|---|---|
| Accepts `Complete registration`? | Yes | Yes |
| Also accepts `Purchase`? | Yes | No |
| Deep goals | Maximize number of conversions; Maximize value of conversions | Maximize number of leads; **Maximize number of qualified leads** |
| Shallower rungs inside the objective | **Yes** — landing page views, link clicks, daily unique reach, impressions | **No** shallower "Other goals" row documented for Leads → Website |
| Platform quality lever | None | **Yes** — qualified leads, fed by CRM lead stages via CAPI |
| Hard prerequisites | Pixel + the chosen event firing | Pixel + **CAPI (mandatory)** + CRM with lead stages syncing per status update |

### What each buys

**Sales → Website buys structural flexibility.** It is the only Website combination documented as holding both the deep conversion goals and the shallow landing-page-view / link-click rungs. Because *"The performance goal of your ad set can be different from your ad objective"*, DR could move down the ladder when the deep event proves too rare — and do it as an **ad-set edit rather than a new campaign**. On an account whose central risk is that the deep event never fires often enough, that optionality is worth real money.

**Leads → Website buys a quality feedback loop.** It is the only path to *"Maximize number of qualified leads"* — the one documented mechanism where DR could tell Meta *which* registrations actually became paid, and have delivery optimize toward people like them. For a business whose failure mode is cheap unqualified interest, that is the most direct answer A3 has. Meta reports *"9.5% lower cost per quality leads"* for website forms (Meta's own aggregate, no methodology published — an assertion, not evidence).

But it is conditional on infrastructure DR may not have, and on a definitional question — whether DR's registration flow is a "website form" in Meta's sense — that Meta does not resolve.

### Conditional decision rule

**If** an audit establishes that (a) CAPI is live or can be stood up, (b) a CRM holds paid-registration status and can sync per-lead updates, and (c) DR's registration flow qualifies as a website form — **then Leads → Website with qualified-leads optimization is the stronger candidate**, because it is the only configuration that buys quality directly rather than inferring it afterward.

**Otherwise Sales → Website**, because it keeps the whole ladder inside one campaign and depends on no infrastructure DR lacks.

**Either way, `OUTCOME_TRAFFIC` should not be retained.** Meta documents Traffic → Website as requiring *"No conversion event required."* DR's present campaign structurally never asks Meta to find people likely to register. That finding survives the correction pass unchanged and is the clearest defect the wave surfaced.

Engagement → Website remains a documented third path (Loomer's route for a custom quality event) but its event list **excludes `Complete registration`**. Instant Forms would unlock the strongest version of the quality lever but replaces DR's registration funnel with a lead-capture funnel — a business-process change, not a setting.

**Practitioner input on this question remains thin and one-sided.** Only Jon Loomer addresses it directly, arguing for Sales on feature availability (`weak`, `PARTIALLY_SUPPORTED`) — and he wrote before qualified-leads reached website forms, so his reasoning does not account for the trade above.

---

## C. Optimization-event ladder

Ranked from closest to business value outward. Rungs move within a chosen objective; **moving between rungs is an ad-set edit, not free** — a change of optimization event is a significant edit and resets that ad set's learning. It is nonetheless far cheaper than an objective change, which requires a new campaign.

### R0 — `Purchase` (Sales objective only)
- **Optimizes toward:** people likely to complete a purchase event on the website.
- **Quality:** highest — it is the business outcome. **Volume:** lowest.
- **Failure mode:** fires too rarely for delivery to stabilise; Meta names *"an infrequent optimization event"* among its causes of learning limited.
- **Viable only if** registration completes on-site with payment, and frequency supports it.

### R1 — `Complete registration` (both objectives)
- **Optimizes toward:** people likely to complete the registration event.
- **Quality:** very high — the closest standard event to DR's actual outcome. **Volume:** very low at current spend.
- **Failure mode:** as R0. Also, if registration is free-then-pay-later, R1 is not the *paid* outcome and can reward non-payers.
- The natural default rung if volume permits.

### R1q — `Maximize number of qualified leads` (Leads objective only) — **new in v2**
- **Optimizes toward:** *"the people in your audience who are most likely to convert after sharing their contact information with you."*
- **Quality:** highest available *without* requiring the deep event itself to be frequent — quality comes from CRM feedback rather than from event depth.
- **Volume:** the optimization event remains the lead; quality is learned from stage data fed back.
- **Prerequisites:** CAPI mandatory (April 2026 for new campaigns, August 2026 for existing); CRM syncing *"CRM events for each lead status update"*; website-form applicability unconfirmed.
- **Failure mode:** without genuine CRM feedback it degrades toward plain lead optimization; and it presumes enough leads for Meta to learn a quality pattern.
- **Sits beside R1 rather than above it** — a different mechanism, not a deeper rung.

### R2 — Qualified custom event — ⚠️ **COMPLIANCE GATE, not buildable as specified in v1**
- **Intended:** a custom event firing only when DR's eligibility criteria are met, keeping the event shallow enough to fire while carrying qualification.
- **Blocking constraint (PLATFORM FACT):** Meta's Business Tools Terms — *"you will not share Business Tool Data with us that (i) you know or reasonably should know is from or about children under the age of 13"* — and, decisively, *"The names you choose and criteria you establish for your events, conversions, and any custom audiences you create must not reflect, imply or be based on any category of information described in this Section 1.h."*
- **DR's participants are 6–12 — entirely under 13.** v1 proposed gating on child age band and school. **That design is not permissible**: it is prohibited in the payload, and prohibited again in the event's name and criteria.
- **What may stay internal:** DR evaluating eligibility inside its own systems is not Business Tool Data. The restriction governs what is *shared with Meta*.
- **What is unverified:** whether an internally-evaluated, generically-named event — child data never leaving DR — is acceptable when its *criteria* are nonetheless DR's child-eligibility rules. A plain reading of the "criteria" sentence may still capture it. **Nothing retrieved settles this.**
- **Status: DR HYPOTHESIS + implementation/compliance gate.** No R2 build may proceed without a compliance review that addresses the criteria sentence, not just the payload.

> **Standing rule.** No implementation of R2, or of any DR optimization event, may place under-13 data or other prohibited information into Meta Business Tools — not in the payload, not in the event name, not in the criteria that fire it.

### R3 — `Landing page view` (DR's current setting, under the wrong objective)
- **Optimizes toward:** *"people who are most likely to click on and load your chosen landing page."*
- **Quality:** low — no expressed intent to register. **Volume:** highest of the usable rungs.
- **Failure mode:** the central A3 risk. Loomer: *"Whenever the algorithm optimizes for top-of-the-funnel engagement, it cares only about volume of those actions and not the quality of them."* Meta's own framing is consistent — the performance goal is *"the desired outcome that our system bids on in the ad auction"* — though Meta adds *"we may prioritize higher-quality clicks."*
- **Use as** a deliberate floor while deeper rungs are unreachable, never as a destination, and never without §D safeguards running.

### R4 — `Link clicks` — deprioritised (corrected reasoning)
v1 claimed this was "strictly worse than R3 at identical cost." **No cost-equivalence evidence exists and that claim is withdrawn.** The real reason: Meta's own definitions separate clicking (`LINK_CLICKS`) from clicking *and loading* (`LANDING_PAGE_VIEWS`). **LPV therefore contains an additional observable step — the page actually loaded — making it a richer behavioural signal for a website funnel.** Cost per result may well differ between the two goals; nothing retrieved establishes their relative cost. R4 is deprioritised for DR on signal-richness grounds, and because a click that never loads the page cannot lead to a registration.

### Switch conditions

Stated as conditions, not cliffs. The only figures used are Meta's own, with Meta's own hedging preserved.

**Reference points, not thresholds:**
- **Learning:** an ad set is learning limited when *"unlikely to receive **about** 50 optimization events in the week after your last significant edit."* Meta hedges this — ad sets exit learning *"as soon as they can deliver stably"*, and *"Learning limited isn't a penalty."*
- **Budget:** *"**In general**, your daily budget should be at least 10 times the average cost of your performance goal."* This is Meta's **rule of thumb**, given as budgeting guidance. It is **not** an eligibility requirement, a viability threshold, or a statement that Meta cannot optimize below it. Falling short means the budget is thin relative to the event's cost — a reason for caution and measurement, **not** an automatic disqualification of that rung.

**Consider moving DOWN (deeper → shallower) when:** the current rung shows persistent inability to accumulate events, delivery is unstable or negligible, and the budget is far below the 10× reference for that event's cost. Meta's own prescribed remedy is exactly this move — *"Consider choosing an optimization event that occurs more frequently"* — so going up-funnel when the deep event is too rare is **platform-sanctioned**.

**Do NOT move down merely because** the rung is under ~50/week or under 10×. Kerhoas dissents directly — *"Many businesses won't hit 50 conversions per week per ad set… That's not a reason to panic or rebuild"* — and Meta states *"Learning limited isn't a penalty."* Persistent learning-limited operation is a cost (Meta: less stable, usually higher CPA), not a disqualification.

**Consider moving UP (shallower → deeper) when:** the deeper rung's observed frequency and budget-to-cost ratio both improve. Re-test rather than assume; the deeper rung is preferred whenever reachable.

**Stop climbing up-funnel when** (Vigneron): *"Going too far up the funnel for your proxy metrics gives the algorithm license to prioritize lower-value activity."* Operationally — stop at the shallowest rung whose ratio to actual registrations stays stable (§D).

**Never change a rung and another variable in the same edit.** Each is a significant edit and resets learning; two at once yields an uninterpretable result on an account this thin.

---

## D. Quality safeguards

### S0 — The platform lever (corrected; v1 wrongly said none existed)

**`Maximize number of qualified leads`, under the Leads objective, works with website forms.** DR would feed paid-registration status back from a CRM through CAPI, per lead status update, and Meta would optimize toward people likely to reach that stage.

Prerequisites, all currently unknown for DR: CAPI live (**mandatory** since April 2026 for new campaigns); a CRM holding registration status; per-status-update syncing; and confirmation that DR's registration flow counts as a "website form."

**If those hold, S0 is strictly the best safeguard available** — it is the only one that changes *who Meta looks for*, rather than detecting a problem after the money is spent. If they do not hold, S1–S4 are all DR has.

### S1–S4 — DR-side safeguards

| # | Safeguard | Method | Applies to |
|---|---|---|---|
| S1 | **Ratio monitoring** | Track proxy events ÷ actual paid registrations over time; a rung is failing when the ratio drifts upward — more events, no more registrations. Vigneron: *"Calculate a ratio of proxy events to desired events"*, checking **stability** *"across campaigns, segments, and time periods"*. Needs bookkeeping, not statistical power — which is why it works at DR's scale. | R1q, R2, R3 |
| S2 | **Correlation check before adopting a rung** | Gardideh: the event should correlate with the outcome (he states ≥0.6, with no derivation shown — treat the *test* as the contribution, not the number) and occur *"within the first 1-3 days"* of the click. | R2, R3 |
| S3 | **Qualification carried by the event** | ⚠️ **Compliance-gated — see R2.** Permissible only if it can be built without child-derived data in the payload, the name, or the criteria. Unverified. | R2 only |
| S4 | **Don't judge a rung by one headline number** | A proxy-event CPA must ultimately be checked against downstream paid registrations, because a rung can look efficient on its own metric while producing nothing. **This principle stands on its own logic — it is NOT proven by the Haus source**, whose DTC iROAS is an incrementality metric and whose halo mechanisms DR does not have. | all rungs |

### What Half 2 must supply

None of S1–S4 is runnable today, and S0's prerequisites are unaudited. Required and currently missing:

1. **Registration-level truth** — how many paid registrations arrived, and when.
2. **A join between registrations and ad exposure** — even coarse weekly counts against weekly spend makes S1 possible.
3. **Qualification data on registrants**, held **internally** — to test whether delivery reaches qualified parents (the AUDIENCE axis). Internal use is unrestricted; transmission to Meta is not.
4. **Conversion/action columns in the DR extract** — no insights CSV currently contains any actions, conversions or landing-page-view column.
5. **Pixel/CAPI reality established** — now doubly important, because CAPI is a hard prerequisite for the S0 lever and therefore for the Leads branch of the objective decision.

Items 4 and 5 are already-scoped Half 2 work. **They are not blockers on building a framework; they are blockers on knowing whether it worked — and item 5 is now also a blocker on the objective choice itself.**

---

## What would change this framework

- **The CAPI/CRM audit comes back positive** → the Leads branch activates and S0 becomes available; the objective decision resolves toward Leads → Website.
- **The audit comes back negative, or "website form" turns out not to cover DR's flow** → Sales → Website, and A3 falls back to S1–S4 alone.
- **Registration completes off-website** → R0/R1 may be unavailable for optimization; the ladder compresses and the omnichannel conversion location needs investigation.
- **Compliance review clears an internally-evaluated generic event** → R2 becomes buildable. If it does not, R2 is struck and the ladder runs R1q / R1 / R3.
- **Wave 1B finds the budget far below the 10× reference for every rung** → the honest output is that delivery will be thin and evidence slow to accumulate, and the business must decide whether to fund more or accept a long, low-confidence read. **It is not a finding that Meta "cannot" be asked to find registrants.**
- **DR data eventually shows R3 delivering registrations at acceptable cost** → the anti-up-funnel position weakens for DR specifically, whatever practitioners say.

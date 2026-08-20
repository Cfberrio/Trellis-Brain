---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-questions.md"
repo_path: domains/ads/meta/intelligence/knowledge/research-questions.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/method
  - discipline-rift
aliases:
  - "Meta Ads Research Questions"
  - "Backlog A1-S2"
---

# Research Question Backlog — Meta Ads Intelligence

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Operating-Rules|Reglas de operación del dominio]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/research-questions.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Created:** 2026-08-13
**Purpose:** the decision-driven backlog for the next research phase. Research is driven by these questions, not by a list of gurus. Every retrieval in the next phase must serve a question here.
**Stopping rule:** evidence saturation, per question — a question closes when additional credible independent evidence is unlikely to materially change the decision. There is no source quota. See `../CLAUDE.md §Evidence saturation`.

**DR, for research purposes:** a local youth-sports registration business — constrained geography (Orlando), parent purchasers, child participants (6–12), relatively low advertising volume, final desired outcome = paid season registration. DR is **not** pre-categorized as lead-gen; the right objective is question A below. Current spend context (~$2.70/day, campaign paused, data 2026-05-12) is preserved as transferability context, not as a fixed constraint.

**Statuses:** `OPEN` · `RESEARCHING` · `ENOUGH_EVIDENCE` · `NO_USEFUL_EVIDENCE_FOUND` · `DEFERRED` · `REOPENED`

**Contract per question:** `decision_impact` · `current_evidence` · `current_conflict` · `DR_context` · `evidence_needed` · `preferred_source_context` · `stop_condition` · `status`

**Question IDs are stable identifiers.** `ads-meta-intel-ingest` validates every ingest's `research_question_ids` against this file, and `ads-meta-intel-research` takes them as input. Never renumber; retire an ID by status, not by deletion.

**Numeric threshold rule (binding on every stop_condition):** never force an exact numerical threshold when credible evidence does not establish one. A conclusion may be a range, a conditional rule, an observable revisit trigger, a qualitative minimum condition, or "no defensible numeric threshold found." Exact numbers only with traceable evidence. A stop_condition that mentions a threshold is satisfied by any of these honest forms.

---

## Research waves — scope control for retrieval

Only the **current wave** receives active discovery/retrieval effort. Later-wave questions may collect incidental evidence when a retrieved source directly contains it, but discovery is never broadened to chase them. This prevents scope explosion, not progress.

| Wave | Questions | Theme | Gate to start |
|---|---|---|---|
| **Wave 1A — Outcome + signal** | A1 · A2 · A3 | business outcome, Meta objective, optimization-event ladder, event quality vs quantity | **Run 2026-08-13; corrected same day; gate PASSES on the corrected framework (v2).** See `output/wave-1a-event-framework.md` and `knowledge/research-runs/2026-08-13_A1-A2-A3.md`. A1 RESEARCHING (conditional decision rule, blocked on a DR audit not on research); A2 and A3 REOPENED after the correction pass. No campaign changes occurred. |
| **Wave 1B — Volume + budget viability** | B1 · B2 · B3 | volume conditions for useful learning, what stays learnable below them, budget logic, viability of 1A's preferred event | **Run 2026-08-13. B1 ENOUGH_EVIDENCE, B3 ENOUGH_EVIDENCE, B2 OPEN (closed as far as external evidence allows — no credible cost source found; DR has no registration-cost data of its own). No A2/A3 reopen triggered.** See `output/wave-1b-volume-budget-framework.md`. |
| **Wave 2A — Campaign architecture** | C1 · C2 · C3 · C4 | campaign count, budget placement, testing/scaling **campaign** separation, revisit triggers | **Run 2026-08-14; patched same day after external audit. All four ENOUGH_EVIDENCE (C2 conditional; C3 at campaign level only). ARCHITECTURE GATE: PASS.** Hypothesis: 1 campaign / keep ad set budget / no separate testing+scaling campaigns. **Ad-set-level creative introduction is NOT decided — it belongs to D1.** See `output/wave-2a-campaign-architecture-framework.md`. No Wave 1 question reopened. |
| **Wave 2B — Creative operating method** | D1 · D2 · D3 · D4 | creative batch size, **same-ad-set vs new-ad-set introduction**, cadence, kill/keep rules, no-spend interpretation | **Run 2026-08-14; final external-evidence patch applied same day. All four ENOUGH_EVIDENCE (D1/D2/D3 conditional; D3 numeric layer `NO_USEFUL_EVIDENCE_FOUND`). CREATIVE OPERATING GATE: PASS. WAVE 2 FINAL GATE: PASS — external Wave 2 research CLOSED.** Method: existing ad set · start with 2–3 per round (**provisional, not a proven optimum**) · one batched change window · review on an **evidence condition, no day-count gate** · 5-branch no-spend diagnostic · manual force-spend rejected but **controlled funded exposure permitted when fundable**. 26/26 stress tests passed (20 original + 6 added by the patch; 4 forced corrections). **No C1/C2 reopen triggered.** See `output/wave-2b-creative-operating-method.md`. |
| **Wave 3 — Audience + measurement** | E1 · E2 · E3 · G1 · G2 | targeting configuration, message/targeting division, attribution, metric layers | **Run 2026-08-14. All five ENOUGH_EVIDENCE (conditional); E2/G2 practitioner layers `NO_USEFUL_EVIDENCE_FOUND`. WAVE 3 GATE: PASS. PRE-EXECUTION RESEARCH GATE: PASS — foundational external research CLOSED.** Locations hard / no interests / campus-radius union in one ad set / 7-day click + 1-day view / four-layer measurement contract. 30/30 stress tests. **No C1/C2/Wave-1 reopen.** See `output/wave-3-audience-measurement-framework.md`. |
| Deferred outside waves | F1 (retargeting — until volume/pool makes it relevant) · S1, S2 (scaling — until Half 2 produces a working base) | — | — |

**Wave 1 rationale:** account architecture should not be designed before we understand what outcome Meta is being asked to optimize toward and whether DR can generate enough signal to learn from it.

### Why Wave 1 splits into 1A → 1B

B1 is written as *"given the selected optimization event…"* — B is **parameterized by A**. Researching budget before an event framework exists means costing an outcome nobody has chosen. So 1A runs first.

**Wave 1A parameterization gate** — 1A hands 1B four things:

1. the candidate campaign objective;
2. a defensible optimization-event ladder;
3. the switch conditions between event levels;
4. the quality safeguards each candidate event requires.

The ladder may be **conditional and provisional** — e.g. a preferred event where signal suffices, a fallback under stated conditions, and up/down-funnel alternatives with explicit tradeoffs. Research determines its real shape; do not treat any illustrative shape as the answer.

**This gate is not "all A research is finished."** It is "enough of an event/objective framework exists to parameterize B." Requiring final saturation of A before B would deadlock the wave, because B is often what *tests* whether A2's preferred event is viable at all.

### The 1A ⇄ 1B feedback loop

```
1A → 1B → viability check → (if needed) REOPEN A2/A3 → re-evaluate B
```

If 1A prefers optimizing toward final registration but 1B shows DR cannot plausibly generate enough final-registration signal at available spend/volume, that evidence **must** be allowed to reopen A2's ladder (status → `REOPENED`, dated, with the B finding that triggered it). The first A answer is never immutable.

**Wave 1 final exit:** A and B together support a defensible initial DR decision framework covering objective · optimization-event ladder · event quality safeguards · signal-volume expectations · budget/learnability logic · what low-volume results can and cannot prove.

That framework is external research and DR HYPOTHESIS territory. **It is not proof that the structure works for DR** — only Half 2 produces that.

---

# P0 — BEFORE FIRST SERIOUS DR CAMPAIGN

## A. Optimization / business outcome — **Wave 1A**

### A1 — What campaign objective best maps to DR's paid-registration funnel?

- **decision_impact:** determines the campaign's objective on relaunch (current campaign is `OUTCOME_TRAFFIC` — never evaluated), what Meta optimizes delivery toward, and the success metric of every later experiment.
- **current_evidence:** none. No expert or official-meta file addresses objective choice for a registration funnel. Both ingested practitioners assume ecommerce purchase optimization.
- **current_conflict:** none recorded — the question has never been researched.
- **DR_context:** funnel is ad → landing page → registration form → paid registration. Whether registrations complete online in one session, or arrive delayed/offline, is itself unverified (Half 2 ground-truth item).
- **evidence_needed:** current Meta documentation of objective/event options for conversion-style funnels; practitioner evidence from registration/appointment/enrollment businesses on which objective they run and why; explicit treatment of low-volume tradeoffs.
- **preferred_source_context:** local services, education/enrichment, registration or appointment businesses; Meta first-party docs.
- **stop_condition:** stop when current Meta objective/event mechanics are understood first-hand AND the available practitioner evidence for comparable registration businesses points to a recommendation that additional sources are unlikely to materially change — including an explicit statement of what would change it (e.g. observed DR registration volume).
- **status:** **RESEARCHING** (2026-08-13, Wave 1A; **revised same day after correction pass**) — Meta mechanics are first-hand and now more complete: Traffic→Website requires no conversion event; `Complete registration` is available under both Leads→Website and Sales→Website; Sales→Website uniquely holds the shallower rungs; **Leads→Website uniquely holds the qualified-leads quality lever**; and a published objective **cannot be changed at all** (new campaign required), which raises the cost of choosing wrong.
  **The v1 single-winner answer (Sales) has been withdrawn.** It rested on the incorrect conclusion that no quality lever existed for website funnels. The corrected position is a **conditional decision rule** in `output/wave-1a-event-framework.md`: Leads→Website if a CAPI/CRM audit clears three prerequisites, otherwise Sales→Website.
  Two blockers remain, and **neither is external research**: (1) a DR-side audit of CAPI/CRM/website-form applicability; (2) the practitioner gap — still no source from a comparable registration business, and the one source that addresses objective choice (Loomer) predates qualified-leads reaching website forms.

### A2 — What event should DR optimize toward at its realistic volume, and when does optimizing further up the funnel make sense?

- **decision_impact:** the optimization event defines what Meta's delivery learns from and what every experiment measures. Choosing registration vs an intermediate event (lead/form-start/LPV) changes budget requirements (see B) and diagnosis design.
- **current_evidence:** PLATFORM FACT — learning-limited threshold framing (~50 optimization events/week, `official-meta/learning-limited.md`); ad set currently optimizes `LANDING_PAGE_VIEWS`. No practitioner evidence on up-funnel fallback strategy.
- **current_conflict:** none recorded.
- **DR_context:** last measured window produced 10 link clicks in 30 days — final-registration volume is plausibly far below any learning threshold; an intermediate event may be structurally necessary at first. That is a hypothesis, not a decision.
- **evidence_needed:** Meta docs on event selection and event quality vs quantity; practitioner evidence on optimizing up-funnel when the end event is rare, and on the failure modes (optimizing toward cheap non-buyers).
- **preferred_source_context:** low-volume conversion accounts; local/registration businesses; Meta first-party docs.
- **stop_condition:** stop when the event ladder (registration → intermediate → LPV) can be ranked for DR with stated switch conditions in both directions, and further evidence would only re-shuffle details, not the ladder.
- **status:** **REOPENED** (2026-08-13, correction pass) — was ENOUGH_EVIDENCE earlier the same day; **the correction pass materially re-shuffled the ladder, which is precisely what the stop_condition says must stop happening before it closes.** Changes: a new rung `R1q` (qualified-leads optimization) was added from platform documentation the first pass had misread; `R2` was **compliance-gated** and is not buildable as specified; `R4`'s exclusion reasoning was withdrawn and replaced; and the ~50/week and 10× figures were corrected from thresholds to hedged reference points.
  The ladder is in better shape than v1 and remains usable for Wave 1B. But a ladder that gained a rung and lost another within hours has not demonstrated stability. **To close:** resolve the R2 compliance question and the offline-vs-server optimization asymmetry. Note the practitioner layer is not the weak link here — **both corrections came from first-party platform documentation**, so further practitioner discovery is not the remedy.

### A3 — How should event quality vs event quantity be balanced?

- **decision_impact:** guards against the classic failure of up-funnel optimization: high event volume, zero registrations.
- **current_evidence:** none beyond general signal-quality rules in `.claude/rules/ads/shared.md` (internal principle, not evidence).
- **current_conflict:** none recorded.
- **DR_context:** parent purchaser with a multi-day decision; a cheap click is easy to buy and worthless if the child is out of age band or out of geography.
- **evidence_needed:** practitioner evidence on quality checks for up-funnel events (lead scoring, downstream conversion-rate monitoring); Meta docs on event quality tools if any apply at DR scale.
- **preferred_source_context:** lead-quality-sensitive local businesses.
- **stop_condition:** stop when a concrete quality-check method exists for whatever event A2 selects, checkable with data DR can actually obtain.
- **status:** **REOPENED** (2026-08-13, correction pass) — was ENOUGH_EVIDENCE earlier the same day on a **finding that turned out to be false**. v1 concluded *"no platform-side lever exists for a website registration funnel"*, based on one developer page. Current Help Centre documentation states the opposite: *"This performance goal can be used with both website forms and instant forms"*, with Conversions API integration now mandatory (April 2026 new campaigns, August 2026 existing).
  Consequences: a genuine platform lever (**S0**) is added and is strictly the strongest safeguard if its prerequisites hold; safeguard **S3** (qualification carried by the event) is now **compliance-gated** — Meta's Business Tools Terms prohibit sharing data from/about under-13s and prohibit event *names and criteria* being based on it, and DR's participants are 6–12; and **S4's attribution to Haus was withdrawn** as an over-read.
  **To close:** (a) audit whether DR has CAPI and a CRM with registration stages; (b) confirm whether DR's registration flow qualifies as a Meta "website form"; (c) resolve whether an internally-evaluated, generically-named eligibility event is permissible under the "criteria" sentence. (a) and (b) are DR audits; (c) may need Meta or legal input. None is a practitioner-research task.

## B. Minimum viable learning volume / budget — **Wave 1B** (gated on the 1A parameterization gate)

**Do NOT pre-answer with a dollar figure.** Budget is derived: outcome/event choice → realistic cost per event → volume needed to learn → budget range. Solving budget independently of the outcome being purchased is the error this section exists to prevent — which is why this whole section waits on Wave 1A's event ladder, and why B findings may reopen A2/A3.

### B1 — Given the selected optimization event, what event volume is needed for useful delivery/learning?

- **decision_impact:** defines whether any given budget can produce interpretable evidence at all; gates every experiment.
- **current_evidence:** PLATFORM FACT — learning-phase and learning-limited docs (~50 events/week framing, "learning limited isn't a penalty"); documented minimum daily budgets exist in `official-meta/optimization-goals-and-attribution.md`.
- **current_conflict:** none.
- **DR_context:** four of Meta's five named learning-limited causes already describe the account at last extract.
- **evidence_needed:** Meta's current budget-minimum and learning mechanics applied to the chosen event; practitioner evidence on what remains learnable below thresholds (directional reads, creative signals) vs what does not.
- **preferred_source_context:** small-account practitioners; Meta first-party docs.
- **stop_condition:** stop when, for the chosen event, we can characterize the volume conditions for stable delivery (as a range or conditional rule — a numeric figure only if credible evidence establishes one), plus what is still learnable below them and what is not — and further sources would not materially move those lines.
- **status:** **ENOUGH_EVIDENCE** (2026-08-13, Wave 1B) — volume conditions characterized as a range/condition anchored to Meta's own ~50/week reference and DR's own historical delivery (metric-specific: ~9 landing page views in one referenced 30-day window; ~10–11 clicks across reported windows — **not one interchangeable event category**); what's learnable below it (delivery health, gross waste, directional trend) vs. not (fine-grained winner calls) is stated. See `output/wave-1b-volume-budget-framework.md §1`. Practitioner layer (Kerhoas dissent, already ingested) converges with Meta's own text; no further discovery needed.

### B2 — What budget range can realistically create that volume, and at what point is DR's budget too low for the chosen objective to produce interpretable evidence?

- **decision_impact:** produces the budget recommendation the business must then decide on — the audit's "Decision 0". Also defines the honest floor: below X, running ads buys impressions, not evidence.
- **current_evidence:** none applicable. Both practitioners' cheapest tactics ($5/day nudge, $100/day minimums) exceed or dwarf DR's current spend; no source addresses sub-$10/day.
- **current_conflict:** none — absence of evidence, not disagreement.
- **DR_context:** ~$2.70/day historical; cost per registration unknown (no conversion data in extracts — Half 2 item).
- **evidence_needed:** realistic cost-per-event ranges for comparable local youth/enrichment offers (competitor context, practitioner cases, any credible benchmark with methodology); arithmetic linking B1's volume to a budget range.
- **preferred_source_context:** local youth activities, enrichment programs, registration businesses in comparable metros.
- **stop_condition:** stop when a defensible budget range (with stated assumptions) and an honest characterization of the interpretability floor — as a range, conditional rule, or qualitative condition; an exact figure only if credible evidence establishes one — can be handed to the business as a decision. Never manufacture a magic number.
- **status:** **OPEN, closed as far as external evidence allows** (2026-08-13, Wave 1B) — DR's own historical cost data (LPV ≈ $12.25, link-click $8–37) applied against Meta's 10× reference; DR runs ~30–45× under it on its shallowest rung. **No credible external cost-per-registration source exists** — ~25 candidates screened, zero survived (content-farm CPL aggregation, unsourced/conflicting learning-phase folklore, one promotional case study with no spend/denominator disclosed). Registration-rung cells are honestly left unfillable rather than estimated. See `output/wave-1b-volume-budget-framework.md §2, §5`. Reopen when DR records its first Meta-attributed registration or a genuinely comparable source surfaces.

### B3 — What can still be learned at low volume versus what cannot?

- **decision_impact:** if the business keeps budget low, this defines the honest research program (directional creative reads, qualitative signals) instead of pretending experiments are powered.
- **current_evidence:** internal only — `output/experiments.md` already frames directional-read methodology; no external evidence.
- **current_conflict:** none.
- **DR_context:** experiments v1 are all gated and explicitly unpowered at current spend.
- **evidence_needed:** practitioner approaches to low-volume decision-making that avoid false conclusions; any Meta guidance on interpreting sparse delivery data.
- **preferred_source_context:** small local advertisers; skeptical/measurement-focused practitioners.
- **stop_condition:** stop when experiments v2 can state, per experiment type, whether it is readable at the chosen budget — with reasoning a critic could check.
- **status:** **ENOUGH_EVIDENCE** (2026-08-13, Wave 1B) — boundary stated using DR's own actual data as the worked example (its 9–11 clicks/30d is the literal "3 clicks vs 2" case the task warns against); two-label DIRECTIONAL / SUFFICIENTLY_STRONG framework defined for future reads. See `output/wave-1b-volume-budget-framework.md §3`.

## C. Campaign architecture

### C1 — One campaign vs multiple campaigns for DR?

- **decision_impact:** the base architecture of the relaunch.
- **current_evidence:** EXTERNAL — Sam Piliero: four-campaign separation (`self_reported_case_study`, moderate, ecommerce, $1k/day). Nick Theriot: one CBO for testing+scaling (`experience_claim`, weak, ecommerce). PLATFORM FACT — three Meta pages support consolidation as a direction; Meta never says one campaign is sufficient. Playbook v1: keep 1/1/1 at current volume (HIGH confidence, driven mainly by scale logic).
- **current_conflict:** the two ingested practitioners directly disagree; both are ecommerce voices from overlapping discourse.
- **DR_context:** currently 1 campaign / 1 ad set / 1 ad, paused.
- **evidence_needed:** independent practitioner evidence outside the current two — ideally from low-volume and/or registration/local contexts; anything that would overturn the consolidation-at-low-volume logic.
- **preferred_source_context:** local services, low-volume accounts; a third+ independent structural voice of any business type.
- **stop_condition:** stop when current Meta mechanics are understood and additional independent practitioner evidence no longer materially changes the single-vs-multi-campaign recommendation for a low-volume, geo-constrained registration business — including the scale threshold at which the answer flips (C4).
- **status:** **ENOUGH_EVIDENCE** (2026-08-14, Wave 2A) — **one campaign.** What saturated it: the platform layer is now understood first-hand, and it identifies exactly one platform-forced driver of campaign count — the objective is campaign-level and *"You cannot change your published campaign objective"* — which does not apply, since DR needs one objective under either Wave 1A branch. The Sam/Nick conflict is resolved **for DR by context, not by vote**: both are ecommerce at 30–370× DR's spend, and Sam's architecture carries preconditions DR does not meet. Discovery found **no credible independent practitioner source** — the available corpus is content-farm material issuing untraceable campaign-count numbers, rejected under the source-quality and numeric-threshold rules. **Revisit condition:** triggers T1 (a second simultaneous objective becomes necessary), T7 (structure delivers stably and volume could support a split), T8 (geographic expansion beyond the Orlando metro) — `output/wave-2a-campaign-architecture-framework.md §5`. Explicitly NOT triggers: ~50 events/week, the 10× budget heuristic, or any practitioner dollar figure.

### C2 — CBO/Advantage+ campaign budget vs ad-set budgets for DR?

- **decision_impact:** budget placement on relaunch; interacts with creative testing (D) and minimum budgets (B).
- **current_evidence:** PLATFORM FACT — **gap closed 2026-08-14**: `official-meta/campaign-budget-and-consolidation.md` now holds first-hand Meta documentation of both modes. Decisive items: Advantage+ campaign budget is *"best suited for campaigns with at least 2 ad sets"*; its entire documented function is allocation **across ad sets**; Meta's stated criteria for ad set budgets are all comparisons *between* ad sets (per-ad-set control, differing value, large audience-size difference, mixed optimization goals or bid strategies); Meta routes hard per-ad-set budget requirements toward ad set budgets rather than campaign-budget spend limits; and **Meta publishes no performance claim for either mode.** EXTERNAL — Jon Loomer ingested 2026-08-14 (5 claims, all C2; 3 `experience_claim`/weak, 2 `opinion`/none; 3 PARTIALLY_SUPPORTED, 1 INSUFFICIENT_EVIDENCE, 1 NOT_APPLICABLE); both prior practitioners assume CBO without arguing it against ABO.
- **current_conflict:** none direct on this axis; the conflict is on campaign count, not budget level.
- **DR_context:** single ad set; question **confirmed near-moot at 1 ad set** — every criterion Meta publishes for choosing a mode is a comparison between ad sets, and allocation/control are identical when only one exists. It decides what testing looks like the moment a second ad set exists.
- **evidence_needed:** first-hand Meta documentation of current CBO/Advantage+ budget behavior (fills the official-meta gap); practitioner evidence at low budgets.
- **preferred_source_context:** Meta first-party docs first; then small-account practitioners.
- **stop_condition:** stop when Meta's current CBO mechanics are documented first-hand and the CBO-vs-ABO call for DR's volume — with its flip conditions — would not materially change with more sources.
- **status:** **ENOUGH_EVIDENCE (conditional)** (2026-08-14, Wave 2A; rationale simplified 2026-08-14 after external audit) — **keep the ad set budget for now**, a low-stakes keep decision rather than a performance claim. What saturated it: Meta's own mechanics and decision criteria are now first-hand, and they resolve the single-ad-set case — allocation and control are identical at one ad set, so only the future-architecture dimension carries weight. **This is a KEEP / no-unnecessary-change decision, not a performance finding** — Meta publishes no performance claim for either mode, and nothing establishes that ABO beats Advantage+ campaign budget for DR. The primary reason is the absence of a reason to change: A+CB's only documented benefit is cross-ad-set allocation, and the mode switch's own learning cost is unestablished. *Secondary context only:* keeping the ad set budget preserves a future second ad set on a different performance goal (Loomer, `PARTIALLY_SUPPORTED`, weak — explicitly not the basis of today's decision). **Not saturated as a general question** — three uncertainties remain, none blocking: whether a mode switch is a significant edit (unknown, which is itself why the branch-safe option was chosen), first-party A+CB eligibility text (practitioner-sourced only), and `ad set budget sharing` (Meta's uncaptured third mode). **Revisit condition:** triggers T2 (a second ad set exists), T3 (ad sets need different performance goals/bid strategies), T4 (ad sets differ greatly in audience size), T6 (in-season protection need) — **and a D1 finding that a new ad set is the right creative-introduction method also reopens C2.** When it reopens, evaluate **all then-current Meta budget options** (campaign budget, ad set budgets, `ad set budget sharing`, and anything newer) — do not assume a permanent CBO-vs-ABO binary.

### C3 — Should testing and scaling be separated at DR's scale?

- **decision_impact:** whether a second campaign ever gets built before scale exists.
- **current_evidence:** EXTERNAL — Sam yes (dedicated scale campaign), Nick no (same CBO) — direct conflict, both ecommerce. Playbook v1 rejects separation at DR volume.
- **current_conflict:** yes — recorded head-to-head.
- **DR_context:** no winner pool exists; separation currently has nothing to separate.
- **evidence_needed:** evidence conditional on volume — at what point separation starts paying; anything from non-ecommerce contexts.
- **preferred_source_context:** practitioners explicit about account-size scoping.
- **stop_condition:** stop when the conditions under which separating testing from scaling starts paying are understood well enough to state a conditional rule with an observable revisit trigger — a numeric threshold only if credible evidence establishes one.
- **status:** **ENOUGH_EVIDENCE — at the CAMPAIGN-SEPARATION level only** (2026-08-14, Wave 2A; scope corrected 2026-08-14 after external audit) — **no separate testing and scaling CAMPAIGNS.** **This does NOT settle whether creative should be introduced into the existing ad set or a new one — that is D1, which remains OPEN.** What saturated the campaign-level question: every precondition a campaign separation would serve fails observably (no winner pool — one ad exists; very thin delivery to divide — ~9 landing page views in one referenced 30-day window, ~10–11 clicks across reported windows; no live delivery needing protection — campaign paused; registration-level Meta signal unmeasured in the available extracts). The Sam/Nick conflict is characterised rather than settled: Sam's method carries an explicit precondition (a rankable winner pool) DR does not meet, making it **inapplicable rather than wrong**. **No new independent evidence was found, and that absence is recorded rather than filled with weak material.** Conditions that could justify separation later: a genuine winner pool (T5), an in-season window where a learning reset would cost real registrations while testing must continue (T6 — DR HYPOTHESIS), capacity to run each structure independently without starving either (T7), or a second objective (T1). **No numeric threshold found or invented for any of them.**

### C4 — At what scale would these architecture recommendations change?

- **decision_impact:** prevents relitigating architecture every month; gives Half 2 a concrete trigger to watch for.
- **current_evidence:** none — neither practitioner scopes their architecture by account size except Sam's asserted (unevidenced) scale-independence of the 80% rule.
- **current_conflict:** none recorded.
- **DR_context:** any threshold will be measured in DR's own event volume once Half 2 runs.
- **evidence_needed:** practitioner statements that scope structure advice by spend/volume; Meta guidance tied to budget/event thresholds.
- **preferred_source_context:** sources that state account context explicitly (a selection rule already).
- **stop_condition:** stop when each C-decision carries a stated, observable revisit-trigger. Triggers may be qualitative or conditional; numeric only where evidence supports one. Precision beyond that is not required.
- **status:** **ENOUGH_EVIDENCE** (2026-08-14, Wave 2A; T7/T8 corrected 2026-08-14 after external audit) — stop_condition met: every C-decision carries at least one observable revisit trigger. Eight triggers in `output/wave-2a-campaign-architecture-framework.md §5` — **T1–T4 anchored in first-party platform facts** (T1 objective immutability; T2 A+CB's ≥2-ad-set condition; T3 mixed optimization goals/bid strategies; T4 audience-size divergence), **T5** in a practitioner's own stated precondition (winner pool), **T6–T8 in DR context and structure facts** (T6 in-season protection; **T7 capacity to support independent structures**; **T8 material multi-market divergence**). **T7 corrected:** it no longer uses learning-phase exit or the "Learning limited" badge as the gate — those are supporting context only; the trigger is whether each proposed structure could operate and be evaluated independently without starving the other. **T8 corrected:** geographic expansion alone does not create a campaign; it must create a *materially independent campaign-level requirement*, and geo/targeting implementation stays with E3. **No defensible numeric threshold was found for any trigger, and none was manufactured.** Explicitly NOT triggers: ~50 optimization events/week, learning-phase status, the 10× budget heuristic, any practitioner dollar figure.

## D. Creative testing structure

### D1 — How many creatives should enter at once, and via same ad set or new ad set?

- **decision_impact:** the relaunch creative plan and every subsequent creative introduction.
- **current_evidence:** EXTERNAL — Sam: new "pack" ad set per round (`experience_claim`, weak); Nick: same CBO (`experience_claim`, weak) — conflict. PLATFORM FACT — "Adding a new ad to your ad set" is an always-significant edit; Meta separately advises avoiding high ad volumes. Playbook v1: batch changes deliberately (principle adopted; neither implementation).
- **current_conflict:** yes — recorded head-to-head; Meta endorses neither remedy.
- **DR_context:** one ad set; cannot fund parallel packs.
- **evidence_needed:** third+ independent view, ideally low-budget; evidence on batch size at low volume.
- **preferred_source_context:** small-account and local-service practitioners.
- **stop_condition:** stop when a concrete relaunch creative-introduction procedure (how many, where, when) is supported such that further sources would refine numbers, not reverse the procedure.
- **status:** **ENOUGH_EVIDENCE (conditional)** (2026-08-14, Wave 2B) — **introduce new creative into the existing ad set; 2–3 per round at current-scale delivery.** What saturated it: a first-party mechanic that discovery had not previously surfaced — Meta's **native Creative Testing** operates *"in an existing campaign so that high-performing ads can continue to run after the test with delivery system learnings retained. There's no need to merge them into another campaign where the learnings would reset."* The platform's own creative-introduction mechanism stays in-campaign, which converges with the consolidation guidance and points away from Sam's "pack ad set" implementation (principle transfers, implementation does not). A second ad set would fragment DR's thin budget and duplicate a small geo audience — **C2 was therefore NOT reopened**, though the escalation path is documented and stress-tested. **Batch size is a derived capacity rule, not a borrowed number**: DR's own ~235–270 impressions/week split across N ads shows that *no* N makes individual ads comparable at current delivery, so 2–3 is chosen for diversity and delivery health, recomputed when delivery changes. A/B testing **rejected at DR scale** on first-party grounds (Meta: A/B ad sets *"may be more vulnerable to under-delivery caused by small audiences"*; remedy is to broaden — DR structurally cannot). Native Creative Testing **deferred** until the suggested ≤20% budget slice is a meaningful absolute amount. **Patched 2026-08-14 (final evidence patch):** confidence lowered **MEDIUM-HIGH → MEDIUM**. Foxwell & Fairbrother associate a dedicated per-batch testing ad set with *"brands with a small creative volume or especially those new to advertising"* — which fits DR. The decision holds on **context, not vote count**: Courtney Fritts (same ecosystem) states that under ~$100/day *"direct competition or manual bids might be your only viable options"*, and DR is an order of magnitude below that; Method 1's proponents name costs (longer learning, ad-set bloat) that land hardest on DR; and Meta's native Creative Testing delivers Method 1's guaranteed-budget benefit **in-campaign**. **"2–3 per round" relabelled a PROVISIONAL LOW-COMPLEXITY STARTING HYPOTHESIS** — the arithmetic proves no batch size makes ads readable, not that 3 beats 2. **Revisit when:** delivery rises enough to fund a creative test or make ads individually comparable; or any finding that a second ad set solves a real problem → surface C2 (T2/T3). See `output/wave-2b-creative-operating-method.md §2`.

### D2 — How should new creative be introduced while minimizing unnecessary learning disruption?

The three layers of this question are deliberately kept separate — do not collapse them:

- **PLATFORM FACT (established):** creative edits and additions to a live ad set are significant edits that cause re-entry into the learning phase — `official-meta/significant-edits.md` places both *"Any change to ad creative"* and *"Adding a new ad to your ad set"* on Meta's always-significant list. That is the full extent of what Meta establishes. **Meta does not state "always batch" or "never drip", and does not recommend any introduction cadence.** Meta separately warns against avoiding the learning phase entirely ("testing new creative… is essential").
- **DR OPERATING HYPOTHESIS (untested):** avoid unnecessary piecemeal creative edits; deliberate batching *may* reduce unnecessary learning disruption on an account that struggles to accumulate events. This is our inference from the platform fact, not a platform recommendation — it remains a DR HYPOTHESIS until DR data bears on it.
- **IMPLEMENTATION (open):** where, how, and how many creatives to introduce per round remains OPEN under D1.

- **decision_impact:** operating rule for all post-launch creative work.
- **current_evidence:** as above. EXTERNAL — both practitioners' minimum-spend remedies carry an unflagged learning cost (validated Claim 5 finding). Playbook Decision 5 adopts batching — reread that decision as hypothesis, not settled fact.
- **current_conflict:** implementation-level (packs vs same set — D1).
- **DR_context:** every reset is expensive at DR's event volume.
- **evidence_needed:** practitioner evidence on introduction cadence at low volume; anything bearing on whether batching's assumed benefit is real.
- **preferred_source_context:** small-account practitioners.
- **stop_condition:** the platform mechanism is saturated; stop on the hypothesis layer when available evidence makes the batching-vs-drip tradeoff at low volume unlikely to shift with more sources, and on implementation when D1 closes.
- **status:** **ENOUGH_EVIDENCE (conditional)** (2026-08-14, Wave 2B) — **batch each round into one deliberate change window; creative is the only variable that moves.** What saturated it: the procedure is fully specified and every prohibition traces to a platform fact, and one **new** first-party sentence upgraded the batching *principle* from pure inference to partially platform-supported — *"if changes are too frequent then your campaign will be constantly adapting and in flux"* (delivery-troubleshooting page), alongside Meta's discouragement of informal on/off testing (*"This can lead to inefficient ad delivery and unreliable test results"*). **Meta still prescribes no cadence**, so the batching *preference* remains a **DR HYPOTHESIS** with an explicit falsification path (framework §13 H2). ~~Review condition is ≥7 days AND accumulated delivery, per Meta's A/B floor.~~ **← SUPERSEDED, see patch note below.** Next round is gated on the current round being decidable, never on the calendar. **Numeric cadence: `NO_USEFUL_EVIDENCE_FOUND`** — every refresh-interval figure discovered was untraceable content-farm material and was rejected. **Patched 2026-08-14 (final evidence patch): the ≥7-day review gate was REMOVED.** It had been transferred from Meta's *A/B-test* guidance, which governs a different mechanism; Meta publishes no minimum observation period for ordinary in-ad-set delivery. Replaced by an evidence condition — *review once the window has been technically clean and enough delivery has accumulated to classify under the D3 ladder; elapsed time is context, not evidence*. Courtney Fritts's *"run for at least 7 days"* is retained only as an EXTERNAL PRACTITIONER CLAIM (`opinion`, `evidence_strength: none`, **undated**). See `output/wave-2b-creative-operating-method.md §3`.

### D3 — What evaluation window and what evidence justify killing or keeping a creative at low volume?

- **decision_impact:** stops both premature kills and zombie creatives; defines the post-launch creative review.
- **current_evidence:** EXTERNAL — Sam: judge at 4–7 days via minimum-spend behavior (`experience_claim`, weak, assumes $100/day); nothing else.
- **current_conflict:** none — single thin source.
- **DR_context:** at DR volume a 4–7 day window may contain single-digit clicks; ecommerce windows likely meaningless.
- **evidence_needed:** kill/keep criteria that function on sparse data (time-based, impression-based, qualitative); practitioner evidence from small accounts.
- **preferred_source_context:** small local advertisers; measurement-minded practitioners.
- **stop_condition:** stop when a kill/keep rule usable at DR's actual delivery volume exists and additional evidence would only tune its parameters.
- **status:** **ENOUGH_EVIDENCE (conditional) on the decision boundary; `NO_USEFUL_EVIDENCE_FOUND` on every numeric threshold** (2026-08-14, Wave 2B) — **a 5-state evidence ladder with four separate kill types, where "not enough evidence" is a valid and currently expected verdict.** What saturated the boundary: Meta instructs that *"When running multiple ads in 1 ad set, evaluate your results at the ad set level"*; Meta's own creative test ships with **"A confidence level is not included"**; Meta's A/B documentation treats *"the test did not find a winner"* as a normal outcome and recommends extending rather than concluding. Together these establish that **at DR's delivery the individual ad is not a readable unit**, which is the wave's central finding. Kill types separated: technical · policy/brand · dominated-performance (requires comparable exposure **repeated across more than one window** — corrected during stress testing, which broke the single-window form) · downstream quality (State 4, not yet reachable). **No defensible spend or impression threshold exists and none was invented**; a *relative* exposure-comparability rule replaced them. "Winner" is explicitly unavailable at ad level today. **Patched 2026-08-14 (final evidence patch):** the dominated-performance kill's non-dollar thresholds — *"same order of magnitude"* exposure and *">1 window"* — were **demoted from qualification rules to confidence-building conditions**, because neither boundary is evidence-established for DR. The kill is now explicitly **operator judgement under documented conditions**, labelled DIRECTIONAL, with NOT_EVALUABLE as the default when conditions are mixed. **Revisit when:** ad-level ordering proves stable across repeated windows at comparable exposure, or registration-level signal becomes measurable (opening State 4). See `output/wave-2b-creative-operating-method.md §4`.

### D4 — How should spend distribution / no-spend across ads be interpreted?

- **decision_impact:** whether no-spend triggers creative work, budget intervention, or patience.
- **current_evidence:** EXTERNAL — Nick: non-spend is a creative verdict, diagnose hook→visual→market→duration→positioning (`multi_account_experience`, weak, INSUFFICIENT_EVIDENCE vs Meta); Nick: 90% no-spend is normal (weak). PLATFORM FACT — Meta's learning-limited causes do not include creative quality; Meta's remedies lean toward raising budget — recorded tension.
- **current_conflict:** partial — Nick's "don't force spend" vs Meta's "raise your budget" (different scopes, unresolved).
- **DR_context:** with 1 ad the question activates the moment a second creative exists.
- **evidence_needed:** independent evidence on CBO per-ad distribution behavior; anything Meta publishes on in-CBO allocation.
- **preferred_source_context:** practitioners explicit about mechanism vs folklore.
- **stop_condition:** stop when DR has an interpretation rule for no-spend (what it means, what to do, what not to do) that further sources would not reverse.
- **status:** **ENOUGH_EVIDENCE** (2026-08-14, Wave 2B) — **a 5-branch ordered diagnostic that must run before any creative judgement.** What saturated it: Meta documents the misreading **by name**. The *"breakdown effect"* page defines it as *"the misinterpretation that our system shifts impressions and spending into underperforming ad sets, placements or ads"*, instructs ad-set-level evaluation for multiple ads in one ad set, and supplies a worked example in which the slice with the **better** final average CPA ($1.10) correctly received **$50** while the worse one ($1.46) received **$450** — because allocation follows marginal, not average, cost. The delivery-troubleshooting page adds that *"it's normal for some ad sets or ads to deliver less than others"* plus a documented non-creative cause list (review state, *Creative limited* / *Creative fatigue*, audience saturation, bid/cost-control competitiveness, frequent pauses, late-day budget changes, ±75% daily pacing). **Nick Theriot's claim is resolved by splitting it:** the *principle* (the system allocates deliberately; forcing spend is usually wrong) **transfers and is now platform-supported**; the *implementation* (a no-spend creative should be abandoned) **does not transfer** — at DR's volume no-spend overwhelmingly means NOT_EVALUABLE. His claim's own `platform_validation_status` stays `INSUFFICIENT_EVIDENCE` (Meta neither states nor refutes it). **Patched 2026-08-14 (final evidence patch): the absolute "never force spend" was replaced by a distinction, not reversed.** Courtney Fritts supplies the operator counter-position (*"Budget for real learning… before calling it quits"*). Final rule: **never manipulate natural delivery to force an ad to spend; obtain the answer through a controlled, funded testing mechanism when the question matters and DR can fund an interpretable test** — five conditions stated, of which DR currently fails only the funding one. Her 3× CPA / 3× production-cost figures do **not** transfer (DR has no measured CPA). See `output/wave-2b-creative-operating-method.md §5`.

## E. Audience / targeting

### E1 — Broad vs interests vs Advantage+ audience in a tightly geo-constrained local registration business?

- **decision_impact:** the ad set's audience configuration on relaunch.
- **current_evidence:** EXTERNAL — Sam: test interests with proven ads only (`opinion`, none — design logic); Nick: creative does the targeting (`opinion`, none) — points opposite to DR's qualification need. PLATFORM FACT gap: no `official-meta/` file on Advantage+ audience mechanics. DR fact: live ad set carries `advantage_audience: 1` over a `DR HISTORIC` custom audience with no visible geo key.
- **current_conflict:** yes — narrow-for-qualification vs broad-for-delivery, unresolved and recorded.
- **DR_context:** residency and age band are hard qualifiers; audience expansion risks both.
- **evidence_needed:** first-hand Meta docs on Advantage+ audience (what expansion can and cannot override — especially geography); practitioner evidence from geo-constrained local businesses.
- **preferred_source_context:** local-business practitioners; Meta first-party docs first.
- **stop_condition:** stop when Meta's expansion mechanics are documented first-hand (what is a hard constraint vs a suggestion) and the broad-vs-constrained call for DR would not materially change with additional comparable-context evidence.
- **status:** **ENOUGH_EVIDENCE (conditional)** (2026-08-14, Wave 3) — **Advantage+ audience with Locations as a HARD CONTROL, no interest/detailed targeting, adult minimum age as a control, expansion OFF.** What saturated it: the stop_condition asked exactly for the hard-vs-suggestion distinction and Meta publishes it explicitly — *"Audience controls limit who can see your ads. You can choose Locations, Minimum age, Custom audiences to exclude and Languages"* vs *"You can suggest Age, Gender, Detailed targeting and Custom audiences to include. **Suggestions don't always constrain your audience**"* (Meta's own example: suggesting Women can still deliver to men). The one setting that breaks location is named: *"we won't target beyond your locations **unless you select Reach more people likely to respond to your ads**."* **Interests are rejected** — non-binding by default, and forcing them via *"Further limit your audience"* narrows an already-small geo audience, worsening the first learning-limited cause Meta names. Meta's own aggregate Advantage+ figures (−14.8%/−9.7%/−7.2% cost per result) are recorded as **Meta assertion, not DR proof** — no population, geography, scale or design disclosed. **Revisit when:** Meta changes the control/suggestion split, DR's serviceable area changes, or DR evidence links an interest to paid registration. See `output/wave-3-audience-measurement-framework.md §2`.

### E2 — What should be fixed by targeting vs carried by creative/message?

- **decision_impact:** division of labor between ad-set settings and the ad itself; shapes both audience config and creative briefs.
- **current_evidence:** EXTERNAL — Nick's creative-creates-audience (`opinion`, none); playbook counter-analysis: creative cannot enforce residency. COMPETITOR — school/age/location named in creative by multiple families (message-side qualification observed in the wild).
- **current_conflict:** yes — same axis as E1.
- **DR_context:** geography must be fixed by settings (creative cannot); age/parent fit may be carried by message (experiments E2/E3 in `output/experiments.md` test exactly this).
- **evidence_needed:** practitioner evidence on message-based qualification for local offers; delivery effects of qualifying copy at low volume.
- **preferred_source_context:** local services; direct-response practitioners with lead-quality focus.
- **stop_condition:** stop when the rule "settings fix X, message carries Y" is stated for DR with each assignment backed by platform fact or evidence, and DR experiments are queued for the genuinely undecidable parts.
- **status:** **ENOUGH_EVIDENCE (conditional)** (2026-08-14, Wave 3); **practitioner layer `NO_USEFUL_EVIDENCE_FOUND`** — **SETTINGS ENFORCE serviceable geography, adult minimum age and exclusions; MESSAGE QUALIFIES school, sport, child age band, format, schedule, price, season dates, beginner-friendly, registration status.** Each assignment traces to a platform fact: those three are documented Audience *controls*; school attendance has no permissible targeting source; and under-13 data must not enter Business Tools **in the payload, the event name, or the criteria**. Nick Theriot's *"creative does all the targeting"* is explicitly **not** promoted to platform truth (`opinion`, `evidence_strength: none`) and points opposite to DR's qualification need. The creative-qualification hypothesis — that program-specific copy makes unqualified people self-select out — remains a **DR HYPOTHESIS** with a falsification path (framework §13 H-B). **Critical distinction preserved:** creative causes self-selection but **verifies nothing** — a parent can see school-specific creative and click without having a child at that school. **Revisit when:** DR data shows qualifying copy failing to improve qualified response across ≥2 rounds. See `§3`.

### E3 — How should school-specific geography affect setup?

- **decision_impact:** whether campaigns/ad sets ever split by school/zone, and how radii are set around campuses.
- **current_evidence:** PLATFORM FACT — `geo-location-targeting.md` (`location_types` default `['home','recent']`; radius mechanics). No practitioner evidence.
- **current_conflict:** none.
- **DR_context:** offer is delivered at named schools; a parent 40 minutes away is unqualified regardless of interest. Orlando tourist-metro effect makes `recent` inclusion costly.
- **evidence_needed:** practitioner evidence on hyper-local radius targeting for venue-based offers; Meta docs on minimum radius and audience-size floors interacting with tight geo.
- **preferred_source_context:** venue-based local businesses (gyms, studios, enrichment centers).
- **stop_condition:** stop when a geo configuration pattern (residents-only? radii? per-school splits?) can be recommended with its audience-size consequences understood.
- **status:** **ENOUGH_EVIDENCE (conditional)** (2026-08-14, Wave 3) — **one ad set whose Locations control is the UNION of tight custom-location radii (or ZIP groups) around DR's active campuses.** The architectural point that makes it work: **multiple locations inside one ad set is not multiple ad sets**, so DR gets per-school geometry at zero fragmentation cost — **C1 REOPEN: NO · C2 REOPEN: NO.** Whole-metro city targeting rejected (city radius floor is 10 miles vs 0.63 for custom locations, and Orlando is a top-tier tourist metro); per-school ad sets rejected (fragments budget, needs a C2 reopen, and Wave 2B established individual units are unreadable at DR volume). **This run closed a long-standing open question**: Meta's Help Centre states location targeting reaches people who *"live in, have recently spent time in or go often to"* the selected areas — three behaviours the API's two-value `location_types` enum does not cleanly map to, recorded as unresolved rather than asserted. **Permanent bound on every geo claim:** *"Due to signal variations, complete accuracy cannot be guaranteed. You might see some ad impressions, or receive messages or leads from outside your location settings."* **Geo serviceability ≠ school eligibility** — proximity never proves enrolment, and no child-based custom audience may be built. **Residents-only availability on DR's campaign path is a DR Ads Manager AUDIT item, not a research gap.** See `§4`.

## F. Retargeting

### F1 — Is a separate retargeting campaign useful at DR's expected traffic volume — and if not, when does it become useful?

- **decision_impact:** whether warm-traffic structure exists at relaunch; a revisit trigger for Half 2.
- **current_evidence:** EXTERNAL — Sam: dedicated narrow retargeting (`experience_claim`, weak); Nick: no retargeting audiences, message-stage creative instead (`opinion`, none) — conflict. Playbook v1: rejected at current volume (no event pool to build audiences from).
- **current_conflict:** yes — audience-based vs message-based retargeting, recorded.
- **DR_context:** 256 reach/30 days historically — no retargeting pool exists yet in any meaningful sense.
- **evidence_needed:** minimum audience sizes for viable retargeting (Meta docs); practitioner evidence on warm-traffic handling for seasonal registration offers (registration windows create natural warm bursts).
- **preferred_source_context:** seasonal/registration businesses.
- **stop_condition:** stop when the conditions under which a separate retargeting structure becomes deliverable and useful for DR are understood — expressed as observable conditions (pool composition, traffic pattern, platform minimums), with a numeric threshold only if credible evidence establishes one — plus a sensible starting shape for when those conditions arrive.
- **status:** DEFERRED — blocked on volume that does not exist; revisit when Half 2 shows a real traffic pool.

## G. Attribution / measurement

### G1 — What attribution settings match a parent's registration decision cycle?

- **decision_impact:** attribution feeds optimization, not just reporting (PLATFORM FACT, `optimization-goals-and-attribution.md`) — the window is a delivery variable.
- **current_evidence:** EXTERNAL — Sam: 7-day click / 1-day engaged / 1-day view, stated with zero rationale (`none_presented`, none). PLATFORM FACT — attribution_spec mechanics documented; allowed windows per objective not enumerated in the stored file.
- **current_conflict:** none — single unsupported source.
- **DR_context:** seasonal considered purchase; parents plausibly convert days after first exposure, possibly cross-device.
- **evidence_needed:** Meta docs on available windows for the chosen objective (depends on A1/A2); practitioner evidence on windows for considered/multi-day decisions.
- **preferred_source_context:** considered-purchase and local-service practitioners.
- **stop_condition:** stop when a window is chosen with a stated rationale tied to DR's decision cycle, and the platform-side options are documented first-hand. Low priority until volume makes the window binding.
- **status:** **ENOUGH_EVIDENCE (conditional)** (2026-08-14, Wave 3) — **standard model · 7-day click · 1-day view · engage-through off if selectable.** Both halves of the stop_condition are met. **Platform options documented first-hand, closing the `window_days` question open since `optimization-goals-and-attribution.md`:** currently supported standard settings for website conversions are **click-through 1-day or 7-day, view-through 1-day, engage-through 1-day** (non-link clicks; video 5s or 97%). **There is no 28-day click option**, so 7-day is the platform ceiling — DR is taking the maximum available, **not copying Sam Piliero's 7/1/1**, which carries `evidence_basis: none_presented` and is explicitly not the basis. Attribution is set **at ad set level** and *"inform[s] ad delivery"*, so it is a delivery variable. Cross-model comparison requires **Compare Attribution Settings**, which is adopted for reporting — and **attribution-window shopping is explicitly prohibited**. Mandatory statement retained: Meta-attributed conversions ≠ all DR registrations ≠ registrations caused by Meta. **Unresolved dependency:** Meta says not all settings are available for certain campaign types; availability under the A1 candidate objectives is unconfirmed and must be checked before an objective is committed. See `§5`.

### G2 — What metrics should be used for delivery, creative, qualified response, and final registration?

- **decision_impact:** the measurement contract for Half 2 — what every diagnosis and experiment reads.
- **current_evidence:** internal only — experiments v1 use CPM/CTR/LPV-rate as directional metrics; no external evidence structure.
- **current_conflict:** none.
- **DR_context:** registration truth lives outside Meta (registration platform / CRM); Meta-side metrics can never confirm qualification alone — a data-join question for Half 2.
- **evidence_needed:** practitioner measurement stacks for local registration businesses; which Meta metrics are trustworthy at low volume vs noise.
- **preferred_source_context:** measurement-focused practitioners; local-service operators.
- **stop_condition:** stop when a four-layer metric table (delivery / creative / qualified response / registration) exists with each metric's source system and low-volume caveat stated.
- **status:** **ENOUGH_EVIDENCE (conditional)** (2026-08-14, Wave 3); **practitioner layer `NO_USEFUL_EVIDENCE_FOUND`** — stop_condition met: the four-layer table exists with source system, denominator, read level and low-volume caveat per metric. Anchored on first-party definitions retrieved this run: **link clicks** = clicks to destinations *"on or off"* Meta (including on-platform full-screen formats); **outbound clicks** = clicks taking people *"off Meta technologies"*; landing page views = click **and** load. **All clicks / link clicks / outbound clicks / LPV are four distinct metrics and are never collapsed.** Correct denominators are fixed: outbound CTR ÷ impressions, **LPV rate ÷ OUTBOUND clicks** — dividing LPV by all-clicks or link-clicks is **prohibited** (this specific error was caught by stress Test 16 and corrected the deliverable). **Layers 3–4 live in DR's own systems, not Meta**, with availability marked AVAILABLE / UNKNOWN / **PROHIBITED** (under-13 data). **Paid registration in DR's registration database is the business ledger; Meta-attributed registrations are a separate number reported separately.** `UNMEASURED` is used, never zero. **The highest-value missing input is the click→registration join** (a campaign identifier surviving to the registration row) — a Half 2 ground-truth audit, not a research gap. See `§6`, `§7`.

---

# P1 — AFTER A WORKING BASE EXISTS

## S. Scaling

### S1 — What does scaling actually mean for DR, and at what event volume should it even be discussed?

- **current_evidence:** none applicable — ecommerce scaling systems were reviewed and rejected as non-transferable; nothing replaced them.
- **stop_condition:** stop when "scaling" is defined in DR terms (more schools? higher budget per school? seasonal pulsing?) with observable entry conditions — a numeric event-volume threshold only if credible evidence establishes one.
- **status:** DEFERRED — do not spend research budget here until Half 2 produces a working base.

### S2 — Vertical vs horizontal scaling, and when should architecture change as budget grows?

- **current_evidence:** none applicable (Sam's scale-campaign mechanics assume ecommerce winner pools).
- **stop_condition:** stop when C4's revisit-triggers exist and at least one credible scaling path for a seasonal local business is documented.
- **status:** DEFERRED

---

# NOT CURRENTLY A RESEARCH PRIORITY

### Placements default — ESTABLISHED, no research budget

- **Position:** current first-party Meta guidance recommends Advantage+ placements / staying opted into all placements as the default. DR runs all placements today. Treat the default as established.
- **Qualifier preserved:** this does **not** mean a placement can never later be excluded. Reopen (status → `REOPENED`) only if: (a) DR's own performance data creates evidence against a placement, (b) platform guidance changes, or (c) a material specific constraint appears (legal, brand-safety, format).
- **History:** playbook Decision 4; Sam's all-placements claim graded INSUFFICIENT_EVIDENCE; DR's own placement data (10 clicks on $82.11) far too thin to justify restriction. The earlier "restrict placements → TEST" hypothesis is deprioritized, not forbidden.
- **status:** ENOUGH_EVIDENCE (as a default) — spending practitioner-research cycles on "should we use all placements by default?" is explicitly prohibited.

---

## Maintenance rules

- New questions enter under the decision they serve, with the full contract. No contract, no backlog entry.
- Status changes are dated in place. A question moving to `ENOUGH_EVIDENCE` states, in one line, what saturated it.
- `stop_condition` never becomes a source count.
- This file drives retrieval. A source with no target question here is a reading list, not research.

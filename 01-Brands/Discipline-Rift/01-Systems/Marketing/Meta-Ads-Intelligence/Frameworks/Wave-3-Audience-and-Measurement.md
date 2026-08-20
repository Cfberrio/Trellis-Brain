---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: framework
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/output/wave-3-audience-measurement-framework.md"
repo_path: domains/ads/meta/intelligence/output/wave-3-audience-measurement-framework.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/framework
  - discipline-rift
aliases:
  - "Wave 3"
  - "Audience and Measurement Framework"
---

# Wave 3 — Audience, Geography, Attribution and Measurement Framework for DR

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-2B-Creative-Operating-Method|Wave 2B — método creativo]]
- [[01-Brands/Discipline-Rift/00-Brand-Core/Avatar|DR Avatar]]
- [[01-Brands/Discipline-Rift/06-DNA/Metrics|DR Metrics DNA]]
- [[01-Brands/Discipline-Rift/06-DNA/Conversion|DR Conversion DNA]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/output/wave-3-audience-measurement-framework.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Date:** 2026-08-14 · **Questions:** E1 · E2 · E3 · G1 · G2
**Knowledge level:** **DR HYPOTHESIS.** Built from PLATFORM FACT + DR CONTEXT FACT (+ a thin, mostly rejected practitioner layer). **Nothing here is proven for DR.** No campaign, ad set, audience, location, attribution setting, Pixel or CAPI configuration was changed or created.
**Inherits:** Waves 1A/1B/2A/2B, unmodified
**Hands to:** external audit → Half 2 (DR ground-truth audits and live execution)

---

## 0. EXECUTIVE ANSWER

```text
Audience configuration:   Advantage+ audience with Locations held as a HARD CONTROL.
                          No detailed-targeting/interest constraints. Adult minimum age as a control.
                          "Reach more people likely to respond to your ads" = OFF — this is the one
                          named setting that would break DR's serviceability guarantee.
Hard controls:            Locations · Minimum age (adult purchaser) · Custom-audience EXCLUSIONS
Suggestions (left soft):  Age upper range · Gender (none) · Detailed targeting (none) ·
                          Custom-audience inclusions
Geo approach:             ONE ad set containing the UNION of tight custom-location radii (or ZIP
                          groups) around DR's active campuses — NOT a whole-metro city selection,
                          and NOT one ad set per school. Multiple locations in one ad set is not
                          multiple ad sets. C1 REOPEN: NO. C2 REOPEN: NO.
Targeting/message split:  SETTINGS enforce serviceable geography and adult purchaser.
                          MESSAGE qualifies school, sport, child age band, format, schedule, price.
                          Creative causes self-selection; it CANNOT enforce or verify anything.
Attribution:              Standard model · 7-day click · 1-day view · engage-through OFF if
                          selectable. 7-day click is the LONGEST window Meta currently offers for
                          website conversions — this is a platform ceiling, not a copied convention.
Measurement layers:       1 Delivery · 2 Creative/Message · 3 Qualified response · 4 Paid registration
Primary business truth:   DR's own registration database — NOT Meta. Meta attribution is an
                          advertising measurement layer, never the business ledger.
Highest-value missing:    A working join between Meta delivery and DR's registration records
                          (ad/campaign identifier carried through to the registration row).
Knowledge level:          DR HYPOTHESIS
```

**The finding that shapes this whole wave:** Meta itself documents which audience inputs are *controls* and which are merely *suggestions*. **Location is a control. Interests, age, gender and audience inclusions are suggestions by default.** DR's binding qualification is geographic serviceability — so DR can hold the one thing that matters as hard, and leave everything else soft, without fighting the platform. Most of Wave 3 follows from that single sentence.

---

## 1. Input from Waves 1–2 (not re-litigated)

Paid season registration is the outcome · parent purchases, child 6–12 participates · not ecommerce · geo-constrained · historical delivery very thin and metric-specific (~9 LPV in one referenced 30-day window; ~10–11 clicks across reported windows) · **no defensible registration CPA exists; registration-level Meta signal is unmeasured in available extracts — not proven absent** · A1 conditional, A2/A3 reopened · **Pixel/CAPI live state UNKNOWN — repo-code absence proved nothing** · ~50/week is not a cliff · 10× is a heuristic · 1 campaign / 1 ad set / keep ad-set budget / no testing-scaling split · creative enters the existing ad set in one batched window, start 2–3 (provisional) · NOT_EVALUABLE is a legitimate verdict · no-spend requires diagnosis before verdict · **DR proof status: NONE.**

---

## 2. E1 — Audience configuration

### E1 CURRENT RECOMMENDATION
**Advantage+ audience, with Locations as a hard control and no interest constraints.**

```text
AUDIENCE MODE:        Advantage+ audience
HARD CONTROLS:        Locations (serviceable geography, §4)
                      Minimum age — adult purchaser floor
                      Custom audiences to EXCLUDE — existing/registered families, if such an
                      audience can be built from permissible adult data
SOFT SUGGESTIONS:     none actively supplied
INTERESTS:            NONE — neither as suggestion nor as control
AGE:                  minimum age as a control; NO upper bound imposed
GENDER:               none — either parent may purchase
LANGUAGE:             NOT restricted by default — see DR decision below
CUSTOM AUDIENCE USE:  exclusions only; inclusions add nothing at DR's list size
EXPANSION:            "Reach more people likely to respond to your ads" = OFF
```

### WHY

**Platform facts (first-hand, `audience-controls-location-and-attribution.md`):**
- *"Audience controls limit who can see your ads. You can choose Locations, Minimum age, Custom audiences to exclude and Languages."*
- *"if you choose Locations, we won't target beyond your locations **unless you select Reach more people likely to respond to your ads**."*
- *"You can suggest Age, Gender, Detailed targeting and Custom audiences to include. **Suggestions don't always constrain your audience.**"* — with Meta's own example that suggesting Women can still deliver to men.
- Suggestions can be converted to controls via *"Further limit your audience"* / unchecking *"Use as a suggestion."*

**The question the brief asked directly — is holding location hard while letting Meta move freely inside it preferable to adding interest constraints? YES**, on four grounds:

1. **Location is the only DR qualifier the platform will actually enforce.** Serviceability is binary for DR — a parent outside the catchment cannot register regardless of interest.
2. **Interests are documented as non-binding by default.** Supplying them creates a false sense of control while changing little.
3. **Converting interests to controls actively harms DR.** It narrows an already-small geo audience, and *"small audience size"* is the first cause Meta names for learning limited (`learning-limited.md`). Wave 1B established DR's delivery is the binding constraint — narrowing further is the wrong direction.
4. **DR has no evidence any interest correlates with paid registration.** Adding one would be inventing a qualifier.

**Age:** the purchaser must be an adult — that is a hard business fact and Minimum age is a documented control, so it is set as one. **No upper bound**, because "parent" is not an age range: guardians and grandparents purchase too, and capping age would exclude qualified buyers for no evidenced gain.

**Gender:** no constraint. Not a business qualifier, and Meta documents gender as a suggestion that need not bind anyway.

**Language — flagged as a DR business decision, not a research conclusion.** Language *is* a control. Orlando has a large Spanish-speaking population, and restricting language would exclude qualified parents. **Default: do not restrict.** If DR's creative and landing page are English-only, that is a creative-coverage decision to make deliberately, not a targeting default.

**Custom audiences:** exclusions are controls and are the useful direction — not paying to reach families already registered for the current season. Inclusions are suggestions and, at DR's list size (historic reach ~256/30 days), carry negligible signal. Note the last-known ad set carries a `DR HISTORIC` custom audience with `advantage_audience: 1` — **an audit item, since under current mechanics an inclusion behaves as a suggestion.**

### PRACTITIONER EVIDENCE
**Thin, and mostly pointing the wrong way for DR.** Nick Theriot's *"creative does all the targeting"* (`opinion`, none) argues against settings-based qualification generally; the playbook already recorded the counter-analysis that **creative cannot enforce residency**. Sam Piliero's *"test interests with proven ads only"* (`opinion`, none) is scale-independent experiment-design logic but presupposes a proven-ad pool DR lacks. **No new practitioner source survived pre-screen this wave (§10).**

### DR TRANSFERABILITY
The mechanics are platform-level and apply directly. What does *not* transfer is any ecommerce assumption that a large addressable audience exists to narrow — DR's audience is small before any targeting is applied.

### WHAT WE REJECTED
| Rejected | Where rational | Why not DR | What would change it |
|---|---|---|---|
| Interest/detailed targeting as controls | Large addressable audiences needing segmentation | Shrinks a tiny geo audience; no evidenced correlation to registration | DR evidence that a specific interest predicts paid registration |
| "Reach more people likely to respond" | Advertisers whose service area is elastic | Breaks the serviceability guarantee — the one thing DR must hold | DR expands its serviceable area |
| Gender/age-range narrowing | Businesses with a genuinely gendered or age-bound buyer | Excludes qualified purchasers for no gain | evidence a segment cannot buy |
| Lookalikes from DR HISTORIC | Accounts with a large, clean seed list | Seed is far too small; inclusion behaves as a suggestion anyway | a materially larger registrant list |
| Meta's "9.7% lower cost per result" as a reason | — | Aggregate claim, no population/geography/design disclosed | a comparable-context study, or DR's own test |

### REVISIT TRIGGERS
Meta changes which inputs are controls vs suggestions · DR's serviceable area changes · DR accumulates a registrant list large enough to make exclusions or lookalikes meaningful · DR evidence that an interest predicts registration.

### STATUS
**ENOUGH_EVIDENCE (conditional)** — the control/suggestion split is first-party and decisive; the residual uncertainty is DR-side configuration, not external evidence.

---

## 3. E2 — Targeting vs message responsibility matrix

| Qualification | Settings | Message | Both | Why | Evidence |
|---|---|---|---|---|---|
| Serviceable geography | **✔ ENFORCE** | ✔ name the area/school | ✔ | Location is a documented control; creative cannot enforce it | PLATFORM FACT |
| Adult purchaser | **✔ ENFORCE** (minimum age) | — | | Minimum age is a control; purchase requires an adult | PLATFORM FACT |
| Already-registered families | **✔ EXCLUDE** | — | | Exclusions are controls | PLATFORM FACT |
| Specific school attendance | ✘ **not targetable** | **✔ QUALIFY** — name the school | | No permissible data source identifies enrolled families; proximity ≠ enrolment | PLATFORM FACT + DR CONTEXT |
| Child grade / age band | ✘ **NEVER** | **✔ QUALIFY** — state the age band | | Under-13 data must not enter Business Tools — payload, event names **or criteria** | PLATFORM FACT (`business-tools-data-restrictions.md`) |
| Sport | ✘ | **✔ QUALIFY** | | Not a reliable targeting attribute; creative states it plainly | DR CONTEXT |
| After-school / on-campus format | ✘ | **✔ QUALIFY** | | The core deliverable; self-selects strongly | DR CONTEXT |
| Practice day / time | ✘ | **✔ QUALIFY** | | Schedule fit is a real disqualifier parents can self-check | DR CONTEXT |
| Price | ✘ | **✔ QUALIFY** | | Filters non-buyers before the click | DR CONTEXT |
| Season length / dates | ✘ | **✔ QUALIFY** | | Real dates only — DR claim rules | DR CONTEXT |
| Beginner-friendly / no experience | ✘ | **✔ QUALIFY** | | Prevents elite-athlete mis-framing (banned language) | DR CONTEXT |
| Registration open / deadline | ✘ | **✔ QUALIFY** | | Only when literally true | DR CONTEXT |
| Residency (as distinct from proximity) | partial — geo is a proxy only | **✔ REINFORCE** | ✔ | Meta: *"complete accuracy cannot be guaranteed"* | PLATFORM FACT |

```text
SETTINGS MUST ENFORCE:            serviceable geography · adult minimum age · exclusions
MESSAGE SHOULD QUALIFY:           school · sport · child age band · format · schedule · price ·
                                  season dates · beginner-friendly · registration status
BOTH SHOULD REINFORCE:            geography / locality
DO NOT TARGET ON:                 child attributes · school attendance · interests as hard controls
DO NOT PUT INTO META BUSINESS
TOOL DATA:                        anything from or about under-13s — not in the payload,
                                  not in an event name, not in the criteria that fire it
```

### The creative-qualification hypothesis — tested, not assumed

**Claim:** hard business constraints should be enforced in settings where the platform allows; creative should carry enough program specificity that unqualified people self-select out.

- **Supported by platform fact:** location/minimum-age/exclusions are controls; child and school attributes are not targetable (and child data is prohibited).
- **Supported by Meta's framing:** suggestions do not bind, so message is the only lever for the qualifications settings cannot express.
- **NOT established:** that qualifying copy improves downstream registration quality. **Nick Theriot's "creative is the targeting" must not become platform truth** — it is `opinion`, `evidence_strength: none`, and it points opposite to DR's need (he advises *widening* the callout to unlock delivery).
- **Remains a DR HYPOTHESIS** with a falsification path (§13).

**Critical distinction preserved:** algorithmic targeting *restricts exposure*; message *causes human self-selection*. Neither substitutes for the other, and **neither verifies anything** — a parent can see school-specific creative and click without having a child at that school (Test 3).

---

## 4. E3 — School / geography configuration

### PLATFORM FACTS THAT DECIDE THIS
- Location targeting reaches people who *"**live in, have recently spent time in or go often to** countries, regions, cities, postal codes"* and US Comscore Markets / congressional districts.
- **The accuracy disclaimer:** *"Due to signal variations, complete accuracy cannot be guaranteed. You might see some ad impressions, or receive messages or leads from outside your location settings."*
- Exclusions depend on *both* current and home location.
- API granularity (`geo-location-targeting.md`): **city radius floor is 10 miles**; **custom-location (address/pin) radius floor is 0.63 miles**; ZIPs supported.
- Location is a **control** under Advantage+ audience, breakable only by *"Reach more people likely to respond to your ads."*

### OPTIONS MATRIX

| Option | Delivery capacity | Qualification quality | Complexity | Measurement readability | Architecture cost | Verdict |
|---|---|---|---|---|---|---|
| **A — one broad Orlando city geo** | Highest | **Poor** — city radius floor is 10 mi; sweeps in a top-tier tourist metro and large unserviceable areas | Lowest | Poor — cannot tell serviceable from not | none | **REJECTED** — buys the cheapest possible clicks from people who cannot register |
| **B — single school-centred radius** | Very low | Excellent for that school | Low | Fine | none | **REJECTED alone** — one school cannot carry the offer, and Test 6 (perfect geo, zero delivery) applies |
| **C — ZIP / postcode groups around campuses** | Moderate | Good | Moderate — needs ZIP list maintenance | Good | none | **VIABLE alternative** to D |
| **D — UNION of tight custom-location radii around each active campus, all inside ONE ad set** | Moderate | **Best available** — 0.63-mile floor allows genuinely local radii, stacked to cover every campus | Moderate | Good | **none — multiple locations ≠ multiple ad sets** | **ADOPTED** |
| **E — one ad set per school** | Fragmented | Excellent per school | High | **Worse, not better** — Wave 2B established individual units are unreadable at DR volume | **C2 REOPEN required** | **REJECTED** |
| **F — store-set / other native structures** | — | — | — | — | — | Not applicable — DR has no store-set use case identified |

### E3 CURRENT RECOMMENDATION
**Option D: one ad set whose Locations control is the union of tight radii around DR's currently active campuses.** Fall back to Option C (ZIP groups) if custom-location radii prove unworkable in the account.

**The architectural point that makes this work:** *multiple locations inside one ad set is not multiple ad sets.* DR gets per-school geometry without paying any fragmentation cost.

```text
C1 REOPEN: NO
C2 REOPEN: NO
```

Neither is triggered, because the recommended geometry needs no additional ad set or campaign. **Had it required one, it would have been surfaced rather than absorbed** (Test 22).

### GEO SERVICEABILITY ≠ SCHOOL ELIGIBILITY — mandatory separation
A parent living near a campus may still have a child at a different school, in the wrong grade, or unable to attend. **Geography is a serviceability filter only.** School eligibility is carried by the **message and the landing page**, and verified — if at all — inside DR's own registration system. **No child-based custom audience may be built, and no claim may be made that Meta can target enrolled families.**

### The "residents only" question — AUDIT REQUIRED
Meta's page states location targeting reaches all three behaviours (live in / recently spent time in / go often to). **Whether a residents-only selection is exposed on DR's specific campaign path under Advantage+ audience was not established from the retrieved documentation**, and the API/UI vocabularies do not map cleanly (`audience-controls-location-and-attribution.md`). **This is a DR Ads Manager audit item, not a research conclusion.** If a residents-only option exists, it is strongly preferred — Orlando's tourist volume makes "recently spent time in" expensive noise (Test 5).

### REVISIT TRIGGERS
Campus list changes · geo delivery proves too thin to learn anything (then widen radii deliberately, accepting the qualification cost) · Meta changes location-behaviour options · DR expands to a second metro with genuinely separate operations (→ evaluate C1, per Wave 2A T8).

### STATUS
**ENOUGH_EVIDENCE (conditional)** — the geometry is decided and requires no architecture change; the residents-only selector and the exact campus radii are **DR-side audit items**, not external research gaps.

---

## 5. G1 — Attribution

### THE PLATFORM CEILING
Meta's currently supported **standard** attribution settings for website conversions:
- **Click-through: 1-day or 7-day**
- **View-through: 1-day**
- **Engage-through: 1-day** (non-link clicks; video played 5 seconds, or 97% if shorter)

**There is no 28-day click option among the supported standard settings.** Attribution model and settings are chosen **at the ad set level** and **inform ad delivery**, not only reporting.

### DECISION MATRIX

| Option | Delivery implication | Reporting implication | Pros for DR | Risks | Availability | Verdict |
|---|---|---|---|---|---|---|
| 1-day click | Optimises to same-day converters | Credits least | Cleanest causal story | **Structurally mismatched** — a parent researching a season rarely decides same-day; would under-credit and mis-train delivery | Yes | **Reject** |
| **7-day click** | Optimises across a multi-day decision | Credits clicked conversions up to 7 days | **The longest window the platform offers**, and the closest available match to a considered purchase | Still shorter than some real decision cycles; cannot be extended | Yes | **ADOPT** |
| +1-day view | Feeds delivery additional signal | Credits non-clickers | Adds scarce signal on a very thin account | **Credit without any click is the weakest evidence of causation**; inflates apparent results | Yes | **ADOPT with reporting discipline** |
| +1-day engage-through | Adds non-link-click and 5-second video signal | Credits still weaker interactions | more signal | A 5-second video play crediting a registration is near-meaningless for DR | Yes | **OFF if selectable — audit item** |
| Incremental model | Optimises to predicted incremental conversions | Different counting basis | Conceptually the right question | Requires conversion volume DR does not have; cannot be compared to standard in the overview table | Exists | **Defer** |
| Custom model | Optimises to external analytics logic | — | — | Requires an external analytics pipeline DR has not established | Exists | **Defer** |

### G1 CURRENT RECOMMENDATION
```text
ATTRIBUTION MODEL:        Standard
CLICK WINDOW:             7-day
VIEW WINDOW:              1-day
ENGAGE-THROUGH:           OFF if selectable (audit)
```

**WHY — and note this is not a copied convention.** Sam Piliero recommends 7-day click / 1-day view with *zero rationale* (`none_presented`, `evidence_strength: none`) and that claim is **not** the basis here. The basis is: DR's purchase is a multi-day considered decision, and **7 days is the maximum click window Meta currently offers.** DR is not choosing a long window over a longer one — it is taking the ceiling.

**PARENT DECISION-CYCLE RATIONALE:** a parent may see an ad, check the schedule, discuss with a partner or the child, and register days later. A 1-day click window would systematically miss that and teach delivery the wrong lesson.

**WHAT THIS DOES NOT PROVE:** nothing about causality. Attribution assigns *credit*, not *cause*.

> **Mandatory statement.** Meta-attributed conversions **≠** all DR registrations **≠** registrations *caused* by Meta. A longer window credits more conversions — that does not mean Meta caused more. A shorter window credits fewer — that does not mean the ads were worse. View-through credit means the person never clicked.

**COMPARE-ATTRIBUTION REPORTING PLAN:** use **Compare Attribution Settings** to view click-only alongside the delivery setting, so DR can see how sensitive its reported results are to the attribution assumption. Meta requires this feature for any comparison across differing models — the overview table must not be used for that.

> **ATTRIBUTION-WINDOW SHOPPING IS PROHIBITED.** The delivery setting is chosen once, in advance, for a stated reason. Comparison views exist to reveal sensitivity, never to select whichever window makes CPA look best. Any reported figure must state the window it came from.

**UNRESOLVED DEPENDENCY:** Meta states that for certain campaign types not all attribution settings are available. **Whether the Wave 1A candidate objectives differ in available settings was not established** and must be confirmed before an objective is committed. The recommendation is otherwise invariant across the branches.

### REVISIT TRIGGER
Meta changes supported windows · the objective branch resolves and constrains options · DR accumulates enough conversion volume for incremental attribution to be meaningful.

### STATUS
**ENOUGH_EVIDENCE (conditional)** — bounded by one stated objective-branch dependency.

---

## 6. G2 — Four-layer measurement contract

### LAYER 1 — DELIVERY / STRUCTURE
*Question: is Meta able to deliver the structure as configured?*

| Metric | Definition | Source | Read level | Low-volume caveat | Can tell | Cannot tell |
|---|---|---|---|---|---|---|
| Spend | amount charged | Meta | ad set | Meta may spend **±75% of daily budget** on a given day | whether budget moves at all | anything about quality |
| Impressions | times shown | Meta | ad set | tiny absolute numbers | delivery is occurring | audience quality |
| Reach | unique people | Meta | ad set | ~256/30d historically | breadth vs repetition | who they were |
| Frequency | impressions ÷ reach | Meta | ad set | unstable at low reach | saturation pressure | fatigue as a verdict |
| CPM | cost per 1,000 impressions | Meta | ad set | volatile | auction cost direction | creative quality |
| Delivery status | Ads Manager column | Meta | ad / ad set | — | **technical blockers**: in review, *Update required*, *Creative limited*, *Creative fatigue* | performance |
| Learning state | Learning / Learning limited | Meta | ad set | expected state for DR | stability context | **NOT a performance verdict** — Meta: *"Learning limited isn't a penalty"* |

### LAYER 2 — CREATIVE / MESSAGE RESPONSE
*Question: is the message generating qualified movement toward DR's site?*

**The four click-family metrics are distinct and must never be collapsed:**

| Metric | Meta's definition | Note |
|---|---|---|
| **All clicks** | every click on the ad, including likes, comments, profile taps | **Do not use for message quality** |
| **Link clicks** | *"clicks on ad links to specified destinations or experiences, **on or off** Facebook and other Meta technologies"* | includes clicks into on-platform full-screen experiences |
| **Outbound clicks** | *"clicks on links that take people **off** Meta technologies"* | **the metric closest to "went to DR's site"** |
| **Landing page views** | click **and** page load (`optimization-goals-and-attribution.md`) | strictly downstream of an outbound click |

**Preferred metrics and their correct denominators:**

| Metric | Formula | Why this denominator |
|---|---|---|
| Outbound CTR | outbound clicks ÷ impressions | measures message pull toward the site |
| **LPV rate** | **landing page views ÷ outbound clicks** | both count leaving-Meta events; the ratio isolates load/friction |
| Cost per outbound click | spend ÷ outbound clicks | comparable across rounds |
| Cost per LPV | spend ÷ LPV | DR's only observed anchor (~$12.25) |

> **PROHIBITED:** dividing LPV by *all clicks* or by *link clicks* and calling it a landing-page conversion rate. The numerator and denominator count different things. This is the specific metric error the contract exists to prevent (Test 16).

**All Layer-2 reads are DIRECTIONAL at DR's volume**, and per Meta's breakdown-effect instruction, with multiple ads in one ad set the **ad set** is the read level.

### LAYER 3 — QUALIFIED RESPONSE
*Question: are the people acting plausible customers for **this** program?*

**This layer lives in DR's own systems, not in Meta.**

| Signal | Source system | Availability | Note |
|---|---|---|---|
| Landed on the correct school/program page | DR website / analytics | **UNKNOWN — audit** | needs page-level analytics |
| Program availability at that campus | DR registration DB | **AVAILABLE** (DR context fact) | internal |
| Serviceable location of the visitor | DR website / registration record | **UNKNOWN — audit** | self-reported at registration |
| Registration started (unpaid) | DR registration DB | **AVAILABLE** — an unpaid enrolment row exists before payment | the natural "qualified lead" stage |
| Registration completed + paid | DR registration DB | **AVAILABLE** | Layer 4 |
| Child grade / age eligibility | DR registration DB | **INTERNAL ONLY — PROHIBITED from Meta Business Tools** | under-13 data: not in payload, name, or criteria |

**Compliance guardrail restated:** DR may evaluate child eligibility inside its own systems freely. It may **not** send that data, or an event whose *criteria* are that data, to Meta. Unresolved legal questions are not to be solved by guessing.

### LAYER 4 — FINAL BUSINESS OUTCOME
*Truth metric: **paid season registration.***

| Metric | Source of truth | Note |
|---|---|---|
| Paid registrations | **DR's registration database** | the business ledger |
| Registration revenue | DR's registration/payment records | — |
| Ad spend | Meta | — |
| Blended cost per paid registration | spend ÷ **total** paid registrations in period | honest but not causal; **compute only if the denominator is real** |
| Meta-attributed registrations | Meta, at the chosen window | **a separate number, reported separately, never substituted for the ledger** |

> **Use `UNMEASURED`, never zero**, wherever the signal has not been established. Registration-level Meta signal is currently unmeasured in the available extracts — that is not evidence that registrations did not occur.

---

## 7. System-of-record and data-join contract

| Business fact | System of record | Meta can observe? | Join key needed | Availability | Half 2 action |
|---|---|---|---|---|---|
| Ad spend | Meta | yes | — | available | extract |
| Impressions / reach / frequency | Meta | yes | — | available | extract |
| Link / outbound clicks | Meta | yes | — | available | **add to Phase 1 extract** (playbook Decision 8 gap) |
| Landing page views | Meta | yes | — | available in API, absent from current extract | **add to extract** |
| Landed on program page | DR site | no | UTM / click id | **UNKNOWN** | audit |
| Registration started | DR DB | not currently | ad/campaign id on the record | **UNKNOWN** | audit |
| Paid registration | **DR DB** | only if an event is sent | ad/campaign id on the record | available internally | audit |
| Revenue | DR DB | only if sent | same | available internally | audit |
| School / program | DR DB | **must not be tied to child data in Meta** | internal only | available internally | keep internal |
| Campaign / ad set / ad | Meta | yes | ids | available | — |
| Date / time | both | yes | timestamp | available | — |

### Minimum useful join contract
> **Carry a campaign/ad-set/ad identifier from the Meta click through to the registration row.** Practically: UTM parameters (or the platform click identifier) on the destination URL, captured by the registration flow and stored on the registration record.

That single link makes it possible to say *"this registration was associated with this campaign"* — with the attribution caveat attached. **No personal identifiers. No child data. No warehouse.**

```text
GROUND-TRUTH AUDIT REQUIRED — the exact mechanism depends on DR's live site and registration
system, which this wave did not modify and must not assume.
```

---

## 8. AUDIENCE / MESSAGE / STRUCTURE diagnostic tree

Run in order. **Stop at the first failure — do not skip ahead to blame the message.**

**STEP 1 — STRUCTURE / DELIVERY.** Did it deliver? Check Delivery status, spend movement, learning state, recent significant edits.
→ Fail = **STRUCTURE problem.** No message or audience verdict.

**STEP 2 — AUDIENCE SERVICEABILITY.** Did delivery stay inside the intended locations? Is "Reach more people likely to respond" off? Does geo breakdown look plausible — *bearing in mind Meta states complete accuracy cannot be guaranteed*?
→ Fail = **AUDIENCE / configuration problem.**

**STEP 3 — MESSAGE RESPONSE.** Among serviceable exposure, are outbound clicks and LPVs occurring?
→ Fail = **MESSAGE is plausible** — never proven from a tiny sample (Wave 2B ladder applies).

**STEP 4 — QUALIFIED RESPONSE.** Did visitors reach the right program page and start registration?
→ Clicks but no qualification = **message qualification, audience qualification, or landing-page mismatch.** Do not assume which.

**STEP 5 — PAID REGISTRATION.** Do qualified interactions convert?
→ Fail = offer · price · landing page · timing · registration UX · expectation mismatch. **Do not automatically blame targeting.**

**STEP 6 — ATTRIBUTION / MEASUREMENT.** Is the outcome being credited at all?
→ **Separate business failure from measurement failure.** Registrations in DR's ledger that Meta does not report = a measurement gap, not a campaign failure (Test 20). A Meta event with no matching registration = an instrumentation problem, not ad success (Test 21).

---

## 9. Principle vs implementation

| External idea | Principle | Transfers | Implementation | Transfers | Why |
|---|---|---|---|---|---|
| Nick: "creative does all the targeting" | Message shapes who responds | **partial** | Rely on creative instead of settings | **no** | Creative cannot enforce residency; location is a documented control |
| Nick: widen the callout to unlock delivery | Narrow messaging suppresses delivery | **partial** | Broaden the hook | **no** | Points opposite to DR's qualification need — this is exactly what Test 28 guards against |
| Sam: test interests only with proven ads | Isolate one variable | **yes**, scale-independent | Build interest ad sets | **no** | No proven-ad pool; interests rejected anyway (§2) |
| Sam: 7-day click / 1-day view | — | **n/a** | Use 7/1/1 | coincidentally same | **Not the basis of G1** — `none_presented`, zero rationale. DR selects 7-day because it is the platform ceiling |
| Vendor "CRM data join" content | Connecting ads to downstream outcomes is necessary | **yes** | Buy an attribution platform / upload customer lists | **no** | Vendor marketing; DR needs a UTM-to-registration link, not a product |

---

## 10. Real-operator evidence this wave

**Ingested: none. This is an honest result, not a shortfall.**

The Wave 3 questions turned out to be **overwhelmingly platform-determined**: which inputs are controls, which are suggestions, which attribution windows exist, and what each click metric counts are all first-party facts that no practitioner opinion can override. One bounded, gap-driven discovery pass was run for the genuine residual (local-service measurement / CRM-join practice) and produced only:

- **content farms** (benly, sona, adlibrary, metalla, coreppc) — generic "track CPL, ROAS, CTR" with no accounts, no methodology;
- **attribution-vendor blogs** (Cometly, ClicksGeek, DOJO AI) — marketing for products DR has not scoped.

All rejected under `CLAUDE.md §Source selection`. **No second cycle was run**, because no material contradiction remained that operator evidence could resolve.

**Reused, not re-ingested:** Nick Theriot (E2), Sam Piliero (E1/G1) — both already on file, both `opinion` / `evidence_strength: none` on these axes. **Clusters unchanged: META FIRST-PARTY · SAM · NICK · LOOMER · FOXWELL ECOSYSTEM.**

**Practitioner status for E2/G2: `NO_USEFUL_EVIDENCE_FOUND`.**

---

## 11. What we rejected

**Whole-metro city targeting.** Rational for businesses serving a whole metro. Not DR: the 10-mile city radius floor plus Orlando's tourist volume buys unserviceable reach. Would become relevant if DR served the entire metro.

**One ad set per school.** Rational where each unit can be funded and read. Not DR: fragments budget, requires a C2 reopen, and Wave 2B established individual units are unreadable at this volume. Relevant if delivery grows enough that per-school reads become interpretable.

**Interest/detailed targeting.** Rational at scale. Not DR: suggestions don't bind; controls shrink a small audience; no evidenced link to registration.

**Advantage+ audience expansion beyond locations.** Rational where the service area is elastic. Never for DR while serviceability is binary.

**Incremental / custom attribution.** Conceptually the right question. Not DR yet: both need volume or an analytics pipeline DR lacks.

**Attribution platforms / customer-list uploads.** Rational at scale with clean adult data. Not DR now: unscoped cost, and any child-linked data is prohibited.

---

## 12. Unknown / uncertain

**Blocking Half 2 execution: none.**

**Non-blocking (all DR-side audits, not research gaps):**
- Whether a residents-only location selection is available on DR's campaign path.
- Whether the attribution setting is editable after publish, and whether that edit is significant.
- Whether attribution options differ across the Wave 1A candidate objectives.
- What the Ads Manager geographic breakdown actually measures.
- Live Pixel/CAPI state — **still UNKNOWN, still not disproven**.
- Whether the registration flow can capture and store a campaign identifier.
- The exact campus radii and ZIP lists.
- Whether the `DR HISTORIC` custom audience is an inclusion behaving as a suggestion.

---

## 13. Half 2 validation contract

**H-A — AUDIENCE.** *Hard geo controls keep delivery serviceable while leaving Meta free inside them.*
Evidence: location is a documented control; expansion is opt-in by name. **If true:** geo breakdown stays inside the intended areas and registrants come from serviceable addresses. **If false:** meaningful delivery or registrant addresses fall outside — check whether expansion is on, then whether the accuracy disclaimer explains the residual. **Data:** geo breakdown + registrant locations. **Reopen:** persistent out-of-area delivery with expansion off.

**H-B — TARGETING VS MESSAGE.** *Program-specific creative qualification reduces low-quality downstream behaviour without unduly shrinking delivery.*
Evidence: DR HYPOTHESIS; Nick points the other way. **If true:** qualified-response rate rises even if CTR falls. **If false:** delivery collapses with no qualification gain. **Data:** outbound CTR + LPV rate + registration starts per round. **Reopen:** two rounds where qualified response does not improve while delivery suffers.

**H-C — GEOGRAPHY.** *Campus-radius union delivers enough serviceable parents without starving the ad set.*
**If true:** delivery persists at a level comparable to the historical baseline while staying in-area. **If false:** delivery collapses → widen radii deliberately, accepting the qualification cost, and record the tradeoff. **Data:** impressions/reach vs baseline; geo breakdown. **Reopen:** starvation, or a campus list change.

**H-D — ATTRIBUTION.** *7-day click / 1-day view captures the practical parent decision cycle without inviting credit-as-causality errors.*
**If true:** most attributed conversions are click-based, and Compare Attribution Settings shows modest sensitivity. **If false:** results are dominated by view-through, or click-attributed conversions cluster at day 6–7 (suggesting the true cycle exceeds the platform ceiling). **Data:** Compare Attribution Settings, click-only vs full. **Reopen:** view-dominance, or day-7 clustering.

**H-E — MEASUREMENT.** *DR can connect Meta delivery to registration truth well enough to diagnose Audience vs Message vs Structure.*
**If true:** a campaign identifier survives from click to registration row, and Meta-attributed counts can be reconciled against the ledger. **If false:** the diagnostic tree stops at Step 4 and DR is blind past the click. **Data:** the join contract in §7. **Reopen:** immediately if the identifier does not persist. **This is the single highest-value item in the contract.**

---

## 14. Stress-test results — 30 scenarios

| # | Scenario | Result |
|---|---|---|
| 1 | Advantage+ interest expansion | **PASS** — §2 records interests as suggestions that do not bind; DR supplies none |
| 2 | Location control | **PASS** — location held hard; expansion named and switched off |
| 3 | School name in creative | **PASS** — §3 states creative self-qualifies but cannot verify enrolment |
| 4 | Parent 30 min away | **PASS** — Step 2 + Layer 3 treat serviceability as a check, not a success |
| 5 | Tourist / recent visitor | **PASS** — §4 flags the three behaviours and the residents-only audit |
| 6 | Perfect geo, zero delivery | **PASS** — Option B rejected on capacity; H-C prescribes deliberate widening |
| 7 | Broad geo, cheap clicks, no registrations | **PASS** — Layer 2 is directional only; Layer 4 is the ledger |
| 8 | Interest targeting improves CTR | **PASS** — §2 refuses without downstream evidence; Test 27/28 logic applies |
| 9 | Age/gender suggestion vs control | **PASS** — table in §2 mirrors Meta's own split, incl. the "Women→men" example |
| 10 | Child eligibility | **PASS** — §3 and Layer 3 prohibit under-13 data in payload, name, or criteria |
| 11 | Day-5 registration | **PASS** — 7-day click selected precisely for this |
| 12 | View-through conversion | **PASS** — §5 mandatory statement separates credit from cause |
| 13 | 28-day shows more conversions | **PASS** — 28-day click is not even available; §5 bars "longer = more accurate" |
| 14 | Meta reports 3, DR reports 5 | **PASS** — Layer 4 keeps the ledger as truth, Meta as a separate number |
| 15 | Diagnose mismatch vs accept Meta | **PASS** — Step 6 separates business from measurement failure |
| 16 | 10 link clicks, 3 outbound clicks | **PASS** — four-metric distinction + prohibited-denominator rule |
| 17 | Outbound click, no LPV | **PASS** — LPV rate isolates load/friction, not creative failure |
| 18 | High CTR, low LPV rate | **PASS** — routed to destination/expectation mismatch |
| 19 | Strong LPVs, zero qualified response | **PASS** — Step 4 moves diagnosis downstream |
| 20 | Registrations exist, Meta event missing | **PASS** — business success + measurement problem |
| 21 | Meta event fires, no registration | **PASS** — instrumentation issue, not ad success |
| 22 | School split needs a 2nd ad set | **PASS** — §4 returns C2 REOPEN: NO *because* the union sits in one ad set; the reopen path is stated |
| 23 | New city | **PASS** — distinguishes new geography from a separate campaign-level requirement (Wave 2A T8) |
| 24 | 3 clicks vs 1 click | **PASS** — Wave 2B evidence ladder governs; no winner |
| 25 | Attribution-window shopping | **PASS** — explicitly prohibited in §5 |
| 26 | Advantage+ aggregate benchmark | **PASS** — §2 rejects Meta's own percentages as a reason |
| 27 | Qualifying message: CTR falls, registrations rise | **PASS** — Layer 4 outranks Layer 2 |
| 28 | Vague message: CTR rises, qualification falls | **PASS** — same precedence, stated explicitly |
| 29 | Geo reporting limitation | **PASS** — accuracy disclaimer captured; geo breakdown is not residency truth |
| 30 | Objective branch changes | **PASS with flag** — E1/E2/E3/G2 invariant; **G1 carries one stated dependency** (attribution availability by objective) |

```text
tests_run: 30
tests_passed: 30
tests_failed: 0
warnings: 1   (Test 30 — G1's objective-branch dependency, stated not hidden)
```

**One rule was corrected during stress testing.** An earlier draft of §6 proposed *LPV ÷ link clicks* as the landing-page rate. **Test 16 broke it** — link clicks include on-platform full-screen entries, so the denominator over-counts. Corrected to **LPV ÷ outbound clicks**, which is the form now in the contract and which changed the final deliverable.

---

## 15. WAVES 1–3 COMBINED PRE-EXECUTION SNAPSHOT

The full external-research hypothesis, visible together for the first time. **This does not modify `dr-playbook.md`.**

```text
Campaign objective/event:  CONDITIONAL — A1 unresolved; Sales→Website is the current-state reading,
                           Leads→Website gated on CAPI/CRM/website-form prerequisites. NOT settled.
Campaigns:                 1
Ad sets:                   1 (last-known; a starting state, not a cap)
Budget strategy:           keep ad-set budget; reopen C2 if a 2nd ad set enters
Creative introduction:     into the existing ad set, one batched change window, start 2-3 (provisional)
Creative evaluation:       5-state ladder; NOT_EVALUABLE is the expected default; no day-count gate;
                           5-branch diagnostic before any no-spend verdict
Audience:                  Advantage+ audience; Locations HARD; minimum age HARD; exclusions HARD;
                           no interests; no gender; expansion OFF
Geo:                       union of tight campus radii (or ZIP groups) in ONE ad set;
                           residents-only = audit item; geo is a serviceability filter, not proof
Message qualification:     school · sport · child age band · format · schedule · price · dates ·
                           beginner-friendly — never child data into Meta
Attribution:               standard · 7-day click · 1-day view · engage-through off (audit)
Delivery metrics:          spend · impressions · reach · frequency · CPM · delivery status · learning state
Creative metrics:          outbound CTR (÷impressions) · LPV rate (÷OUTBOUND clicks) · cost/outbound click
                           · cost/LPV — all DIRECTIONAL, read at ad-set level
Qualified-response:        DR systems only — program page, registration start, serviceable location
Business outcome:          paid registration, in DR's registration database — the ledger
Measurement gaps:          click→registration join (highest value) · LPV/action columns absent from the
                           current extract · Pixel/CAPI live state UNKNOWN
Knowledge level:           DR HYPOTHESIS throughout — DR proof status: NONE
```

---

## 16. HALF 2 INPUT CONTRACT

```yaml
half_2_input_contract:

  knowledge_level: DR_HYPOTHESIS

  business_outcome:
    final_truth: paid_season_registration
    system_of_record: DR_registration_database   # not Meta

  optimization:
    objective_event_status: CONDITIONAL_UNRESOLVED
    legitimate_branches: [sales_website, leads_website_if_prerequisites_clear]

  architecture:
    campaigns: 1
    ad_sets: 1
    budget: ad_set_budget

  creative:
    introduction: existing_ad_set_one_batched_window
    evaluation: five_state_ladder_directional_only
    no_spend: five_branch_diagnostic_before_verdict

  audience:
    audience_mode: advantage_plus_audience
    hard_controls: [locations, minimum_age_adult, custom_audience_exclusions]
    suggestions: []                      # none supplied
    prohibited_or_avoided_inputs:
      - interests_as_controls
      - gender_narrowing
      - age_upper_bound
      - reach_more_people_likely_to_respond   # breaks serviceability
      - any_under_13_data_in_payload_event_name_or_criteria

  geography:
    configuration: union_of_campus_radii_or_zip_groups_in_one_ad_set
    serviceability_rule: "geo is a serviceability filter; Meta states complete accuracy cannot be guaranteed"
    school_qualification_rule: "message and landing page qualify school; Meta cannot target enrolled families"
    architecture_reopen: {C1: false, C2: false}

  attribution:
    delivery_setting: {model: standard, click: 7_day, view: 1_day, engage_through: off_if_selectable}
    reporting_comparison: "Compare Attribution Settings — click-only alongside; window-shopping prohibited"
    unresolved_dependency: "attribution availability by objective not confirmed for A1 branches"

  measurement:
    delivery_layer: [spend, impressions, reach, frequency, cpm, delivery_status, learning_state]
    creative_layer: [outbound_ctr, lpv_rate_over_outbound_clicks, cost_per_outbound_click, cost_per_lpv]
    qualified_response_layer: [program_page_reached, registration_started, serviceable_location]  # DR systems
    final_registration_layer: [paid_registrations, revenue, blended_cost_per_registration, meta_attributed_separately]

  required_ground_truth_audits:
    - Ads Manager: is a residents-only location selection available on DR's campaign path
    - Ads Manager: current DR HISTORIC custom audience — inclusion behaving as a suggestion
    - Ads Manager: is engage-through separately selectable
    - Ads Manager/Events Manager: live Pixel/CAPI state (still UNKNOWN)
    - Website/registration: can a campaign identifier be captured and stored on the registration row
    - Extract: add link clicks, outbound clicks, landing page views and action columns to Phase 1

  required_data_fields:
    - campaign_id / adset_id / ad_id
    - UTM or click identifier on the destination URL
    - program/school identifier on the landing page
    - registration_started timestamp
    - paid_registration timestamp
    - registration amount
    # NO personal identifiers. NO child data.

  evidence_labels: [DIRECTIONAL, SUFFICIENTLY_STRONG]

  unresolved:
    blocking_half_2: []
    non_blocking:
      - residents_only_availability
      - attribution_editability_after_publish
      - attribution_options_by_objective
      - geo_breakdown_semantics
      - pixel_capi_live_state
      - join_mechanism_feasibility

  first_questions_DR_must_answer:
    audience: "Does delivery stay inside the serviceable campus areas, and do registrants come from them?"
    message: "Does program-specific qualifying creative improve qualified response even if CTR falls?"
    structure: "Can a campaign identifier survive from the Meta click to the registration row?"
```

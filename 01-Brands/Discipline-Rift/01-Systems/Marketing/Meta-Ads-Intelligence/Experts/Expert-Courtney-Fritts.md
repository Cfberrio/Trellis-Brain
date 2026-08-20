---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/courtney-fritts.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/courtney-fritts.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Courtney Fritts"
---

# Courtney Fritts

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Andrew-Foxwell|Andrew Foxwell — mismo cluster de independencia]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/courtney-fritts.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** courtney-fritts
**Watchlist priority:** 1
**Topics:** creative_testing · creative_strategy · campaign_structure
**Sources processed:** 2
**Panel status:** **SOURCE_CONTRIBUTOR** (assigned 2026-08-19). Two sources, **both UNDATED** — publication year is not determinable from retrieval, which alone prevents any claim here from carrying a decision about current platform behaviour. Additionally shares the `foxwell-ecosystem` independence cluster: **she and Andrew Foxwell are one voice, not two confirmations.** Her budget-scoped statement on direct competition below ~$100/day remains directionally useful and is not deleted.
**Last updated:** 2026-08-14
**Independence cluster:** **FOXWELL ECOSYSTEM** — publishes on foxwelldigital.com, shares a cluster with `andrew-foxwell.md`. **Not an independent confirmation of that source, and these two do not agree on everything** (see Contradictions).

## Sources processed

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.foxwelldigital.com/blog/why-creatives-dont-spend-on-meta-ads` | article | **null** (byline "Oct 14", year not determinable from retrieval) | 2026-08-14 | **2** | D3, D4 |
| `https://www.foxwelldigital.com/blog/meta-creative-testing-finding-your-path-to-consistent-winners` | article | **null** (byline "Dec 31", year not determinable) | 2026-08-14 | **2** | D1, D3 |

**Dating weakness — flagged, not guessed.** Neither retrieval yielded a year. Per the ingest contract an undated claim is weak because platform behaviour changes without changelogs, and `published_at: null` is recorded rather than a plausible reconstruction. **This materially caps how much weight these claims may carry alone**, and is the reason the D1 decision in `output/wave-2b-creative-operating-method.md` rests primarily on first-party Meta mechanics and DR's own arithmetic, with Fritts recorded as converging support rather than as the basis.

**Stated context:** agency-side paid social, ecommerce/DTC framing. Claims multi-account experience: *"We've managed accounts scaling from thousands to tens of thousands in daily spend"* and *"We've seen every testing methodology work—and fail."* **No case studies, client results, or performance data are presented in either article.**

**Retrieval:** WebFetch (native), full body, both.

---

## Claims — "Finding your path to consistent winners" (undated)

### creative_testing — Testing method must be chosen by account context, not by best practice

```yaml
topic: creative_testing
claim: No single creative-testing method is universally correct; the right method depends on daily budget, creative production volume relative to budget, performance predictability, risk tolerance, and account maturity/data density.
recommended_action: "Select a creative-testing method by assessing your budget, creative volume, data density, account maturity and risk tolerance rather than adopting a single best-practice method."
context: choosing among competing creative-testing methods
business_type: ecommerce
spend_level: "author claims experience across accounts from thousands to tens of thousands per day"
conversion_volume_context: "'data density' named as a determining factor"
research_question_ids: [D1]
published_at: null
source_url: https://www.foxwelldigital.com/blog/meta-creative-testing-finding-your-path-to-consistent-winners
author: Courtney Fritts
evidence: "We've managed accounts scaling from thousands to tens of thousands in daily spend" / "We've seen every testing methodology work—and fail." / determining factors named: daily budget size, creative production volume relative to budget, performance predictability/consistency, risk tolerance, account maturity/data density
timestamp: "framework selection"
confidence: high
evidence_basis: multi_account_experience
evidence_basis_details: "Cross-account experience asserted; no case studies, metrics, or comparative results presented for any method."
evidence_strength: weak
platform_validation_status: NOT_APPLICABLE
```

> "We've seen every testing methodology work—and fail."

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** **yes** · **implementation_transfers:** n/a
**reason:** `NOT_APPLICABLE` — a strategy-selection assertion Meta documentation cannot validate. **The principle transfers cleanly and is scale-independent**: it is a direct external endorsement of the context-conditional posture this domain already applies, and a caution against the "best practice" framing that produced most of the rejected content-farm material. Costs nothing to adopt.

### creative_testing — Under roughly $100/day, direct competition may be the only viable method

```yaml
topic: creative_testing
claim: For accounts under approximately $100/day, dedicated testing structures are not viable and direct competition between ads (or manual bidding) may be the only workable approach; for accounts producing only 1-3 concepts weekly on limited budgets, a consolidated budget approach with minimums is more efficient than a per-batch testing ad set.
recommended_action: "At low daily budgets, let ads compete directly rather than building dedicated testing structures."
context: "accounts under $100/day"
business_type: ecommerce
spend_level: "under $100/day; contrasted with 'under $5K/day: ~$100 per ad set daily' and 'larger accounts: ~$1000 per ad set'"
conversion_volume_context: "1-3 concepts weekly with limited budgets"
research_question_ids: [D1]
published_at: null
source_url: https://www.foxwelldigital.com/blog/meta-creative-testing-finding-your-path-to-consistent-winners
author: Courtney Fritts
evidence: "Method 3 (direct competition) or Method 4 (manual bids) might be your only viable options." (stated for accounts under $100/day) / for accounts producing 1-3 concepts weekly with limited budgets, a CBO-with-minimums approach is suggested as more efficient than a per-batch testing ad set
timestamp: "budget-scoped guidance"
confidence: medium
evidence_basis: multi_account_experience
evidence_basis_details: "Budget-scoped recommendation asserted from agency experience. No data, no comparison, and the $100/day boundary is given without derivation. Confidence medium because the method labels ('Method 3', 'Method 4') were captured through a summarising retrieval rather than a full verbatim method table."
evidence_strength: weak
platform_validation_status: NOT_APPLICABLE
```

> "Method 3 (direct competition) or Method 4 (manual bids) might be your only viable options."

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** **yes** · **implementation_transfers:** partial
**reason:** **The single most directly relevant external statement found in this wave for D1.** DR's historical spend is roughly an order of magnitude *below* the $100/day boundary at which this author says dedicated testing structures stop being viable — so on this author's own scoping, DR is well inside "direct competition is the only option" territory. **This converges with, and does not create, DR's decision**, which rests on Meta's in-campaign creative-test design, consolidation guidance, and DR's own delivery arithmetic. **The $100/day figure must not become a DR threshold** — it is undated, underived, and asserted; only the direction transfers. Also note the internal tension with `andrew-foxwell.md`, recorded below.

---

## Claims — "Why creatives don't spend on Meta ads" (undated)

### creative_testing — Non-spend is attributed to creative signals, especially early engagement

```yaml
topic: creative_testing
claim: Ads receive little spend because Meta's system predicts weak engagement from early signals — hooks that fail in the first seconds, pacing that causes early drop-off, and overused creative patterns.
recommended_action: "Diagnose non-spend by examining hook strength, pacing and early drop-off rather than assuming a delivery fault."
context: ads under-delivering within a live structure
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [D4]
published_at: null
source_url: https://www.foxwelldigital.com/blog/why-creatives-dont-spend-on-meta-ads
author: Courtney Fritts
evidence: "The first three seconds decide everything. If users aren't stopping, the rest of your story kind of doesn't matter." / "If most users are dropping off before 5 seconds, your creative isn't being rejected for its offer...the ad creative is being rejected for its pacing." / Meta "punishes content that leads to app exits or disengagement."
timestamp: "causes"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Conceptual explanation of algorithmic behaviour. No test data, account examples, or comparative metrics presented anywhere in the article."
evidence_strength: none
platform_validation_status: INSUFFICIENT_EVIDENCE
```

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** `INSUFFICIENT_EVIDENCE` — Meta's documented causes of under-delivery (`creative-testing-ab-testing-and-delivery-diagnostics.md`, `learning-limited.md`) include audience size, budget, bid/cost controls, auction competitiveness, creative fatigue and audience saturation. **Meta does document *Creative limited* / *Creative fatigue* delivery statuses, so creative-side causes are real** — but Meta does not state that low spend indicates weak hooks or pacing, and this author presents no evidence for the mechanism. **This is the same position as Nick Theriot, from the same discourse, and must not be counted as independent corroboration of it.** At DR's delivery, attributing non-spend to creative would skip the documented non-creative causes entirely.

### creative_testing — Give a creative enough spend and time before killing it

```yaml
topic: creative_testing
claim: A creative should not be judged until it has accumulated meaningful spend and run for a meaningful period; single-digit-dollar spend is insufficient for the system to evaluate it.
recommended_action: "Spend at least 3x your CPA (or 3x the creative's production cost) before killing a creative, and ideally also let it run at least 7 days."
context: deciding whether to kill an under-spending creative
business_type: ecommerce
spend_level: "references ads sitting at '$6 of spend' and '$5-$10 in spend' as insufficient"
conversion_volume_context: null
research_question_ids: [D3, D4]
published_at: null
source_url: https://www.foxwelldigital.com/blog/why-creatives-dont-spend-on-meta-ads
author: Courtney Fritts
evidence: "Budget for real learning. Try to spend at least 3× your CPA (or 3x the amount you paid for the creative to be made) before calling it quits...Ideally your creative would get one or both of these things above AND also run for at least 7 days."
timestamp: "recommendations"
confidence: high
evidence_basis: opinion
evidence_basis_details: "Rule of thumb asserted with no derivation, no data, and no account context for the multiplier or the 7-day figure."
evidence_strength: none
platform_validation_status: NOT_APPLICABLE
```

> "Try to spend at least 3× your CPA (or 3x the amount you paid for the creative to be made) before calling it quits… Ideally your creative would get one or both of these things above AND also run for at least 7 days."

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** **yes** · **implementation_transfers:** **no**
**reason:** **Two distinct contributions, and they must be separated.**
(1) **PRINCIPLE — transfers.** "Do not kill a creative that has not accumulated meaningful exposure" is the same conclusion DR's evidence ladder reaches from Meta's side, and it is a genuine external counter-position to reflexive killing.
(2) **The "at least 7 days" figure is the only external, non-Meta statement located that bears on a natural-delivery observation window.** It matters because DR's previous review condition borrowed 7 days from Meta's *A/B-test* guidance — a different mechanism. This claim means a multi-day floor can be stated as an **EXTERNAL PRACTITIONER CLAIM (`opinion`, `evidence_strength: none`, undated)** rather than mis-attributed to Meta. **It is weak evidence and must be labelled as such.**
(3) **The numbers do not transfer.** DR has **no measured cost-per-registration**, so "3× CPA" is uncomputable; "3× creative production cost" is a production-economics heuristic unrelated to statistical readability. `NOT_APPLICABLE` — a spending-discipline heuristic Meta documentation cannot validate.

---

## Contradictions within this cluster

**Recorded, material, and unresolved by either author.** `andrew-foxwell.md` associates the dedicated per-batch testing ad set with *"brands with a small creative volume or especially those new to advertising"*. This author states that under ~$100/day, direct competition or manual bids *"might be your only viable options"*.

**One scopes by creative volume, the other by budget.** DR is low on both; its **binding constraint is budget**, so the budget-scoped statement governs for DR. This is a context resolution, **not a vote** — and note that the two positions come from the *same ecosystem*, so their disagreement is evidence that the question is genuinely context-dependent rather than settled.

## Open questions from this source

- **Neither article's publication year could be determined.** Both are treated as weak on that basis alone.
- The $100/day boundary, the 3× multipliers and the 7-day figure are all asserted without derivation, data, or account context.
- The full "Method 1–4" taxonomy was captured through a summarising retrieval rather than verbatim; the method labels should be re-verified before any of them is cited by name.
- No results are presented for any method, so nothing here evidences that any approach *outperformed* another.

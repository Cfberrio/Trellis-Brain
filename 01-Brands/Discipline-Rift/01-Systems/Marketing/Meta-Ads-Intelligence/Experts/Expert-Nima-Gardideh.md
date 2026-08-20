---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/nima-gardideh.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/nima-gardideh.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Nima Gardideh"
  - "Pearmill"
---

# Nima Gardideh

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-1A-Objective-and-Optimization-Event|Wave 1A — objetivo y evento de optimización]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/nima-gardideh.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** nima-gardideh
**Role:** Co-founder / CTO, Pearmill (performance agency)
**Topics:** optimization · measurement · campaign_structure
**Sources processed:** 1
**Panel status:** **SOURCE_CONTRIBUTOR** (assigned 2026-08-19). Co-founder/CTO of a performance agency, so Meta operation is plausible — but this file holds **one blog post on his own agency's site, with no account, spend, client or volume data**. His conversion-event criteria framework is a genuine contribution and its claims stand on their own merit. What is not established is that he belongs at the same confidence level as the operators with dated, multi-source, in-account material. **Status is about corroboration depth, not claim quality, and no claim here is downgraded because of it.**
**Last updated:** 2026-08-13
**Evidence model:** v2. Evidence is **self-reported** and not independently verified.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://pearmill.com/blog/how-to-choose-the-best-conversion-events-for-google-meta-ads-to-lower-cac` | article | 2025-05-22 | 2026-08-13 | **2** | A2, A3 |

**Stated context:** agency practice across mixed ecommerce and B2B/SaaS clients. No client spend or account volume disclosed.

---

## Claims — article (2025-05-22)

### optimization — Three testable criteria for choosing a conversion event

```yaml
topic: optimization
claim: A conversion event is suitable for optimization only if it fires often enough, occurs soon enough after the click, and correlates strongly with revenue.
recommended_action: "Select an optimization event that fires at least 50 times per week, occurs within 1-3 days of the click, and shows a correlation with revenue of at least 0.6."
business_type: agency
spend_level: null
conversion_volume_context: "states a 50-events-per-week floor for the chosen event"
research_question_ids: [A2]
published_at: 2025-05-22
source_url: https://pearmill.com/blog/how-to-choose-the-best-conversion-events-for-google-meta-ads-to-lower-cac
author: Nima Gardideh
evidence: "pick an event that happens within the first 1-3 days" / "correlation of at least 0.6 or higher" / "fires at least 50 times / week"
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Criteria asserted as agency practice. A general outcome claim is made — 'We have examples of CAC reducing by 50% by picking a better event to optimize towards' — with no client named, no baseline, and no dataset."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** high (as a test) · **modification_required:** yes (thresholds)
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **This is the most directly usable A2 contribution in the batch**, because it converts "pick a good event" into three checks DR can actually run against its own funnel: does the candidate event fire enough, does it happen fast enough after the click, and does it actually track the outcome we care about. The 0.6-correlation and 1–3-day criteria are distinctive — no other source in this batch states them. The **50/week floor is not independent evidence**: it restates the same industry heuristic that traces back to Meta's own learning-phase framing (see the framework note in the batch report). The correlation test in particular cannot be run by DR today — it requires paired event and registration data, i.e. a Half 2 capability.

---

### optimization — When the ideal event is too rare, qualify the event rather than move up-funnel

```yaml
topic: optimization
claim: Where the desired event fires too rarely, gate the signup flow with qualifying questions and fire the optimization event only for users whose answers qualify them.
recommended_action: "Add qualifying questions to the sign-up flow, and send the conversion event to the ad network only when people answer in the right combination."
business_type: agency
spend_level: null
conversion_volume_context: null
research_question_ids: [A2, A3]
published_at: 2025-05-22
source_url: https://pearmill.com/blog/how-to-choose-the-best-conversion-events-for-google-meta-ads-to-lower-cac
author: Nima Gardideh
evidence: "add questions to your sign-up flow and qualify the users coming from paid traffic before you let them sign-up" / "send events to ad networks when people answer the questions in the right combination."
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Described as agency practice; no test, comparison, or account result presented for the qualified-event approach specifically."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** high · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** **This is a genuinely different answer to A2/A3 than the rest of the batch, and it maps unusually well onto DR.** Every other source frames the low-volume problem as a vertical choice — move up the funnel or don't. This one moves *sideways*: keep the event shallow enough to fire, but only let it fire for people who qualify. DR's qualification criteria are unusually crisp and knowable at form time — child's age band (6–12) and school/geography — which is exactly the input this method needs. It directly addresses A3's core risk (cheap actions from parents who can never register) without requiring a platform feature Meta does not offer for website funnels.

Modification required: DR has no signup gating today, and building it is a landing-page/form change outside this domain. It also trades volume for quality at an account that is already volume-starved — so it may make the learning problem worse, not better. That tension is real and is exactly what Wave 1B must cost out.

---

## Contradictions within this author

None internal.

## Open questions from this author

- No account data supports the 50%-CAC-reduction claim; no client, baseline, or period is given.
- The 0.6 correlation threshold is asserted with no derivation — why 0.6 rather than 0.4 or 0.8 is unexplained.
- The qualified-event method is not costed: he never addresses how much volume is lost by gating, or what happens when gating pushes an already-thin event below the delivery system's needs.

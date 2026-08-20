---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/haus.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/haus.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Haus"
---

# Haus

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Taylor-Holiday|Taylor Holiday]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Wave-3-Audience-and-Measurement|Wave 3 — audiencia, geo, atribución y medición]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/haus.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** haus
**Type:** measurement vendor (incrementality-testing platform) — organizational author, no individual credited
**Topics:** measurement · campaign_structure · creative_testing
**Sources processed:** 1
**Panel status:** **ORGANIZATIONAL_SOURCE** (assigned 2026-08-19). Not a person — a measurement vendor with no individual author credited, so no operator claim is being made or implied. It carries **the strongest evidence basis in the panel** (640 aggregated incrementality experiments) **and** a declared conflict of interest, since its recommendation is the service it sells. Both facts belong on the label together. Its findings may be cited as vendor-aggregated evidence; its prescription is discounted.
**Last updated:** 2026-08-13
**Evidence model:** v2. All evidence is **self-reported by the vendor** and not independently verified.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://www.haus.io/blog/optimizing-meta-ads-a-playbook-for-brands` | article | 2025-08-15 | 2026-08-13 | **4** | A2, A3 |

**Stated context:** DTC/ecommerce brands. Findings aggregated from **640 Haus incrementality experiments across hundreds of brands spanning different industries**. No individual author credited. **Commercial interest declared:** Haus sells incrementality testing, and its A3-relevant conclusion ("test incrementality rigorously") is the service it sells. Weigh accordingly — that does not make the experimental findings wrong, but it is the one source in this batch whose recommendation and product coincide exactly.

---

## Claims — article (2025-08-15)

### campaign_structure — Mid-funnel effects differ across direct incremental return, post-treatment lift, and off-DTC halo

> **Corrected 2026-08-13 after audit.** This claim was originally written as "mid-funnel looks worse *in-platform* but measures better incrementally." That was a misreading. **DTC iROAS in the source is already an incrementality metric**, not Meta's in-platform attributed ROAS. Haus therefore does **not** evidence any claim about Meta's platform reporting being systematically misleading. What it evidences is that the *same* optimization choice measured differently across three incremental outcomes.

```yaml
topic: optimization
claim: In a large ecommerce/omnichannel corpus, mid-funnel optimization produced lower direct DTC incremental return but higher post-treatment lift and larger off-DTC halo effects than lower-funnel optimization.
recommended_action: When evaluating a mid-funnel optimization choice, measure more than direct incremental return — post-treatment and off-channel effects moved in the opposite direction in this corpus.
business_type: ecommerce
spend_level: null
conversion_volume_context: "aggregate across 640 incrementality experiments; mid-funnel ran at 85% lower daily spend than lower-funnel"
research_question_ids: [A2, A3]
published_at: 2025-08-15
source_url: https://www.haus.io/blog/optimizing-meta-ads-a-playbook-for-brands
author: Haus
evidence: "Mid-funnel campaigns delivered 14% lower DTC iROAS at 85% lower daily spend than lower-funnel campaigns, but these were offset by 9% higher post-treatment lift and larger omnichannel (retail) halo effects."
timestamp: null
confidence: high
evidence_basis: self_reported_test
evidence_basis_details: "Aggregated results of 640 controlled incrementality experiments (test/control). Directional percentages published; underlying per-experiment data and methodology detail not published."
evidence_strength: moderate
platform_validation_status: NOT_APPLICABLE
```

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** **Transferability is limited, and the corrected reading makes it more limited than first recorded.** Two of the three measured outcomes — post-treatment lift and off-DTC/retail halo — depend on a multi-channel structure DR does not have. DR sells one thing, in one metro, through one channel; there is no retail halo for a mid-funnel choice to show up in. So the specific finding largely does not travel.

What survives is narrow and worth keeping: **an optimization choice can look different depending on which outcome you measure it against, so a single headline number is a weak basis for judging one.** That is a caution about measurement design, not evidence about Meta's reporting, and not evidence about DR.

IMPLEMENTATION does not transfer at all: DR cannot run incrementality experiments at its volume.

---

### optimization — Mid-funnel works best precisely where lower-funnel lacks data

```yaml
topic: optimization
claim: Mid-funnel optimization is most useful for brands whose purchase-event volume is too low for lower-funnel optimization to work well.
recommended_action: Consider mid-funnel optimization when purchase-event volume is insufficient for lower-funnel optimization.
business_type: ecommerce
spend_level: null
conversion_volume_context: "explicitly scoped to brands with fewer than 5,000 purchase events per week"
research_question_ids: [A2]
published_at: 2025-08-15
source_url: https://www.haus.io/blog/optimizing-meta-ads-a-playbook-for-brands
author: Haus
evidence: "Mid-funnel tactics work particularly well for brands with less than 5,000 purchase events per week — cases where lower-funnel optimization might not have enough data to work optimally."
timestamp: null
confidence: high
evidence_basis: self_reported_test
evidence_basis_details: "Attributed to the same 640-experiment corpus. The <5,000/week figure is a segmentation boundary, not a measured threshold, and no per-segment result is shown."
evidence_strength: moderate
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** **The single most on-point external claim found for A2** — it states the up-funnel-when-volume-is-thin logic as a measured pattern rather than folklore, and it points the same way as Meta's own learning-limited remedy. But read the scale honestly: **5,000 purchase events per week is Haus's LOW bucket.** DR's last measured window produced 10 link clicks in 30 days. The direction transfers; the boundary is roughly three orders of magnitude away from DR and must never be cited as if DR sits inside their sample.

---

### measurement — Upper-funnel shows higher new-customer share and large off-platform halo

```yaml
topic: measurement
claim: Upper-funnel campaigns reach a higher proportion of new customers and generate substantial sales impact not visible in platform reporting.
recommended_action: null
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [A3]
published_at: 2025-08-15
source_url: https://www.haus.io/blog/optimizing-meta-ads-a-playbook-for-brands
author: Haus
evidence: "These campaigns achieved 21% more impact on new customers (81% vs. 67% for lower-funnel), and a 138% halo effect on non-DTC sales." / "For some tactics, $100 of reported revenue in-platform correlated to $600 of incremental business gains once all channels were counted (this was especially true for brand awareness campaigns)."
timestamp: null
confidence: high
evidence_basis: self_reported_test
evidence_basis_details: "Same experiment corpus; percentages only, no sample sizes or per-brand breakdown. The $100→$600 figure is explicitly scoped to 'some tactics'."
evidence_strength: moderate
platform_validation_status: NOT_APPLICABLE
```

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** The mechanism depends on multi-channel distribution (retail halo, non-DTC sales) that DR does not have — DR sells one thing through one channel. Recorded because it is the evidentiary basis for the claim above, not because DR should expect a halo.

---

### measurement — Validate optimization choices with incrementality, not platform metrics

```yaml
topic: measurement
claim: In-platform metrics alone are insufficient to judge whether an optimization choice is working.
recommended_action: Run rigorous incrementality testing (test/control) rather than relying on in-platform reporting to evaluate an optimization decision.
business_type: ecommerce
spend_level: null
conversion_volume_context: null
research_question_ids: [A3]
published_at: 2025-08-15
source_url: https://www.haus.io/blog/optimizing-meta-ads-a-playbook-for-brands
author: Haus
evidence: "Test incrementality rigorously. Don't rely on in-platform metrics alone, especially if much of your business impact happens outside the DTC environment."
timestamp: null
confidence: high
evidence_basis: opinion
evidence_basis_details: "Prescription, not a finding — and it is precisely the service the author sells. The 640-experiment corpus demonstrates the method was used; it does not evidence that every advertiser should buy it."
evidence_strength: none
platform_validation_status: NOT_APPLICABLE
```

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** no
**reason:** PRINCIPLE — do not let platform-attributed cost-per-event be the only judge of an optimization choice — is sound and cheap to hold. IMPLEMENTATION is out of reach: a holdout/geo-split requires volume DR does not have, and splitting DR's delivery would starve both cells. For DR the usable substitute is downstream truth (did registrations actually arrive?), which is a Half 2 capability, not a test design.

---

## Contradictions within this author

None internal.

## Interpretation cautions (added 2026-08-13)

- **"DTC iROAS" is an incrementality measure, not platform-attributed ROAS.** Do not cite this source for any claim about Meta's in-platform reporting. It never measured that.
- The corpus is ecommerce/omnichannel. Its headline effects run through retail halo and off-DTC sales — mechanisms **DR does not have**.
- The genuinely useful DR principle in this area — *a proxy-event CPA must ultimately be checked against downstream paid registrations* — is sound but **is not proven by this source**. It stands on its own logic and belongs to DR's Half 2 measurement design. Do not attribute it to Haus.

## Open questions from this author

- No per-segment results are published for the "<5,000 purchase events per week" bucket, so the claim that mid-funnel helps low-volume brands is asserted from the corpus rather than shown for that slice.
- No floor is stated. Nothing indicates whether the pattern survives at very low volume, and the article never contemplates accounts in DR's range.
- "Mid-funnel" is never defined as a specific event, so which rung of a ladder it corresponds to is unresolved.

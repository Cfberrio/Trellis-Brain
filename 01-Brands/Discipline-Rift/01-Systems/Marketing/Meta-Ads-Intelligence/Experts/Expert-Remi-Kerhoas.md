---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/experts/remi-kerhoas.md"
repo_path: domains/ads/meta/intelligence/knowledge/experts/remi-kerhoas.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/expert
  - discipline-rift
aliases:
  - "Rémi Kerhoas"
  - "Remi Kerhoas"
---

# Rémi Kerhoas

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Corpus/Video-Corpus-Coverage|Corpus de video — cobertura 463]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Contradictions-Register|Registro de contradicciones]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Learning-Phase|Meta oficial — learning phase]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/experts/remi-kerhoas.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Slug:** remi-kerhoas
**Role:** agency practitioner, contributor to Search Engine Land
**Topics:** optimization · measurement · platform_changes
**Sources processed:** 1
**Panel status:** **SOURCE_CONTRIBUTOR** (assigned 2026-08-19). One Search Engine Land article, admitted deliberately as the **only dissent from the 50-events-per-week consensus** — which is exactly why it must not be quietly upgraded: a lone counterweight carries more weight than it has earned if it is treated as an operator finding. This file already records that its **evidence is experience only, citing no account data, case study, or external research anywhere**. Keep the dissent; keep the label.
**Last updated:** 2026-08-13
**Evidence model:** v2.

## Sources processed

| Canonical URL | Type | Published | Captured | Claims | Questions |
|---|---|---|---|---|---|
| `https://searchengineland.com/meta-ads-ai-best-practices-better-results-455324` | article | 2025-05-13 | 2026-08-13 | **3** | A1, A2, A3 |

**Stated context:** agency practice; explicitly discusses niche, high-ticket, and SMB accounts that never reach conventional volume thresholds. No spend or client data disclosed. **Evidence is experience only** — the article cites no account data, case study, or external research anywhere.

**Why this source was shortlisted:** it is the only source found that *dissents* from the 50-events-per-week consensus. Its value is as a counterweight, not as corroboration.

---

## Claims — article (2025-05-13)

### optimization — The 50-per-week threshold can be gone below

```yaml
topic: optimization
claim: The conventional 50-results-per-week-per-ad-set guidance can be lowered where the customer journey justifies it, and failing to reach it is not grounds for restructuring.
recommended_action: "Do not rebuild an account merely because an ad set will not reach 50 results per week; judge against the customer journey instead."
business_type: agency
spend_level: null
conversion_volume_context: "explicitly addresses niche and high-ticket businesses that will not reach 50 conversions per week per ad set"
research_question_ids: [A2]
published_at: 2025-05-13
source_url: https://searchengineland.com/meta-ads-ai-best-practices-better-results-455324
author: Rémi Kerhoas
evidence: "Meta Ads used to advise for 50 results per week per ad set. From my experience, you can lower that figure, especially if it makes sense in terms of the customer journey." / "Many businesses won't hit 50 conversions per week per ad set, especially in niche or high-ticket industries. That's not a reason to panic or rebuild."
timestamp: null
confidence: high
evidence_basis: experience_claim
evidence_basis_details: "Explicitly framed as personal experience ('From my experience'). No account data, no comparison, no example account given."
evidence_strength: weak
platform_validation_status: PARTIALLY_SUPPORTED
```

**applicability_to_DR:** high · **modification_required:** no
**principle_transfers:** yes · **implementation_transfers:** yes
**reason:** **Directly relevant, because DR will not reach 50 registrations per week under any budget it is likely to fund.** If the only available reading of the threshold were "below 50 you cannot optimize," DR's entire event question would collapse into "you may not use a deep event." This source says that reading is too strong.

`PARTIALLY_SUPPORTED` is deliberate: Meta's own wording supports the *softness* of the threshold — `learning-phase.md` says ad sets exit learning *"as soon as they can deliver stably"* and that ~50 is where that *"usually"* happens, and `learning-limited.md` states plainly *"Learning limited isn't a penalty."* So Meta corroborates that 50 is not a hard floor. What Meta does **not** support is the further implication that operating below it is fine — Meta says learning-limited ad sets are *"less stable and usually have a higher CPA."* The claim is right that it is not a rebuild trigger; it is silent on what it costs.

---

### optimization — Use a manually defined qualified-visit custom conversion instead of the default goal

```yaml
topic: optimization
claim: A manually configured custom conversion representing a qualified visit is preferable to accepting the platform's default goal setup.
recommended_action: "Use the Conversions performance goal with a manually created 'qualified visit' custom conversion rather than the default option."
business_type: agency
spend_level: null
conversion_volume_context: null
research_question_ids: [A2, A3]
published_at: 2025-05-13
source_url: https://searchengineland.com/meta-ads-ai-best-practices-better-results-455324
author: Rémi Kerhoas
evidence: "Instead, you need to use the Conversions goal and manually set up a qualified visit custom conversion. This subtle difference will have a massive impact on your funnel."
timestamp: null
confidence: medium
evidence_basis: experience_claim
evidence_basis_details: "Asserted with an emphatic outcome claim ('massive impact') and no supporting measurement whatsoever."
evidence_strength: weak
platform_validation_status: UNVALIDATED
```

**applicability_to_DR:** medium · **modification_required:** yes
**principle_transfers:** yes · **implementation_transfers:** partial
**reason:** Points the same direction as Gardideh's qualified-event method from an independent source — define the event yourself around quality rather than accepting a generic one. That convergence is worth noting, though both are assertions rather than evidence. What "qualified visit" means concretely is never defined here, so DR would have to define it (time on page? scroll? reaching the registration step?), and DR cannot currently see whether such an event correlates with registration. The "massive impact" phrasing is exactly the kind of unmeasured superlative this system exists to discount.

---

### measurement — Server-side tracking is not worth the effort for low-volume SMBs

```yaml
topic: measurement
claim: Server-side tracking implementation is not worthwhile for SMB advertisers with low conversion volumes.
recommended_action: "Do not prioritize server-side tracking implementation for an SMB with low conversion volume."
business_type: agency
spend_level: null
conversion_volume_context: "scoped to SMBs with low conversion volumes"
research_question_ids: [A3]
published_at: 2025-05-13
source_url: https://searchengineland.com/meta-ads-ai-best-practices-better-results-455324
author: Rémi Kerhoas
evidence: "However, for SMBs with low conversion volumes, it's most certainly not worth the effort."
timestamp: null
confidence: medium
evidence_basis: opinion
evidence_basis_details: "Bare assertion; no cost/benefit shown, no threshold for 'low volume', no evidence."
evidence_strength: none
platform_validation_status: NOT_APPLICABLE
```

**applicability_to_DR:** low · **modification_required:** yes
**principle_transfers:** partial · **implementation_transfers:** no
**reason:** Recorded because it bears on the *cost* of A3 safeguards, and because it points **against** the direction most sources push (send more/better signal back). But it is the weakest-evidenced claim in this batch — a bare assertion with no threshold — and DR's Pixel/CAPI state is currently unknown either way (playbook Decision 7, unresolved audit). It must not be used to justify skipping a tracking audit; it is one practitioner's unevidenced cost judgment.

---

## Contradictions within this author

None internal.

## Cross-source note

Dissents from the 50/week consensus that every other source in this batch either assumes or restates. Recorded here so a later synthesis does not treat the consensus as unanimous.

## Open questions from this author

- No evidence is offered for lowering the 50/week figure, and no alternative figure or condition is proposed.
- "Qualified visit" is never operationally defined.
- The server-side-tracking claim states no volume threshold and no cost estimate.

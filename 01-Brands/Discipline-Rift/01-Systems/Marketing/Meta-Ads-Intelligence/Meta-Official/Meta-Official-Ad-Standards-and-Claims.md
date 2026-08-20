---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/ad-standards-and-claims.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/ad-standards-and-claims.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Meta Ad Standards"
meta_topic: Advertising Standards — review process, advertiser responsibility, claim rules
gate_mapping: creative clarity, offer-message fit
meta_publisher: Meta
meta_source_urls:
  - https://transparency.meta.com/policies/ad-standards/
retrieval_method: webfetch_full_body
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: partial
---

# Advertising Standards — review, responsibility, and claims

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/ad-standards-and-claims.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Only the Advertising Standards **introduction** page was retrieved first-hand. Sub-policy pages under `/ad-standards/deceptive-content/` returned HTTP 404 to WebFetch at the paths tried — see Open questions. Nothing on this page is sourced from those unretrieved pages.

## What Meta states

**Policy structure.** Meta organizes the Advertising Standards into: Community Standards compliance, unacceptable content, fraud and scams, restricted goods and services, objectionable content, intellectual property infringement, social/electoral/political advertising, product-specific policies, and business asset policies.

**Review is automated and continuous.** *"Our ad review system relies primarily on automated tools to check ads and business assets against our policies."* Review typically completes *"within 24 hours, although it may take longer in some cases."*

Critically: *"ads remain subject to review and re-review at all times, and may be rejected or restricted for violation of our policies at any time."*

Approval is not permanent. An ad that ran for weeks can be actioned later.

**Responsibility sits with the advertiser.** *"It is an advertiser's responsibility to understand and comply with our policies outlined in Meta's Advertising Standards, our Terms of Service and any other applicable terms and guidelines, in addition to all local laws, regulations."*

And on ongoing compliance after launch: *"It is your responsibility to understand and comply with our policies."*

## What Meta does not state

**On this page, Meta states no specific rule about exaggerated or unsubstantiated outcome claims.** Meta maintains a dedicated "Unrealistic Outcomes" policy under deceptive content, but that page was not retrieved, so its text is not quoted here and must not be paraphrased into this file.

Also absent from the retrieved page:

- Any child- or minor-specific advertising rule. Meta maintains separate teen-advertising policies; none is quoted here.
- Any definition of what evidence substantiates a claim.
- Any statement about the volume or rate of automated false positives.

## Why it matters for DR

Gate items: **creative clarity**, **offer-message fit**.

Two things from the retrieved page bear directly on DR.

**1. Continuous re-review means claim discipline is an operating practice, not a launch checklist.** Because *"ads remain subject to review and re-review at all times"*, a creative that passed review is not settled. For a seasonal advertiser this is a real exposure: an ad rejected mid-season, during the narrow registration window it was built for, costs the window — not just the ad.

**2. Meta's responsibility language and DR's own claim rules point the same way, from different motives.** DR's domain context (`domains/ads/meta/discipline-rift/CLAUDE.md`) already forbids treating confidence, friends, sportsmanship or discipline as a primary promise, and forbids inventing measurable claims the business does not track. Meta's standards put compliance responsibility squarely on the advertiser.

This convergence matters for how Sprint 1's competitor evidence gets used. `competitors/patterns.md` records that **all five brand families** lead with confidence or character growth as the headline outcome, and that KidStrong runs *"96% of kids experience a boost in self-confidence."* That is precisely the shape of claim DR cannot copy — not primarily because of Meta policy, but because DR does not measure it. The patterns file already flags this as `applicability_to_DR: low` with `modification_required: yes`. This file is the platform-side reason to keep that flag rather than relax it later: a measured-sounding claim that DR cannot substantiate is exposed both to DR's own rules and to an automated review system that re-reviews indefinitely.

A competitor running a claim is not evidence that the claim is permitted, and certainly not that it is substantiated. It is evidence that it has not been actioned yet.

Not a recommendation. The condition: any DR creative carrying an outcome claim should be traceable to something DR actually measures.

## Open questions

### Unrealistic Outcomes sub-policy

```yaml
gap: Advertising Standards → Deceptive Content → Unrealistic Outcomes
status: deferred_until_claim_requires_validation
attempted: 2026-08-13
attempt_detail: >-
  transparency.meta.com/policies/ad-standards/deceptive-content/unrealistic-outcomes
  returned HTTP 404 to WebFetch with and without a trailing slash. Correct path
  not established. Rendered-browser retrieval not attempted.
```

**Why deferred rather than chased.** DR's own claim rules (`domains/ads/meta/discipline-rift/CLAUDE.md`) already forbid treating confidence, friends, sportsmanship or discipline as a primary promise, and forbid publishing measurable claims the business does not track. Those rules are stricter than anything Meta's policy is likely to require, and they bind DR regardless of what the sub-policy says.

So the missing text does not currently block a campaign decision. It becomes worth retrieving at the moment a specific DR creative carries an outcome claim that needs platform-side validation — not before.

### Other open items

- Retrieve Meta's teen/minor advertising policy, and confirm whether it constrains DR at all given DR targets parents rather than children.
- Whether Meta documents any substantiation standard for outcome claims.

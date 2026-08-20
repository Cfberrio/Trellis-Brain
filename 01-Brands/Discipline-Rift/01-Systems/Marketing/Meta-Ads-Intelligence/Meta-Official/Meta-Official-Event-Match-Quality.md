---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/event-match-quality.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/event-match-quality.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "EMQ"
meta_topic: Event Match Quality — scoring and customer information parameter priority
gate_mapping: tracking / signal quality
meta_publisher: Meta
meta_source_urls:
  - https://www.facebook.com/business/help/765081237991954
retrieval_method: rendered_browser
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: full_page
---

# Event Match Quality (EMQ)

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/event-match-quality.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Retrieved with a rendered browser. Pairs with `conversions-api-customer-parameters.md`, which carries the hashing and normalization rules.

## What Meta states

**Scope.** *"Event match quality is available for website events sent through the Conversions API with the action source parameter set to Website."*

**What it measures.** *"Event match quality indicates how effective the customer information parameters sent with your server event may be at matching events to Meta accounts."*

**Why matching matters, in Meta's words:** *"Matched events help you attribute conversions to your ads and deliver them to people who are more likely to convert, which can result in better ad performance and lower cost per action."*

Note this is a delivery claim, not only a reporting one — matching feeds optimization.

**Scoring.** *"Meta calculates a score from 0 to 10 based on the quality of customer information you're sending for a specific server event and the percentage of event instances matched to Meta accounts."*

**Freshness.** *"The last 48 hours of data are used to calculate scores, so it's important to send events regularly to keep your event match quality scores up to date."*

Scores exist for all standard and custom web events.

**Parameter priority — Meta's own ranking.** This is the part that changes decisions:

| Parameter | Priority |
|---|---|
| Email | **High** |
| Click ID | **High** |
| Facebook Login ID | Medium |
| Birthdate | Medium |
| Country | Medium |
| Phone number | Medium |
| External ID | Medium |
| Browser ID | Medium |
| Lead | Low |
| First name | Low |
| Last name | Low |
| City | Low |
| Zip or Postal Code | Low |

**General guidance:** *"To help improve the rate at which your events are matched to Meta accounts, send multiple customer information parameters when available."*

**Legal note Meta states directly:** *"Meta Business Tools Terms expressly require you to have lawful rights to collect, use and share data before providing it to us. The Terms also require you to hash contact information as provided in our developer documentation and not share any data that includes sensitive information."* Meta explicitly defers the compliance plan to the advertiser's own counsel.

## What Meta does not state

- **No target score.** Meta gives a 0–10 scale and never says what counts as good, acceptable, or broken. Any "aim for 8+" style figure is not Meta's claim and must not be recorded here.
- No statement of how much each priority tier contributes to the score, or how priority and match percentage combine.
- EMQ is scoped to Conversions API website events. Meta does not state an equivalent score for pixel-only setups on this page.
- No statement about what a score change means in delivery terms — the benefit language is qualified ("may", "can result in").

## Why it matters for DR

Gate item: **tracking / signal quality**.

The priority table corrects an intuition that looks obviously right and is not. DR's registration form collects an unusually complete identity payload — parent name, phone, city, zip, because the child attends a named school. Reading `conversions-api-customer-parameters.md` alone suggests that richness is a large advantage.

Meta's ranking says most of it is **Low** priority: first name, last name, city, zip. The two **High** parameters are **Email** and **Click ID**.

Two consequences worth checking against DR's setup:

1. **Click ID (`fbc`) is High priority and is the one most easily lost.** It is not something a parent types — it is captured from the click and must survive the journey to the server event. Any redirect, form embed, cross-domain hop, or missing cookie capture between the ad click and the registration submission drops a High-priority parameter silently. For DR, whose registration may sit on a third-party or subdomain registration system, this is a live risk, not a theoretical one.
2. **Email is High and is certainly collected** at registration. The question is whether it reaches Meta correctly normalized — trimmed and lowercased per the developer rules — not whether it exists.

The 48-hour scoring window also matters for a seasonal advertiser: outside a registration push, DR may send few events, and a score computed on 48 hours of sparse data is thin. Read EMQ during a live registration window, not in the off-season.

Not a recommendation. Three conditions to verify: is CAPI running at all, does `fbc` survive to the server event, and is email normalized before hashing.

## Open questions

- What is DR's current EMQ, and is CAPI live? Belongs to the DR domain.
- Deduplication between pixel and CAPI for the same registration event — needs `Deduplication for Meta Pixel and Conversions API events` retrieved.
- Whether a pixel-only setup has any comparable diagnostic. Not stated on this page.

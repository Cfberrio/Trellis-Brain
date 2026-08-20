---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: index
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/README.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/README.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Meta oficial — índice"
  - "Meta Official Index"
  - "Documentación oficial de Meta"
---

# Meta oficial — índice de la base documental

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/README.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Tier-2 evidence in this domain's source hierarchy: what Meta officially documents about its own platform.

Its job is to be the thing expert claims get checked against. Sprint 3's playbook stage grades every public-expert claim `SUPPORTED / PARTIALLY_SUPPORTED / CONFLICTING / OUTDATED / INSUFFICIENT_EVIDENCE` — and that grade is meaningless unless the reference base is first-hand, dated, and traceable.

## What earns a file here

One file per topic, and every topic maps to an item in the DR recommendation gate:

| Gate item | Topic files | State |
|---|---|---|
| geo accuracy | `geo-location-targeting.md` | verified |
| learning conditions | `learning-phase.md` | verified |
| learning conditions, setup quality | `optimization-goals-and-attribution.md` | verified |
| tracking / signal quality | `conversions-api-customer-parameters.md` | verified |
| tracking / signal quality | `event-match-quality.md` | verified |
| placement control | `placements.md` | verified |
| tracking / signal quality, setup quality | `aggregated-event-measurement.md` | verified |
| creative clarity, offer-message fit | `ad-standards-and-claims.md` | partial — see its open questions |

Three decision-critical gaps closed 2026-08-13, all rendered first-hand:

| Gate item | File | State |
|---|---|---|
| learning conditions, setup quality | `significant-edits.md` | verified |
| learning conditions, setup quality | `learning-limited.md` | verified |
| tracking / signal quality | `pixel-capi-deduplication.md` | verified |

Added 2026-08-13 for Wave 1A (research questions A1/A2/A3):

| Gate item | File | State |
|---|---|---|
| setup quality, learning conditions, tracking / signal quality | `campaign-objectives-and-optimization-events.md` | partial — ODAX objective↔optimization_goal mapping table returned 404; recorded as an open question rather than filled from a search summary. **Corrected same day**: the first pass wrongly concluded no quality lever existed for website funnels, having read only the developer page. |
| tracking / signal quality, setup quality | `business-tools-data-restrictions.md` | partial — under-13 and prohibited-data warranties, plus the rule that event *names and criteria* must not be based on restricted categories |

**Standing lesson from the 2026-08-13 correction pass:** the developer documentation and the Business Help Centre disagreed on whether qualified-leads optimization supports website forms, and the first pass picked one without noticing the other existed. Where a decision turns on a capability, **check both surfaces** and record the discrepancy rather than resolving it silently.

One gap is deliberately **deferred**, not forgotten: Advertising Standards → Unrealistic Outcomes, `status: deferred_until_claim_requires_validation`, recorded in `ad-standards-and-claims.md`. DR's own claim rules are stricter than the policy is likely to require, so the missing text blocks no current decision. Retrieve it when a specific DR creative carries an outcome claim needing platform-side validation.

**The bar for adding a file is decision impact, not completeness.** A topic that cannot change setup, signal quality, learning conditions, geo accuracy, placement control, creative clarity or offer-message fit does not belong here, however well documented it is.

## Standing finding: check before repeating received wisdom

`aggregated-event-measurement.md` documents that Meta has removed the 8-conversion-event prioritization requirement, the conversion-domain selection step, and domain verification for event configuration — for accounts that have the rollout. Those three steps remain among the most repeated pieces of Meta advice in circulation.

This is the concrete argument for the whole directory. When Sprint 3 grades an expert claim, the grade for advice like this is `OUTDATED`, not `CONFLICTING` — the advice was correct when given. Preserve that distinction; marking a once-correct expert simply "wrong" is its own inaccuracy.

A topic that maps to no gate item does not belong here, however interesting the documentation is.

## Document contract

Every file carries this front matter:

```yaml
topic:
gate_mapping:          # which DR recommendation-gate item(s) this serves
publisher: Meta        # official sources only — this directory holds no expert opinion
source_urls: []        # exact pages fetched, not search results
retrieval_method:      # webfetch_full_body | rendered_browser
captured_at:
last_verified_at:
completeness:          # full_page | partial | enum_only
```

And these sections:

- **What Meta states** — Meta's own wording, quoted. Not paraphrase-with-confidence.
- **What Meta does not state** — the boundary. This section is what stops a later reader treating silence as permission.
- **Why it matters for DR** — routed through the gate, in DR's actual context: local Orlando, parent payer, kids 6–12, on-campus after-school seasons.
- **Open questions** — what still needs a source.

## Hard rules

1. **Official Meta sources only.** Expert commentary belongs in `knowledge/experts/`, which does not exist yet and is out of scope for this sprint. A Meta employee's personal post is not official documentation.
2. **First-hand retrieval.** A claim traces to a page that was actually fetched. A search-engine summary of a Meta page is not the page — search snippets are how a paraphrase becomes a citation.
3. **Undated content does not enter.** Platform documentation changes silently and without changelogs. Every file carries `captured_at`, and a stale `last_verified_at` is a signal to re-verify, not to trust.
4. **Quote the boundary.** Where Meta documents a default, record the default. Where Meta is silent, say Meta is silent — do not fill it with what is probably true.
5. **No DR recommendations here.** This directory records what the platform does. Turning that into a DR action is Sprint 3's job, after DR's own performance data gets a vote.

## Retrieval note — Business Help Centre is not fetchable

Verified 2026-08-13. Three official Meta surfaces behave differently:

| Surface | WebFetch result |
|---|---|
| `developers.facebook.com/docs/**` and `/documentation/**` | Full body |
| `transparency.meta.com/policies/**` | Full body |
| `facebook.com/business/help/**` | **Title only** — JS shell, no server-rendered body |

Several gate topics (learning phase, event match quality, performance goals) live only on the Business Help Centre. Prefer the developer-documentation equivalent wherever one exists — it is usually more precise, because an API enum is exact where help-centre prose is descriptive. Where no equivalent exists, the page must be retrieved with a rendered browser and the file must record `retrieval_method: rendered_browser`.

Do not substitute a search-result summary for a page that could not be fetched. That is rule 2, and it is the rule most likely to be broken under time pressure.


---

## Los 16 documentos en esta carpeta

Cada nota conserva en su frontmatter la metadata original de captura: `meta_topic`, `gate_mapping`, `meta_source_urls`, `retrieval_method`, `captured_at`, `last_verified_at`, `completeness`. Eso es lo que las hace citables.

| Documento | Ítem de la compuerta de recomendación |
|---|---|
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Campaign-Objectives-and-Optimization-Events\|Objetivos de campaña y eventos de optimización]] | calidad del setup |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Optimization-Goals-and-Attribution\|Objetivos de optimización y atribución]] | calidad del setup · tracking |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Learning-Phase\|Learning phase]] | condiciones de aprendizaje |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Learning-Limited\|Learning limited]] | condiciones de aprendizaje |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Significant-Edits\|Significant edits]] | condiciones de aprendizaje |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Campaign-Budget-and-Consolidation\|Presupuesto de campaña y consolidación]] | calidad del setup |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Geo-Location-Targeting\|Segmentación geográfica]] | exactitud del geo |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Audience-Controls-Location-Attribution\|Controles de audiencia, ubicación y atribución]] | exactitud del geo · tracking |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Placements\|Placements]] | control de placements |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Creative-Testing-AB-Testing-Delivery-Diagnostics\|Creative testing, A/B testing y diagnóstico de entrega]] | claridad creativa |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Ad-Standards-and-Claims\|Ad Standards y reglas de claims]] | claridad creativa · ajuste oferta-mensaje |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Pixel-CAPI-Deduplication\|Pixel, CAPI y deduplicación]] | calidad de tracking / señal |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Conversions-API-Customer-Parameters\|Conversions API — parámetros de cliente]] | calidad de tracking / señal |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Event-Match-Quality\|Event Match Quality (EMQ)]] | calidad de tracking / señal |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Aggregated-Event-Measurement\|Aggregated Event Measurement (AEM)]] | calidad de tracking / señal |
| [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Business-Tools-Data-Restrictions\|Business Tools — restricciones de datos]] | cumplimiento · tracking |

> [!warning] Regla de uso
> Estas notas son **PLATFORM FACT**: definen qué hace la plataforma. **No dicen qué convierte a padres de Orlando.**
> Toda cita conserva la URL de Meta y la fecha de captura. Un documento capturado hace meses puede haber cambiado — antes de una decisión importante, re-verifica contra la URL original.

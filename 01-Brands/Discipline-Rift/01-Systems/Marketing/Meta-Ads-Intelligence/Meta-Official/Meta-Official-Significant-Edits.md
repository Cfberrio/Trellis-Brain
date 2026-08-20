---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/significant-edits.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/significant-edits.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Significant edits"
meta_topic: Significant edits — which changes reset the learning phase
gate_mapping: learning conditions, setup quality
meta_publisher: Meta
meta_source_urls:
  - https://www.facebook.com/business/help/316478108955072
retrieval_method: rendered_browser
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: full_page
---

# Significant edits and the learning phase

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/significant-edits.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Retrieved with a rendered browser. Closes an open question left by `learning-phase.md`.

## What Meta states

### The distinction Meta actually draws

> *"Every edit you make (during the learning phase or after it) has some effect on delivery, but not every edit causes the ad set to reenter the learning phase. Only a significant edit causes an ad set to reenter the learning phase."*

Two separate consequences, and they are commonly collapsed into one:

| | Effect |
|---|---|
| **Any edit** | has "some effect on delivery" |
| **A significant edit only** | causes the ad set to re-enter the learning phase |

Meta restates why re-entry costs something: *"the delivery system is exploring the best way to deliver your ad set based on the optimization event you chose… This can lead to less stable performance and a higher cost per result."*

### Always significant

Meta's list, verbatim:

- *"Any change to targeting"*
- *"Any change to ad creative"*
- *"Any change to optimization event"*
- *"Adding a new ad to your ad set"*
- *"Pausing your ad set for 7 days or longer (the ad set reenters the learning phase once you unpause the ad set)"*
- *"Changing bid strategy"*

On Advantage+ campaign budget: *"switching your campaign bid strategy might cause multiple ad sets within the campaign to reenter the learning phase."*

### Conditionally significant — depends on magnitude

> *"A change to any of the following areas may or may not be significant, depending on the magnitude of the change"*

- Ad set spending limit amount
- Bid control, cost per result goal or ROAS goal amount
- Budget amount

Meta's own illustration: *"if you increase your budget from $100 to $101, that isn't likely to cause one or more ad sets to reenter the learning phase. However, if you change your budget from $100 to $1000, one or more ad sets may reenter the learning phase."*

With Advantage+ campaign budget, *"adjusting your campaign budget might cause multiple ad sets within the campaign to reenter the learning phase."*

### Advantage+ campaign budget — what does not reset learning

Meta answers four questions directly, all "No":

- Budget distribution across ad sets does not cause re-entry.
- An edit made at ad set level does not cause *other* ad sets in the campaign to re-enter — *"as long as the edit is made at the ad set level."*
- Adding a new ad set to the campaign does not cause the existing ad sets to re-enter.
- Initial learning with Advantage+ campaign budget *"​will take the same time as ad set budgets."*

(Meta also states that changing a disclaimer on social-issue/electoral/political ads is significant. Not applicable to DR.)

## What Meta does not state

- **No threshold for "magnitude."** The $100→$101 vs $100→$1000 example is an illustration, not a rule. Meta publishes no percentage or absolute cutoff at which a budget change becomes significant. Do not invent one.
- The conditional cases use "may or may not" and "might". Meta does not commit to when they trigger, and neither should any downstream file.
- No statement about whether several small edits accumulate into a significant one.
- No statement on how long after an edit the re-entry is registered.
- Nothing about pausing for *less* than 7 days — only the 7-days-or-longer case is documented.

## Why it matters for DR

Gate items: **learning conditions**, **setup quality**.

**"Any change to ad creative" is significant.** This is the operationally sharp one. Creative iteration — the thing an intelligence system naturally produces recommendations for — resets learning every time. Sprint 1's `patterns.md` observed competitors holding copy constant while varying media and CTA across many ad IDs; on DR's volume, each such change is a learning reset, and `learning-limited.md` shows the clock restarts from the last significant edit.

That does not mean "never change creative." Meta explicitly warns against trying to avoid the learning phase (see `learning-phase.md`). It means creative changes should be batched deliberately rather than trickled, because each trickle restarts a ~7-day window that DR's volume may already struggle to fill.

**"Adding a new ad to your ad set" is significant.** Adding a variant is not a free test. It resets the ad set.

**Budget changes are the seasonal trap.** DR sells seasons with registration windows, so pushing budget up as a window opens is the natural move. Meta says a large budget change may cause re-entry — at precisely the moment the window is shortest and stable delivery matters most. Magnitude is undefined, so this is a risk to plan around, not a rule to compute against.

**The Advantage+ answers reduce one fear.** If DR runs campaign budget, adding an ad set or editing one ad set does not reset the others. Structural changes at ad set level are safer than they are often assumed to be.

Not a recommendation. The checkable condition: how often is DR's account edited, and does the edit cadence leave any ad set a full uninterrupted week?

## Open questions

- No published magnitude threshold for budget or bid changes — likely unknowable from documentation.
- Whether pausing under 7 days has any learning effect. Not addressed.
- Whether the "some effect on delivery" of non-significant edits is measurable anywhere in reporting.

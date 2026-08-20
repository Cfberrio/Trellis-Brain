---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/learning-phase.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/learning-phase.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Learning phase"
meta_topic: Learning phase, significant edits, and learning limited
gate_mapping: learning conditions, setup quality
meta_publisher: Meta
meta_source_urls:
  - https://www.facebook.com/business/help/112167992830700
retrieval_method: rendered_browser
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: full_page
---

# Learning phase

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/learning-phase.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Retrieved with a rendered browser. `facebook.com/business/help` returns a title-only JS shell to WebFetch — see `README.md`.

## What Meta states

**Definition.** *"The learning phase is the period when the delivery system still needs to learn about how an ad set may deliver and perform. During the learning phase, the delivery system is exploring the best way to deliver your ad set when you either create a new ad or ad set or make a significant edit to an existing one."*

The Delivery column reads "Learning" while this is happening.

**The threshold — read the hedging carefully.** Meta's exact wording:

> *"While the delivery system never stops learning about the best way to deliver an ad set, ad sets exit the learning phase as soon as they can deliver stably. This usually occurs after about 50 results in the week after the ad set's last significant edit."*

Three qualifications sit in that sentence and are routinely dropped when it is cited:

1. The exit condition is **"as soon as they can deliver stably"** — 50 is a description of when that usually happens, not the rule itself.
2. **"about 50"**, not exactly 50.
3. **"results"**, not "conversions" — results means the ad set's chosen optimization event.

Meta documents exactly one numeric exception: *"For Shops ads, you need a minimum of 17 purchases through your website and 5 through Meta for the learning phase to complete."*

**Best practices Meta states verbatim:**

- *"Wait to edit your ad set until it's out of the learning phase… By editing an ad, ad set or campaign during the learning phase, you reset learning and delay our delivery system's ability to optimize."*
- *"Avoid unnecessary edits that cause ad sets to re-enter the learning phase… Only edit your ads or ad set when you have reason to believe that the edit should improve performance."*
- *"Avoid high ad volumes. When you create many ads and ad sets, the delivery system learns less about each ad and ad set than when you create fewer ads and ad sets. By combining similar ad sets, you also combine learnings."*
- *"Use realistic budgets. If you set a very small or inflated budget, the delivery system has an inaccurate indicator of the people for whom the delivery system should optimize. Set a budget large enough to get enough total results and avoid frequent budget changes (which can cause an ad set to re-enter the learning phase)."*

**On performance during learning:** *"During the learning phase, ad sets are less stable and usually have a higher CPA."* And: *"performance is less stable, so your results aren't necessarily indicative of future performance."*

**Learning limited.** *"If your ad set isn't getting enough results to exit the learning phase, the Delivery column status reads 'Learning limited.'"*

**Meta explicitly warns against over-correcting:** *"The learning phase is necessary to help the delivery system best optimize ads, so you shouldn't try to avoid the learning phase completely. Testing new creative and marketing strategies is essential for improving your performance over time."*

## What Meta does not state

- **This page does not enumerate what counts as a significant edit.** That lives on a separate page (`Significant edits and learning phase`) which has not been retrieved. Do not assert which specific edits reset learning from this file.
- No causes-and-fixes list for learning limited — also a separate unretrieved page.
- No statement that 50 is a hard floor, and none that an ad set below it cannot exit. The text says the opposite: stability is the criterion.
- Nothing about how learning interacts with campaign-level budget optimization.

## Why it matters for DR

Gate items: **learning conditions**, **setup quality**.

DR is a local single-market advertiser selling seasons. The relevant arithmetic: an ad set needs roughly 50 results within a **7-day window** to exit learning. If DR's optimization event is a completed registration, and registrations arrive at fewer than ~50/week per ad set, that ad set does not reliably exit the learning phase — and Meta states plainly that ad sets in that state are "less stable and usually have a higher CPA."

That is a structural constraint, not a tuning problem. Three of Meta's own best practices compound it:

- **"Avoid high ad volumes"** and **"combining similar ad sets… combines learnings"** — argues directly against splitting a small local budget across many ad sets. This is the same conclusion the $40/day low-frequency floor points to in `optimization-goals-and-attribution.md`, arriving from a different direction.
- **"Set a budget large enough to get enough total results"** — the budget question is not what DR can afford in total, but whether any single ad set clears the results threshold.
- **"Avoid frequent budget changes"** — seasonal advertisers with registration windows are structurally tempted to push budget up and down around a season start, and each change risks re-entering learning.

The honest read: DR's volume may make full learning-phase exit unrealistic on a registration event. Meta's own text says not to try to avoid the learning phase — but it also says results during learning are not indicative. So conclusions drawn from a permanently-learning ad set are weak evidence, and that affects how DR's own diagnostics should be interpreted, not just how campaigns are built.

Not a recommendation. A condition to check: what is DR's actual weekly result count per ad set, and does any ad set exit learning?

## Open questions

- Retrieve `Significant edits and learning phase` and enumerate what resets learning.
- Retrieve `About learning limited` for Meta's stated causes and fixes.
- Does a lighter-weight optimization event (landing page view, lead) clear ~50/week where registration does not — and at what cost to signal quality? Trade-off, not yet sourced.

---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/learning-limited.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/learning-limited.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Learning limited"
meta_topic: Learning limited — definition, causes, and Meta's stated fixes
gate_mapping: learning conditions, setup quality
meta_publisher: Meta
meta_source_urls:
  - https://www.facebook.com/business/help/269269737396981
retrieval_method: rendered_browser
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: full_page
---

# Learning limited

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/learning-limited.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Retrieved with a rendered browser. Closes an open question left by `learning-phase.md`.

## What Meta states

**Definition.** *"If your ad set isn't getting enough optimization events to exit the learning phase, the Delivery column reads Learning limited."*

**It is not a penalty.** Meta says so explicitly: *"Learning limited isn't a penalty – it's an indication that your budget isn't being spent effectively because the ad delivery system can't optimize performance with your current setup."*

**The threshold, in Meta's own hedged wording:**

> *"An ad set becomes learning limited when it is unlikely to receive **about 50 optimization events** in the week after your last significant edit."*

Read precisely:

- **"about 50"** — not exactly 50.
- **"optimization events"** — the event the ad set is optimizing for, whatever that is. Not "conversions", not "purchases", not "registrations" unless that is the selected optimization event.
- **"in the week after your last significant edit"** — a rolling 7-day window anchored to the last significant edit, not to campaign launch. See `significant-edits.md` for what resets that anchor.
- **"is unlikely to receive"** — this is a forward-looking prediction by the delivery system, not a retrospective count. Meta adds: *"This diagnosis can happen any time after you create an ad set or make a significant edit to an existing one."*

**Meta does not say "Meta requires 50 conversions."** It says an ad set is diagnosed learning limited when it looks unlikely to reach about 50 optimization events in that window.

**Documented exception.** *"For Shops ads, an ad set becomes learning limited when it hasn't generated a minimum of 17 purchases through your website and 5 through Meta after 7 days."*

**Stated causes.** *"Generally, an ad set becomes learning limited when the ad set is limited by small audience size, low budget, low bid or cost control, high auction overlap, an infrequent optimization event, or other issues such as running too many ads at the same time."* If the cause is a low bid or cost control, Meta says a tooltip appears on hover.

**Meta's stated fixes**, verbatim:

| Fix | Meta's reasoning |
|---|---|
| Combine ad sets and campaigns | *"Combining ad sets and campaigns will help you get the results you need faster, which means you'll see stable results sooner."* |
| Expand your audience | *"The larger the audience, the more opportunities for people to complete your optimization event."* |
| Raise your budget | *"If your budget is too low to receive enough optimization events, the ad set is unlikely to exit the learning phase."* |
| Raise your bid or cost control | *"If your bid or cost control is too low to receive enough optimization events, the ad set is unlikely to exit the learning phase."* |
| Change your optimization event | *"Consider choosing an optimization event that occurs more frequently. For example, move from purchases to add to cart."* |

**Recovery.** *"If a learning limited ad set receives enough optimization events since your last significant edit, it will move from Learning limited to Active."*

Note Meta writes "enough", not "50", for the exit condition.

**Diagnostics.** Optimization events can be added as a reporting column: Columns → Customize columns → check Optimization events → Apply.

## What Meta does not state

- No exact number for "enough optimization events" to recover. Only "about 50" for the diagnosis.
- No definition of "small audience size", "low budget", or "high auction overlap" in numeric terms.
- No statement about how much worse performance actually is while learning limited — only that budget "isn't being spent effectively".
- No guidance on how long an ad set may run learning limited before intervening.
- No statement about whether a permanently learning-limited ad set still improves at all over time.

## Why it matters for DR

Gate items: **learning conditions**, **setup quality**.

Four of Meta's five stated causes plausibly describe a small local advertiser by construction: small audience size, low budget, an infrequent optimization event, and running too many ads at once. DR is one metro, one age band, a parent audience, and a conversion event that fires when a season registration completes. Learning limited is the expected state for that shape of account, not an anomaly.

That reframes it. Meta's own words — *"isn't a penalty"* — matter, because "learning limited" reads like a failure and invites thrashing. Thrashing means edits, and per `significant-edits.md` most meaningful edits are significant, which restarts the very window the ad set is failing to fill. The trap is self-reinforcing.

Two of Meta's five fixes are genuinely available to DR and inside the gate:

- **Combine ad sets and campaigns** — consolidation, not expansion. Converges with the learning-phase best practice ("avoid high ad volumes", "combining similar ad sets… combines learnings") and with the documented $40/day low-frequency budget floor in `optimization-goals-and-attribution.md`. Three separate Meta pages point the same way: fewer, better-funded ad sets.
- **Change to a more frequent optimization event** — Meta's own example moves from purchases to add-to-cart, i.e. deliberately optimizing for a shallower event to get volume. For DR the analogous move would be optimizing to something upstream of completed registration. That is a real trade against signal quality, and it is a decision, not an obvious win — a shallower event is easier to hit and less correlated with revenue.

Two fixes are constrained for DR: "expand your audience" runs against geo accuracy on a local on-campus offer, and "raise your budget" is a business constraint this domain does not get to set.

Not a recommendation. The checkable conditions: is any DR ad set showing Learning limited, does the tooltip name bid/cost control as the cause, and what is DR's actual weekly optimization-event count per ad set?

## Open questions

- What Meta counts as "enough" to recover, versus the "about 50" used to diagnose.
- Whether DR's optimization event is currently registration or something shallower. Belongs to `domains/ads/meta/discipline-rift/`.
- Whether auction overlap is contributing — Meta names it as a cause but publishes no way to quantify it here.

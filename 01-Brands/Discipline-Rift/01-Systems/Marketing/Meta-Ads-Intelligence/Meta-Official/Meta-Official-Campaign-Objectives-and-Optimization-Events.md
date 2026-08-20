---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/campaign-objectives-and-optimization-events.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/campaign-objectives-and-optimization-events.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Campaign objectives"
meta_topic: Campaign objectives (ODAX), conversion locations, and which events can be optimized toward
gate_mapping: setup quality, learning conditions, tracking / signal quality
meta_publisher: Meta
meta_source_urls:
  - https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/
  - https://developers.facebook.com/blog/post/2023/02/13/outcome-driven-ad-experiences-update/
  - https://developers.facebook.com/blog/post/2021/12/21/simplifying-campaign-objectives-outcome-driven-ad-experiences/
  - https://developers.facebook.com/docs/marketing-api/adset/destination_type/
  - https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/
  - https://developers.facebook.com/docs/meta-pixel/reference
  - https://developers.facebook.com/documentation/ads-commerce/conversions-api/conversion-leads-integration
  - https://developers.facebook.com/docs/marketing-api/conversions-api/
  - https://www.facebook.com/business/help/416997652473726
  - https://www.facebook.com/business/help/2035196646663270
  - https://www.facebook.com/business/help/1431172887335181
  - https://www.facebook.com/business/help/355670007911605
  - https://www.facebook.com/business/help/782657799338685
  - https://www.facebook.com/business/help/279369167153556
  - https://www.facebook.com/business/help/2169779963333459
retrieval_method: webfetch_full_body (developers.facebook.com) + rendered_browser (facebook.com/business/help)
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: partial
research_questions: [A1, A2, A3]
revision_note: >-
---

# Campaign objectives, conversion locations, and optimizable events

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/campaign-objectives-and-optimization-events.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Retrieved first-hand for Wave 1A (A1/A2/A3). Companion to `optimization-goals-and-attribution.md`, which holds the `optimization_goal` enum, `attribution_spec`, `bid_strategy` and minimum daily budgets, and to `learning-limited.md` / `learning-phase.md`, which hold the event-volume mechanics.

## What Meta states

### The objective set is ODAX-only for new campaigns

The Campaign (`ad-campaign-group`) reference lists both legacy and current objectives. The six current ones are each annotated **"newer objective"**:

`OUTCOME_APP_PROMOTION` · `OUTCOME_AWARENESS` · `OUTCOME_ENGAGEMENT` · `OUTCOME_LEADS` · `OUTCOME_SALES` · `OUTCOME_TRAFFIC`

The 2023 developer blog states the cutover verbatim:

> *"Beginning with Marketing API v17.0 (to be released in Spring 2023), campaigns can only be created with simplified objectives."*

and lists the deprecated legacy objectives verbatim:

> *"APP_INSTALLS, BRAND_AWARENESS, CONVERSIONS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS"*

**Caution on the reference page itself:** it still carries the stale sentence *"We will continue supporting these original objectives throughout 2022."* That prose is years out of date; the v17.0 blog is the governing statement. Recorded because a future reader fetching only the reference page could be misled.

The 2021 announcement describes what the advertiser is asked to choose:

> *"[advertisers] can select their designed business outcomes (e.g. Awareness, Traffic, Engagement, Leads, App Promotion, Sales) and the interface will guide advertisers to the most optimal campaign setup/creation paths to achieve that outcome."*

### Conversion location is expressed as `destination_type`, and it is objective-scoped

From the `destination_type` reference, verbatim:

- `OUTCOME_LEADS` supports: *"ON_AD, LEAD_FROM_MESSENGER, LEAD_FROM_IG_DIRECT, PHONE_CALL, UNDEFINED, WEBSITE, APP"*
- `OUTCOME_SALES` supports: *"WEBSITE, MESSENGER, PHONE_CALL"*

**Both `OUTCOME_LEADS` and `OUTCOME_SALES` support a `WEBSITE` destination.** A website-completed conversion is therefore reachable under either objective; the platform does not force the choice.

### Website conversion optimization requires a pixel and a named event

`promoted_object`, verbatim: *"The object this ad set is promoting across all its ads. Required with certain campaign objectives."* For website conversion optimization the documented combinations are:

- `pixel_id`
- `pixel_id` and `custom_event_type`
- `pixel_id` and `pixel_rule` and `custom_event_type`

Allowed `custom_event_type` values, verbatim:

> *"AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER"*

`COMPLETE_REGISTRATION`, `PURCHASE`, `LEAD`, `SCHEDULE`, `SUBMIT_APPLICATION`, `SERVICE_BOOKING_REQUEST` and `CONTENT_VIEW` are all in that list — i.e. all are nameable as the optimization event for a website conversion ad set.

The Pixel reference lists the standard events verbatim:

> *"AddPaymentInfo, AddToCart, AddToWishlist, CompleteRegistration, Contact, CustomizeProduct, Donate, FindLocation, InitiateCheckout, Lead, Purchase, Schedule, Search, StartTrial, SubmitApplication, Subscribe, ViewContent"*

### Meta's own remedy for an infrequent optimization event is to move UP the funnel

This is the single most decision-relevant platform fact for A2, and it is Meta's own, from `learning-limited.md`:

> Fix — **Change your optimization event**: *"Consider choosing an optimization event that occurs more frequently. For example, move from purchases to add to cart."*

Listed alongside its stated causes of learning limited, which include *"an infrequent optimization event"*.

So: choosing a shallower, more frequent optimization event when the deeper one is too rare is **documented first-party remedy**, not practitioner folklore. What Meta does not do is tell you which event, or what the cost of the trade is.

### Qualified-leads optimization IS available for website forms — corrected 2026-08-13

**This section replaces an earlier, wrong conclusion in this file.** The first pass relied on the developer Conversion Leads page and concluded that no platform-side quality lever existed for a website funnel. Current Help Centre documentation, rendered first-hand, contradicts that.

From *"About performance goals for lead ads"*, verbatim:

> *"Maximize number of qualified leads: Use this performance goal to increase the quality of your leads. Your ad will be shown to the people in your audience who are most likely to convert after sharing their contact information with you."*

> *"If you want to improve lead quality, you can use the performance goal Maximize number of qualified leads to show your ads to people more likely to convert. **This performance goal can be used with both website forms and instant forms.**"*

Meta publishes separate reported results for each surface, verbatim:

> *"Lead ads that use Conversions API for CRM integration and the performance goal Maximize number of qualified leads for instant forms saw 21% lower cost per quality leads compared to lead ads that used Maximize number of leads. Lead ads that use the Maximize number of qualified leads for their website forms saw 9.5% lower cost per quality leads compared to lead ads that used Maximize number of leads."*

(These are **Meta-reported aggregate figures with no methodology published** — platform marketing claims, not verifiable evidence. Record them as Meta's assertion, not as a measured benefit DR should expect.)

#### Prerequisite: Conversions API, and the timeline is now

Stated at the top of the same page, verbatim:

> *"We are evolving our leads quality optimization to maximize campaign performance. **Beginning April 2026, the qualified leads performance goal is no longer available for new campaign creation without Conversions API integration. Existing campaigns will be impacted beginning August 2026.**"*

Both dates are in the past or current as of this capture (2026-08-13). Treat CAPI integration as a **hard prerequisite** for any new campaign using this goal.

#### What signal must be sent back

From *"Set up your CRM for qualified leads"*, verbatim:

> *"If you select this option during ad creation, it's recommended that you connect your customer relationship management (CRM) system to send information to Meta about your leads. After you connect your CRM, you can choose the stages in your sales funnel based on your performance goals."*

> *"Note: During the learning phase, upload CRM events for each lead status update. When a lead's information changes in your CRM, send the latest update as an event."*

So the mechanism is: lead-stage progression fed back from a CRM through CAPI, per status change — not a one-off conversion ping.

#### Resolving the old-versus-current documentation

Both statements are first-party and they are **not reconciled by Meta anywhere found.** Recording the difference rather than picking a winner:

| Source | Statement | Reading |
|---|---|---|
| Developer doc, *Conversions API for CRM integration* | *"The Conversion Leads performance goal is currently only compatible with Facebook/Instagram's Lead Ads (Instant Forms)."* | Uses the older feature name (**"Conversion Leads"**), and is scoped to that developer integration guide. |
| Help Centre, *About performance goals for lead ads* (current) | *"Maximize number of qualified leads … can be used with both website forms and instant forms."* | Uses the current Ads Manager name (**"Maximize number of qualified leads"**), carries the April/August 2026 CAPI notice, and reports website-form results separately. |

**Most likely reading — stated as an inference, not a fact:** the same capability, renamed and extended to website forms, with the developer page not yet updated. The Help Centre page is the one carrying 2026 dates and surface-specific results, so it is treated as current here. **The developer page is not dismissed** — if a build ever depends on this, the discrepancy must be confirmed with Meta directly before committing to the architecture.

Note also what "website forms" means: a lead ad whose form lives on the advertiser's website. Whether DR's existing registration flow qualifies as a "website form" in Meta's sense is **not established** and is a build-time question.

### A published campaign objective cannot be changed

From *"How to edit Facebook and Instagram campaigns in Meta Ads Manager"*, verbatim:

> *"Note: You cannot change your published campaign objective. You can always stop your campaign and create a new one if you want to change the objective."*

The same page states generally: *"Editing certain details of your campaign, ad set or ad may restart the learning phase or cause the ad review system to re-review your ad."*

This is stronger than "changing objective is a significant edit". **It is not editable at all** — a different objective means a new campaign, losing that campaign's accumulated history. Any framework that treats objective choice as revisable-in-place is wrong.

### Which conversion EVENTS are selectable, by objective and conversion location

Retrieved with a rendered browser from *"Available conversion locations and events by objective in Meta Ads Manager"*. Verbatim rows that matter here:

| Objective | Conversion location | Conversion events (verbatim) |
|---|---|---|
| **Traffic** | Website | *"No conversion event required."* |
| **Engagement** | Website | *"Add to wishlist, Contact, Customize product, Donate, Find location, Schedule, Search, Start trial, Submit application, Subscribe, View content."* |
| **Leads** | Website | *"Complete registration, Contact, Find location, Lead, Schedule, Search, Start trial, Submit application, Subscribe, View content."* |
| **Sales** | Website | *"Add payment info, Add to cart, Add to wishlist, Complete registration, Donate, Initiate checkout, Purchase, Search, Start trial, Subscribe, View content."* |
| **Sales** | Website and in-store | *"Add to cart, Add payment info, Add to wishlist, Complete registration, Initiate checkout, Purchase, Start trial, Search, Subscribe, View content."* |

Meta defines the terms verbatim: *"The conversion location is the place where your desired business outcome will occur. Depending on the conversion location you select, you'll then choose a conversion event. The conversion event you choose will tell us the action you want your audience to take."*

**`Complete registration` is selectable under BOTH Leads→Website and Sales→Website.** Note also `Purchase` exists only under Sales, and Engagement→Website offers neither.

For omnichannel, verbatim: *"create a campaign with the Sales objective and select Website and in-store or Website, app and in-store as your conversion location to **track and optimize** conversions across digital and physical channels."*

### Which PERFORMANCE GOALS are available, by objective and conversion location

Retrieved with a rendered browser from *"Performance goals available by ad objective and conversion location in Meta Ads Manager"*. The rows that decide the ladder:

| Objective → conversion location | Performance goals (verbatim) |
|---|---|
| **Traffic → Website** | Traffic goals: *"Maximize number of landing page views"*, *"Maximize number of link clicks"*. Other goals: daily unique reach, conversations, impressions |
| **Leads → Website** | Leads goals: *"Maximize number of leads"*, *"Maximize number of qualified leads"* — **no shallower "Other goals" row is listed** |
| **Sales → Website** | Conversion goals: *"Maximize number of conversions"*, *"Maximize value of conversions"*. Other goals: *"Maximize number of landing page views"*, *"Maximize number of link clicks"*, *"Maximize daily unique reach"*, *"Maximize number of impressions"* |

**Sales → Website is the only website combination documented as carrying both the deep conversion goals and the shallower landing-page-view / link-click goals inside one objective.**

### What choosing a performance goal actually does — and Meta's own budget rule

From *"About performance goals"*, verbatim:

> *"When you choose a performance goal for an ad set, you're telling the ad delivery system to get you that result as efficiently as possible. In other words, **your performance goal is the desired outcome that our system bids on in the ad auction**."*

> *"The performance goal of your ad set **can be different from your ad objective**. For example, you can select Sales as your ad objective, but optimize for link clicks within an ad set."*

> *"Note: To improve performance, we may prioritize higher-quality clicks."*

And — retrieved incidentally, but useful for Wave 1B — Meta's budget-to-goal guidance:

> *"Remember that some performance goals may require more budget than others. For example, a conversion may cost more than a landing page view… **In general, your daily budget should be at least 10 times the average cost of your performance goal.** For example, if you want to optimize for link clicks and your average cost per link click is $5, your daily budget should be at least $50."*

**Read the framing precisely.** Meta introduces this with *"In general"*, inside a section titled *"How performance goals can affect your budget and bid strategy"*, phrased as something to *"ensure"* when selecting budget and bid strategy. It is a **rule of thumb / reference point**, and Meta states it as such.

It is **not** documented as: an eligibility requirement, a binary viability threshold, a guarantee, or a statement that Meta cannot optimize below it. Nothing on the page says delivery fails, learning is impossible, or a goal is unavailable under 10×. Any downstream wording implying "budget < 10× event cost → rung impossible/unaffordable" overstates the source and must be narrowed.

Its correct use is as one of several reference points Wave 1B tests against — alongside event volume, the learning-phase framing, observed delivery, and what remains learnable below those references.

### Server events vs offline events are documented differently

The Conversions API overview accepts *"website events, app events, business messaging events and offline conversions"* originating from *"an advertiser's server, website platform, mobile app, or CRM"*.

It states server events *"may be used in measurement, reporting, or optimization in a similar way as other connection channels."*

For **offline** events it states, narrower: *"Offline events may be used for attributed offline events measurement, offline custom audience creation or measurement."* **Optimization is absent from that sentence.**

Record this as a documented asymmetry, not as a proven prohibition — the page does not say offline events *cannot* optimize; it simply does not list optimization among their uses, while listing it for server events. The distinction matters for any funnel whose true conversion completes off-website.

## What Meta does not state

- **Which objective any given business should choose.** Meta documents that Leads and Sales both permit a Website conversion location and both offer `Complete registration` as a conversion event. It does not say which is correct for a registration funnel, and it publishes no decision rule. **This is the boundary: Meta establishes what is available, never what DR should pick.**
- **The developer-side ODAX mapping table remains unretrieved.** The Ad Set reference points to it — *"Please refer to the Outcome-Driven Ads Experiences mapping table…"* — but that doc URL returned **HTTP 404** on 2026-08-13 (two URL variants tried). The Help Centre tables above cover the same ground in Ads Manager vocabulary and were used instead; the API-enum-level mapping (which `optimization_goal` string pairs with which objective) is still not established first-hand and must not be asserted.
- **Whether DR's existing registration flow counts as a "website form"** for qualified-leads purposes. Meta says the goal works with "website forms" but does not define the term against an arbitrary on-site registration process.
- **Whether the developer Conversion Leads page is stale or describes a narrower feature.** The two first-party statements are not reconciled by Meta; the reading above is an inference.
- **A second tension on offline optimization.** The Conversions API page omits optimization from its offline-events sentence, while the conversion-locations page says omnichannel locations *"track and optimize conversions across digital and physical channels."* Not necessarily contradictory — different mechanisms — but not reconciled from first-party text either.
- **No guidance on how much signal quality is lost when moving up the ladder.** Meta says to pick a more frequent event; it never quantifies or even qualifies the cost of doing so.
- **Which standard events are optimization-eligible versus measurement-only.** The Pixel reference lists the events and their properties but carries no such statement. The `custom_event_type` enum is the closest available evidence of optimizability, and it is an API field list, not a statement about delivery quality.
- **Any guidance on choosing a deeper versus shallower funnel event**, beyond the learning-limited remedy above. Meta gives one worked example (purchases → add to cart) in an ecommerce vocabulary and stops. No thresholds, no decision rule, no statement of what is lost.
- **Any quality-versus-quantity guidance for website conversions.** The only documented mechanism (Conversion Leads) is explicitly scoped to Instant Forms. Meta publishes nothing equivalent for a website-completed conversion, and silence here must not be read as "quality is not a risk".
- **Whether a completed registration counts as a "low-frequency action"** for the $40/day minimum-daily-budget bucket — still open from `optimization-goals-and-attribution.md`.

## Why it matters for DR

Gate items: **setup quality**, **learning conditions**, **tracking / signal quality**.

**A1.** DR's current campaign runs `OUTCOME_TRAFFIC`, and Meta documents that Traffic → Website requires **no conversion event at all**. That is the sharpest platform observation available: DR's present setup structurally never asks Meta to find people likely to register. Both Leads → Website and Sales → Website accept `Complete registration` as the conversion event, so the real objective choice is between those two — and Meta publishes no rule for choosing. Platform observation, not a recommendation.

**A2.** Three platform facts define the ladder before any practitioner speaks:

1. `Complete registration` is selectable under both candidate objectives, so the deepest sensible event is technically available.
2. Meta's own learning mechanics (~50 optimization events/week per ad set) collide with DR's historical volume, and **Meta's own documented remedy is to choose a more frequent optimization event**.
3. *"The performance goal of your ad set can be different from your ad objective"* — and **Sales → Website is the only website combination carrying both the deep conversion goals and the shallower landing-page-view / link-click goals inside one objective.**

Together these mean a ladder is walkable *without replacing the campaign* if the objective is Sales. That matters because **a published objective cannot be edited at all** — switching later means stopping the campaign and building a new one, forfeiting its history. Moving between rungs inside one objective is an ad-set edit: still a significant edit that resets that ad set's learning, but far cheaper than a rebuild.

Under Leads → Website the documented goals are leads and qualified leads only, with no shallower rung inside the objective — **but Leads is also the only path to the qualified-leads quality lever.** So the objectives trade flexibility against quality feedback rather than one dominating. This is a structural argument to be tested, not a decision.

**A3.** A platform-side quality lever **does** exist and is available for website forms: *"Maximize number of qualified leads"*, under the **Leads** objective, fed by CRM lead-stage data through the Conversions API — which is now a hard prerequisite (April 2026 for new campaigns; August 2026 for existing).

Three conditions gate it for DR, and all three are unresolved:

1. **CAPI must exist.** DR's Pixel/CAPI state is currently unknown in either direction (playbook Decision 7 — an audit nobody has run).
2. **A CRM with lead stages must exist and sync back**, per lead status update. DR would need paid-registration status flowing back as events.
3. **The "website form" definition** must cover DR's registration flow.

Separately, the offline-event asymmetry still stands: Meta lists offline events for *"measurement, offline custom audience creation or measurement"* without naming optimization, while the omnichannel conversion locations claim to *"track and optimize"* across channels. If DR's registration completes off-website, which mechanism applies is unresolved.

**What changed and why it matters:** the first pass concluded no platform lever existed, on the strength of one developer page. That conclusion was wrong, and it was wrong in the direction of foreclosing an option. Checking the second surface reopened a whole objective branch — which is the argument for reading more than one first-party page before declaring a boundary.

## Open questions

- **Confirm with Meta directly** whether qualified-leads optimization applies to an arbitrary on-site registration flow, or only to a Meta-recognised "website form". Decides whether the A3 lever is real for DR specifically.
- Retrieve the developer ODAX mapping table from a working URL to establish the API-enum-level objective ↔ `optimization_goal` pairings.
- Establish whether a website `Complete registration` optimization falls in the $40/day "low-frequency actions" minimum-budget bucket (carried over from `optimization-goals-and-attribution.md`) — interacts directly with the 10×-cost budget rule above.
- Establish whether the omnichannel "Website and in-store" conversion location genuinely optimizes on offline signal, and what it requires.
- Confirm current allowed `window_days` per objective/goal (carried over, still open).

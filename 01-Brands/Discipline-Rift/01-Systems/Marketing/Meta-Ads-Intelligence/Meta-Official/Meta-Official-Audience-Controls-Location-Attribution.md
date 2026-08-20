---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/audience-controls-location-and-attribution.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/audience-controls-location-and-attribution.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Advantage+ audience controls"
meta_topic: Advantage+ audience controls vs suggestions, current location-targeting behaviour, attribution models and settings, and click-metric definitions
gate_mapping: geo accuracy, tracking / signal quality, setup quality
meta_publisher: Meta
meta_source_urls:
  - https://www.facebook.com/business/help/938372127764391
  - https://www.facebook.com/business/help/273363992030035
  - https://www.facebook.com/business/help/202297959811696
  - https://www.facebook.com/business/help/460276478298895
  - https://www.facebook.com/business/help/284415655604125
retrieval_method: rendered_browser
captured_at: 2026-08-14
last_verified_at: 2026-08-14
completeness: partial
research_questions: [E1, E2, E3, G1, G2]
---

# Audience controls, location targeting, attribution, and click metrics

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/audience-controls-location-and-attribution.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Retrieved first-hand for Wave 3. All pages read with a rendered browser (`facebook.com/business/help` returns a JS shell to WebFetch).

Companion to `geo-location-targeting.md` (Marketing API `geo_locations` / `location_types`) and `optimization-goals-and-attribution.md` (`attribution_spec`, bid strategies). **This file closes two open questions those files recorded** — the Help Centre location-behaviour vocabulary, and the currently supported attribution windows.

`completeness: partial` — substantial capture, not exhaustive.

---

## 1. Advantage+ audience — controls vs suggestions

From *"About Audience controls and Audience suggestions in Advantage+ audience"*, verbatim:

> *"Audience controls limit who can see your ads. You can choose **Locations, Minimum age, Custom audiences to exclude and Languages**."*

> *"For example, if you choose Locations, **we won't target beyond your locations unless you select Reach more people likely to respond to your ads**."*

> *"Audience suggestions automatically show ads to people most likely to respond. We'll show ads to people matching your suggestion, **and other audiences when it's likely to improve performance**. Audience suggestions won't be shown outside your audience controls."*

> *"You can suggest **Age, Gender, Detailed targeting and Custom audiences to include. Suggestions don't always constrain your audience.**"*

> *"For example, if you suggest the gender Women, it's possible that your ads could also deliver to men if Meta's AI finds them likely to respond."*

And the mechanism that converts a suggestion into a constraint, verbatim:

> *"If reaching a specific audience is more important than getting best performance, select **Further limit your audience** or **Further limit the reach of your ads** to select Age, Gender, Detailed targeting and Custom audience inclusions as Audience controls. **You may have to uncheck the box Use as a suggestion.**"*

**The operative split, stated by Meta:**

| Input | Default status under Advantage+ audience |
|---|---|
| Locations | **CONTROL** — Meta will not target beyond it *unless* "Reach more people likely to respond to your ads" is selected |
| Minimum age | **CONTROL** |
| Custom audiences to **exclude** | **CONTROL** |
| Languages | **CONTROL** |
| Age | **SUGGESTION** — convertible to a control |
| Gender | **SUGGESTION** — convertible to a control |
| Detailed targeting (interests/behaviours) | **SUGGESTION** — convertible to a control |
| Custom audiences to **include** | **SUGGESTION** — convertible to a control |

Meta also states Advantage+ audience is unavailable for Special Ad Category campaigns (housing, employment, financial products/services) and for Social Issues, Elections and Politics ads.

### Meta's own aggregate performance claims

From *"About Advantage+ audience"*, verbatim:

> *"The Awareness objective could get 14.8% lower cost per result. The Traffic, Engagement and Leads objectives could get 9.7% lower cost per result. The Sales and App promotion objectives could get 7.2% lower cost per result."*

Meta describes the inputs its AI uses as *"Past conversions, Meta Pixel data, Interactions with previous ads"*, and states: *"Meta recommends A/B testing with Advantage+ audience for almost all campaign types, except retargeting campaigns."*

**These are Meta-published aggregate figures with no advertiser population, geography, account scale, or experimental design disclosed.** Record as Meta's assertion, never as evidence that the feature is better for a specific local advertiser.

---

## 2. Location targeting — current behaviour

From *"About location targeting in Meta Ads Manager"*, verbatim:

> *"Location targeting lets you reach people who **live in, have recently spent time in or go often to** countries, regions, cities, postal codes and in US regions such as Comscore Markets and congressional districts."*

**This closes the open question in `geo-location-targeting.md`.** The Help Centre vocabulary is three behaviours — *live in* · *recently spent time in* · *go often to* — against the API's two-value `location_types` enum (`home`, `recent`). **The mapping between the UI's three options and the API's two values is not stated on either page and must not be asserted.**

**The accuracy disclaimer, verbatim, and it is load-bearing:**

> *"Meta technologies use a variety of signals to show ads to people who are within your location targeting selections. **Due to signal variations, complete accuracy cannot be guaranteed. You might see some ad impressions, or receive messages or leads from outside your location settings.**"*

Additional documented behaviour, verbatim:

> *"Sometimes people may also see an ad organically, leading to engagement such as likes, comments and shares on the ad outside the targeted location. Meta may also show preview ads to people connected to the business, even if they're outside the targeted location. You won't be charged for preview impressions."*

On exclusions, verbatim:

> *"When you exclude locations, who sees your ad depends on whether their current location or home location is excluded. For example, someone who lives in an included location may see your ad while visiting an excluded location. If someone's current location and home location are excluded, they won't see your ad at all."*

On third-party comparison, verbatim: *"third-party reporting may not match our campaign reporting."*

---

## 3. Attribution models and settings

From *"About attribution models and attribution settings"*, verbatim:

> *"Meta Ads Manager lets you customize your ad attribution by choosing an attribution model and attribution settings (for standard attribution only) **at the ad set level**."*

> *"When creating an ad set in Meta Ads Manager, you can choose an attribution model, **which inform ad delivery** and determine how conversions can be credited to your ads. Currently, Meta offers the following attribution models: standard or incremental."*

Models, verbatim:
- *"**Standard attribution** optimizes delivery for selected time windows and user behaviors, and allows advertisers to choose whether to credit conversions based on ad impressions, clicks and/or video plays."*
- *"**Incremental attribution** optimizes delivery for incremental conversions using models that predict whether a conversion is caused by an ad."*
- *"**Custom attribution** lets you share granular attribution data from your external analytics tool with Meta so our ad delivery system optimizes toward outcomes based on your attribution logic."*

**The currently supported standard settings for website and in-store conversions, verbatim:**

> *"**Click-through:** Counts events that occurred within **1-day or 7-day** after a link click on your ad."*
> *"**View-through:** Counts events that occurred within **1-day** after an impression of your ad."*
> *"**Engage-through:** Counts events that occurred within **1-day** after a non-link click action on your ad. Engage-through actions include any clicks on your ad, excluding link clicks. For video ads, it also includes when a video is played for 5 seconds, or for 97% of the video if the video length is less than 5 seconds."*

Meta adds: *"Some accounts may still use prior versions of click-through and engage-through attribution while this feature is rolling out"*, and that for certain campaign types not all settings are available.

**Comparison rules, verbatim:**

> *"Results cannot be compared in the Campaign Overview table across ad sets with different attribution models. Each attribution model uses different counting mechanisms, and comparing across different attribution models will lead to inaccurate conclusions. To accurately compare across, use the **Compare Attribution Settings** feature."*

**Read this precisely: the longest click window currently selectable for website conversions is 7 days, and the only view and engage windows are 1 day.** A 28-day click window does not appear among the supported standard settings on this page.

---

## 4. Click metrics — link clicks vs outbound clicks

From *"About link clicks and outbound clicks"*, verbatim:

> *"The metric **link clicks** reports the number of clicks on ad links to specified destinations or experiences, **on or off** Facebook and other Meta technologies."*

Meta's examples of link clicks include *"Clicks on ad formats that take someone into a full-screen experience, such as lead forms, Instant Experience and collection."*

> *"**Outbound clicks** show the number of clicks on links that take people **off** Meta technologies."*

Meta's worked example, verbatim: *"when someone clicks the Instant Experience below, a full-screen experience opens where someone can scroll through content and images. We measure the click on the ad in Feed as a **link click** and the subsequent click from within the full-screen experience leading out to the advertiser's website as an **outbound click**."*

**Therefore link clicks ⊇ outbound clicks conceptually, and they are not interchangeable.** Combined with `optimization-goals-and-attribution.md`'s separation of `LINK_CLICKS` from `LANDING_PAGE_VIEWS` (click vs click-and-load), this establishes three distinct metrics — **all clicks, link clicks, outbound clicks — plus landing page views as a fourth, strictly downstream, concept.**

---

## What Meta does not state

- **How the UI's three location behaviours map to the API's `home` / `recent` values.** Neither page reconciles them; `travel_in` / "go often to" equivalence is not asserted.
- **What "Reach more people likely to respond to your ads" does quantitatively** — only that selecting it permits targeting beyond the chosen locations. No bound, no opt-out consequence described.
- **What the geographic breakdown in reporting actually represents** — residence, impression location, or another concept. Not stated on the retrieved page; the accuracy disclaimer implies it cannot be treated as residency truth.
- **Whether attribution setting is editable after publish, or whether changing it is a significant edit.** `significant-edits.md` does not list it. Unresolved.
- **Any minimum radius for custom locations from the Help Centre side** — the 0.63-mile floor is API-documented (`geo-location-targeting.md`) and was not re-confirmed here.
- **Whether attribution options differ by objective for the Wave 1A candidate branches.** The page says "for certain types of campaigns, not all attribution settings will be available" and names app re-engagement, not the Sales/Leads website distinction.
- **Any methodology behind the Advantage+ audience percentage claims.**
- **Whether Advantage+ audience is available under every Wave 1A candidate objective** beyond the Special Ad Category exclusions listed.

## Why it matters for DR

Gate items: **geo accuracy**, **tracking / signal quality**, **setup quality**.

**Location is a control, not a suggestion — and that is the single most useful fact in this file for DR.** DR's residency requirement is a hard business constraint, and Meta's own framing permits DR to hold it hard while letting the system optimise freely *inside* it. The named exception — *"Reach more people likely to respond to your ads"* — is the one setting that would break DR's serviceability guarantee, and it is now identified by name.

**Interests and age/gender are suggestions by default.** Any DR reasoning that treats a detailed-targeting entry as a guarantee is wrong under current mechanics unless "Use as a suggestion" is unchecked. This bears directly on E1 and E2.

**The accuracy disclaimer bounds every geo claim DR can make.** Meta states plainly that impressions and leads can arrive from outside the location settings. Geo targeting is therefore a *serviceability filter*, never a residency guarantee — which is exactly the distinction E3 must preserve.

**Attribution: 7-day click is the maximum currently available**, so choosing it is not copying a practitioner convention — it is selecting the longest window the platform offers, on an account whose purchase decision is multi-day. View-through and engage-through are 1-day only, and both credit conversions with no click at all.

**Attribution informs delivery, not only reporting**, and is set per ad set — so it is a delivery variable, and cross-ad-set comparisons require Compare Attribution Settings rather than the overview table.

## Open questions

- Confirm whether the attribution setting can be edited after publish and whether that edit is significant.
- Establish what the Ads Manager geographic breakdown measures.
- Retrieve *"Reach more people likely to respond to your ads"* on its own page, if one exists, to document its exact scope.
- Confirm attribution availability under each Wave 1A candidate objective before any objective is committed.

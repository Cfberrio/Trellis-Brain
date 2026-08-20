---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/pixel-capi-deduplication.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/pixel-capi-deduplication.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Pixel CAPI deduplication"
  - "event_id"
meta_topic: Pixel + Conversions API event deduplication
gate_mapping: tracking / signal quality
meta_publisher: Meta
meta_source_urls:
  - https://www.facebook.com/business/help/823677331451951
  - https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/
retrieval_method: rendered_browser + webfetch_full_body
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: full_page
---

# Pixel + Conversions API deduplication

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/pixel-capi-deduplication.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Two first-hand sources: the Business Help Centre article (rendered browser) and the developer documentation (WebFetch). They agree; the developer page adds the time window.

**This file documents the rule. It is not a claim that DR has a deduplication problem — DR's implementation has not been examined.**

## What Meta states

### Why duplicates happen

A "redundant setup" sends the same event through both channels. Meta: deduplication is *"the process of ensuring that the same event, sent from both the Meta Pixel (browser) and the Conversions API (server), is counted only once in your reporting."*

Meta frames the redundant setup as intentional and useful — *"Pixel relies on browser data, which can be blocked or lost due to browser settings or connectivity issues"*, while the Conversions API is *"more resilient to browser limitations and ad blockers."* Sending both is how lost events get recovered. Deduplication is the cost of that recovery, not a defect.

### When deduplication is needed

| Situation | Meta's answer |
|---|---|
| Same event from both sources (e.g. Purchase from both) | Deduplication needed |
| Different events from each source (e.g. AddToCart from browser, Purchase from server) | Not needed |

### The mechanism — two methods

**Method 1 — `event_id` + `event_name` (Meta's primary).** Conditions, verbatim:

- *"The `event_name` (e.g., Purchase) must match between the Pixel and Conversions API events."*
- *"The `event_id` must be identical for both events."*

The developer documentation states the same in implementation terms: *"a Meta Pixel's `eventID` must match the Conversion API's `event_id`"* and *"a Meta Pixel's `event` must match the Conversion API's `event_name`."*

**Method 2 — `event_name` + `fbp` and/or `external_id`.** *"Alternatively, deduplication can also occur if the event_name and either the external_ID or fbp parameters match."*

The developer page adds a limitation not stated in the Help Centre article: this method *"only works for deduplicating events sent first from the browser and then through the server"*, and will not deduplicate if the browser event has not arrived *"within 48 hours."*

**Which event survives.** *"If server and pixel events are similar, Meta prefers the event received first."*

**What deduplication covers:** redundant pixel events (identical event and eventID), redundant server events (identical `event_name` and `event_id`), and redundant pixel + server events (matching `event_name` and `event_id`, or `event_name` and `external_ID`/`fbp`).

### The time window

From the developer documentation: *"events are only deduplicated if they are received within 48 hours of when we receive the first event with a given `event_id`."*

### Consequence of getting it wrong

Meta is explicit about the downstream damage:

> *"Without deduplication, you may see artificially high conversion numbers, which can mislead optimization and budget allocation decisions."*

Named impacts: conversion rate inflation, unreliable ROAS, and over-reported attribution. Meta also warns the reverse failure exists — inaccurate event IDs *"may cause conversions to be wrongly deduplicated"*, i.e. real conversions discarded.

Both directions are failures. Too little deduplication inflates; too much deletes.

### Monitoring and diagnostics Meta documents

- **Events Manager dashboard** — *"shows all received events, their sources, and deduplication status."*
- **Test Events tool** — *"Send test events to verify which are received, deduplicated, or dropped."*
- **Event setup tool** — troubleshoot errors.
- **Meta Ads Data Advisor** — a Chrome extension, for diagnostics.

Meta's stated troubleshooting sequence: check `event_id` consistency across sources; review events in Events Manager with Test Events; validate that `event_name` and `event_id` are *"formatted identically across sources"*; watch for unexpected spikes or drops in event counts.

**Common issues Meta names:** mismatched or missing `event_id`; delays between browser/app and server event delivery; incorrect parameter names or values.

**Partner integrations may handle it.** *"Many platforms (e.g., Shopify, WooCommerce) automatically handle deduplication parameters."* Manual setup requires adding the parameters in code.

## What Meta does not state

- No statement of what a healthy deduplication rate looks like. There is no published target.
- No statement on how delayed a server event may be before the "prefers the event received first" rule produces a wrong outcome, beyond the 48-hour window.
- The Help Centre article does not repeat the 48-hour window; it appears only in the developer documentation. The two pages are consistent but not identical in coverage.
- No guidance specific to low-volume advertisers, where a small absolute number of mis-deduplicated events is a large proportion.

## Why it matters for DR

Gate item: **tracking / signal quality**.

The consequence Meta names is not a reporting nuisance — it is *"mislead optimization and budget allocation decisions."* Duplicate registrations would make DR's cost per registration look better than it is, on an account whose volume is low enough that a handful of duplicates moves the number materially. A local advertiser with few weekly conversions has the least statistical cushion for this and the least chance of noticing it by eye.

It also compounds with `learning-limited.md`. Optimization events are the currency of exiting the learning phase. Over-deduplication (wrongly discarding real conversions) does not only under-report — it removes optimization events from an account that, on Meta's own stated causes, is already at risk of being learning limited for having too few.

Three specifics worth noting for a later DR audit, all conditions rather than findings:

1. **`event_id` must be identical, and `event_name` must match.** If DR's registration flow runs on a third-party or subdomain registration system, the browser and server events may originate in different systems — which is exactly where a shared unique `event_id` is hardest to guarantee.
2. **If a partner integration handles registration**, deduplication parameters may already be automatic. Meta names Shopify and WooCommerce; whether DR's registration platform does this is unknown here.
3. **Method 2 depends on `fbp`** — the same browser-side identifier family as the `fbc` Click ID flagged in `event-match-quality.md` as High priority and easily lost. A journey that drops browser identifiers degrades both matching and fallback deduplication at once.

Not a recommendation, and not a diagnosis. The checkable conditions: does DR send the same event from both pixel and CAPI, is a shared `event_id` present, and what does Events Manager show as deduplication status during a live registration window.

## Open questions

- Does DR run CAPI at all, and does its registration platform emit both events? Belongs to `domains/ads/meta/discipline-rift/`.
- No published healthy-rate benchmark for deduplication.
- Whether the 48-hour window applies identically to Method 1, or only to the `fbp`/`external_id` fallback where it is stated.

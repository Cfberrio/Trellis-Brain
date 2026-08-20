---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/aggregated-event-measurement.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/aggregated-event-measurement.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "AEM"
  - "Aggregated Event Measurement"
meta_topic: Aggregated Event Measurement (AEM) — current state for website events
gate_mapping: tracking / signal quality, setup quality
meta_publisher: Meta
meta_source_urls:
  - https://www.facebook.com/business/help/721422165168355
retrieval_method: rendered_browser
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: full_page
---

# Aggregated Event Measurement

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/aggregated-event-measurement.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

Retrieved with a rendered browser, including accordion content not present in the page's visible text.

**This is the highest-value file in the knowledge base so far, because it documents that widely-repeated advice is now obsolete.**

## What Meta states

**What AEM is.** *"Meta's Aggregated Event Measurement is a protocol that allows for the measurement of web and app events from people using iOS 14 and later devices. Aggregated Event Measurement processing includes privacy protective measures like removing identifiers, adding differential privacy, and aggregating the data across users before personalizing ads we show and measuring how they perform."*

**For website events:** *"Aggregated Event Measurement helps us recover limited measurement of website conversions from people using iOS 14.5 and later devices."*

### The web event configuration requirements have been removed

Meta's current wording, under "Changes to website conversion campaigns":

> *"We've introduced updates to website conversion campaigns. Now, there are no steps you need to take for your events to be processed through Aggregated Event Measurement."*

The four changes Meta lists, quoted:

1. *"You no longer need to prioritize 8 conversion events per domain for web conversion optimization, and you don't need to turn on value sets in order to use value optimization."*
2. *"The Aggregated Event Measurement tab in Meta Events Manager has been removed because you no longer need to configure your web events."*
3. *"You aren't required to verify your website domains for purposes related to event configuration. However, you may still need to verify your domain for other reasons."*
4. *"You don't need to select a conversion domain when you create a campaign in Ads Manager."*

**The rollout qualifier is load-bearing.** Meta frames these as *"We are gradually introducing updates"* and prefixes the list with *"Here are the changes you'll see when you have access."* This is a staged rollout, not a completed universal change. An account may or may not have it.

**CAPI does not escape AEM.** *"Events sent to Meta via the Conversions API may also be processed in accordance with limits set by Aggregated Event Measurement."*

**Also captured:** as of October 9, 2024, Meta sends AEM reporting to mobile measurement partners. App-side, AEM now covers the app promotion objective and is *"currently not supported for custom event optimization."*

## What Meta does not state

- **No date for when the web-event changes complete**, and no way documented on this page to check whether a given ad account has access. "When you have access" is the only qualifier given.
- No statement of what the AEM limits on Conversions API events actually are — only that limits apply.
- No statement of what replaced the 8-event prioritization mechanism internally. Meta says configuration is unnecessary, not that constraints vanished.
- Nothing about how AEM affects reporting for a low-volume local advertiser specifically.

## Why it matters for DR

Gate items: **tracking / signal quality**, **setup quality**.

**This is the clearest example so far of why this knowledge base exists.** "Prioritize your 8 conversion events", "verify your domain for event configuration", and "set your conversion domain" are among the most repeated pieces of Meta advice in circulation, and Meta's own current documentation says each is no longer required for accounts with access.

For Sprint 3's grading, any expert claim asserting those steps should be graded against this file — the likely grade is `OUTDATED`, not `CONFLICTING`, since the advice was correct when given. That distinction matters: an expert who said this in 2023 was right, and a playbook that quietly marks them wrong is itself misleading.

For DR concretely: if someone audits the account and reports "the 8 events are not prioritized" or "the conversion domain is not set" as defects, that finding needs checking against this page before it becomes work. It may be a non-issue — or it may be real, if DR's account has not received the rollout. Both are possible and the page gives no way to tell from documentation alone.

The CAPI note also tempers `conversions-api-customer-parameters.md` and `event-match-quality.md`: server-side sending improves matching, but Meta states AEM limits may still apply to those events. CAPI is not a route around iOS measurement limits.

Not a recommendation. The checkable condition: does DR's account show the AEM tab in Events Manager, and is anything in DR's current setup built on requirements Meta has since removed?

## Open questions

- How to determine whether a specific ad account has the rollout. Not documented on this page.
- What AEM limits actually apply to Conversions API events.
- Whether domain verification is still needed for DR for any of the "other reasons" Meta alludes to but does not enumerate here.

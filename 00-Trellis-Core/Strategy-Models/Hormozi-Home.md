---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
owner: Trellis
last_updated: 2026-04-28
sensitivity: internal
hub_role: system-hub
---

# Hormozi Home

## Parent
- [[Strategy-Models-Home|Strategy Models Home]]

## Purpose
Entry point for the Hormozi strategy domain inside Trellis-Core. Holds abstract commercial models extracted from Hormozi's books and material. Used as a reference layer for offer design, lead generation, pricing, monetization, and sales logic across brands.

Hormozi is a shared reference domain. It is not a brand. It does not store voice, copy, or brand-specific examples.

## Domain Rules
- All notes in this domain are prefixed `Hormozi-`.
- Brand notes may link to Hormozi notes through `## Strategy References`.
- Hormozi notes must not link back into brand notes.
- Generic filenames (`Offer`, `Pricing`, `Message`, `Value`, `Funnel`) are prohibited inside this domain — they collide with existing brand notes.
- See [[Hormozi-Linking-Contract|Hormozi Linking Contract]] for the full contract.

## Children
- [[Hormozi-Linking-Contract|Hormozi Linking Contract]]

### Book Hubs (extracted)
- [[01-100M-Offers/00-Book-Home|100M Offers — Book Home]]
- [[03-100M-Money-Models/00-Book-Home|100M Money Models — Book Home]]
- [[04-100M-Lost-Chapters/00-Book-Home|100M Lost Chapters — Book Home]]
- [[05-Branding/00-Book-Home|Branding — Book Home]]
- [[06-Fast-Cash/00-Book-Home|Fast Cash — Book Home]]
- [[07-Hooks/00-Book-Home|Hooks — Book Home]]
- [[08-GOATed-Ads/00-Book-Home|GOATed Ads — Book Home]]
- [[09-Lifetime-Value/00-Book-Home|Lifetime Value — Book Home]]
- [[10-Lead-Nurture/00-Book-Home|Lead Nurture — Book Home]]
- [[11-Price-Raise/00-Book-Home|Price Raise — Book Home]]
- [[12-Marketing-Machine/00-Book-Home|Marketing Machine — Book Home]]
- [[13-Pricing/00-Book-Home|Pricing — Book Home]]
- [[14-Retention/00-Book-Home|Retention — Book Home]]

## Not Yet Extracted
- 100M Leads (slot `02-` reserved by numbering convention; folder not created).
- Any additional Hormozi material released after this index date.

## Related
- [[Strategy-Models-Home|Strategy Models Home]]
- [[00-Trellis-Core/Routing-Rules|Routing Rules]]
- [[00-Trellis-Core/Metadata-Standard|Metadata Standard]]

## Retrieval Rule
Load Hormozi notes only when the task is strategic (offer construction, pricing logic, lead acquisition logic, monetization, value framing, sales objection structure). Do not load Hormozi for voice, tone, or evidence tasks.

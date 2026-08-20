---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/official-meta/placements.md"
repo_path: domains/ads/meta/intelligence/knowledge/official-meta/placements.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/meta-official
  - discipline-rift
aliases:
  - "Placements"
  - "Advantage+ placements"
meta_topic: Placement targeting — publisher platforms, positions, and defaults
gate_mapping: placement control
meta_publisher: Meta
meta_source_urls:
  - https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/placement-targeting
retrieval_method: webfetch_full_body
captured_at: 2026-08-13
last_verified_at: 2026-08-13
completeness: partial
---

# Placement targeting

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Official/Meta-Official-Index|Meta oficial — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Experts-Index|Expertos — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Frameworks/Frameworks-Index|Frameworks — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Open-Questions/Open-Questions-and-Verification-Queue|Preguntas abiertas y cola de verificación]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/official-meta/placements.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

## What Meta states

**`publisher_platforms`:** `facebook`, `instagram`, `threads`, `messenger`, `audience_network`.

**Positions documented per platform:**

| Platform | Positions |
|---|---|
| Facebook | `feed`, `right_hand_column`, `marketplace`, `video_feeds`, `story`, `search`, `instream_video`, `facebook_reels`, `facebook_reels_overlay`, `profile_feed`, `notification` |
| Instagram | `stream`, `story`, `explore`, `explore_home`, `reels`, `profile_feed`, `ig_search`, `profile_reels` |
| Messenger | `sponsored_messages`, `story` |
| Audience Network | `classic`, `rewarded_video` |
| Threads | `threads_stream` |
| WhatsApp | `status` |

**The default is everything.** Quoted: *"If you do not specify anything for a particular placement field, Facebook considers all possible default positions for that field."* Meta's own example: selecting only `facebook` for `publisher_platforms` without specifying positions defaults to "all default Facebook positions such as `feed`, `right_hand_column`, and so on."

**Documented restrictions:**

- `right_hand_column` cannot be used alone for video, collection, or canvas ads
- Audience Network cannot be selected alone as a publisher platform
- Facebook or Messenger `story` cannot be selected independently — must pair with `feed` or Instagram `story`
- `notification` cannot be selected independently — must pair with `feed`
- `threads_stream` requires Instagram `stream`
- WhatsApp `status` requires Instagram `story`

## What Meta does not state

- **This page documents the API surface, not Advantage+ placements guidance.** Meta's recommendation to use automatic/Advantage+ placements, and its stated reasoning, live on Business Help Centre pages not retrieved here. Do not attribute a recommendation to Meta from this file.
- No performance, cost, or delivery-volume claims per placement. Nothing here says any placement performs better.
- No statement about creative asset requirements or aspect ratios per position.
- No statement about which positions are eligible for which objectives.

## Why it matters for DR

Gate item: **placement control**.

The operative fact is the same shape as the geo default: **unspecified means all**. An ad set that never touched placements is running across every default position of every selected platform, including surfaces whose context has nothing to do with a parent researching an after-school season.

For DR this is a creative-clarity problem as much as a delivery one. A single creative rendered into `feed`, `story`, `reels`, `right_hand_column` and `marketplace` is being asked to work in formats with different aspect ratios, different sound expectations, and very different attention. The Sprint 1 competitor sweep is relevant context here: `patterns.md` records no format consensus across the five brand families — Soccer Shots ran 100% video, Skyhawks 67% static image. Format choice is contested in the category, which makes placement control a live decision for DR rather than a settled default.

The restriction list also constrains structure: `story` cannot be isolated on Facebook or Messenger, so a story-only test is not directly expressible there. Any DR placement experiment has to be designed around that.

Not a recommendation. Meta publishes no performance claim per placement, and nothing here says DR should narrow or widen. The checkable condition is: what is DR's ad set actually set to, and is the creative appropriate for every position it is being served into?

## Open questions

- Retrieve Meta's Advantage+ placements guidance and its stated rationale, so the "narrow vs automatic" question has an official position recorded rather than an inferred one.
- Per-position creative specs — needed before any placement recommendation is actionable.
- Whether placement breakdown reporting is available at the position level for a small account. Not sourced.

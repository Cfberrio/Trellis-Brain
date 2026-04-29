---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: core
status: active
canonical: true
used_for_ai: true
source_type: curated
owner: Trellis
last_updated: 2026-04-28
sensitivity: internal
hub_role: leaf
---

# Hormozi Linking Contract

## Parent
- [[Hormozi-Home|Hormozi Home]]

## Purpose
Defines how the Hormozi strategy domain connects to the rest of the Trellis Brain. Prevents brand contamination, name collisions, and graph drift as Hormozi material is added.

## Core Principles
1. Hormozi is a shared reference domain, not a brand.
2. Hormozi notes are abstract. They contain frameworks, principles, and decision logic — never brand voice, copy, evidence, or examples.
3. Brand context flows toward Hormozi for inspiration. Hormozi context never flows back as brand truth.

## Linking Direction
- Brand notes may link to Hormozi notes through a `## Strategy References` section.
- Hormozi notes must not link into brand notes.
- Hormozi notes may link to other Hormozi notes, to `Strategy-Models-Home`, and to Trellis-Core infrastructure (`Routing-Rules`, `Metadata-Standard`).
- Cross-brand contamination through Hormozi is prohibited. A Hormozi note never references CTS, DR, OEV, RV, or any brand-specific asset.

## Naming Rules
- Every Hormozi note filename starts with `Hormozi-`.
- Generic names are prohibited inside this domain because they collide with existing brand notes:
  - prohibited: `Offer.md`, `Pricing.md`, `Message.md`, `Value.md`, `Funnel.md`, `Sales.md`, `Delivery.md`, `Constraints.md`, `Opportunities.md`, `KPIs.md`, `Avatar.md`, `Positioning.md`
  - required form: `Hormozi-Grand-Slam-Offer.md`, `Hormozi-Value-Equation.md`, `Hormozi-Pricing.md`, `Hormozi-Core-Four.md`, `Hormozi-Lead-Magnet.md`
- Book-folder filenames inside `01-100M-Offers/` etc. follow the same prefix rule, except for the per-book `00-Book-Home.md` which is local-scoped by its folder.

## Link Style Rules
- Use full-path links when linking from a brand note to a Hormozi note. Canonical notes live one level deeper, inside the per-book folder. Example:
  `[[00-Trellis-Core/Strategy-Models/01-100M-Offers/Hormozi-Grand-Slam-Offer|Hormozi — Grand Slam Offer]]`
- Inside the Hormozi domain, short links are acceptable because the `Hormozi-` prefix already disambiguates.
- When ambiguity is possible (a name that could exist elsewhere), always use the full path including the book folder.

## Metadata Rules
All Hormozi notes use the existing Trellis metadata standard. No new dialect.
- `brand: Trellis-Core`
- `area: strategy-models`
- `subarea: hormozi`
- `note_type: home | strategy-model | core`
- `status: active | draft | review`
- `canonical: true` for distilled framework notes; `false` for raw source extracts
- `used_for_ai: true`
- `source_type: curated | imported | derived` (use `imported` for raw book extracts; `derived` for distilled frameworks)
- `source_reference:` book + chapter or page when applicable
- `sensitivity: internal`
- `hub_role: system-hub | leaf`

Do not invent fields. Do not create a parallel schema.

## Tags Rule
Tags are not required for this domain. Structure carries routing. Add a tag only when it provides retrieval value that folder + frontmatter + links cannot provide.

## Brand Reference Pattern
Inside any brand note that wants to anchor to Hormozi, add:

```md
## Strategy References
- [[00-Trellis-Core/Strategy-Models/01-100M-Offers/Hormozi-Grand-Slam-Offer|Hormozi — Grand Slam Offer]]
- [[00-Trellis-Core/Strategy-Models/01-100M-Offers/Hormozi-Value-Equation|Hormozi — Value Equation]]
```

The `## Strategy References` section is the only sanctioned bridge between brand notes and Hormozi notes.

## Anti-Patterns
- copying Hormozi prose into brand notes as canonical voice
- naming a Hormozi note with a generic word that collides with a brand note
- linking from a Hormozi note into a brand-specific asset
- duplicating a Hormozi framework across multiple book folders instead of one canonical home
- adding Hormozi tags to brand notes
- treating raw book extracts as canonical truth — extracts are evidence; frameworks are canonical

## Related
- [[Hormozi-Home|Hormozi Home]]
- [[Strategy-Models-Home|Strategy Models Home]]
- [[00-Trellis-Core/Metadata-Standard|Metadata Standard]]
- [[00-Trellis-Core/Routing-Rules|Routing Rules]]

---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: core
status: active
canonical: false
used_for_ai: true
source_type: curated
owner: Trellis
last_updated: 2026-04-28
sensitivity: internal
hub_role: leaf
book: 100M-Money-Models
---

# 100M Money Models — Source Map

## Parent
- [[00-Book-Home|100M Money Models — Book Home]]

## Purpose
Index that maps source material (PDF chapters, page ranges) to the distilled framework notes derived from it. Bridge between the source artifact and canonical notes. Does not contain book content itself.

## Source Artifact
- File: `/Users/cberrio04/Documents/CLAUDE CODE/hormozi-books/100M Money Models_ How To Make Money  -  Alex Hormozi  -  100M, 2025  -  dc9d320234c3d4c24ab59a1cca27f678  -  Anna's Archive_compressed.pdf`
- Format: PDF (163 pages)
- Status: extracted

## Section → Framework Map

| # | Source Section | Pages | Canonical Framework Note | Status |
|---|---|---|---|---|
| 1 | Start Here | pp. 10–16 | — | source-only |
| 2 | Section I: What's A Money Model? | pp. 18–22 | [[Hormozi-Money-Model\|Hormozi — Money Model]] | extracted |
| 3 | The Four Types of Offers That Make Money Models | pp. 23–25 | [[Hormozi-Money-Model\|Hormozi — Money Model]] | extracted |
| 4 | Section II intro: Attraction Offers | pp. 27–28 | [[Hormozi-Attraction-Offers\|Hormozi — Attraction Offers]] | extracted |
| 5 | Win Your Money Back | pp. 30–35 | [[Hormozi-Attraction-Offers\|Hormozi — Attraction Offers]] | extracted |
| 6 | Giveaways | pp. 37–43 | [[Hormozi-Attraction-Offers\|Hormozi — Attraction Offers]] | extracted |
| 7 | Decoy Offer | pp. 45–50 | [[Hormozi-Attraction-Offers\|Hormozi — Attraction Offers]] | extracted |
| 8 | Buy X Get Y Free | pp. 51–56 | [[Hormozi-Attraction-Offers\|Hormozi — Attraction Offers]] | extracted |
| 9 | Pay Less Now or Pay More Later | pp. 58–61 | [[Hormozi-Attraction-Offers\|Hormozi — Attraction Offers]] | extracted |
| 10 | Free Goodwill Offer | pp. 63–65 | — | source-only (review request, not a Money Model mechanism) |
| 11 | Attraction Offers Conclusion | p. 66 | — | source-only (recap) |
| 12 | Section III intro: Upsell Offers | pp. 67–68 | [[Hormozi-Upsell-Offers\|Hormozi — Upsell Offers]] | extracted |
| 13 | The Classic Upsell | pp. 70–74 | [[Hormozi-Upsell-Offers\|Hormozi — Upsell Offers]] | extracted |
| 14 | Menu Upsell | pp. 76–83 | [[Hormozi-Upsell-Offers\|Hormozi — Upsell Offers]] | extracted |
| 15 | Anchor Upsell | pp. 85–88 | [[Hormozi-Upsell-Offers\|Hormozi — Upsell Offers]] | extracted |
| 16 | Rollover Upsell | pp. 90–94 | [[Hormozi-Upsell-Offers\|Hormozi — Upsell Offers]] | extracted |
| 17 | Upsell Offers Conclusion | p. 96 | — | source-only (recap) |
| 18 | Section IV intro: Downsell Offers + Rules of Downselling | pp. 97–99 | [[Hormozi-Downsell-Offers\|Hormozi — Downsell Offers]] | extracted |
| 19 | Payment Plan Downsells | pp. 101–106 | [[Hormozi-Downsell-Offers\|Hormozi — Downsell Offers]] | extracted |
| 20 | Trial With Penalty | pp. 108–114 | [[Hormozi-Downsell-Offers\|Hormozi — Downsell Offers]] | extracted |
| 21 | Feature Downsells | pp. 116–121 | [[Hormozi-Downsell-Offers\|Hormozi — Downsell Offers]] | extracted |
| 22 | Downsell Offers Conclusion | p. 123 | — | source-only (recap) |
| 23 | Section V intro: Continuity Offers | pp. 124–125 | [[Hormozi-Continuity-Offers\|Hormozi — Continuity Offers]] | extracted |
| 24 | Continuity Bonus Offers | pp. 127–133 | [[Hormozi-Continuity-Offers\|Hormozi — Continuity Offers]] | extracted |
| 25 | Continuity Discount Offers | pp. 135–141 | [[Hormozi-Continuity-Offers\|Hormozi — Continuity Offers]] | extracted |
| 26 | Waived Fee Offer | pp. 143–146 | [[Hormozi-Continuity-Offers\|Hormozi — Continuity Offers]] | extracted |
| 27 | Continuity Offers Conclusion | p. 147 | — | source-only (recap) |
| 28 | Section VI: Make Your Money Model | pp. 148–155 | [[Hormozi-Money-Model-Assembly\|Hormozi — Money Model Assembly]] | extracted |
| 29 | Ten Years In Ten Minutes | pp. 157–159 | [[Hormozi-Money-Model-Assembly\|Hormozi — Money Model Assembly]] (recap reference) | extracted |
| 30 | Final Thoughts | pp. 160–161 | — | source-only |

### Many-to-one mappings (documented)
- **All five Attraction Offer chapters** (Win Your Money Back, Giveaways, Decoy, Buy X Get Y Free, Pay Less Now or Pay More Later) → `Hormozi-Attraction-Offers`. Each is a section in the parent note. They share the same purpose (turn strangers into customers + cover acquisition cost) and read better together than as separate files.
- **All four Upsell chapters** (Classic, Menu, Anchor, Rollover) → `Hormozi-Upsell-Offers`. Same logic.
- **All three Downsell chapters** (Payment Plan, Trial With Penalty, Feature) + Rules of Downselling → `Hormozi-Downsell-Offers`.
- **All three Continuity chapters** (Bonus, Discount, Waived Fee) → `Hormozi-Continuity-Offers`.
- **Section I + Four Types of Offers chapter** → `Hormozi-Money-Model` (definition + architecture).
- **Section VI + Ten Years In Ten Minutes recap** → `Hormozi-Money-Model-Assembly`.

### Mapped to existing canonical notes in `01-100M-Offers/`
- Continuity Bonus Offers → applies the bonus mechanism canonical at [[../01-100M-Offers/Hormozi-Bonuses|Bonuses]]. Not duplicated.
- Feature Downsell removing guarantees → applies the guarantee mechanism canonical at [[../01-100M-Offers/Hormozi-Guarantees|Guarantees]]. Not duplicated.
- Anchor Upsell → operationalizes price-anchoring logic from [[../01-100M-Offers/Hormozi-Pricing-Power|Pricing Power]]. Anchor Upsell is its own mechanism (sequence + sales script), so it lives canonically here under `Hormozi-Upsell-Offers`; the underlying anchoring logic is not redefined.
- Pay Less Now or Pay More Later → uses a conditional satisfaction guarantee, mechanism canonical at [[../01-100M-Offers/Hormozi-Guarantees|Guarantees]].

One-to-many mappings: not used.

## Conventions
- Raw extract notes (when needed) live in this folder as `Hormozi-100M-Money-Models-Raw-<Section>.md` with `canonical: false`, `source_type: imported`. None created for this book — source distilled directly; provenance carried via `source_reference` frontmatter on each canonical note plus this map.
- Canonical framework notes live under `03-100M-Money-Models/` with the `Hormozi-` prefix, `canonical: true`, `source_type: derived`.
- Each of the 16 specific Money Model mechanisms is documented as a **section** inside the relevant offer-type note rather than as a separate file. This matches the retrieval grain used in `01-100M-Offers/` and prevents fragmentation.

## Related
- [[00-Book-Home|100M Money Models — Book Home]]
- [[Hormozi-Linking-Contract|Hormozi Linking Contract]]

## Extraction Status
- **Complete.** All 27 substantive sections mapped (across 6 sections of the book). 6 canonical notes extracted. 7 sections classified source-only (Start Here, Free Goodwill review request, four section conclusions, Final Thoughts). 0 raw extract notes required.

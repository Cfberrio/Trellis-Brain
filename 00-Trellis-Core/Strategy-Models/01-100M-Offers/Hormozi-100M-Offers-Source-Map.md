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
book: 100M-Offers
---

# 100M Offers — Source Map

## Parent
- [[00-Book-Home|100M Offers — Book Home]]

## Purpose
Index that maps source material (PDF chapters, page ranges) to the distilled framework notes derived from it. Bridge between source artifacts and canonical Hormozi framework notes. Does not contain book content itself.

## Source Artifact
- File: `/Users/cberrio04/Documents/CLAUDE CODE/hormozi-books/100m-offers_compressed.pdf`
- Format: PDF (138 pages)
- Status: extracted

## Section → Framework Map

| # | Source Section | Pages | Raw Extract Note | Canonical Framework Note | Status |
|---|---|---|---|---|---|
| 1 | Start Here | pp. 13–14 | — | — | source-only |
| 2 | How We Got Here (Ch. 1) | pp. 17–22 | — | — | source-only |
| 3 | Grand Slam Offers (Ch. 2) | pp. 23–29 | — | [[Hormozi-Grand-Slam-Offer\|Hormozi — Grand Slam Offer]] | extracted |
| 4 | Pricing: The Commodity Problem (Ch. 3) | pp. 33–40 | — | [[Hormozi-Grand-Slam-Offer\|Hormozi — Grand Slam Offer]] + [[Hormozi-Pricing-Power\|Hormozi — Pricing Power]] (many-to-one shared) | extracted |
| 5 | Pricing: Starving Crowd (Ch. 4) | pp. 41–47 | — | [[Hormozi-Starving-Crowd\|Hormozi — Starving Crowd]] | extracted |
| 6 | Pricing: Charge What It's Worth (Ch. 5) | pp. 49–56 | — | [[Hormozi-Pricing-Power\|Hormozi — Pricing Power]] | extracted |
| 7 | Value Offer: The Value Equation (Ch. 6) | pp. 61–70 | — | [[Hormozi-Value-Equation\|Hormozi — Value Equation]] | extracted |
| 8 | Free Goodwill (Ch. 7) | pp. 71–72 | — | — | source-only |
| 9 | Value Offer: The Thought Process (Ch. 8) | pp. 73–76 | — | [[Hormozi-Offer-Creation\|Hormozi — Offer Creation]] | extracted |
| 10 | Creating GSO Part I: Problems & Solutions (Ch. 9) | pp. 77–82 | — | [[Hormozi-Offer-Creation\|Hormozi — Offer Creation]] | extracted |
| 11 | Creating GSO Part II: Trim & Stack (Ch. 10) | pp. 85–92 | — | [[Hormozi-Offer-Creation\|Hormozi — Offer Creation]] | extracted |
| 12 | Enhancing The Offer: intro (Ch. 11) | pp. 97–100 | — | [[Hormozi-Grand-Slam-Offer\|Hormozi — Grand Slam Offer]] (architecture confirmation) | extracted |
| 13 | Enhancing: Scarcity (Ch. 12) | pp. 103–107 | — | [[Hormozi-Scarcity\|Hormozi — Scarcity]] | extracted |
| 14 | Enhancing: Urgency (Ch. 13) | pp. 109–111 | — | [[Hormozi-Urgency\|Hormozi — Urgency]] | extracted |
| 15 | Enhancing: Bonuses (Ch. 14) | pp. 113–116 | — | [[Hormozi-Bonuses\|Hormozi — Bonuses]] | extracted |
| 16 | Enhancing: Guarantees (Ch. 15) | pp. 117–124 | — | [[Hormozi-Guarantees\|Hormozi — Guarantees]] | extracted |
| 17 | Enhancing: Naming (Ch. 16) | pp. 127–131 | — | [[Hormozi-Naming\|Hormozi — Naming]] | extracted |
| 18 | Your First $100,000 (Section V) | pp. 136–138 | — | — | source-only |

### Many-to-one mappings (documented)
- **Commodity Problem (Ch. 3) + Charge What It's Worth (Ch. 5)** → `Hormozi-Pricing-Power`. Ch. 3 also contributes the formal four-component GSO definition and the agency-software 22.4× walkthrough to `Hormozi-Grand-Slam-Offer`.
- **Thought Process (Ch. 8) + GSO Part I (Ch. 9) + GSO Part II (Ch. 10)** → `Hormozi-Offer-Creation`. One sequential workflow.
- **Enhancing Offer intro (Ch. 11)** confirms the architectural placement of Scarcity / Urgency / Bonuses / Guarantees / Naming as offer-level levers (not selling-level). Feeds `Hormozi-Grand-Slam-Offer`.

One-to-many mappings: not used.

## Conventions
- Raw extract notes (when needed) live in this folder as `Hormozi-100M-Offers-Raw-<Section>.md` with `canonical: false`, `source_type: imported`. None created for this book — source distilled directly; provenance carried via `source_reference` frontmatter on each canonical note plus this map.
- Canonical framework notes live under `01-100M-Offers/` with the `Hormozi-` prefix, `canonical: true`, `source_type: derived`.

## Related
- [[00-Book-Home|100M Offers — Book Home]]
- [[Hormozi-Linking-Contract|Hormozi Linking Contract]]

## Extraction Status
- **Complete.** All 16 chapters mapped. 10 canonical notes extracted. 4 sections classified source-only. 0 raw extract notes required.

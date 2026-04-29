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
book: Price-Raise
---

# Price Raise — Source Map

## Parent
- [[00-Book-Home|Price Raise — Book Home]]

## Purpose
Index that maps source material (PDF section, page ranges) to the distilled framework notes derived from it. Bridge between the source artifact and canonical Hormozi framework notes for this book. Documents reuse mappings to canonical notes that already live in `01-100M-Offers/`. Does not contain book content itself.

## Source Artifact
- File: `/Users/cberrio04/Documents/CLAUDE CODE/hormozi-books/Price Raise_compressed.pdf`
- Title: *$100M Playbook: Price Raise — How to Raise Prices Without Losing Customers*
- Author: Alex Hormozi
- Publisher: Acquisition.com (2025)
- Format: PDF (28 pages including front matter; ~25 pages of body)
- Status: extracted

## Section → Framework Map

| # | Source Section | Pages | Raw Extract Note | Canonical Framework Note | Status |
|---|---|---|---|---|---|
| 1 | Raise Prices (Trey narrative) | pp. 1–2 | — | — | source-only (operating thesis "don't wait for disaster" folded into [[Hormozi-Price-Raise-Play\|Price-Raise-Play]] Strategic Implications) |
| 2 | Outline of This Playbook | pp. 2–3 | — | — | source-only (table of contents) |
| 3 | Why Raising Prices Is A Good Idea | p. 3 | — | [[Hormozi-Price-Raise-Play\|Hormozi — Price Raise Play]] | extracted (operating thesis + race-to-bottom framing; principle reuses [[../01-100M-Offers/Hormozi-Pricing-Power\|Pricing Power]]) |
| 4 | Vicious vs. Virtuous Price Cycle | pp. 4–5 | — | [[Hormozi-Price-Raise-Play\|Hormozi — Price Raise Play]] (operational extension with emotional investment / demandingness / conviction / gratitude variables) | extracted (extends, does not duplicate, [[../01-100M-Offers/Hormozi-Pricing-Power\|Pricing Power]]) |
| 5 | My Rules For Raising Prices | pp. 5–7 | — | [[Hormozi-Price-Raise-Rules\|Hormozi — Price Raise Rules]] | extracted |
| 6 | How To Pick Your Price | pp. 7–9 | — | [[Hormozi-Price-Test-Math\|Hormozi — Price Test Math]] | extracted |
| 7 | The Perfect Price Raise Letter — Section #1 R: Remind | p. 10 | — | [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] | extracted |
| 8 | The Perfect Price Raise Letter — Section #2 A: Address | pp. 10–11 | — | [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] | extracted |
| 9 | The Perfect Price Raise Letter — Section #3 I: Invest | pp. 11–12 | — | [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] | extracted |
| 10 | The Perfect Price Raise Letter — Section #4 S: Soften | pp. 12–13 | — | [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] | extracted |
| 11 | The Perfect Price Raise Letter — Section #5 E: Explain (3 customer types) | pp. 13–14 | — | [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] | extracted |
| 12 | What This Letter Looks Like All Together | p. 14 | — | [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] | extracted (as worked-template inside Practical Use) |
| 13 | What to Do Next (single jump vs. stair-step) | p. 15 | — | [[Hormozi-Price-Raise-Play\|Hormozi — Price Raise Play]] (rollout options) + [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] (stair-step discount mechanic) | extracted (many-to-one) |
| 14 | What To Do About Incoming Customers | pp. 15–16 | — | [[Hormozi-Price-Raise-Play\|Hormozi — Price Raise Play]] (sales-team objection script) | extracted |
| 15 | My Gym Price Increase Letter (long-form sample) | pp. 17–20 | — | [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] (Notes / Limits — older, longer, less concise, still worked) | extracted (illustrative comparison only) |
| 16 | Why You Should Actually Do This | pp. 21–22 | — | [[Hormozi-Price-Raise-Play\|Hormozi — Price Raise Play]] (Strategic Implications — upside/downside lists) | extracted |
| 17 | Price Raise Checklist | p. 23 | — | [[Hormozi-Price-Raise-Play\|Hormozi — Price Raise Play]] (Practical Use checklist) | extracted |
| 18 | Appendix: The Price Raise Letter Template | pp. 24–25 | — | [[Hormozi-RAISE-Letter\|Hormozi — RAISE Letter]] (Practical Use — verbatim template) | extracted |

### Many-to-one mappings (documented)
- **p. 15 ("What to Do Next")** → contributes to both [[Hormozi-Price-Raise-Play|Price-Raise-Play]] (single-jump vs. stair-step rollout choice) and [[Hormozi-RAISE-Letter|RAISE-Letter]] (the stair-step discount mechanic that lives inside the Soften section).
- **pp. 4–5 ("Vicious vs. Virtuous Cycle")** → contributes to [[Hormozi-Price-Raise-Play|Price-Raise-Play]] as the operational extension of the principle. Principle itself remains canonical in [[../01-100M-Offers/Hormozi-Pricing-Power|Pricing Power]].

### One-to-many mappings
- **pp. 5–7 ("My Rules For Raising Prices")** → all 9 rules are folded into a single canonical note ([[Hormozi-Price-Raise-Rules|Price-Raise-Rules]]) rather than fragmented per rule. Each rule does not have enough independent retrieval value to justify its own note.

### Mapped to existing canonical notes in 01-100M-Offers (reuse, not duplication)
Price Raise reuses these concepts as inputs. Canonical home stays in `01-100M-Offers/`. Price Raise notes link out, not duplicate.

| Price Raise use | Canonical note (already extracted) |
|---|---|
| Pricing posture / virtuous cycle / race-to-the-bottom / Dan Kennedy quote | [[../01-100M-Offers/Hormozi-Pricing-Power\|Hormozi — Pricing Power]] |
| Value Equation behind "raise value to back the raise" (Invest section of letter) | [[../01-100M-Offers/Hormozi-Value-Equation\|Hormozi — Value Equation]] |
| Vanishing-discount mechanic as a softening lever (Soften section of letter) | [[../01-100M-Offers/Hormozi-Scarcity\|Hormozi — Scarcity]] / [[../01-100M-Offers/Hormozi-Urgency\|Hormozi — Urgency]] |

## Conventions
- Raw extract notes (when needed) live in this folder as `Hormozi-Price-Raise-Raw-<Section>.md` with `canonical: false`, `source_type: imported`. None created for this book — source distilled directly; provenance carried via `source_reference` frontmatter on each canonical note plus this map.
- Canonical framework notes live under `11-Price-Raise/` with the `Hormozi-` prefix, `canonical: true`, `source_type: derived`.

## Related
- [[00-Book-Home|Price Raise — Book Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]
- [[../01-100M-Offers/00-Book-Home|100M Offers — Book Home]]
- [[../01-100M-Offers/Hormozi-Pricing-Power|Hormozi — Pricing Power]]

## Extraction Status
- **Complete.** 18 sections mapped. 4 canonical notes extracted in this folder. 2 sections classified source-only (Trey narrative, table of contents). 3 reuse mappings to existing canonical notes in `01-100M-Offers/`. 0 raw extract notes required.

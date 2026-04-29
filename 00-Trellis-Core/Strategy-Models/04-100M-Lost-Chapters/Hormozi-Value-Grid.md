---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Lost Chapters — Section C: Back End: The Value Grid (pp. 69–73)"
sensitivity: internal
hub_role: leaf
book: 100M-Lost-Chapters
---

# Hormozi — Value Grid

## Parent
- [[00-Book-Home|100M Lost Chapters — Book Home]]

## Purpose
A diagnostic visualization that replaces the linear value-ladder/stair-step model with a 2D grid of prospects × offers. Lets you read 30D Cash, LTGP, CAC ceiling, and offer-mix economics directly off a single picture. Hormozi calls it "how I actually think about increasing LTV." Cut from `$100M Offers` as too conceptual.

## Core Idea
The standard "value ladder" depicts customers ascending price tiers in sequence (Offer 1 → 2 → 3 → 4). In practice, customers do not ascend linearly — they buy Offer 1 then skip to Offer 4, or skip 1 and 2 and buy 3 and 5, or buy multiple offers at the same price tier solving different needs. The grid handles all of this: rows are offers, columns are prospects, cells are buy/no-buy with revenue, and the totals row is the actual LTV-per-prospect.

The grid makes two things visual that the ladder hides: (1) **non-linear buying patterns**, and (2) **the absolute revenue from each offer** (so you can see which row matters and which is decorative).

## Framework / Structure

### What the grid contains
- **Rows** — the offers in your stack, top to bottom (front-end attraction → upsells → continuity).
- **Columns** — prospects, typically a representative cohort (e.g., 10 prospects from a single ad spend).
- **Cells** — whether that prospect bought that offer + revenue contribution.
- **Bottom totals row** — sum revenue per prospect, average revenue per prospect (= 30D Cash if you sum only the 30-day-billing rows; = LTGP if you sum all rows).

### What it tells you immediately
- **CAC ceiling** = total revenue ÷ prospects-needed-to-walk-in. (10 of 50 leads walked in for $600 total → break-even at $12/lead.)
- **30D Cash** = sum of revenue from offers billing within 30 days, ÷ prospects.
- **Real CAC ceiling after labor** = revenue minus the labor cost of working/closing leads. Hormozi's example: $600 revenue minus $600 labor → break-even at $0/lead. Most small businesses live here without realizing it.

### Two grids compared (Hormozi's example)

*Front-end-only business:*
- 10 prospects in, 8 take a trial, 3 convert to paid back-end → $600 total / 10 prospects = $60 per show, **30D Cash = $75**.

*Same business after stacking offers:*
- High-ticket offer with downsells, then upsells over the first 30 days → **30D Cash = $1,763**.
- ~14–15× revenue lift on the same prospect cohort. Without changing traffic, the second business can outspend the first by 15× per lead and remain just as profitable.

### How "no" prospects still generate revenue
The grid surfaces revenue from people who said no to the primary offer — because the business offered them a complementary wellness/lifestyle review and sold supplements at that review (the "Free with Alternate Revenue Stream" mechanic; see [[Hormozi-Upsell-Free-Alt-Revenue|that note]]). The grid is what makes this contribution visible. The ladder hides it as a "lost lead."

## Strategic Implications

- **The back end informs the front end.** Total revenue per prospect (read off the bottom row) is what you can spend on acquisition. A business with $1,763 / prospect can pay $1,500 / lead and still profit; a competitor at $75 / prospect cannot. That's the structural "outspend anyone on any platform" advantage.
- **Linearity is a fiction.** The ladder model implies prospects must climb tier 1 → tier 2 → tier 3. The grid shows real buying — fractal, non-sequential, multi-offer-same-tier. Designing a money model around a fictional sequence misses revenue.
- **Offer additions must be evaluated on the grid, not on intuition.** Adding an offer that one prospect takes for $50 may look exciting in isolation; on the grid it's one cell out of 100. Adding an offer that 70% take at $200 is a row that shifts the totals materially. The grid forces evaluation against the cohort, not the anecdote.
- **30D Cash dominates LTGP for cash flow.** The grid separates 30-day-billing rows from later rows visually. This is what links the value grid back to [[Hormozi-Customer-Financed-Acquisition|CFA]]: only the 30-day rows feed credit-card-float economics.
- **Consulting case (in-source).** The competitor making 70× less profit on the same vertical and same total sales had one offer with no upsell or continuity. Their grid was a single row. Same prospects, single revenue contribution per column, ~10× per-customer revenue gap, ~50% higher CAC.

## Practical Use

To build a value grid for a business:

1. **List every offer** the business has, ordered by where it sits in the buyer journey: attraction → up-front cash → upsell/downsell → continuity → repeat.
2. **Pick a cohort** — last month's actual prospects, or a representative 10/50/100.
3. **Mark the cells.** Cell value = price × take-rate (or actual revenue from that prospect for that offer). Be honest — if take-rate is 5% on a $1,000 offer, cell average is $50.
4. **Sum down (per offer)** to find which offers are doing the work and which are decorative.
5. **Sum across (per prospect)** and divide by prospect count → average revenue per prospect.
6. **Filter to 30-day rows** → 30D Cash. Filter to all rows → LTGP.
7. **Compare against CAC** to find the spend ceiling.

To improve the grid:
- Add rows that solve adjacent customer needs (see [[Hormozi-Offer-Stacking|Offer Stacking]] — Identify Adjacent Customer Needs).
- Add downsells under high-ticket rows so the "no" cells aren't empty.
- Add a "no sale sale" path so prospects who reject the front end still hit at least one revenue row.

## Notes / Limits
- The grid is a diagnostic, not a forecasting tool. Take rates change with traffic source, season, sales staff. Use it to spot structural gaps; don't use it to project quarterly revenue.
- The 14–15× revenue lift in the worked comparison is illustrative of *what's possible*, not a benchmark to expect. Realistic LTV uplift from offer stacking depends on the avatar and business type.
- Best paired with one-on-one sales (phone or in-person) where downsells can be improvised. Pure digital pages cannot do real-time downsells; the grid for a pure digital business has fewer responsive cells.
- The grid does not replace [[Hormozi-CFA-Three-Levers|CFA Three Levers]] — it visualizes what those levers compute, but doesn't replace the per-channel CAC discipline.

## Source Basis
- `$100M Lost Chapters`, "Back End: The Value Grid" (pp. 69–73) — Dan Kennedy rephrasing, $50k consulting day anecdote, ladder vs grid framing, two-grid comparison ($75 vs $1,763 30D Cash), 14–15× revenue lift, "no sale" generated-revenue mechanic.
- Author note: chapter cut from `$100M Offers` for being "too conceptual," though Hormozi states "It's how I actually think about increasing LTV."
- Indexed in [[Hormozi-100M-Lost-Chapters-Source-Map|100M Lost Chapters — Source Map]].

## Related
- [[00-Book-Home|100M Lost Chapters — Book Home]]
- [[Hormozi-100M-Lost-Chapters-Source-Map|100M Lost Chapters — Source Map]]
- [[Hormozi-Offer-Stacking|Hormozi — Offer Stacking]] — the construction process the grid visualizes
- [[Hormozi-Customer-Financed-Acquisition|Hormozi — Customer Financed Acquisition (CFA)]] — 30D Cash sourced from the 30-day rows of the grid
- [[Hormozi-CFA-Three-Levers|Hormozi — CFA Three Levers]] — math behind the totals row
- [[Hormozi-Upsell-Free-Alt-Revenue|Hormozi — Upsell: Free with Alternate Revenue Stream]] — how "no" cells become revenue rows
- [[Hormozi-Home|Hormozi Home]]

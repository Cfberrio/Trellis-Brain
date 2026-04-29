---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Lifetime Value — '#1 Increase Prices' (pp. 8–9), 'Pro Tip: Start Low Then Go Up' (p. 9)"
sensitivity: internal
hub_role: leaf
book: Lifetime-Value
---

# Hormozi — Price Testing Method

## Parent
- [[00-Book-Home|Lifetime Value — Book Home]]

## Purpose
Operating procedure for **Lever 1 of the [[Hormozi-Crazy-Eight|Crazy Eight]]** — raise prices on the same product. Distinct from [[../01-100M-Offers/Hormozi-Pricing-Power|Pricing Power]], which is the *strategic posture* (premium pricing, commodity trap, virtuous cycle); this note is the *operational test loop* (how to raise price, by how much, how often, what to measure, when to stop). Hormozi runs price tests more frequently than any other test in business; this is the procedure he runs.

## Core Idea
Pricing affects gross profit more than any other lever. A 10%-margin business that raises price 20% with sales held flat does not grow 20% — it triples. Every price dollar drops to gross profit. The asymmetry is so large that frequency-of-testing, not size-of-test, is the dominant variable. The operator's job is to nudge price up continuously and watch the conversion-rate × LTGP product, not to find a "right price" in one shot.

> "The only thing more expensive than testing price is not testing price at all and having a business that's under-monetized for life."

## Framework / Structure

### The Test Objective
Maximize:
```
Conversion Rate × Lifetime Gross Profit per customer
```
Not revenue. Not unit volume. The price that produces the highest product of those two terms is the profit-maximizing price. Selling more units at lower margin is *worse* than selling fewer at higher margin if the LTGP gap dominates.

### The Operating Loop
1. **Set baseline.** Record current price, current conversion rate, current LTGP.
2. **Set the new price.** Inform sales / update site / change copy.
3. **Compute the break-even conversion rate.** The conversion rate at the new price below which you'd be making *less* gross profit than at the old price. Formula:
   ```
   Break-even Conv Rate = (Old Price × Old Conv Rate) / New Price
   ```
   (Approximation when COGS is small relative to price; otherwise compute on gross profit per unit.)
4. **Track conversion at the new price.** If new conversion rate > break-even, the price hike is a winner.
5. **Test again.** Keep nudging price up until the *Conv × LTGP* product drops. That's the ceiling.

### Test Frequency
**Every quarter.** Hormozi cites a ProfitWell research finding of a tight relationship between company profitability and frequency of price testing. Quarterly is the documented cadence; companies that test less often under-monetize.

### Step-Size — "Start Low, Then Go Up"
**Nudge +20% every 10 sales** until conversion drops dramatically. Then revert one step to the sweet spot.

Why "start low":
- You need actual sales to verify demand exists at all.
- Early sales surface delivery friction ("run water through the pipes") before scaling.
- Price-up has lower regret cost than price-down (you can give early customers a refund or bonus to true up; you can't claw back revenue from underpricing for years).

### Recovery Rules When You Overshoot
If a price test runs too high too long:
- **Bonus stacking.** Add bonuses to customers who paid the high price. Equalizes perceived value without setting a discount precedent.
- **Refund the difference.** Cleanest when individual customers are upset enough to ask. More expensive than bonuses but eliminates churn risk on the affected cohort.

Hormozi has used both. The cost of these recovery moves is small versus the years of profit recovered by finding the new ceiling.

## Strategic Implications

- **Price testing is a process, not an event.** The operator who tests once at incorporation never tests again is the operator under-monetizing for life. The price ceiling moves as the business gets better; the test must move with it.
- **Conversion × LTGP, never revenue.** Operators optimizing on revenue will systematically under-price because revenue rewards volume; gross profit rewards price. The LTGP-anchored test is the only one that actually maximizes the bottom line.
- **The break-even conversion rate is the gate, not the goal.** Beating break-even means the test won; staying *near* break-even means you've hit the ceiling and should revert. The operator who keeps pushing past the break-even point starts destroying total gross profit.
- **Frequency dominates magnitude.** A 5%/quarter test cadence beats a 20% one-shot test, because the loop captures market drift, value-build improvements, and demand-curve shape in a way a single test can't.
- **Doubling price as a diagnostic.** Hormozi cites buying a company and *doubling* the price as the only intervention — and tripling the business. This is an outlier case that worked because the underlying offer was severely underpriced. The procedure above is for ongoing optimization; the doubling move is the one-shot for known-underpriced acquisitions.

## Practical Use

**Quarterly price-test SOP.**

| Step | Action | Output |
|---|---|---|
| 1 | Pull last quarter's price, units sold, conversion rate, LTGP | Baseline metrics |
| 2 | Compute current Conv × LTGP product | Baseline target |
| 3 | Raise price +20% (or +10% in fragile markets) | New price live |
| 4 | Compute break-even conv rate | Pass/fail threshold |
| 5 | Run for ≥10 sales or ≥4 weeks (whichever first) | Test data |
| 6 | If conv rate > break-even AND Conv × LTGP > baseline → keep, schedule next test next quarter | Permanent price change |
| 7 | If conv rate < break-even OR Conv × LTGP < baseline → revert one step | Confirmed ceiling |
| 8 | Bonus-stack or refund any over-priced cohort if needed | Cohort goodwill maintained |

**Pre-launch pricing (new offer, no data).** Start *below* your gut price. Sell to ~10 customers, observe conversion. Raise +20%. Repeat. The first 30 sales reveal the demand curve at no cost — the operator who launches at a guess-price either over-shoots and churns out, or under-shoots and never recovers the margin.

**Sales-call price test.** Brief the sales team explicitly that the price moved. Track close rate at the new price separately from any other shifts. Don't run a price test concurrently with a product change — you won't be able to attribute the conversion shift.

## Notes / Limits

- The +20%/10-sales nudge is Hormozi's heuristic, not a law. In B2B with long sales cycles, the cadence stretches; in transactional retail, the nudge can be smaller and faster.
- Conversion rate × LTGP requires the LTGP estimate to be roughly right. Use [[../04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers|CFA Three Levers]] for the calculation; fragile LTGP estimates produce fragile pricing decisions.
- "Test price every quarter" assumes a stable product. Concurrent product, audience, or positioning changes confound the test.
- Bonus-stacking as recovery only works if the bonuses are genuinely valuable and not perceived as a face-saving move. If they're junk, the cohort still churns.
- This note is the operational layer. The strategic question — "should we be premium-priced at all?" — belongs to [[../01-100M-Offers/Hormozi-Pricing-Power|Pricing Power]].

## Source Basis
- *$100M Playbook: Lifetime Value*, "#1 Increase Prices" (pp. 8–9) — margin-leverage math (10% × 20% = 3×); Conv × LTGP optimization rule; quarterly testing cadence; ProfitWell relationship between test frequency and profitability; "doubled the price, tripled the business" acquisition example.
- *Lifetime Value*, "Pro Tip: Start Low Then Go Up" (p. 9) — +20% per 10 sales nudge rule; bonus / refund recovery moves for over-shot tests; "the only thing more expensive than testing price is not testing price at all" framing.
- Indexed in [[Hormozi-Lifetime-Value-Source-Map|Lifetime Value — Source Map]].

## Related
- [[Hormozi-Crazy-Eight|Hormozi — The Crazy Eight]] — parent framework (Lever 1)
- [[Hormozi-Cost-Reduction-Levers|Hormozi — Cost Reduction Levers]] — companion margin lever (Lever 2)
- [[../01-100M-Offers/Hormozi-Pricing-Power|Hormozi — Pricing Power]] — strategic posture this method operationalizes
- [[../04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers|Hormozi — CFA Three Levers]] — LTGP math the test depends on
- [[00-Book-Home|Lifetime Value — Book Home]]
- [[Hormozi-Lifetime-Value-Source-Map|Lifetime Value — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]

---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Price Raise — 'How To Pick Your Price' (pp. 7–9)"
sensitivity: internal
hub_role: leaf
book: Price-Raise
---

# Hormozi — Price Test Math

## Parent
- [[00-Book-Home|Price Raise — Book Home]]

## Purpose
Quantitative decision tool for choosing the profit-maximizing price. Models the trade-off between price, conversion rate, churn, LTV, and total return per fixed traffic. Used to identify the new price *before* it is rolled out to the existing base via the [[Hormozi-RAISE-Letter|RAISE Letter]]. Operationalizes Rule 10 ("Do the math") in [[Hormozi-Price-Raise-Rules|Price Raise Rules]] and the test-on-new-customers gate in Rule 6.

## Core Idea
The best price is **the price that makes the most money** — not the highest price, not the average market price, and not the price the operator is comfortable with. Pricing is a multivariable function of conversion rate, churn rate, and LTV — and the relationships between price and those variables are *not proportional*. Raising price erodes conversion and churn, but rarely in proportion to the price change.

The corollary: a price raise can lose customers and still make more money. A price raise can also fail to raise enough revenue to offset its conversion and churn cost. The only way to know which is which is to model it.

## Framework / Structure

### The model
Price is one input. Four downstream variables move with it:

| Variable | Definition | How it usually moves with a price increase |
|---|---|---|
| **Clicks** | Traffic to the offer — fixed for a given test period | Constant (held fixed for the comparison) |
| **Conversion rate** | % of clicks that become buyers | **Drops** as price rises |
| **Churn** | % of subscribers who cancel each period | **Rises** as price rises (sometimes only at large jumps) |
| **LTV** | Lifetime value per customer | **Rises** as price rises (because price × duration is the dominant term, even when churn rises) |

Total return per fixed traffic = `Clicks × Conv Rate × LTV`. Compare across price points.

### Worked example from the source
Hormozi's three-row chart, reproduced exactly:

| Price | Clicks | Conv Rate | Sales | Churn | LTV | Total Return | Difference |
|---|---|---|---|---|---|---|---|
| $10 | 100 | 5% | 5 | 10% | $100 | $500 | — |
| $20 | 100 | 4% | 4 | 10% | $200 | $800 | +60% |
| $100 | 100 | 2% | 2 | 33% | $300 | $600 | +20% |

Reading the table:

- **$10 baseline.** 100 clicks → 5% convert → 5 sales. 10% monthly churn → 10-month average customer lifespan → $100 LTV. Total return: 5 × $100 = **$500**.
- **$20 (2× price).** Conversion drops to 4% (5 → 4 sales). Churn unchanged at 10% → LTV doubles to $200. Total return: 4 × $200 = **$800** — a **60%** increase over baseline despite losing one customer per 100 clicks.
- **$100 (10× price).** Conversion drops to 2% (5 → 2 sales). Churn rises to 33% — average lifespan compresses to ~3 months → LTV = $300. Total return: 2 × $300 = **$600**. Better than $10 baseline (+20%), but worse than the $20 price point.

The optimal price in this dataset is $20 (or somewhere near it), not the highest price tested.

### The decision rule
1. **Total return per cohort goes up** under the new price → the raise is profitable. Roll out.
2. **Total return goes down** under the new price → the raise is too high or value is too thin. Test a different price between baseline and the failed point.
3. **Total return goes up but less than expected** → there is likely a more profitable price point between the tested points. Test the interpolated range.

In the worked example, the next test would be **$39–$59** (between $20 and $100), because the data suggests the optimum is somewhere above $20 but well below $100.

### What the math actually proves
The chart demonstrates one structural fact: **conversion rate and churn rate both suffer as prices go up — but not always proportionally to the price increase**. As long as the LTV gain exceeds the conversion loss × churn cost, the raise increases total return. If the price doubles and conversion drops less than 50%, the raise is profitable. If conversion drops more than 50%, the raise is unprofitable at that price point.

Bottom line: **if you can double your price and close 20% fewer deals, with all else staying the same, you should do it.** That is exactly the relationship between $10 and $20 in the chart.

### How to actually test
The least-risky way to test is on **new customers** (per [[Hormozi-Price-Raise-Rules|Rule 6]]). They have no reference price; they see the new price as the price. Run the new price for long enough to gather meaningful conversion and churn data:
- Conversion can be observed within days/weeks depending on traffic.
- Churn requires at least one billing cycle, ideally two, to see whether the new price's churn pattern stabilizes.

Once new-customer data shows the new price beats the old price on total return, roll out to the existing base via the [[Hormozi-RAISE-Letter|RAISE Letter]].

## Strategic Implications

- **Pricing is a search problem, not a guess.** The right price is found by testing prices at intervals and reading the total-return curve. Operators who skip this step and "pick a number that feels right" leave money on the table on either side — too low (vicious cycle) or too high (broken funnel).
- **The optimum is rarely the highest price tested.** The 10× ($100) row in the example proves the operator's intuition wrong: bigger raises don't always mean bigger profits. Beyond a point, conversion and churn losses outweigh LTV gains.
- **Churn dynamics matter more than conversion dynamics.** Conversion is a one-time cost per cohort. Churn is a recurring cost. A price that holds churn flat (or even slightly reduces it, because higher-paying customers are stickier) compounds; a price that triples churn for a 3× price multiplier breaks even at best.
- **The math is the floor, not the ceiling.** A correctly priced offer pulls higher-value customers, which produces second-order effects (better referrals, better testimonials, lower demandingness) that the chart's static variables don't capture. The chart is the conservative case.
- **Without the test, the raise is a faith move.** Operators who skip testing and roll out a raise across the existing base are betting their churn and conversion intuitions are correct — and the source's case studies suggest those intuitions are usually wrong, in both directions.

## Practical Use

Worksheet for pricing a raise:

1. **Pull the baseline.** Measure (or estimate from existing data): clicks per period, conversion rate, churn rate, and LTV at the current price.
2. **Pick a candidate price.** Start with 2× current price (the $10 → $20 move in the example). This is the conservative starting test.
3. **Run the test.** Show the new price to a defined cohort of new customers (a date-cutoff cohort works fine). Measure conversion immediately, churn at one and two billing cycles.
4. **Compute total return.** `Clicks × New Conv Rate × New LTV`. Compare to baseline.
5. **Iterate.**
    - If new total return > baseline by a healthy margin → test a higher price (e.g., 3×).
    - If new total return ≈ baseline → optimum is near current price; test slightly lower or hold.
    - If new total return < baseline → roll back to baseline and test a smaller raise (1.5× instead of 2×).
6. **Search the gap.** Once two price points are known (one better, one worse), the optimum is between them. Test 1–2 intermediate prices.
7. **Lock the price** at the highest tested point that still beats baseline. This becomes the new price for both new customers and (after the RAISE letter) the existing base.

## Notes / Limits

- **Recurring vs. one-time products.** The chart assumes a recurring/subscription product (LTV depends on churn). For one-time-purchase products, churn is irrelevant and LTV = price. The decision simplifies to: total return = `Clicks × Conv Rate × Price`. Conversion still matters; churn drops out.
- **Floor on traffic.** Conversion-rate measurements are noisy at low click volumes. With very small traffic, the test cohort needs to be wider (more time, more channels) to produce a meaningful signal.
- **Churn lag.** Churn changes don't show up immediately. A raise tested for two weeks captures conversion well but tells you almost nothing about churn. Hold the test long enough to cover at least one full billing cycle, ideally two.
- **The chart's specific numbers are illustrative.** The 5% / 4% / 2% conversion rates and 10% / 10% / 33% churn rates are not universal coefficients. They show the shape of the relationship; the actual elasticity is per-business and must be measured.

## Source Basis
- *$100M Playbook: Price Raise*, "How To Pick Your Price" (pp. 7–9) — full 3-row table; the $10 / $20 / $100 worked example; the next-test-range guidance ($39–$59); the 20% / 50% conversion-loss decision rules; the test-on-new-customers gate.
- Indexed in [[Hormozi-Price-Raise-Source-Map|Price Raise — Source Map]].

## Related
- [[Hormozi-Price-Raise-Play|Hormozi — Price Raise Play]]
- [[Hormozi-Price-Raise-Rules|Hormozi — Price Raise Rules]]
- [[Hormozi-RAISE-Letter|Hormozi — RAISE Letter]]
- [[../01-100M-Offers/Hormozi-Pricing-Power|Hormozi — Pricing Power]]
- [[../01-100M-Offers/Hormozi-Value-Equation|Hormozi — Value Equation]]
- [[00-Book-Home|Price Raise — Book Home]]
- [[Hormozi-Price-Raise-Source-Map|Price Raise — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]

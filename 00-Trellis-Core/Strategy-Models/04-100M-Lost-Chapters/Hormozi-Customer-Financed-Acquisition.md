---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Lost Chapters — Section B: The Expensive Customer Problem (intro pp. 37–38, PPD/30D Cash worked examples pp. 53–61, Levels of CFA pp. 63–65)"
sensitivity: internal
hub_role: leaf
book: 100M-Lost-Chapters
---

# Hormozi — Customer Financed Acquisition (CFA)

## Parent
- [[00-Book-Home|100M Lost Chapters — Book Home]]

## Purpose
Defines Customer-Financed Acquisition: the condition under which a business uses customer cash (not loans, savings, or investors) to fund customer acquisition. Establishes the 30-day-cash threshold, the three CFA levels, and the compounding behavior that removes "cash to get customers" as a growth bottleneck. The conceptual core of `$100M Money Models` — Hormozi cut these chapters from that book as "too conceptual" but kept them here for readers who want the underlying logic.

## Core Idea
A dollar today is worth more than a dollar tomorrow. If a customer's first 30 days of gross profit pays for the next customer, you compound; if it pays for two more customers, you double monthly. CFA's purpose is not just profit — it's removing **cash availability** as a constraint, so the only remaining bottleneck is operations.

The 30-day window is load-bearing: 30 days is the amount of interest-free credit any business can get via a credit card. Float new-customer CAC on the card, collect 30-day GP, pay the card off, repeat. You finance growth with customers, not lenders.

## Framework / Structure

### The Equation
- **Survival floor**: `30D GP > CAC` — break even on the customer within the credit cycle.
- **Hormozi's working minimum**: `30D GP > 2× CAC` — every customer pays for two more.

Where:
- **30D GP** = gross profit collected from a new customer in their first 30 days (price minus fulfillment cost, summed across upsells/continuity that bill in the window).
- **CAC** = total cost to acquire that customer (ads, payroll, sales, software, commissions). See [[Hormozi-CFA-Three-Levers|CFA Three Levers]] for calculation.

### The Three Levels of CFA

Each level reflects how much of growth the customer pays for.

**Level 1 — `30D GP < CAC`**
You eventually come out ahead but the gap is funded by life savings, loans, lines of credit. Hormozi: "speaking from lots of experience… it sucks." Many big businesses live here, but they have capital. Bootstrapped businesses should avoid this level.

**Level 2 — `30D GP = CAC` (in 30 days)**
Credit-card budget *is* the marketing budget. Float CAC on the card, GP arrives before the bill, pay off, refloat. Customer count is capped by credit limit. Expand by paying early, raising the limit, or adding cards. Stable but bounded.

**Level 3 — `30D GP > 2× CAC` (in 30 days)**
Customers pay for themselves *and* the next customer. From here, all customers are effectively free; cash is no longer the constraint. This is where Hormozi has scaled all his businesses. First year of Gym Launch ran 100× — $100k spend → $10M return. The constraint shifted to operations, not acquisition.

### Compounding at Level 3 (Hormozi's 12-Month Doubling Table)

If every dollar of extra GP is reinvested into acquisition at Level 3:

| Month | New Customers | Total Customers |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 4 | 7 |
| 4 | 8 | 15 |
| 5 | 16 | 31 |
| 6 | 32 | 63 |
| 7 | 64 | 127 |
| 8 | 128 | 255 |
| 9 | 256 | 511 |
| 10 | 512 | 1,023 |
| 11 | 1,024 | 2,047 |
| 12 | 2,048 | 4,095 |

One customer paid for; 4,094 financed by customer GP. (Source PDF lists month-8 cumulative as 256; doubling implies 255 — the table preserves the source numbers as printed.)

### 30D Cash — Hormozi's most prized metric
*30D Cash = gross profit extracted from a new customer in their first 30 days.* Distinct from LTGP (whole lifetime) and from 30-day revenue (no fulfillment cost subtracted). The single number that gates whether Level 2 / Level 3 is achievable on a credit-card budget.

### Worked Example — "Normal" Lemonade Business (Level 1 territory)
- $10/mo subscription, 80% GM ($8 GP/mo), 5-month average tenure → $40 LTGP.
- CAC = $20. Payback period = 2 months and 1 week.
- Day 0: -$20. Day 30: -$12. Day 60: -$4. Day 90: +$4 (first profit). Day 150: +$20 then customer cancels.
- Doubled investment in 5 months — but rent/software/owner pay still come from the same $20. Hard to grow.

### Worked Example — "Wonderful" Lemonade Business (Level 3 territory)
- Same product/margin. CAC = $1, payback = 7 days.
- Day 0: -$1 → Day 7: +$7 → Day 14: +$56 (7 customers, $8 GP each) → Day 22: +$105 (7 more customers from $7 reinvested) → Day 30: +$105 → Day 37–51: renewals stack to +$225.
- Total marketing cash spent across the cycle: **$1**. Everything else is house money. Casino analogy: bet $1, win $8, pocket the original $1, gamble the $7.

## Strategic Implications

- **Operations becomes the bottleneck, not cash.** Once Level 3 lands, the limit is service capacity. That's the *good* problem this framework engineers.
- **Credit card as float instrument.** The 30-day window is not arbitrary — it matches interest-free credit-card terms. CFA design implicitly accepts that constraint and works inside it.
- **Why most small businesses are Level 1.** Median small-business owner makes $72,489/year (Payscale, cited). At that return for that risk, Uber driving is a better risk-adjusted job. The reason owners stay: the *promise* of more. CFA is the mechanism that makes "more" mathematically reachable rather than aspirational.
- **CFA is downstream of LTGP and CAC, but speed is the differentiator.** Two businesses with identical LTGP and CAC differ by payback period. Doubling cash in 1 month vs 3 months compounds quarterly to 4× faster growth (2³ = 8× vs 2× in three months).
- **CFA changes who finances growth.** The chapter author note frames it directly: *"This process is intended for businesses to get financing from their clients rather than outside investors. If you apply the concepts, you will have no need for outside capital."*

## Practical Use

To diagnose where a business sits on CFA:

1. Compute true CAC (per [[Hormozi-CFA-Three-Levers|CFA Three Levers]] — including all sales, payroll, ads, software).
2. Compute 30D Cash — sum of GP from initial sale + any upsells/continuity that bill within 30 days, minus fulfillment cost.
3. Classify:
   - 30D Cash < CAC → Level 1. Either find capital or restructure offers/upsells to push 30D Cash up.
   - 30D Cash ≈ CAC → Level 2. Stable; growth gated by credit limit. Add an upsell or bundle to push toward Level 3.
   - 30D Cash > 2× CAC → Level 3. Cash is no longer the constraint. Solve operations.
4. Lever priorities (in order): raise 30D Cash via stacked offers (see [[Hormozi-Offer-Stacking|Offer Stacking]]) → lower CAC via avatar tightening (see [[Hormozi-Avatar-Selection|Avatar Selection]]) and channel optimization → compress payback period via faster billing cadence and earlier upsells.

To reach Level 3 from Level 2:
- Add an immediate upsell to the initial transaction (see [[Hormozi-Upsell-Free-Alt-Revenue|Free with Alternate Revenue Stream]] for one mechanism).
- Add a discount + one-time fee structure to inject cash up front (see [[Hormozi-Continuity-Discount-Plus-Fee|Discount + One-Time Fee]]).
- Compress the time-to-first-payment. Revenue billed Day 7 funds Day 8 acquisition.

## Notes / Limits
- The 12-month doubling table assumes 100% reinvestment of GP into acquisition and unlimited operational capacity. Real businesses cap on service capacity well before month 12.
- Level 3 requires the same "minimum standard" of 2× — Hormozi's first Gym Launch year ran 100× return, far outside this floor. Two-times is the threshold, not the goal.
- Sales/operations/cash-collection cycles must support a true 30-day GP. B2B businesses with net-60 or net-90 invoicing functionally cannot run Level 2 on credit-card float.
- "30D Cash" definition is gross-profit-based. Net-profit thresholds are different and outside this framework's scope (CFA assumes fixed costs are covered separately).
- Source PDF cumulative-customer figures in the doubling table contain a minor arithmetic quirk at month 8 (printed 256 vs implied 255); the framework's compounding logic is unaffected.

## Source Basis
- `$100M Lost Chapters`, Section B intro / "Customer Financed Acquisition" (pp. 37–38) — definition, "30 Day GP > CAC" / "30D GP > 2× CAC" thresholds.
- `$100M Lost Chapters`, "Payback Period = PPD" (pp. 53–61) — 30D Cash definition, Normal vs Wonderful Lemonade worked examples, casino analogy.
- `$100M Lost Chapters`, "Levels of Customer Financed Acquisition" (pp. 63–65) — three levels, 12-month doubling table, Acquisition Masters framing, Payscale median small-business benchmark.
- Author notes: chapters cut from final draft of `$100M Money Models` for being "too conceptual."
- Indexed in [[Hormozi-100M-Lost-Chapters-Source-Map|100M Lost Chapters — Source Map]].

## Related
- [[00-Book-Home|100M Lost Chapters — Book Home]]
- [[Hormozi-100M-Lost-Chapters-Source-Map|100M Lost Chapters — Source Map]]
- [[Hormozi-CFA-Three-Levers|Hormozi — CFA Three Levers]] — calculation method for CAC, LTGP, PPD
- [[Hormozi-Value-Grid|Hormozi — Value Grid]] — visualization of LTV stacking that drives CFA
- [[Hormozi-Offer-Stacking|Hormozi — Offer Stacking]] — primary lever to push 30D Cash up
- [[Hormozi-Promotion-Wrappers|Hormozi — Promotion Wrappers]] — wrapper choice constrains 30D Cash
- [[Hormozi-Home|Hormozi Home]]

---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Pricing — 'Three Models Of Pricing' (pp. 18–20); 'Three Metrics To Determine Value-Driven Pricing' incl. price-test table (pp. 20–21)"
sensitivity: internal
hub_role: leaf
book: Pricing
---

# Hormozi — Value-Driven Pricing Model

## Parent
- [[00-Book-Home|Pricing — Book Home]]

## Purpose
Defines the three pricing models an operator can use, ranks them, and gives a measurement method for actually finding the value-driven price empirically. Distinct from [[../01-100M-Offers/Hormozi-Pricing-Power|Pricing Power]] (which is the *posture* — why premium pricing works structurally) — this note is the *operating model and measurement method* for choosing a price level.

## Core Idea
Most operators set price by looking at competitors. That imports the competitors' economics, which are usually broken. The right pricing model is **value-based pricing**: price set by what the customer is willing to pay for the value they receive — not by cost-plus-markup and not by competitor average. Value-based pricing is the only model that allows price to rise as you make the product more valuable to customers, and the only model that forces you to keep talking to customers to find out what they want.

To find the value-driven price empirically, run a small structured price test on three variables: conversion rate, churn, and lifetime gross profit. The "perfect" price is the one that **maximizes total return per click** (or per lead), not the one that maximizes new customers or first-purchase revenue.

## Framework / Structure

### The Three Pricing Models

| Model | Definition | Pros | Cons |
|---|---|---|---|
| **Cost-plus** | Costs + arbitrary markup. | Simple. Covers cost. | Ignores willingness to pay (WTP). Costs change. Costs are unknown to the customer and irrelevant to them. Misses upside on customers who would have paid more. |
| **Competitor-based** | Average of what competitors charge. | Simple. Possibly closer to market WTP. | "You're a copycat." Strategy is built on someone else's business and customers, not yours. Most copied competitors are broke — copying them imports their economics. |
| **Value-based** | What the customer is willing to pay (WTP) for the value delivered. | Allows price to rise as value rises. Forces customer conversation. Lets you charge 2–5× market rate when product is genuinely better. New customers may pay more than current ones. Customer-research compounds. | Focuses on per-customer value over total customer count. Requires more thinking and operational work. Different type of work than most operators are used to. |

The book's stated rule: **value-based pricing is where you want to be.** The other two are listed primarily to be ruled out.

### The Three Metrics for Finding the Value-Driven Price
When testing a price level empirically, observe three measurable outputs:

1. **Conversion rate** at the current price — how many people buy.
2. **Churn / repurchase rate** at the current price — how many times they buy or how long they stay.
3. **Lifetime value** (specifically lifetime gross profit) at the current price — what each buyer is worth.

For non-luxury goods, raising price typically reduces both conversion rate and repurchase rate. The question is *by how much* relative to the price lift.

### The Price-Test Table
Hormozi's working format for documenting a price test:

| Price | Clicks | Conv Rate | Sales | Churn | LTV | Total Return | Difference |
|---|---|---|---|---|---|---|---|
| $10 | 100 | 5% | 5 | 10% | $100 | $500 | — |
| $20 | 100 | 4% | 4 | 10% | $200 | $800 | +60% |
| $100 | 100 | 2% | 2 | 33% | $300 | $600 | +20% |

Read by the **Total Return** column, not by Conv Rate, Sales, or even LTV in isolation. In this example $20 wins: it produces the highest total return per 100 clicks ($800), even though it produces fewer sales than $10 and lower LTV per buyer than $100.

The "perfect" price (the rule, stated explicitly): **the price that makes you the most money — not the one that gets you the most customers, and not the one that maximizes the first purchase.**

### Why "perfect" is total return, not LTV per customer
LTV per customer optimizes a single buyer; total return optimizes the sale of fixed-cost traffic. For the same advertising spend (same clicks/leads), the price level that produces the highest total return is the one that converts that traffic into the most lifetime gross profit — which is the actual constraint for a paid-acquisition business.

For organic-traffic businesses, the same logic holds with a different denominator (per visitor, per lead, per consultation slot).

## Strategic Implications

- **Cost-plus and competitor-based pricing are diagnostic flags, not strategies.** If an operator's pricing rationale is "we cover our costs plus 30%" or "we're at the market average," they have not made a pricing decision — they've outsourced it. Re-anchor to value-based reasoning before any tactical pricing change.
- **The exercise of testing price is itself the lever.** Profitwell data (carried in [[Hormozi-Pricing-Profit-Leverage|Pricing-Profit-Leverage]]) shows companies that test pricing more frequently make more profit and grow faster. The price-test table is the operating tool for doing this.
- **Total return ≠ max LTV.** Operators who chase the highest LTV-per-customer often overprice, lose volume, and end up with lower total return on the same traffic. Operators who chase the lowest churn often underprice for the same reason. Total return per click is the integrating metric.
- **Value-based pricing is iterative, not one-shot.** As the product gets better (more value), value-based price moves up. This forces a feedback loop: customer conversation → product improvement → price increase. Cost-plus and competitor pricing have no such loop.
- **WTP is asymmetric across customer segments.** Different buyer avatars within the same business commonly have 5–10× different WTP (covered in detail in [[Hormozi-Pricing-Rules|Pricing Rules]]). One value-based price across them under-monetizes the high-WTP segment. Multi-tier value pricing is the operationalization.
- **Pricing follows value, not vice versa.** Value-based price increases without underlying value increases produce churn. Pair every meaningful price lift with a documented value lift (see [[Hormozi-Pricing-Rules|Pricing Rules]] — "raising prices = raising value").

## Practical Use

To choose or revise a price using the value-driven method:

1. **Rule out the wrong models first.** Confirm pricing is not currently set by (a) cost-plus or (b) competitor average. If either is true, the next step is the price test, not a small adjustment to the existing logic.
2. **Define the test denominator.** Per 100 clicks, per 100 leads, per 100 consult slots — whatever the unit of fixed-cost traffic is for the business.
3. **Pick three price levels.** A baseline (current price), one ~2× current, and one materially higher (5–10×). Wide spreads beat narrow ones — the goal is to find the *shape* of the response curve, not to fine-tune.
4. **Run the test long enough to observe churn at each level.** Conversion is fast; churn takes weeks to months. A test that captures only conversion under-measures total return.
5. **Build the price-test table.** Conv rate, churn, LTV (lifetime gross profit), total return per 100 units of traffic. Compute the Difference column relative to baseline.
6. **Pick the price that maximizes Total Return**, unless a deliberate short-term strategy (e.g., land grab, capacity-constrained business) overrides it.
7. **Re-test on a cadence.** Annually minimum. Quarterly preferred. Each test compounds the data set on customer WTP.
8. **Pair price changes with value changes.** When raising price materially, document the corresponding value lift (delivery improvement, expanded scope, faster outcome) so the price-to-value gap stays positive — see [[../01-100M-Offers/Hormozi-Pricing-Power|Pricing Power]].

For multi-segment businesses: run a separate price-test table per buyer avatar. If WTP differs by 3× or more between segments, the operating answer is multi-tier pricing, not one weighted-average price.

## Notes / Limits

- "Conv rate, churn, LTV" assumes the business measures these. Operators without basic funnel and churn measurement need that infrastructure before the price test produces clean signal — see [[../Hormozi-Linking-Contract|Hormozi Linking Contract]] convention on measurement-first work.
- The price-test table is a measurement tool, not a pricing oracle. It tells you which of the *prices you tested* maximized return — not what price you should have tested. Iteration is required.
- "Different types of work" caveat: value-based pricing requires sustained customer-conversation discipline. Operators without that habit will set a value-based price once and then drift back to cost-plus reasoning the next time costs change. Build a calendar trigger.
- The "perfect price" framing is rhetorical — there is no static optimum, because value, costs, competitors, and WTP all move. The framework is a method for re-finding the optimum on cadence.
- Luxury and Veblen goods invert parts of the WTP logic (higher price increases demand). The value-based model still applies; the response curve looks different. Hormozi flags this explicitly under the Round Up play (luxury items typically end on round 0/5, not .99).

## Source Basis
- *$100M Playbook: Pricing*, "Three Models Of Pricing" (pp. 18–20) — definitions and pros/cons of cost-plus, competitor-based, and value-based pricing; explicit ruling that value-based is the desired model.
- *Pricing*, "Three Metrics To Determine Value-Driven Pricing" (pp. 20–21) — conversion rate, churn, LTV as the three measured variables; the price-test table; the "perfect price = the one that makes you the most money, not the one that gets you the most customers" rule; "Total Return" column as the integrating metric.
- Indexed in [[Hormozi-Pricing-Source-Map|Pricing — Source Map]].

## Related
- [[Hormozi-Pricing-Profit-Leverage|Hormozi — Pricing Profit Leverage]]
- [[Hormozi-Pricing-Rules|Hormozi — Pricing Rules]]
- [[Hormozi-Instant-Profit-Pricing-Plays|Hormozi — Instant Profit Pricing Plays]]
- [[../01-100M-Offers/Hormozi-Pricing-Power|Hormozi — Pricing Power]]
- [[../01-100M-Offers/Hormozi-Value-Equation|Hormozi — Value Equation]]
- [[00-Book-Home|Pricing — Book Home]]
- [[Hormozi-Pricing-Source-Map|Pricing — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]

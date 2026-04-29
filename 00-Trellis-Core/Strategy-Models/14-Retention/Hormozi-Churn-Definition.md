---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Retention — 'What Is Churn?' (p. 9); 'Price, Value, And Churn' (pp. 10–12)"
sensitivity: internal
hub_role: leaf
book: Retention
---

# Hormozi — Churn Definition

## Parent
- [[00-Book-Home|Retention — Book Home]]

## Purpose
Defines churn precisely so the rest of the Retention canon can be reasoned about without ambiguity. Establishes the price–value–churn relationship that governs which lever to pull first when retention is weak (raise value vs. lower price), and provides the price–conversion–LTV evidence table that justifies running price tests with churn as a co-output, not just conversion.

## Core Idea
> "Price is what you pay. Value is what you get." — Buffett, restated by Hormozi.
>
> Churn = customers who leave a fixed cohort over a fixed window, divided by that starting cohort. If perceived value > price, customers stay; if perceived price > value, they leave.

Two things operators get wrong:
1. They mix new customers into the denominator. They do not. Churn is computed on the **starting pool only**.
2. They optimize price without watching churn. Price affects conversion *and* churn — usually in opposite directions to revenue. The right price is the one that maximizes total return (sales × LTV), not the one with the lowest churn.

## Framework / Structure

### Definition (with worked example)
- Take the customer count at the start of the period (`P0`).
- Take the customer count at the end of the period from that same starting cohort only (`P1`).
- `Churn % = (P0 − P1) / P0`.
- `Retention % = 1 − Churn %`.

Worked example (Hormozi's, p. 9):
- 100 customers month-start (`P0 = 100`).
- 95 of those 100 still customers month-end (`P1 = 95`).
- Churn = 5 / 100 = **5%**. Retention = 95%.

**First-pool rule.** New signups during the same period do not enter the denominator. You can sign 0 or 1,000 new customers; if you still lost 5 of the original 100, churn is still 5%. Mixing in new signups masks the loss and is the most common reporting error.

### Price–Value–Churn relationship
Two ways to keep `value > price`:
1. **Provide more value** (preferred — see [[Hormozi-Value-Per-Second|Value Per Second]]).
2. **Lower the price** (last resort — concedes pricing power).

Hormozi's inversion question is the operator's diagnostic tool:
> "What would make my customers leave?" → Then do the exact opposite.

| Behaviors that churn 100% of customers | Behaviors that retain 100% of customers |
|---|---|
| Ignore them | Talk with them |
| Break promises | Keep promises |
| Miscommunicate | Communicate clearly |
| Treat them poorly | Treat them like royalty |
| Set unrealistic expectations | Set realistic expectations |
| Hide progress / updates | Give status updates |
| Keep them away from other happy customers | Connect them with other happy customers |
| Make your product hard to use | Make consumption maximally easy |

> "Seems obvious. But nobody does it. Because… it's work."

### Price × Conversion × Churn × LTV evidence table
At a fixed clicks budget (100), a typical service-business curve looks like this (Hormozi, p. 11):

| Price | Clicks | Conv Rate | Sales | Churn | LTV | Total Return | Δ vs. baseline |
|---|---|---|---|---|---|---|---|
| $10 | 100 | 5% | 5 | 10% | $100 | $500 | — |
| $20 | 100 | 4% | 4 | 10% | $200 | $800 | +60% |
| $100 | 100 | 2% | 2 | 33% | $300 | $600 | +20% |

Reading rules:
- The **best price is the price that maximizes total return**, not the price with lowest churn ($20 here).
- Price typically degrades both conversion and churn, but **not proportionally**. If you can double price and lose 20% of conversions with churn flat, do it.
- Higher price → higher churn is a documented Skool-platform pattern, not just a single case. Test the band between the best and the second-best price (here: $39–$59). Pricing-procedure: [[../09-Lifetime-Value/Hormozi-Price-Testing-Method|Hormozi — Price Testing Method]].

### Mispricing rule
> "Match your business model with the pricing model that makes the most sense."

The most common mispricing error: trying to make something **recurring** out of a product whose value is **one-time** (education, setup, an artifact). The recurring fee fights perceived value every cycle; churn climbs to match. Use the [[Hormozi-Annual-Payment-Options|Big-Head-Long-Tail variant]] when the value mix is one-time-heavy with a small ongoing tail.

## Strategic Implications
- **Churn is denominator-locked.** A churn metric that includes new signups is not a churn metric — it is a net-growth metric. Treat the two separately or you will optimize the wrong lever.
- **Price testing without churn telemetry is malpractice.** A price that lifts revenue this month and triples churn next month destroys LTV. Always test price with conversion *and* churn measured.
- **Value-creation beats price-cutting on equal footing.** Both close the value-vs-price gap; only one preserves pricing power, only one compounds (happier customers → referrals → CAC down).
- **The inversion question outperforms most retention frameworks.** "What would make customers leave? — now do the opposite" is faster and more actionable than most retention checklists, and it produces business-specific answers instead of generic best practices.
- **Mispricing is a churn cause, not a pricing problem.** When the model is wrong (recurring on top of one-time value), no amount of retention activity offsets it. Fix the model first.

## Practical Use
1. **Compute churn correctly** every period. Lock the denominator to the starting cohort. Report churn separately from net new.
2. **Run the inversion drill** with the team: list every behavior that would maximize churn for your specific business; invert each line into a retention practice; assign owners.
3. **Build the price–conversion–churn table** for your own product across at least three price points before declaring a "best price." Test the band between the top two.
4. **Audit the model.** If a one-time-value purchase is being sold recurring, restructure to Big-Head-Long-Tail or one-time-with-optional-continuity ([[Hormozi-Annual-Payment-Options|Annual Payment Options]] / [[../03-100M-Money-Models/Hormozi-Continuity-Offers|Continuity Offers]]).
5. **Feed the rest of the checklist.** Every other lever in this book ([[Hormozi-Activation-Points|Activation Points]] through [[Hormozi-Customer-Journey-Milestones|Customer Journey Milestones]]) operates inside the price/value frame defined here.

## Notes / Limits
- **The numbers in the table are illustrative.** "The price in the example doesn't matter, but the relationship between the numbers does." Do not import the table values; reproduce the *shape* with your own data.
- **Lower price ≠ lower churn automatically.** Skool data shows the high-price tier has high churn, but a $0 product is not a retention strategy — it has no buyer commitment to retain against. Price floors exist below which retention collapses for psychological reasons (no skin in the game).
- **Inversion is a generator, not a checklist.** It produces hypotheses. The Churn Checklist's nine levers are the tested hypotheses across many businesses.

## Source Basis
- *$100M Playbook: Retention*, "What Is Churn?" (p. 9) — definition, calculation, first-pool rule.
- *Retention*, "Price, Value, And Churn" (pp. 10–11) — Buffett quote, inversion question, churn-100% / retain-100% lists.
- *Retention*, "Relationship Between Price and Churn" (pp. 11–12) — price × clicks × conv × churn × LTV table; "test, test, test" rule; Skool pattern (higher price → higher churn); mispricing recurring vs. one-time.
- Indexed in [[Hormozi-Retention-Source-Map|Retention — Source Map]].

## Related
- [[Hormozi-Value-Per-Second|Hormozi — Value Per Second]]
- [[Hormozi-Churn-Economics|Hormozi — Churn Economics]]
- [[Hormozi-Churn-Checklist|Hormozi — Churn Checklist]]
- [[Hormozi-Annual-Payment-Options|Hormozi — Annual Payment Options]]
- [[../01-100M-Offers/Hormozi-Value-Equation|Hormozi — Value Equation]]
- [[../01-100M-Offers/Hormozi-Pricing-Power|Hormozi — Pricing Power]]
- [[../09-Lifetime-Value/Hormozi-Price-Testing-Method|Hormozi — Price Testing Method]]
- [[../04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers|Hormozi — CFA Three Levers]]
- [[00-Book-Home|Retention — Book Home]]
- [[Hormozi-Retention-Source-Map|Retention — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]

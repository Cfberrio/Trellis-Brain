---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Price Raise — 'My Rules For Raising Prices' (pp. 5–7)"
sensitivity: internal
hub_role: leaf
book: Price-Raise
---

# Hormozi — Price Raise Rules

## Parent
- [[00-Book-Home|Price Raise — Book Home]]

## Purpose
Fixed set of operating constraints applied to any price raise. Each rule is independently load-bearing — violating one collapses the rollout's economics or its trust with the customer base. Distinct from the [[Hormozi-Price-Raise-Play|Price Raise Play]] (the umbrella mechanism) and the [[Hormozi-RAISE-Letter|RAISE Letter]] (the communication mechanism). These rules govern *what an operator can and cannot do* before, during, and after a raise.

## Core Idea
Most operators avoid raising prices because they fear losing some customers — and by avoiding raises, eventually lose all of them when the business fails. The rules exist to remove the operator's discretion from the high-emotion decisions (grandfathering, lifetime deals, raise frequency) and replace it with constraints that protect the business's long-term pricing power.

> "If you've got the power to raise prices without losing business to a competitor, you've got a very good business. And if you have to have a prayer session before raising the price by a tenth of a cent, then you've got a terrible business." — Warren Buffett, quoted by Hormozi.

The rules below assume the operator is not running a "terrible business" by Buffett's definition — i.e., the product genuinely helps customers. Internalize before deciding to raise.

## Framework / Structure

### Rule 1 — Don't grandfather existing customers
Value depends on price. If your value goes up, your price should too — *for everyone*. Do not lock customers into the old price as a "loyalty courtesy." Locking in a price limits your future options for what you can deliver and how you can deliver it. Not worth it.

The softening mechanism for the existing base is the **vanishing loyalty discount** in [[Hormozi-RAISE-Letter|RAISE Letter]] Section #4 — not permanent grandfathering.

### Rule 2 — Don't do lifetime deals
Same principle, harder to undo. A lifetime deal locks the operator into a future they can't predict. Every operator Hormozi knows who started this way ends up fixing it later — usually with friction and customer resentment.

### Rule 3 — Never sell a "one-time price for lifetime access"
Unless fulfillment truly costs the operator zero dollars. "Forever" lasts much longer than the cash collected. The economics fail when the prepaid cash runs out but the delivery obligation continues. Theoretically, if LTV-from-lifetime-access > LTV-from-recurring, it works. Empirically, no large company runs a lifetime-for-one-payment model — model success, not failure.

### Rule 4 — It's OK to be insecure in the beginning, but raise as you improve
Early-stage products usually deserve early-stage prices. Don't resent early adopters for paying less — that's the deal you offered. As the brand and product mature, raise prices to match. Resenting your customers is a tax on both sides: bad for them, bad for you.

### Rule 5 — Raise prices at least once per year
Buffett bought See's Candies decades ago. He let managers run every decision *except one* — price. He sent them new prices every year. Average raise: ~10% per year. Some years up to 17%. Over 50+ years, that compounds into the dominant value driver of the business. If price is the *only* variable a $400B-net-worth investor reserved for himself, that's a tell about its leverage.

Operator default: **annual cadence, minimum.**

### Rule 6 — Test price raises on new customers before rolling out to the whole base
Two reasons:
1. **Data.** A raise tested cold gives you real conversion + churn data before any existing customer sees the change. The math is proven on real money, not a forecast.
2. **Confidence and social proof.** Knowing that other people said yes without hesitation gives the operator and the team confidence in the raise. It also lets the letter to the existing base reference that "the marketplace has already agreed with you" — the increase isn't invented, it's confirmed.

This rule is the gating mechanism for the entire rollout. If new-customer data doesn't support the raise, don't push it onto the base.

### Rule 7 — Meet 1-on-1 if the raise is ≥50%
A raise above 50% almost always indicates a *big* mistake earlier in pricing. The trust required to keep a customer through a 50%+ raise is higher than what a letter can carry alone. Rule: do everything in the [[Hormozi-RAISE-Letter|RAISE Letter]] *and* schedule individual conversations with affected customers.

The Shopify-competitor case (raised $30→$3,000, lost one customer out of 300) is the canonical example: the CEO got on the phone with all 300. The 100× raise was tolerated because the conversation existed.

### Rule 8 — Don't fear the raise (the elasticity assumption is usually wrong on the downside)
Operators consistently overestimate how much they will lose to a raise. The Shopify case is the extreme; the more common case is "raised X%, lost Y%, where Y is much lower than expected, and net revenue went up materially." If customers see the value, they stay.

This is the rule that overrides the operator's emotional resistance. The empirical pattern across Hormozi's observed cases is that **price elasticity is asymmetric**: prices rise more cleanly than operators predict.

### Rule 9 — Pair the raise with a launch when possible (within 90 days)
Every business has new products, features, or promotions launching. The best window to raise prices is the same quarter as a launch. Frame the existing-customer raise as **early-adopter pricing** for the new thing. The raise drafts off the launch's momentum — the customer's reference frame is "I'm getting something new," not "I'm paying more for the same thing."

### Rule 10 — Do the math
Know what percentage of customers you can lose and still make more money before raising prices. If you've already tested on new customers (Rule 6), you have the inputs. The math tool: [[Hormozi-Price-Test-Math|Price Test Math]].

If the math says the raise is profitable even at the *worst* tolerable churn assumption, the raise is structurally safe — the operator's only remaining risk is execution.

## Strategic Implications

- **The rules collectively neutralize the operator's loss-aversion bias.** Operators left to their own intuition grandfather, hesitate, and underprice. The rules force a different default: raise annually, raise on the whole base, prove with data, soften with mechanism (the letter), don't lock the future.
- **Rule 1 + Rule 5 together create a one-way ratchet.** Raise on everyone, every year. Without Rule 1, Rule 5 fragments into a price-tier mess. Without Rule 5, Rule 1 becomes a one-time event the operator avoids forever. Both rules are required.
- **Rule 6 is the gating rule.** It is the single most important rule for de-risking a raise. Without test data on new customers, the raise on the existing base is a guess. With test data, it's an arithmetic operation.
- **Rule 3 is the trap most consultants/coaches/info-product operators fall into.** Lifetime access offers convert well *initially* and bankrupt you slowly. The rule's purpose is to prevent the operator from selling a future version of the business they don't yet own.
- **Rule 9 reframes the raise as a feature event.** Customers experience launches as "good things." Wrapping the raise inside a launch window changes the emotional framing without changing the math.

## Practical Use

Pre-raise audit. Before sending any raise letter, the operator should be able to answer "yes" to all of the following:

- [ ] No customers are grandfathered into pre-raise pricing? (Rule 1)
- [ ] No lifetime / one-time-for-forever deals are being sold or honored without exit? (Rules 2, 3)
- [ ] Has price been raised in the last 12 months? (Rule 5) — if no, schedule now.
- [ ] Has the new price been tested on new customers and does the data support it? (Rule 6) — if no, test before rolling out.
- [ ] If the raise is ≥50%, is 1-on-1 outreach planned for affected customers? (Rule 7)
- [ ] Is the raise paired with a launch within 90 days, or scheduled to be? (Rule 9) — non-blocking, but increases tolerance.
- [ ] Has the math been worked out (price × conversion × churn × LTV)? (Rule 10) — see [[Hormozi-Price-Test-Math|Price Test Math]].

If any audit item is "no," fix it before sending the letter.

## Source Basis
- *$100M Playbook: Price Raise*, "My Rules For Raising Prices" (pp. 5–7) — all 9 rules verbatim. Note: Rule 8 ("Fear not") and Rule 10 ("Do the math") are presented as distinct rules in the source; this note preserves that structure rather than collapsing them.
- Buffett / See's Candies anecdote (Rule 5), Shopify competitor anecdote (Rules 7, 8) — used as evidence inside the source.
- Indexed in [[Hormozi-Price-Raise-Source-Map|Price Raise — Source Map]].

## Related
- [[Hormozi-Price-Raise-Play|Hormozi — Price Raise Play]]
- [[Hormozi-Price-Test-Math|Hormozi — Price Test Math]]
- [[Hormozi-RAISE-Letter|Hormozi — RAISE Letter]]
- [[../01-100M-Offers/Hormozi-Pricing-Power|Hormozi — Pricing Power]]
- [[00-Book-Home|Price Raise — Book Home]]
- [[Hormozi-Price-Raise-Source-Map|Price Raise — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]

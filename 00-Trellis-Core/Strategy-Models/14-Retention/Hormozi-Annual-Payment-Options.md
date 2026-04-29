---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Retention — 'Churn Checklist #6: Add Annual Payment Options' (pp. 26–27); agency comparison table cross-referenced from $100M Offers (p. 27)"
sensitivity: internal
hub_role: leaf
book: Retention
---

# Hormozi — Annual Payment Options

## Parent
- [[00-Book-Home|Retention — Book Home]]

## Purpose
Lever #6 of the [[Hormozi-Churn-Checklist|Churn Checklist]]. Restructures payment terms so that customers who want to stay longer can **pay to stay longer**, and so that the operator collects more cash up front and reduces churn risk per cycle. Provides three payment-structure variants (annual billing, Big-Head-Long-Tail, founder rate), the pricing rules for each, and the LTV evidence that makes the case.

## Core Idea
> "Customers who pay for longer stays… stay longer."

The mechanism is partly behavioral (sunk-cost commitment) and partly structural (you removed 11 churn opportunities from each annual customer). Adding the option costs almost nothing; pricing the option correctly requires thought.

## Framework / Structure

### Variant 1 — Annual billing option (default)
**Choice architecture:**
- **Mandatory annual** (only way to pay): decreases sales, decreases churn, sometimes nets more profit. Use for high-touch / phone- or webinar-sold products.
- **Optional annual** (offered alongside monthly): typically captures **10–20%** of buyers when priced "buy 10 months, get 2 free" (~16% off). Use for website-checkout / lower-price-point products.
- **Steeper discount on annual** lifts annual take-rate without removing the monthly option.

**Pricing rule (precise):**
- If average customer stays **less than 12 months**, price annual **above** the average-stay revenue (capture upside vs. current life).
  - Worked example: avg 6 months × $1,000/mo = $6,000 avg revenue → price annual **above $6,000**.
- If average customer stays **more than 12 months**, price annual at "buy 10 get 2 free" (16% off retail annual).

### Variant 2 — Big-Head-Long-Tail (one-time setup + small recurring)
> "I call this a 'big head, long tail' where you might charge $6,800 upfront for education or a setup fee, then $199 for the community and everything after that."

**Mechanism:**
- The **one-time upfront** captures the **one-time value** in the offer (education, implementation, setup, artifact).
- The **small recurring** captures the **consumable value** (ongoing community, ongoing access).
- Each priced **according to its own value type**.

**Why it works:**
- Solves the [[Hormozi-Churn-Definition|mispricing trap]] — recurring fee no longer fights one-time perceived value cycle after cycle.
- Recurring fee is small enough that retention compounds: 30 months of LTV at $199 = $5,970 on top of the $6,800 head → total LTV ~$12,800 vs. $6,800 alone.
- Compatible with both ascending sales motions:
  1. **Free community → high-ticket 1-time → low-ticket recurring community.**
  2. **Paid group → upsell on the phone to the high-ticket 1-time.**

**Critical rule:**
> "Make sure to include the recurring fee WITH the 1-time upfront fee and not make it a second sale. Otherwise, you lose the price anchor between the first big purchase and second small recurring that drives the retention."

The recurring price must feel small *relative to* the upfront purchase. Sold separately, it loses the anchor and competes with all other monthly bills the customer has — and churns at a normal rate.

### Variant 3 — Founder rates
> "A founder rate is a discount for the owner of a business. A 50% decrease is a great way to start (provided gross margins still there)."

**Mechanism:**
- A meaningful, named discount tied to a specific operator role/identity.
- 50% off is the reference number; adjust to maintain gross margin.

**Why it works:**
- Discount appears as recognition, not weakness.
- Identity-tied pricing creates loss-aversion later — losing "founder pricing" is more painful than losing a generic discount, which improves retention.
- Pairs naturally with [[Hormozi-Cancellation-Saves|Cancellation Saves]] ("you'll lose your founder pricing" is one of the documented loss-aversion levers).

### Cross-reference: agency table evidence (p. 27, reused from *$100M Offers*)
Hormozi reuses the agency commodity-vs-Grand-Slam comparison table to anchor the upfront-fee mechanic in evidence:

| Metric | Commodity | Grand Slam | Difference |
|---|---|---|---|
| Ad spend | $10,000 | $10,000 | unchanged |
| Impressions | 300,000 | 300,000 | unchanged |
| Response rate | 0.00013 | 0.00033 | 2.5× (more appealing) |
| Appts booked | 40 | 100 | result |
| Show rate | 75% | 75% | unchanged |
| Appts shown | 30 | 75 | result |
| Closing % | 16% | 37% | 2.3× (more value, more buy) |
| Appts closed | 5 | 28 | result |
| Price | $1,000 | $3,997 | 4× (one-time vs. recurring) |
| **Total** | **$5,000** | **$112,000** | **22.4× cash up front** |
| ROAS | 0.5 : 1 | 11.2 : 1 | get paid to acquire |

**Reading rule:** higher one-time upfront capture (Big-Head) compounded with stronger offer (Grand Slam — see [[../01-100M-Offers/Hormozi-Grand-Slam-Offer|Grand Slam Offer]]) flips the unit economics from cost-of-acquisition to paid-to-acquire. The Big-Head-Long-Tail variant in this lever is one operational way to engineer this shift inside a recurring business.

## Strategic Implications
- **Annual billing is structurally a churn-reducer, not just a cash-collector.** 11 fewer renewal decisions per year per annual customer is the lever, regardless of the discount math.
- **Big-Head-Long-Tail solves the recurring-on-one-time-value mispricing.** When the value mix is heavy on one-time deliverables (education, setup, artifact) with a small ongoing tail, Big-Head-Long-Tail aligns price structure with value structure and frequently doubles LTV for the same product.
- **Founder rates are a retention lock disguised as a perk.** Identity-anchored pricing introduces loss aversion that pays back at every cancellation moment.
- **Optional > mandatory in most B2C / low-touch contexts.** The 10–20% who self-select into annual deliver the lift; mandating annual sacrifices the other 80–90% of buyers.
- **Annual customers are pre-screened for retention.** They voluntarily committed to a year — they are by definition the best-fit half of your buyer base. Treat them as your high-priority cohort for [[Hormozi-Customer-Survey-ACA|surveys]] and [[Hormozi-Customer-Journey-Milestones|ascension]].

## Practical Use
1. **Compute average-months-stayed.** That number sets your annual pricing rule (above-average if <12, "buy 10 get 2 free" if >12).
2. **Add the annual option** to your checkout / sales motion. Default to optional for low-touch, mandatory only where high-touch sales support it.
3. **Audit value mix for Big-Head-Long-Tail fit.** If a meaningful portion of your value is one-time (education, setup, implementation, artifact) with a smaller ongoing tail, restructure into BHLT. Bundle the recurring inside the one-time sale to preserve the anchor.
4. **Test founder rates** for owner / decision-maker buyers in B2B. Start at 50% off (verify gross margin holds).
5. **Connect founder pricing to [[Hormozi-Cancellation-Saves|Cancellation Saves]].** The "you'll lose your founder pricing" line is the most documented loss-aversion close; design the cancellation flow to use it.
6. **Watch annual take-rate.** If take-rate is <10% on optional annual, the discount is too shallow. Raise it.

## Notes / Limits
- **Annual mandatory tanks low-touch checkout.** Imposing annual-only on a self-serve $29/mo SaaS will likely halve top-of-funnel conversion. Use only where sales-led delivery supports the conversation.
- **Big-Head-Long-Tail requires real one-time value.** The upfront fee must be backed by a genuinely one-time deliverable (an artifact, a transformation, a high-touch onboarding). Charging $6,800 upfront for nothing more than "access" produces refunds at scale.
- **Founder rates degrade if everyone qualifies.** The 50% discount has to mean something — gate it on identity (owner / founder) or it becomes a generic price drop and loses the loss-aversion lever later.
- **Do not split BHLT into two purchases.** Two-step checkout breaks the anchor and turns the recurring into a normal subscription — which churns normally.
- **Annual revenue ≠ annual realized revenue.** Watch refund/dispute rates on annual buyers. Annual reduces *churn* but can produce concentrated refund exposure if onboarding fails.

## Source Basis
- *$100M Playbook: Retention*, "Churn Checklist #6: Add Annual Payment Options" (pp. 26–27) — mandatory vs optional choice architecture; annual take-rate (10–20% at "buy 10 get 2 free"); pricing rule (above avg if <12 months stayed; "buy 10 get 2 free" if >12 months); Big-Head-Long-Tail variant ($6,800 upfront + $199 recurring → LTV $6,800 → $12,800 example); two ascending sales motions (free → high-ticket → recurring; paid group → phone upsell); critical rule (include recurring with one-time, do not make it a second sale); founder rates variant (50% reference).
- *Retention*, agency comparison table (p. 27) — reused from *$100M Offers*; cross-references [[../01-100M-Offers/Hormozi-Grand-Slam-Offer|Grand Slam Offer]] as the Big-Head-Long-Tail evidence anchor.
- Indexed in [[Hormozi-Retention-Source-Map|Retention — Source Map]].

## Related
- [[Hormozi-Churn-Definition|Hormozi — Churn Definition]]
- [[Hormozi-Cancellation-Saves|Hormozi — Cancellation Saves]]
- [[Hormozi-Customer-Survey-ACA|Hormozi — Customer Survey & ACA]]
- [[Hormozi-Customer-Journey-Milestones|Hormozi — Customer Journey Milestones]]
- [[Hormozi-Churn-Checklist|Hormozi — Churn Checklist]]
- [[../03-100M-Money-Models/Hormozi-Continuity-Offers|Hormozi — Continuity Offers]]
- [[../03-100M-Money-Models/Hormozi-Upsell-Offers|Hormozi — Upsell Offers]]
- [[../01-100M-Offers/Hormozi-Grand-Slam-Offer|Hormozi — Grand Slam Offer]]
- [[../01-100M-Offers/Hormozi-Pricing-Power|Hormozi — Pricing Power]]
- [[../09-Lifetime-Value/Hormozi-Crazy-Eight|Hormozi — The Crazy Eight]]
- [[00-Book-Home|Retention — Book Home]]
- [[Hormozi-Retention-Source-Map|Retention — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]

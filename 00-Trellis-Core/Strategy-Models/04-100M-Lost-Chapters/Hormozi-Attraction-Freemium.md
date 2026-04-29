---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Lost Chapters — Section C: Attraction Offer: Freemium (pp. 93–96)"
sensitivity: internal
hub_role: leaf
book: 100M-Lost-Chapters
---

# Hormozi — Attraction: Freemium

## Parent
- [[00-Book-Home|100M Lost Chapters — Book Home]]

## Purpose
A specific attraction-stage mechanic for businesses with near-100% incremental margins (software, media). Give a continuously-valuable core piece away free, monetize via upsells to paid tiers. Hormozi's explicit warning: *"This is one of the most dangerous acquisition strategies, but also can be one of the most powerful."*

## Core Idea
**Freemium is an acquisition strategy, not a business model.** Critical distinction. The free product is not the business — it is a no-cost lead source that supplies the sales/marketing team with prospects to upsell. The model only works if (1) the free product is so valuable people come via word of mouth (ad spend → $0 or near-$0), (2) it costs almost nothing to fulfill per additional user, (3) it provides continuous (not one-time) value, and (4) it doesn't give away enough to remove the upgrade motive.

## Framework / Structure

### Three Design Constraints
The free thing must:
1. **Cost almost nothing to fulfill** per incremental user.
2. **Provide continuous value** (not one-shot).
3. **Limit use in some way** that anyone using it regularly would want to remove the limit.

If any one fails, the model breaks.

### B2B vs B2C Pattern
- **B2B:** give away something that **exposes a hole** in the prospect's business — a hole your paid product solves. The free product is a diagnostic; the paid product is the treatment.
- **B2C:** give away something people use, with a friction-creating limit (ads to remove, storage to expand, time-limited access). Once they start using it, they'd benefit from increasing the limit.

### Why It Pairs with Software
Software is uniquely suited because (1) marginal cost per user ≈ $0, and (2) the design intent is continuous value. The hard problem reduces to: *exactly how much, and which features, to give away.*

### Examples (in-source)
- **Dropbox** — free storage up to a cap; paid above.
- **Spotify** — free music with ads; paid removes ads.
- **Wistia** — free video uploads up to a cap; paid above.
- **Gmail** — free email; paid above storage cap, with fear-of-loss (deletion) on the limit.

### True CAC for Freemium
Standard CAC formulas don't apply directly. Real CAC = (cost to service one free user) ÷ (free-to-paid conversion rate).

Worked example:
- $0.05/mo to service a free user.
- 1% upgrade rate.
- True CAC = $0.05 / 0.01 = **$5/mo per paid customer**.
- If average paid revenue ≥ $15/mo, the business can be profitable.

### Three Failure Modes
1. **Conversion problem.** Free-to-paid % too low. Paid revenue can't cover free fulfillment.
2. **Value problem.** Give-away isn't valuable enough to spread. Marketing required to attract free users → costs no longer ~$0.
3. **Cost problem.** Free thing spreads, but per-free-user fulfillment cost is too high relative to paid revenue. Business loses money serving free customers.

### Capital Requirement
Almost every freemium success in the source list (Dropbox, Spotify, etc.) had outside funding. Hormozi: *"If you do not have investors and large amounts of capital, I would not recommend this structure."* The model assumes runway to absorb the free-fulfillment burn while conversion machinery scales.

### Critical Constraint: Free Only
This mechanic does **not** work with a discount variation. Either fully free or this isn't the strategy. (Discount + upgrade is a different mechanic — see [[Hormozi-Continuity-Discount-Plus-Fee|Discount + One-Time Fee]].)

## Strategic Implications

- **Acquisition strategy ≠ business model.** Founders confuse these. The free product cannot be the source of revenue; revenue comes from paid upgrades. Designing the free product as if it were the business is the most common failure pattern.
- **Capital is a prerequisite, not an option.** Without funding to absorb the free-fulfillment cost while spreading and converting, freemium is structurally unsustainable.
- **Fit is narrow.** Software and media-with-near-zero-marginal-cost qualify. Service businesses, physical products with non-trivial fulfillment cost, and most local businesses do not.
- **Upselling is easier than selling.** The strategic upside, when it works: pre-qualified pool of users already comfortable with the product, and sales team upsells (not cold sells). High-take-rate upsells justify the free-fulfillment cost.
- **Inclusion is for completeness, not recommendation.** Hormozi explicitly includes this for a complete picture of acquisition strategies. He does not recommend it for typical businesses, and notes he's seen freemium *done incorrectly by really smart people more times than correctly.*

## Practical Use

Eligibility check before considering freemium:

1. **Marginal cost per additional user ≈ $0?** If no → not a fit.
2. **Continuous-value product (used over time)?** If no → not a fit.
3. **Capital reserves sufficient to absorb free-fulfillment burn for 12–24 months?** If no → not a fit.
4. **Differentiation strong enough to drive organic word-of-mouth?** If no → ad spend reintroduces, killing the model's economics.

If all four pass:
1. **Design the limit.** What about the free use creates the upgrade motive (storage, ads, feature gates, fear-of-loss)?
2. **Compute true CAC** = service cost ÷ upgrade rate. Confirm < paid ARPU.
3. **Build sales/upgrade machinery** that operates against the free-user pool — not cold marketing.
4. **Monitor the three failure modes** (conversion, value-spread, cost). Each has a different fix.

## Notes / Limits
- Author note: chapter cut from `$100M Money Models` because Hormozi *"didn't think it applied to enough businesses."* Treat as a niche-fit framework, not a default option.
- Conversion rates and service-cost figures in the worked example are illustrative; real numbers vary by product. The *form* of the calculation generalizes.
- This is the only attraction mechanic in Lost Chapters that Hormozi actively warns against without specific qualifications. Take the warning at face value.
- Does not pair with a discount wrapper (per Free vs Discount note in source).

## Source Basis
- `$100M Lost Chapters`, "Attraction Offer: Freemium" (pp. 93–96) — strategy-vs-model distinction, B2B vs B2C patterns, four examples (Dropbox/Spotify/Wistia/Gmail), three design constraints, true CAC worked math, three failure modes, capital requirement, free-only constraint.
- Author note: chapter cut from `$100M Money Models`; included for completeness despite narrow fit.
- Indexed in [[Hormozi-100M-Lost-Chapters-Source-Map|100M Lost Chapters — Source Map]].

## Related
- [[00-Book-Home|100M Lost Chapters — Book Home]]
- [[Hormozi-100M-Lost-Chapters-Source-Map|100M Lost Chapters — Source Map]]
- [[Hormozi-Offer-Stacking|Hormozi — Offer Stacking]] — Freemium is one Attract option in the stack
- [[Hormozi-Promotion-Wrappers|Hormozi — Promotion Wrappers]] — Freemium is an extreme of the Free wrapper
- [[Hormozi-Customer-Financed-Acquisition|Hormozi — Customer Financed Acquisition (CFA)]] — Freemium violates Level 2/3 in the early years; capital substitutes for customer financing
- [[Hormozi-Home|Hormozi Home]]

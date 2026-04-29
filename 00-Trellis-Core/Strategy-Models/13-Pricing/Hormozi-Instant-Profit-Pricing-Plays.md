---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Pricing — 'Just Raise It' framing (pp. 25–27); 10 Pricing Plays (pp. 28–59); recap table (p. 61)"
sensitivity: internal
hub_role: leaf
book: Pricing
---

# Hormozi — Instant Profit Pricing Plays

## Parent
- [[00-Book-Home|Pricing — Book Home]]

## Purpose
Catalog of the 10 low-risk pricing tactics ("Instant Profit Pricing Plays") from the *Pricing* playbook. Each is designed to lift revenue with minimal or zero impact on conversion and minimal operational change. Combined, they total a 26.8%–63.8% revenue lift on top of existing pricing — which, on typical small-business margins (7–10%), is a 3–6× profit lift. Designed to be picked from à la carte: most operators only need one or two to materially move profit.

This umbrella note holds all 10 plays with a uniform internal structure (Mechanism / Math / Implement / Caveat) so each play remains decision-useful at the play level without fragmenting into 10 separate notes.

## Core Idea
> "Every business has loads of these tiny little pricing easter eggs hidden under little stones." — Hormozi (Just Raise It, p. 26)

The plays exploit one structural fact: most of an operator's costs (delivery, CAC) don't scale with price. So small revenue lifts that don't move conversion drop almost entirely to the bottom line. The thesis is operationalized in [[Hormozi-Pricing-Profit-Leverage|Pricing-Profit-Leverage]]; this note is the tactical implementation.

The right way to use this note is **not** to implement all 10. Pick the one or two with the best fit-to-business and the lowest implementation cost. Re-evaluate quarterly.

## Framework / Structure

### Cumulative Lift Table (the playbook overview)

| # | Play | Revenue Lift |
|---|---|---|
| 1 | Monthly → 28-Day Billing Cycles | 8.3% |
| 2 | Multi-Form + CC Processing Fee | 3–4% |
| 3 | Sales Tax | 0–10% |
| 4 | Annual CPI Increase | 3–10% |
| 5 | Longer-Duration Billing Options (Annual Billing) | 10–15% |
| 6 | Round Up (.99 / 7→9) | 1–3% |
| 7 | Annual Renewal Fee On Top Of Monthly | 10% |
| 8 | Continued Access / Automatic Continuity | 10% |
| 9 | Ultra-High Ticket Anchor | 10–15% |
| 10 | Priced Guarantee / Warranty | 5–20% |
| — | **Total combined** | **26.8% – 63.8%** |

Worked context: a $1M business at 9% net margin → +26.8% revenue would produce ~$268K extra revenue → $358K profit (vs. $90K baseline) — a ~4× profit lift.

---

### Play #1 — Monthly → 28-Day Billing Cycles
**Mechanism.** Monthly billing produces 12 cycles/year. Billing every 28 days (or weekly equivalents) produces 13 cycles. The extra cycle is pure profit at the same per-cycle conversion rate.

**Math.** $100/mo → $100 per 28 days = $1,300/yr (vs. $1,200/yr) = +8.3% revenue. On a 20%-margin business, that lifts net margin from 20% → ~26.1% — a +41.5% profit lift.

**Implement.** (1) Change contracts for new customers immediately. (2) Set a date to migrate existing customers. (3) Be upfront — call it a price increase if needed. (4) Frame as "reinvestment in the business."

**Caveat / advice.** Bill every 4 weeks, not weekly or bi-weekly — weekly cadences create pause requests and billing hassle. Display weekly for the lowest perceived price; bill on the 4-week cycle. Stick with 4-week, 12-week, or longer.

---

### Play #2 — Processing Fees & Second Form of Payment
**Mechanism.** After the customer agrees to the price, ask: "How did you want to pay?" Then: "Great, it's just a 3.99% card processing fee." If they balk, offer to waive the fee in exchange for a **second form of payment** held on file. Second card on file directly attacks involuntary churn from card declines.

**Math.** Recurring payments suffer 1.2%–1.7% monthly involuntary churn from card-info changes. On a 5%-monthly-churn business, that's 24–34% of total churn. On a $100/mo / 5% churn business:

| Situation | Price | Churn/Mo | LTV |
|---|---|---|---|
| Old | $100 | 5.0% | $2,000 |
| Accept fee | $104 | 5.0% | $2,080 (+4%) |
| Add 2nd card (1.2% saved) | $100 | 3.8% | $2,631 (+31%) |
| Add 2nd card (1.7% saved) | $100 | 3.3% | $3,030 (+51%) |

The 2nd-card path produces ~7–13× more LTV lift than the fee path alone.

**Implement.** Update sales script. Accept second form of payment. Have customer authorize both. Re-run failed transactions next day on the alternate card.

**Caveat / advice.** Worst case: 4% revenue lift for no work, no conversion drop. Best case: massive LTV lift via reduced involuntary churn. Hormozi reports "never seen anyone lose a sale because of adding a processing fee."

---

### Play #3 — Sales Tax
**Mechanism.** When sales tax applies, charge it to the customer rather than absorbing it. Tax comes off the top line, so absorbing it shreds margin (5% tax on a 20%-margin business = 25% of profit gone).

**Math.** Restaurant case (8% province tax): $25,000/mo agreed → $27,000 invoice. The marketer's framing: "I don't cover taxes. My price is what I get." The client paid.

**Implement.** (1) Get agreement on the price. (2) On the invoice or at point-of-sale, add the line: *"State tax code [X] mandates that personal services are subject to N% sales tax."* Keep it dry, matter-of-fact, "as you already know." (3) List tax as a separate line item before total. (4) If they balk, "get in the angry boat" — be more annoyed about the tax than they are: "Think I like charging this tax? I hand it right over to Uncle Sam."

**Pro tips.** (a) **Menu pricing**: add "All prices subject to sales tax and an additional 4% processing fee" line at the bottom. (b) **Reincorporate** in a state without sales tax for the relevant service if applicable (administrative work, but reclaims a meaningful chunk of profit).

**Caveat / advice.** Cannot charge taxes you don't pay. Otherwise: there is no world where giving away a chunk of profit for zero customer value makes sense.

---

### Play #4 — Annual Price Increases (CPI Clause)
**Mechanism.** Build a fixed annual price-increase right into the contract (5–15%/yr). Inflation erodes margin every year regardless — either the operator captures it proactively or watches it disappear into cost increases.

**Math.** $100/mo at 5% annual increase → $122/mo by year 4 (+22% absolute). At 12% annual → $157/mo by year 4. Compounded over 5 years that's a 57%+ price lift. Inflation comparison: $100 of 2017 spending power is ~$79 in 2024; an operator who never raised price has lost ~21% of effective price.

**Worked context.** Warren Buffett raised See's Candies prices 50+ times over 51 years (sometimes 17%/yr). Pricing was the one variable he insisted on controlling personally. Resulted in $1B+ of profit attributed to that single lever.

**Implement.** (1) Pick a percentage (5–15% is the comfortable range). (2) Add to all new contracts. (3) Sales script: *"To reinvest in keeping our integrity and delivering [X] at the highest possible quality, we keep our prices standard with the CPI. That way we don't have any incentive to cut quality as the cost of goods rises."* (4) Don't mention during the sale — bring up during paperwork.

**Caveat / advice.** Few customers balk under 15%. Without this clause, operators frequently realize after 5 years they haven't raised price and have effectively lost 20%+ of margin to inflation.

---

### Play #5 — Annual Billing (Longer-Duration Billing Options)
**Mechanism.** Offer longer billing cadences as a payment option — annual, quarterly, semi-annual. Less frequent billing produces less churn and more upfront cash.

**Math.** Profitwell data on billing cycle vs. churn:

| Billing Cycle | Monthly Churn | Price | LTV | Gain vs. Monthly |
|---|---|---|---|---|
| 1× per year | 2% | $100 | $5,000 | 5.35× |
| 4× per year | 5% | $100 | $2,000 | 2.14× |
| 12× per year | 10.7% | $100 | $935 | baseline |

Annual billing produces ~5× the LTV of monthly billing.

**Conversion pattern Hormozi observed in his portfolio:** with a 16% discount on annual ("buy 10 get 2 free"), 10–15% of customers select annual on a sales page; 30% if annual is the *default* selection; 35–40% over phone sales.

**Implement.** (1) Add longer-duration options to pricing. (2) Always offer the **highest price first** — quote the full annual amount with no discount. (3) Then offer the prepaid annual discount (~17%). (4) If declined, offer a quarterly prepaid discount (~8%). (5) If declined, offer standard monthly. **First number anchors the conversation** — operator must say it.

**Pro tip — High Conversions + Annual Billing.** Sell a short upfront term (6–12 weeks) to build trust, then upsell to annual prepay. Combines easier conversion with the long-term-stick benefit.

**Caveat / advice.** Don't *only* offer annual — that drops conversions. Always-offer-with-incentive is the safe move. "Zero risk more money play."

---

### Play #6 — Round Up (.99 endings + 7→9)
**Mechanism.** Adjust price endings: convert prices ending in .00 → .99, and prices ending in 7 → 9. Tiny absolute changes, no operational impact, no measurable conversion drop in Hormozi's gym data.

**Math.** Worked example from Hormozi's gyms (weekly billing):

| Old Price | New Price | Old Annualized | New Annualized | Annual Difference |
|---|---|---|---|---|
| $47/wk | $49/wk | $2,444 | $2,548 | +$104 (+4.25%) |
| $37/wk | $39/wk | $1,924 | $2,028 | +$104 (+5.4%) |
| $27/wk | $29/wk | $1,404 | $1,508 | +$104 (+7.4%) |

Adding .99 on top:

| Old Price | New Price | Old Annualized | New Annualized | Annual Difference |
|---|---|---|---|---|
| $47/wk | $49.99/wk | $2,444 | $2,599 | +$155 (+6.36%) |
| $37/wk | $39.99/wk | $1,924 | $2,079 | +$155 (+8.1%) |
| $27/wk | $29.99/wk | $1,404 | $1,559 | +$155 (+11.1%) |

On the average gym at 12.5% net margin, the 6.36–11.1% revenue lift roughly doubles profit.

**Implement.** Change 7s to 9s. Add .99 to all fees. Change contracts for new customers immediately.

**Caveat / advice.** **Luxury** items end on round 0/5, not .99 — luxury buyers want the price to *not* feel like a deal; high price *is* the value signal. **Premium ≠ luxury** — premium goods (where price reflects underlying value) can still use .99 / 7→9.

---

### Play #7 — Annual Renewal Fee On Top Of Monthly
**Mechanism.** Sign customers on an annual contract with three components: startup fee, monthly rate, and annual renewal fee. Customers focus on the monthly number; the annual fee adds ~10–25% to effective rate without affecting how the price is *advertised*.

**Math.** Tanning-salon model (mentor John, sold to LA Fitness):

| Fees | Annualized | Effective Monthly |
|---|---|---|
| $39 × 12 | $468 | $39/mo |
| $39 × 12 + $99 × 1 | $567 | $47/mo (+20%) |

Sizing the renewal fee:
- 0.5× monthly → +4.15% revenue
- 1× monthly → +8.3% revenue
- 2× monthly → +16.6% revenue
- 3× monthly → +24.9% revenue

**Implement.** (1) Pick renewal fee at 1–3× monthly rate. (2) Add a "reason why" — *"You pay this for rate protection. If you don't agree, you'll be subject to any price changes."* Alternate: *"This allows you to go month-to-month after the year without a cancellation fee."* (3) Add to contract; have customer initial both the monthly rate and the renewal fee. Call it "rate protection" or "cancellation fee prepayment."

**Pro tip.** Pair a setup fee with a renewal fee — this lets the operator waive one to incentivize signup while keeping the other.

**Caveat / advice.** If they balk at the renewal fee, drop it — they don't get the benefit (rate protection / no cancel fee). This *protects against losing the sale* while capturing extra revenue from the customers who don't push back.

**Author note.** This play conflicts with Play #5 (annual billing) — pick whichever fits the market. Play #5 is preferred where customers will accept annual; Play #7 is the workaround for price-conscious markets where annual upfront kills conversion.

---

### Play #8 — Automatic Continuity
**Mechanism.** Sell a paired-down, very-low-cost-to-deliver version of the product as an automatic continuity bolt-on at the end of the front-end purchase. Priced at 5–20% of the main thing. Customer agrees upfront. After the front-end term completes, billing rolls automatically into the lower-priced ongoing version.

**Math.** Example economics:

```
Front-end product:
  Price: $2,000/mo · Duration: 4 months · Gross margin: 70% · LTV: $5,600

Automatic continuity bolt-on:
  Price: $200/mo (10% of monthly) · Gross margin: 90% · Duration: 20 months · Conversion to bolt-on: 50%
  LTV impact: +$1,800 (32% lift, $5,600 → $7,400)
  Profit impact: 25–100% lift depending on margin structure
```

The seller who taught Hormozi this play: $750,000/yr from one contract line, "Continued Access" rolling lifetime-access courses into $99/mo after year one.

**Implement.** (1) Pull every front-end product. (2) Find the feature(s) that deliver value but cost little to maintain. (3) Price at 5–20% of normal. (4) Bolt onto every front-end purchase; only earned after the customer completes a defined initial term (helps stick rate). (5) Remarket to the resulting low-ticket pool to ascend them later.

**Examples of bolt-on continuity:** continued support, tech support, priority support, price protection, continued access, community access, insurance/warranty, any small high-margin feature peeled off as the "default" recurring option.

**Caveat / advice.** **Disclose it upfront** — this is not "undisclosed continuity" or "forced" continuity. Customers must agree. In Hormozi's experience, customers like knowing there's a more cost-effective version at the end of the term — sunk-cost reasoning makes continuity feel rational.

**Mapping out.** This play is a pricing-mechanic *application* of the broader continuity-offer model. Canonical home for the model: [[../03-100M-Money-Models/Hormozi-Continuity-Offers|Hormozi — Continuity Offers]].

---

### Play #9 — Ultra High Ticket Anchor
**Mechanism.** Add a "mac daddy" version of the product priced 10× or more above the main offer. Two effects: (a) anchors the main price as appearing more affordable by comparison, lifting conversion on the main; (b) a small percentage of buyers select the high-ticket version, dramatically lifting LTV.

**Math.** Baseline (main + downsell only):

| Price | Take Rate | Added LTV |
|---|---|---|
| $500 | 80% | $400 |
| $200 | 20% | $40 |
| **Old LTV** | | **$440** |

After adding the ultra-high ticket option (10% take rate):

| Price | Take Rate | Added LTV |
|---|---|---|
| $5,000 | 10% | $500 |
| $500 | 70% | $350 |
| $200 | 20% | $40 |
| **New LTV** | | **$890** |

Per-customer LTV lifts from $440 → $890 (~2×). Plus the main $500 product converts higher because the $5,000 anchor reframes it.

**Implement.** Think of the most absurd version of the product — the price the operator would happily deliver at. Offer that **first** in the sales conversation (like the tailor: $16,000 suit shown first, $2,000 suit shown second feels like relief). Get the gasp. Then move to the main offer if they can't.

**Caveat / advice.** Be willing to actually deliver the high-ticket version. If the price stresses the operator out when someone buys, raise it more — until the price makes the operator smile when accepted. Hormozi notes one peer's outcome: after adding the mac-daddy version, "everyone started buying his mac daddy product" and it became most of his revenue.

---

### Play #10 — Guarantee / Warranty Upsell
**Mechanism.** After the customer agrees to buy, offer a guarantee or warranty as a paid upsell at 5–30% of product price. Apple's AppleCare is the canonical example — billions of revenue selling what was originally free.

**Math.** Working numbers:
```
$1,000 product · $100 guarantee · $100 cost to replace
1 in 20 buyers asks for warranty:
  20 warranties × $100 price = $2,000 revenue
  − $100 cost to fix the 1 claim
  = $1,900 pure "guarantee" profit per 20 sales
```

If you set the guarantee price equal to your cost-of-goods, you literally never lose money on it (revenue covers the cost of an extra delivery, and you still keep the original sale revenue).

Examples (book table):

| Product | Price | Guarantee | Guarantee Price | Take Rate | Refund Rate | Added LTV | Added Revenue |
|---|---|---|---|---|---|---|---|
| Wooden Table | $1,000 | "No watermarks or replacement" | $100 | 45% | 5% | $43 | +4.3% |
| Personal Training | $3,000 | "Lose weight or money back" | $2,000 | 35% | 10% | $630 | +21.0% |
| Dry Cleaning | $200 | "No tears/stains or money back" | $20 | 25% | 5% | $5 | +2.4% |

Reminder: 4% revenue lift on a 7–10% margin business is often a 20%+ profit lift.

**Implement.** Update the sales script. After purchase: *"You just want the standard warranty on that?"* If they ask what it is: *"Oh, it's for anyone who likes that extra bit of peace of mind. If anything happens to your X you're covered. A lot of people do it."* Charge for this "invisible" product. If a buyer requests the guarantee, check whether they bought it.

**Pro tip — Cover commissions.** If sales reps are paid 10% commission and 50% of customers take a 10% guarantee upsell, the upsell revenue covers ~half of total commissions paid. One line in the sales script, no operational drag.

**Caveat / advice.** Works at any price (shipping insurance proves this). Buyers hate risk and will pay to offload it. Even when a buyer didn't pay for the guarantee, the operator can still grant the refund — "be the nice guy" — and capture the upsell revenue from the rest.

---

## Strategic Implications

- **Stack, don't substitute.** The 10 plays are designed to combine. A monthly subscription business that adds 28-day cycles + processing fee + annual CPI + .99 endings + warranty upsell can layer 5 plays for ~25–30% combined revenue lift in a quarter, with no acquisition or product change.
- **Pick by fit, not by lift size.** The biggest revenue lift on paper (Play #10 warranty at +20%) is wrong for a service business that has nothing to warranty. The smallest lift (Play #6 .99 endings at +1–3%) is wrong for a luxury brand. Match the play to the business.
- **Display vs. bill is a recurring lever.** Plays #1 (28-day cycles displayed weekly), #5 (annual billing displayed monthly), #7 (annual renewal fee on top of advertised monthly) all exploit the display/bill split. The principle from [[Hormozi-Pricing-Rules|Pricing Rules]] (#14) sits underneath these three plays.
- **Risk-transfer plays are pure margin.** Plays #2 (processing fee), #3 (sales tax), #10 (warranty) all transfer cost or risk from operator to customer. Conversion impact is small to none, but the lift drops 100% to the bottom line.
- **Anchor + continuity is a paired play.** Play #8 (Automatic Continuity) and Play #9 (Ultra High Ticket Anchor) combine well: the anchor lifts main-offer conversion, and the continuity recaptures churned/finished customers into a low-ticket recurring pool. Together they often double LTV without changing the front-end product.
- **One-line scripting changes are disproportionately profitable.** Plays #2, #4, #7, #9, #10 are all literally one or two added lines in a sales script or contract. They are systematically under-implemented because they feel "too small to bother with" — which is exactly the [[Hormozi-Pricing-Profit-Leverage|profit-leverage]] error this book is written to correct.

## Practical Use

A working selection process for an operator new to this catalog:

1. **Filter by business type.**
   - Recurring/subscription: prioritize Plays #1, #2, #4, #5, #6, #7, #8.
   - Service/consult: prioritize Plays #2, #3, #4, #9, #10.
   - Physical goods: prioritize Plays #6, #9, #10.
   - Restaurant / on-premise: prioritize Plays #2, #3, #4, #6.
2. **Pick 1–2 highest-fit plays** with the lowest implementation cost. Ship those first.
3. **Measure the conversion delta** over 30–60 days. If conversion drops more than the revenue lift, revert that play and try another.
4. **Stack a second wave** at quarter end. The cumulative table is a 1–2 year roadmap, not a single sprint.
5. **Document each play in the contract / script** so it survives staff turnover. Plays that live only in the operator's head get dropped on the next handover.
6. **Re-evaluate quarterly.** Profitwell's data (carried in [[Hormozi-Pricing-Profit-Leverage|Pricing-Profit-Leverage]]): pricing-test cadence itself is a profit driver.

## Notes / Limits

- The 26.8%–63.8% combined lift assumes all plays are applicable and conversion stays flat. In practice, plays compound non-linearly (some fight each other) and conversion will move a little. Treat the combined number as a directional ceiling, not a forecast.
- Plays #5 (annual billing) and #7 (annual renewal fee) **conflict** in some markets. Annual billing is cleaner where customers will accept it; annual renewal fees are the workaround for price-conscious markets that won't.
- Play #8 (Automatic Continuity) requires honest disclosure. "Forced" or "undisclosed" continuity damages reputation, generates chargebacks, and exposes the business to consumer-protection action. Hormozi flags this explicitly.
- Play #3 (Sales Tax) cannot be applied to taxes the operator does not actually owe. It is a recovery play, not an invented surcharge.
- Play #6 (Round Up) inverts for genuine luxury goods — they should end in 0 or 5, because high price is itself the value signal for that category.
- Play #10 (Warranty / Guarantee) works only when the operator can model the actual claim rate. Underprice it relative to claims and it becomes a margin sink.
- The plays are tactical. They do not substitute for [[Hormozi-Value-Driven-Pricing-Model|value-based pricing]] at the model level — they are optimizations on top of a value-priced foundation. Applied to an underpriced or commodity-priced product, the lifts are smaller and less stable.
- Play-specific origin anecdotes (gym owner, ad-agency friend, Canadian marketer, real-estate friend, mentor John, $5M/yr education seller, tailor, Apple) are absorbed inline above. They are illustrative, not load-bearing — the math and implementation are the canonical content.

## Source Basis
- *$100M Playbook: Pricing*, "Just Raise It" + "Small Percentages. Big Changes." + "The *Instant Profit* Pricing Playbook" framing (pp. 25–27) — restaurant 4%-fee → 44% profit case; cumulative 26.8%–63.8% framing; the overview table.
- *Pricing*, "Pricing Play #1: Monthly to 28 Day Billing Cycles" (pp. 28–29) — gym-owner origin; 12 vs. 13 cycle math; weekly-display-bill-monthly advice.
- *Pricing*, "Pricing Play #2: Processing Fees & Second Form of Payment" (pp. 30–32) — ad-agency origin; LTV tables for 5% and 10% churn; involuntary-churn-via-card-decline data (1.2–1.7% monthly).
- *Pricing*, "Pricing Play #3: Sales Tax" (pp. 33–35) — Canadian marketer origin; reincorporation pro-tip; menu-pricing pro-tip; "angry boat" objection-handling.
- *Pricing*, "Pricing Play #4: Annual Price Increases" (pp. 36–38) — real-estate-friend origin; 5% and 12% compounding tables; Warren Buffett See's Candies case (50+ raises in 51 years).
- *Pricing*, "Pricing Play #5: Annual Billing" (pp. 39–41) — Patrick Campbell / Profitwell origin; billing-cycle vs. churn vs. LTV table (1×/yr=2% churn=$5,000 LTV); 16%-discount conversion patterns; anchor-the-highest-price-first pro-tip.
- *Pricing*, "Pricing Play #6: Round Up" (pp. 42–44) — gym-pause origin; St. Jude's grocery anecdote; 7→9 and .99 worked tables; luxury-vs-premium caveat.
- *Pricing*, "Pricing Play #7: Annual Renewal Fee On Top Of Monthly" (pp. 45–48) — mentor John / tanning salon / LA Fitness origin; $39+$99 worked example; renewal-fee-as-multiple-of-monthly sizing table; rate-protection scripting.
- *Pricing*, "Pricing Play #8: Automatic Continuity" (pp. 49–53) — $5M/yr education seller origin ($750K from one contract line); $2,000/mo + $200/mo continuity worked economics; bolt-on examples list; disclosure caveat.
- *Pricing*, "Pricing Play #9: Ultra High Ticket Anchor" (pp. 54–55) — tailor / $16K-suit origin; 10% take-rate worked LTV table ($440 → $890).
- *Pricing*, "Pricing Play #10: Guarantee and Warranty Upsells" (pp. 56–59) — Apple/AppleCare origin; $1,000 product / $100 guarantee math; three-product example table (table, training, dry cleaning); cover-commissions pro-tip.
- *Pricing*, "The *Instant Profit* Pricing Playbook" recap (p. 61) — final consolidated table.
- Indexed in [[Hormozi-Pricing-Source-Map|Pricing — Source Map]].

## Related
- [[Hormozi-Pricing-Profit-Leverage|Hormozi — Pricing Profit Leverage]]
- [[Hormozi-Value-Driven-Pricing-Model|Hormozi — Value-Driven Pricing Model]]
- [[Hormozi-Pricing-Rules|Hormozi — Pricing Rules]]
- [[../01-100M-Offers/Hormozi-Pricing-Power|Hormozi — Pricing Power]]
- [[../03-100M-Money-Models/Hormozi-Continuity-Offers|Hormozi — Continuity Offers]]
- [[00-Book-Home|Pricing — Book Home]]
- [[Hormozi-Pricing-Source-Map|Pricing — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]

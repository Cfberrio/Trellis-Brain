---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Lost Chapters — Section B: The Three Levers of CFA (pp. 39–41), Know The Levers (p. 43), Cost To Acquire a Customer = CAC (pp. 45–47), Lifetime Gross Profit (pp. 49–51), Payback Period = PPD (pp. 53–61)"
sensitivity: internal
hub_role: leaf
book: 100M-Lost-Chapters
---

# Hormozi — CFA Three Levers

## Parent
- [[00-Book-Home|100M Lost Chapters — Book Home]]

## Purpose
Calculation method for the three variables that determine whether Customer-Financed Acquisition works: **CAC** (Cost to Acquire a Customer), **LTGP** (Lifetime Gross Profit), and **PPD** (Payback Period). Companion to [[Hormozi-Customer-Financed-Acquisition|CFA]] — that note defines the framework, this note defines the math. Hormozi cut these from `$100M Money Models` because "money math" intimidated readers, but they are the operational lens behind every acquisition decision.

## Core Idea
Three levers fully describe a business's growth potential:
1. **Get more customers** → lower CAC.
2. **Make them worth more** → raise LTGP.
3. **Do it faster** → shorten PPD.

CAC is a hard science (you can know it exactly). LTGP is an estimate (improves as the business ages). PPD ties the other two to the calendar and is what turns abstract margin into compound growth.

## Framework / Structure

### Lever 1 — CAC (Cost to Acquire a Customer)

Definition: total spend to acquire a customer including ads, payroll to media buyer, creative team, software, sales commissions and salaries.

Formula:
```
CAC = (All Marketing & Sales Costs in period) ÷ (Customers acquired in period)
```

**Hormozi's three calculation examples** (different channel mixes, same method):

*(a) Outreach.*
- $200/mo email software + $3,000/mo cold emailer + $100/sale × 8 sales = $4,000.
- 8 customers → CAC = $4,000 / 8 = **$500**.

*(b) Content marketing.*
- 2 media team @ $5,000/mo = $10,000 + 10 sales × $100 commission = $1,000. Total = $11,000.
- 10 customers → CAC = $11,000 / 10 = **$1,100**.

*(c) Paid ads.*
- $4,000 media buyer + $20,000 ad spend + $1,000 software + 10 × $1,000 commissions = $35,000.
- 10 customers → CAC = $35,000 / 10 = **$3,500**.

Hormozi diagnostic: when investing in a company, run a full acquisition diagnostic by channel. Half the time one channel performs significantly better than others — concentrate spend there.

Common error: founders report ad spend per customer (not full CAC). A "$200 sale" can really cost $500 across all the sales/marketing functions feeding it.

### Lever 2 — LTGP (Lifetime Gross Profit)

Definition: total gross profit collected from a customer over their full lifetime. Distinct from net profit (which subtracts all costs, including overhead).

**Step 1 — Gross profit per customer.**

*Product example.* $100 sale - $20 fulfillment = $80 GP. Gross margin = 80%.

*Service example.* 1 rep at $6,000/mo serves 10 clients at $3,000/mo each → $30,000 revenue – $6,000 cost = $24,000 GP, 80% margin, $2,400 GP per customer.

**Step 2 — Average transactions per customer.**

Three methods:
1. Export customer data, sort by transaction count, average that column.
2. For recurring revenue, use churn. Churn = (customers lost in period) ÷ (customers at start of period). Sign-ups during the period don't affect churn.
3. Use the smaller of the two: a back-of-napkin estimate.

Note on churn: 100 customers at start, 95 at end (regardless of new sign-ups) → 5 lost / 100 = 5% churn.

**Step 3 — Multiply or divide.**

- *Physical product*: `LTGP = GP × avg transactions`. Example: $80 × 4 = $360.
- *Recurring service*: `LTGP = GP per period ÷ Churn`. Example: $2,400 ÷ 5% = $48,000.

**Strategic framing.** "LTGP is the arms race of business" (Hormozi's rephrasing of Dan Kennedy: *"He who can spend the most to acquire a customer wins"*). CAC has a floor at $0; LTGP has no ceiling. CAC is about getting customers; LTGP is about keeping them. Of the two, raising LTGP is harder than making advertising more efficient — which is why it's the more durable competitive advantage.

### Lever 3 — PPD (Payback Period)

Definition: time to break even on what you spent to get a customer. Hits when cumulative GP from the customer ≥ CAC.

**Worked example.** $50/mo GP per customer, $100 CAC. First payment Day 1 returns $50; second payment Day 31 returns the other $50. PPD = 31 days.

**Why PPD compounds.**
- 1-month payback: 2× cash month 1 → 4× month 2 → 8× month 3.
- 3-month payback: 2× cash by month 3.
- Same three months, **4× difference in growth potential**, compounded quarterly.

PPD is the conversion factor between LTGP/CAC efficiency and calendar time — the link between unit economics and growth velocity.

## Strategic Implications

- **Calculate CAC by channel, not in aggregate.** Aggregation hides the channel that's actually paying for itself; the others are dragging the average. The first move when investing in a business is always: split CAC by channel.
- **CAC has a floor; LTGP doesn't.** Optimization energy spent on CAC has diminishing returns; energy on LTGP has compounding returns. Both matter, but the long game is LTGP.
- **GP, not net profit.** All three levers are computed in gross-profit terms. Mixing in fixed costs / overhead breaks the comparability across customers and channels.
- **PPD is the speed governor.** Two businesses with identical LTGP and CAC differ in growth rate by PPD alone. Compress payback with earlier upsells (see [[Hormozi-Offer-Stacking|Offer Stacking]]) and faster billing cadence.
- **Estimate, don't perfect.** LTGP always grows as a business ages because old customers buy more. Calculation methods are deliberately back-of-napkin; precision arrives only after years of cohort data.

## Practical Use

Operating playbook:

1. **Pull last 3/6/9/12 months of marketing + sales spend.** Sum it.
2. **Pull customer count for the same window.**
3. **Compute CAC by channel** if attribution allows. Otherwise compute aggregate, then split estimated %.
4. **Compute GP per customer** using the product or service formula above.
5. **Compute average transactions** (or churn for recurring).
6. **Multiply or divide** to get LTGP.
7. **Compute PPD** by walking through monthly GP collection until cumulative GP ≥ CAC.
8. **Stack against CFA thresholds** — feed all three numbers into [[Hormozi-Customer-Financed-Acquisition|CFA]] to classify Level 1/2/3.

Diagnostic shortcut: if `CAC ≤ 3× industry average`, the lever to focus on is LTGP. If `CAC > 3×`, you have either an advertising or sales problem — diagnose with the question *"Do my engaged leads have the problem I solve and the money to spend?"* (See [[Hormozi-Lead-Getting-Employees|Lead-Getting Employees]] for full diagnostic tree.)

## Notes / Limits
- LTGP is an estimate, not an audited figure. The "right" number is the one that's *directionally* correct and consistent across periods.
- Churn-based LTGP assumes steady-state churn. Early-stage businesses with high churn volatility need cohort analysis instead.
- CAC inputs must include all sales-and-marketing payroll, not just commissions. Founders chronically under-count overhead in CAC.
- Author note flags math depth: chapters were cut from `$100M Money Models` because "everyone gets scared with math." This note is for operators who want the math; lighter teams can use [[Hormozi-Customer-Financed-Acquisition|CFA]] alone.

## Source Basis
- `$100M Lost Chapters`, "The Three Levers of CFA" (pp. 39–41) — three-lever framing.
- `$100M Lost Chapters`, "Know The Levers" (p. 43) — provenance / depth setup.
- `$100M Lost Chapters`, "Cost To Acquire a Customer = CAC" (pp. 45–47) — three worked examples (outreach, content, paid ads), diagnostic note on channel splitting.
- `$100M Lost Chapters`, "Lifetime Gross Profit (LTGP)" (pp. 49–51) — GP definition, churn definition, two LTGP formulas, "arms race of business" framing, Dan Kennedy reference.
- `$100M Lost Chapters`, "Payback Period = PPD" (pp. 53–61) — definition, $50/$100 worked example, 4× compounding analysis.
- Author notes: cut from `$100M Money Models` for math density.
- Indexed in [[Hormozi-100M-Lost-Chapters-Source-Map|100M Lost Chapters — Source Map]].

## Related
- [[00-Book-Home|100M Lost Chapters — Book Home]]
- [[Hormozi-100M-Lost-Chapters-Source-Map|100M Lost Chapters — Source Map]]
- [[Hormozi-Customer-Financed-Acquisition|Hormozi — Customer Financed Acquisition (CFA)]] — the framework these levers feed
- [[Hormozi-Value-Grid|Hormozi — Value Grid]] — visualization for LTGP/30D Cash
- [[Hormozi-Avatar-Selection|Hormozi — Avatar Selection]] — top-of-funnel lever that improves CAC and LTGP simultaneously
- [[Hormozi-Home|Hormozi Home]]

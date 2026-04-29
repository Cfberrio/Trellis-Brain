---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Retention — 'Solving Problems Like The Big Boys' (pp. 5–6)"
sensitivity: internal
hub_role: leaf
book: Retention
---

# Hormozi — Common Factors Method

## Parent
- [[00-Book-Home|Retention — Book Home]]

## Purpose
A meta problem-solving method Hormozi credits to his Department-of-Defense consulting days, then re-applied to gym churn to produce the [[Hormozi-Five-Horsemen-Of-Retention|Five Horsemen]] and (via the Skool dataset) the broader [[Hormozi-Churn-Checklist|Churn Checklist]]. Generalizable beyond retention — it is the method behind both Hormozi frameworks in this book and applies any time the operator faces a complex problem where domain experts already exist. Belongs in the Retention canon as the methodological origin point of the rest of the book.

## Core Idea
> "Talking to people who already know your problem gets you solutions faster than doing it all on your own."
>
> Three steps: ask experts (plural) → collect every answer → solve for the **overlap**.

The bias eliminator is the plural. Any single expert's answer is contaminated by their personal style, history, and incentives. Across many experts, the personal overlay cancels and the structural problem reveals itself in the factors that show up everywhere.

## Framework / Structure

### The three-step method
1. **Ask experts (plural) about the problem.** Experts = people who have already solved this exact problem in the field, not consultants and not theorists. In Hormozi's gym case: gym owners with <3% MoM churn for the last 6 months.
2. **Get all their answers.** Capture comprehensively. Every factor each expert names. Volume matters because the overlap signal only emerges from coverage.
3. **Find common threads (Common Factors Analysis).** Overlap every expert's list. The factors that show up across most experts are the structural ones — solve for those first. Idiosyncratic factors are personal style.

### Worked example (Hormozi's Five Horsemen)
- **Problem:** average gym owner with 15% MoM churn losing 83% of members per year.
- **Experts:** the subset of owners with <3% MoM churn for 6 consecutive months.
- **Answers:** every churn-reducing tactic each one ran.
- **Overlap:** the same five factors appeared across every low-churn owner — became the [[Hormozi-Five-Horsemen-Of-Retention|Five Horsemen of Retention]].
- **Output:** rolled out across the program, churn went 15% → 7% → 3% across three months ("shaking the three" pattern).

### Why the overlap rule works
- **Removes bias.** Each expert's idiosyncratic preferences appear in only one list and wash out.
- **Surfaces structure.** Factors that show up across many experts are doing structural work, not personal-style work.
- **Compresses solution space.** A 25-tactic master list collapses to a 5-factor checklist that can actually be executed.
- **Ranks by signal, not by sentiment.** Factors named by 8 of 10 experts beat the one tactic the loudest expert named — even if the loudest expert is the most successful.

## Strategic Implications
- **The fastest path through a hard problem is usually a known path someone has already walked.** Operators routinely rebuild solutions from first principles when domain experts are reachable. The method exists because reinvention is the slowest move available.
- **Plurality is the bias control.** A single mentor, a single consultant, a single book — none of them survive their personal context. The method only works at sample size; one or two experts is anecdote.
- **Common factors > best practices.** "Best practices" lists are usually a single author's curation. Common-factor analysis is the same exercise done with the source-data exposed and the overlap visible.
- **The method is recursive.** Once a Five-Horsemen-style framework exists, run the Common Factors Method again at the next layer (e.g., the dataset shifts from "gym owners" to "Skool hosts" → produces the Churn Checklist). Each cycle deepens the framework.

## Practical Use
1. **Define the problem precisely** in one sentence, with measurable success ("get monthly churn under 3% within 6 months"). Vague problems produce vague overlaps.
2. **Identify experts using the success metric.** Filter to operators who have already achieved the target outcome — not theorists, not adjacent-field operators.
3. **Interview enough of them.** Practical floor: ~10 experts; Hormozi's gym sample was the entire low-churn cohort in his program. More is better. Ask the same questions the same way each time.
4. **Tabulate every factor each expert names.** One row per factor, one column per expert. Plus a checkmark grid.
5. **Sort by overlap count.** The factors named by most experts go to the top.
6. **Take the top N factors and ship them as the framework.** Hormozi shipped 5. The cut-line is "the highest-frequency factors that explain the outcome and that an operator can actually execute."
7. **Re-run periodically.** When the dataset changes (new platform, new market, new scale), re-run the method on the new expert pool.

## Notes / Limits
- **Method requires a population of experts to interview.** Brand-new categories with no operator base have no expert pool to overlap. In those cases, run a smaller version against your own customers' best users (apply the same method to find your activation point — see [[Hormozi-Activation-Points|Activation Points]]).
- **Survivorship bias is the trap.** "<3% churn for 6 months" is a survivorship filter. The overlap reveals what successful operators *do*; it does not capture what unsuccessful operators *also* did and failed at. Pair the analysis with a quick comparison to a control group of high-churn operators if survivorship risk is high.
- **Overlap is a correlation signal, not a causal proof.** Common factors usually correlate with the outcome and often cause it; not always. Treat the framework as a tested hypothesis, not a theorem. Real validation is shipping it and watching the metric move (Hormozi's 15% → 3% rollout).

## Source Basis
- *$100M Playbook: Retention*, "Solving Problems Like The Big Boys" (pp. 5–6) — three-step DoD-consulting method; "common factors analysis" definition; gym-cohort application that produced the Five Horsemen.
- Indexed in [[Hormozi-Retention-Source-Map|Retention — Source Map]].

## Related
- [[Hormozi-Five-Horsemen-Of-Retention|Hormozi — Five Horsemen of Retention]]
- [[Hormozi-Churn-Checklist|Hormozi — Churn Checklist]]
- [[Hormozi-Activation-Points|Hormozi — Activation Points]]
- [[00-Book-Home|Retention — Book Home]]
- [[Hormozi-Retention-Source-Map|Retention — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]

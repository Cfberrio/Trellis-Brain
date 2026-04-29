---
brand: Trellis-Core
area: strategy-models
subarea: hormozi
note_type: strategy-model
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "$100M Playbook: Retention — 'Churn Checklist #7: Exit Interviews or Cancellation Videos' (pp. 28–29); Churn Checklist tear-off (p. 34)"
sensitivity: internal
hub_role: leaf
book: Retention
---

# Hormozi — Cancellation Saves

## Parent
- [[00-Book-Home|Retention — Book Home]]

## Purpose
Lever #7 of the [[Hormozi-Churn-Checklist|Churn Checklist]]. Converts the cancellation moment from a passive loss into an active save mechanism. Operating thesis: about half the customers who reach a cancellation call can be saved if the operator runs a structured conversation rather than processing the cancellation as a transaction. The other half produce free product feedback. Either outcome is more valuable than letting them silently click "cancel."

## Core Idea
> "You can usually save half of the people who will hop on a cancellation call."

A cancellation request is not a final decision. It is a request for a conversation that the customer expects you to refuse to have. Force the conversation — by policy and onboarding-set expectation — and the save rate is structurally non-trivial. The half who still leave hand you the most expensive form of customer research available (post-mortem on real failure). Both halves are upside relative to a one-click cancel flow.

> "Tell new customers you require cancellation calls."

Set the expectation upfront. Cancellation-by-call is a documented term of service, not an obstacle invented at exit.

## Framework / Structure

### The 50% save heuristic
- ~50% say "F you" → free, high-signal product feedback. Document and apply.
- ~50% are saveable on the call. Two save patterns apply.

### The two save patterns

**1. Save with a redo.**
> "Let me give it another shot and I'll make it right."

Use when the customer's experience fell short of what was sold. The save is operator-side — you re-do the work or service moment that broke. Cost-cheap when relationship and lifetime value justify it.

**2. Save with an upsell.**
Use when the customer's failure-to-get-value was diagnostically a *level-of-service* mismatch — they bought the wrong tier. Move them up; credit their existing payment toward the higher program.

> "You should have been sold into that anyways. And that's on me."

Mechanism: the customer still wants the result; they don't want to leave; the gap was that the offer they bought could not deliver it. Upgrading produces:
- a higher-ticket sale,
- a customer who finally gets the result,
- elimination of the actual root cause of churn.

Operator move: find the unmet expectation; check whether your higher program meets it.

### Channel preference
> "The chances you'll 'save' them on a call are higher than in email or text."

Voice → text → email is the descending save-rate order. Default to voice.

### Save script — the vent-then-validate pattern
For text/email reach-out (when call is not possible):
> "Hey, no pressure. I would love to hear all the reasons you hate me. It would really help me out so that in the future I can avoid it."

On the call itself:
1. **Let them vent.** Do not rebut.
2. **Out-anger the customer.** "That's completely ridiculous. You're 100% correct." Only one person can be in the angry boat at a time. Sitting in the angry seat *with* them removes the seat they came to sit in.
3. **Ask for the make-right.** "Will you give me the opportunity to make it right?"
4. **Lock in the roadmap.** "And just so we're clear — if these things happened, you would be happy?" The answer becomes the operator's checklist for the save.

The customer is rarely after a fight. They want to feel validated. Validation re-opens the relationship.

### Loss-aversion levers (after vent + validate)
> "Tell them what they're gonna lose that they spent time on or gave them status."

Specific things to surface:
- **Custom URLs** — anything personalized, named, or earned.
- **Posts / content / data** — work product they created on the platform.
- **Access** — exclusive groups, calls, tiers.
- **Founder pricing** — grandfathered rate that disappears on cancel and cannot be recovered.

Why it works: humans weigh loss roughly 2× as heavily as equivalent gain. Surfacing what they will *lose* engages a different system than surfacing what they will keep gaining.

> "Many software companies are experts at this. If you lose your data, or it's hard to move it, or you lose work you've done… it's less likely you'll cancel."

### Resell on goal achievement
> "Resell them on why staying helps them achieve their goals."

The customer originally bought to reach a result. Cancellation is implicit declaration that the result is no longer believed reachable through this purchase. The save is to re-link the product to the original goal.

### Cancellation video fallback (high-volume / low-price businesses)
When unit economics make 1-on-1 cancellation calls uneconomical, replace with a forced cancellation video before the cancel button.

Two video jobs:
1. **Resell** — remind them why they started.
2. **Surface losses** — remind them what canceling forfeits.

Asynchronous, scalable, lower save rate than a call but materially better than zero-friction cancel.

### Action step (per source)
> "Tell new customers you do cancellation calls. Get the customers on the phone. Resell them."

Three operational moves: announce policy at signup, route cancel requests to a call, run the script.

## Strategic Implications

- **Cancellations are the most under-priced customer-research channel a business has.** The half who still leave have *just paid you in advance* with their time on a call. Most businesses throw that data away. Operators who capture it learn faster than competitors who only listen to customers who stay.
- **Friction at exit is legitimate when it produces an actual save conversation.** It is illegitimate when it traps customers who genuinely want out. The line is whether you can *save* the conversation, not whether you can *delay* the cancellation.
- **The 50% heuristic is independent of category.** The mechanism is the conversation, not the product type. Documented to work across info products, software, and high-touch service.
- **Save-with-upsell is structurally counterintuitive but dominant.** A cancellation that ends in a higher-ticket sale is a *better* outcome than the original retention. Operators who only think in "save / lose" miss this third quadrant.
- **Loss-aversion levers must be real, not invented.** Surfacing fake losses ("you'll lose your special status") that the customer can verify don't exist destroys trust faster than a clean cancel. Use only assets that the customer actually built or access that actually disappears.
- **Founder pricing is a retention asset, not just a sales tool.** Building grandfathered rates into pricing structure creates a defensible cancellation-saves lever for years.
- **The cancellation-video fallback is a hedge, not a substitute.** Default to calls. Switch to video only when math demands.

## Practical Use

Implementation checklist:
1. **Set policy at signup.** Disclose: "Cancellations require a 5-minute call." Document in TOS and onboarding.
2. **Route cancel requests to a calendar.** Cancel button → booking page, not a confirmation page. The operator (or a save-trained CSM) takes the call.
3. **Build the save kit.**
   - Vent-then-validate script.
   - Decision tree: redo vs. upsell.
   - Loss-list specific to your product (custom URLs, data, posts, founder pricing, exclusive access).
   - Higher-tier offer at the ready (with credit-toward-upgrade pricing).
4. **Track save rate.** Target ≥ 50% saved per the source. If lower, the script is wrong; if higher, the friction may be over-applied (genuine bad-fit customers being trapped).
5. **Capture the lost-half feedback.** Every "F you" answer logged to a feedback file with category tag. Weekly review → product backlog.
6. **For high-volume / low-ticket products**: build the cancellation video. Two scenes: "Why you started" + "What you'll lose." Place it in the cancel flow before the final confirmation.

Operator script for the validation moment:
1. "Tell me everything that's wrong. I want it all."
2. "That's ridiculous. You're 100% right."
3. "Will you let me make this right?"
4. "If A, B, C happened, would you be happy?"
5. (If yes) "Done. Here's the plan." (Then deliver, with a check-in date booked on the same call — see [[Hormozi-Customer-Onboarding|Customer Onboarding]] for follow-through pattern.)

## Notes / Limits

- "Save half" is Hormozi's documented experience, not a guarantee. Save rate scales with operator skill and offer-tier match. New CSMs running this for the first time should expect lower until trained.
- Save-with-upsell only applies when a higher-tier offer genuinely exists *and* the customer's failure was tier-mismatch, not product failure. Forcing an upsell on someone whose product simply did not work creates worse outcomes than letting them leave.
- Forced cancellation calls produce real friction and are perceived as predatory in some categories (consumer subscriptions, low-ticket B2C). Calibrate to category — high-ticket B2B can absorb the friction; impulse-purchase B2C cannot.
- Loss-aversion language can backfire if overplayed. "You'll lose everything" reads as manipulation. Stick to *specific, real* losses (this URL, that data file, that pricing tier).
- Source explicitly notes: voice > text > email for save rate. Do not optimize for operator convenience over save rate.
- Some jurisdictions regulate "click to cancel" — verify legal exposure before mandating phone-only cancellation.

## Source Basis
- *$100M Playbook: Retention*, "Churn Checklist #7: Exit Interviews or Cancellation Videos" (pp. 28–29) — 50% save heuristic, save-with-redo / save-with-upsell patterns, vent-then-validate script, loss-aversion list (data, posts, access, founder pricing), high-volume cancellation-video fallback.
- *$100M Playbook: Retention*, Churn Checklist tear-off (p. 34) — action-step summary used in Practical Use.
- Indexed in [[Hormozi-Retention-Source-Map|Retention — Source Map]] (row 23).

## Related
- [[Hormozi-Churn-Checklist|Hormozi — Churn Checklist]]
- [[Hormozi-Churn-Definition|Hormozi — Churn Definition]]
- [[Hormozi-Customer-Curation|Hormozi — Customer Curation]]
- [[Hormozi-Customer-Survey-ACA|Hormozi — Customer Survey & ACA]]
- [[Hormozi-Customer-Journey-Milestones|Hormozi — Customer Journey Milestones]]
- [[../03-100M-Money-Models/Hormozi-Upsell-Offers|Hormozi — Upsell Offers]] (save-with-upsell tier mechanics)
- [[../01-100M-Offers/Hormozi-Value-Equation|Hormozi — Value Equation]] (vent-then-validate is a Perceived Likelihood lever applied at exit)
- [[00-Book-Home|Retention — Book Home]]
- [[Hormozi-Retention-Source-Map|Retention — Source Map]]
- [[../Hormozi-Home|Hormozi Home]]
- [[../Hormozi-Linking-Contract|Hormozi Linking Contract]]

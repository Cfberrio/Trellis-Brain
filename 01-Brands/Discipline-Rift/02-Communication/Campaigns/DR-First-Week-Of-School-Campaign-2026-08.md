---
brand: Discipline-Rift
area: communication
subarea: campaigns
note_type: campaign
status: draft
canonical: false
used_for_ai: true
source_type: derived
source_reference: "Trellis repo domains/content/discipline-rift/campaigns/2026-08-first-week-of-school-email.md — primary approved by Luis 2026-08-09; §0 five rules + §0.1 production-run learnings from his ChatGPT HTML build; GHL-ready HTML kit at repo email-html/. Refreshed 2026-08-10."
owner: Luis
last_updated: 2026-08-10
sensitivity: internal
hub_role: leaf
audience: parent
channel: [email]
campaign: first-week-of-school-2026-08
---

## Parent
- [[01-Brands/Discipline-Rift/02-Communication/Communication-Home|DR Communication Home]]

## Related
- [[DR-Email-Design-Spec|DR Email Design Spec]] — render contract (now carries the §5.2/§9/§10.1/§11 production rulings)
- [[DR-Parent-Email-Template|DR Parent Email Template]] — the binding drafting contract derived from this campaign
- [[01-Brands/Discipline-Rift/02-Communication/Campaigns/DR-Email-Rewrite-Retrospective-2026-08|Email Rewrite Retrospective]] — full analysis of Luis's breakdown
- [[01-Brands/Discipline-Rift/06-DNA/Problem-Map|DR Problem Map]] — P1, P4, P9, X1
- [[01-Brands/Discipline-Rift/03-Evidence/Founder-Voice/Founder-QA-Library-Full|Founder Q&A Library]] — source interview

> **Build artifacts:** GHL-ready HTML lives in the Trellis repo at `domains/content/discipline-rift/email-html/` — `dr-boilerplate-ghl.html` (reusable 13-slot skeleton) + `2026-08-back-to-school.html` (this campaign, verified reference build). The shipped HTML from Luis's ChatGPT build is pending archive as ground truth.

# DR — First Week of School Campaign (August 2026)

**Brand:** Discipline Rift · Orlando / Central Florida
**Audience:** Parent house list — non-converted leads + prior-season parents who haven't re-registered
**Goal:** Registrations during the first week of school, while the after-school block is the live problem
**Platform:** GHL (email). Merge syntax `{{contact.*}}` only.
**Source:** Luis Torres founder interview (55 Q&A — canonical transcript in Trellis-Brain `03-Evidence/Founder-Voice/Founder-QA-Library-Full.md`) + `communication-rules.md` + `popup-funnel-v2/`
**Status:** Primary email **APPROVED by Luis 2026-08-09** (his finalized structure, verbatim, typos cleaned). Variants B/C rewritten to the same rules, pending his read. Open items in §5.

**Reads with:** [email-design-spec.md](../email-design-spec.md) (render contract) · [dr-marketing-context-from-qa.md](../dr-marketing-context-from-qa.md) (message hierarchy) · [../../ops/discipline-rift/problem-map.md](../../../ops/discipline-rift/problem-map.md) (what this copy is trying to fix)

---

## 0. COPY RULES FROM LUIS — 2026-08-09 (binding for all DR parent-facing marketing)

Luis reviewed the first draft of the primary email and rewrote it. Five rules came out of that review plus what his finalized version deliberately excludes. These override anything below them and anything in older files.

1. **Never diagnose the reader's child, never imply practice is boring.** The attention-gap point ("hold attention on something that isn't entertaining") was cut entirely — not reworded, cut. It confirms a parent's private insecurity ("my child will get distracted") and sells a dull product in the same breath. If a developmental point can't be stated without either effect, it doesn't ship.
2. **Never position as beginner-only.** "Most of our players have never played the sport" tells the family of a returning or experienced player this isn't where they grow — it trades retention for acquisition. A first-timer can start from zero AND a returning player keeps developing; when experience level comes up at all, that's the frame.
3. **Method as fact, not lecture.** Parents never hear method names (retrieval practice, blocked practice, serial practice). "We have a method that does X" — teach, drill, play, not luck — is the ceiling of detail. The science stays internal (coach training, curriculum docs).
4. **The dashboard feeds the parent-child conversation. It never replaces it.** The child answering "fine" is not a reason to stop asking — it's the reason to give the parent the coach's perspective, so they can ask more and deeper questions. Any copy implying "you won't have to ask" is wrong. Parents, players, and coaches communicating clearly is the point; the dashboard is how the parent walks in informed.
5. **One email, few points, chosen hard.** The first draft was an essay. Pick the points most valuable to parents and stop. His finalized version also cuts: the fear frame (replaced with a positive one), the proof stack (55 schools / Level 2 / supervised — trust lives on the site and later touches), all urgency mechanics (deadlines, tier-ladder placement, "the team forms without them," registration-minutes), the age line, and founder editorializing. Close warm, not with a squeeze.

Ruling on CTAs: **one unique action, rendered twice** — a Register button after the hook and one at the end. This supersedes "exactly one CTA button per email" as previously written; the rule was always about competing actions, not button count.

### §0.1 Production-run learnings — 2026-08-09 (Luis built the HTML in ChatGPT against the design spec)

- **The deliverable is built HTML, not a copy doc.** Luis pasted his own raw draft (typos intact) into ChatGPT with the design spec as the prompt — the cleaned repo copy never entered production. Future campaigns ship as GHL-ready HTML + subject/preview alongside the doc, so copy gates and design rules travel as one artifact.
- **He designs by reacting to renders** ("invert it," "get rid of that line," "same layout as before"). First pass = something he can look at, not something he must read.
- **Subject style ruling:** calendar-anchored, plain, direct question. Shipped subject: `Back to school this Tuesday. Are you ready?` Shipped preview: `The supplies are ready. Now what will fill your child's time after 3 PM?`
- **Placement rule for the gap frame:** the after-school-gap framing is allowed in subject/preview *as an open question* — never in the body as fear.
- **Copy compresses at design stage** ("everything else: 80%"). Approval doesn't freeze copy; write lines that survive halving.
- **School start is Tuesday 2026-08-11** (per shipped subject) — resolves open item 2's Monday assumption.
- **Send-check flags raised** (may be in the built HTML): typos "phsyical" / "a real games" / "the teaching the skills"; the internal parenthetical "(not just a bunch of nonsense)"; button URL = homepage rather than `/register` school search.
- **Post-transcript edits by Luis (off-record):** the bedtime line changed and content was cut further below the approved 230 words. **The shipped HTML file is the ground truth and is not yet in the repo** — obtain `discipline-rift-back-to-school-email.html` and archive it under `email-html/sent/` to extract the final deltas precisely.
- **Build-side lessons:** unhosted logo assets silently mutated the design (text-wordmark hero born from the missing PNGs — now the approved fallback); the chain ends in GHL's custom-code editor; Luis's homepage CTA was an explicit instruction, not an oversight; he accepts AI-proposed hero phrases when short; his iteration grain is one element per message → HTML must be block-deletable.

---

## 1. THE STRATEGIC READ

*(Internal analysis. Nothing in this section is parent-facing language — see §0 before lifting any phrase into copy.)*

### 1.1 The commercial moment

The first week of school is the only week when a parent is actively building their child's schedule from zero and has not yet defaulted. By week three the after-school block is filled. The parent is also in list-completion mode — supplies, shoes, forms — which is the campaign's leverage: the email adds one item to a list they're already working through. Per §0.5, the frame is positive ("sports belong on that list") not fear ("the empty block fills itself").

### 1.2 The insight that carries the email

Q13: *"If a child enters a place where there is no clear method, everything depends on luck — on whether they happen to get a teacher who teaches well."* This reframes the purchase from convenience to risk, and it's the one axis where DR can't be price-compared. Per §0.3 it ships as method-as-fact: a method exists, here's what it does, no names.

### 1.3 The readiness gaps

Two ship (motor coordination; what a child does the first time something is hard). The attention gap is real, drives internal method design (Q12, Q34), and is banned from parent-facing copy per §0.1. Both shipped gaps are written as universal to the age with DR carrying the burden — never as a deficiency in the reader's child.

### 1.4 The dashboard

Q4/Q22/Q47: progress is invisible to parents, obvious to coaches, and the child under-narrates. The dashboard closes that gap — coach's update after every practice, progress, photos. Per §0.4 the pitch is "when you ask and hear 'fine,' you'll have more to go on," never "you won't have to ask."

### 1.5 Segments and variants

The self-disqualifying parent ("my kid isn't a sports kid," Q39/Q20) is the largest unaddressed segment — Variant C. The comparison-shopper gets Variant B. Q53 (clubs sell college pipelines) stays implicit: make the near-term concrete, don't name competitors.

### 1.6 Not used in this campaign

DRVC girl story (retention/brand asset — organic + in-season Week 4; consent-gated, involves a minor), Q48 scholarship/pro talk (banned elite positioning), coach-alignment friction and Sebastián's injury (internal), any unmeasured number.

---

## 2. PRIMARY EMAIL — APPROVED (Luis, 2026-08-09)

**Send:** First day of school, 7:00 PM ET.
**Segment:** Full parent list, non-registered. Suppress `reg_paid` and anyone mid-sequence in popup-funnel-v2 Branch A.

**Subject:** `The one thing not on the school supply list`
**Preview text:** `Backpack, shoes, schedule — done. One thing left.`

---

Hi {{contact.first_name}},

The supply list is done. Shoes, backpack, folders, the new bedtime.

But what else isn't on the list? Maybe sports and physical activity?

Yes — sports are as important as everything else. 80% of brain cells focus on movement.

**[ REGISTER ]([REGISTER_LINK])**

Points for our parents to be mindful of:

**1. How their body moves through space.**

The coordination between what they see, where they are, and what they do with it. We're seeing larger groups of players behind in motor coordination.

**2. What they do the first time something is hard.**

At this age, the first conclusion is almost always "I can't do this." What they learn to do next is the part that follows them into the classroom and everywhere else.

**Every practice runs on a method, not mood.**

We teach the skill until a child who has never touched a ball understands it. We drill it in a format they will actually stay engaged in. Then we play a real game using it.

If a program has no method, your child's development comes down to luck. It depends on whether they happen to get a coach who is good at explaining things.

**Easy for you — we will do what is necessary.**

No transportation needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school.

And if you ask "How was practice?" and just hear "Fine":

You will receive one update after every practice from the coach with the information that matters, through the parent dashboard — where you can see your child's progress and photos from the court.

Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season.

**[ REGISTER ]([REGISTER_LINK])**

Wishing your child a valuable, enriched school year.

Coach Luis
Founder, Discipline Rift
info@disciplinerift.com · (407) 614-7454

---

> **Build notes.**
> - Two renders of the same Register CTA (top + bottom) per the §0 ruling. Button label `REGISTER`, uppercase, per the design spec.
> - **The 80% line ships pending phrasing check (open item 1).** The defensible version of the underlying fact: about 80% of the brain's neurons sit in the cerebellum — the part that runs movement. Confirm the wording Luis wants; a parent who searches it should find it holds up.
> - "The information that matters" replaces Luis's internal parenthetical; same meaning, parent-safe.
> - Update cadence is **after every practice**, per Luis's approved copy. This supersedes the `[WEEKLY_UPDATE_DAY]` token from the funnel files for this campaign.
> - Convenience line verbatim per the standing rule. Global footer per `popup-funnel-v2` §2.4.

---

## 3. VARIANT B — "Two questions I get every August"

**Send:** Day 3 · 9:00 AM ET · non-openers of the primary. Rewritten to §0 rules; pending Luis's read.

**Subject:** `Two questions I get every August`
**Preview text:** `And the one that actually decides how the season goes.`

---

Hi {{contact.first_name}},

Every August I get the same two questions. How much is it, and when does it start.

Fair questions. The start date for your school is on your school's page. On cost — it's low cost, everything included, and you see the exact number for your school on the payment screen, before you enter a card.

Here's the question almost nobody asks: **how do you teach it?**

It's the one that decides what your child actually walks away with. Because without a method, a season comes down to luck — whether your child happens to get a coach who is good at explaining things.

Ours is simple to say and hard to do:

**Teach.** Break the skill down until a child who has never touched a ball understands it.

**Drill.** Repeat it in a format they'll actually stay engaged in, with correction.

**Play.** A real game using the exact thing they just learned, so it lands before they go home.

Same structure every week, at every school, grouped by age — because a kindergartner and a fifth grader do not learn or play the same way. A first-timer starts from zero. A player who already knows the sport keeps growing, because the teaching is tiered, not one-size.

No transportation needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school.

Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season.

**[ REGISTER ]([REGISTER_LINK])**

Coach Luis
Founder, Discipline Rift
info@disciplinerift.com · (407) 614-7454

---

> **Build note:** the price answer states where the number lives without promising it in writing — no dollar figure, per the standing rule. No method names per §0.3.

---

## 4. VARIANT C — "If your child isn't 'the sporty one'"

**Send:** Day 5 · 6:30 PM ET · all still unregistered. Rewritten to §0 rules; pending Luis's read.

**Subject:** `If your child isn't "the sporty one"`
**Preview text:** `The player who surprises our coaches most started off to the side.`

---

Hi {{contact.first_name}},

If you're reading this thinking *my kid isn't really a sports kid* — I want to tell you which player surprises our coaches the most.

It isn't the one who shows up already good.

It's the one who spends the first couple of practices standing slightly outside the group. Quiet. Not sure they want to be there. And then somewhere in the middle of the season, they're the one demonstrating the drill for everybody else.

That happens often enough that we plan for it.

Here's what usually happens in between. The first time a skill doesn't work, almost every child this age reaches the same conclusion: *I can't do this.* What we teach next is most of the point of the whole thing — you can try again, you can ask for help, you can use the correction the coach just gave you. A child who learns to ask for help in a gym is learning something that has very little to do with the gym.

The season is built so a child starting from zero can get there — and so a player who already knows the sport keeps growing. The teaching is tiered, not one-size.

No transportation needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school.

And when you ask about practice, you'll know what to ask about: the coach sends an update after every practice through the parent dashboard, with your child's progress and photos from the court.

Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season.

**[ REGISTER ]([REGISTER_LINK])**

Coach Luis
Founder, Discipline Rift
info@disciplinerift.com · (407) 614-7454

---

## 5. OPEN ITEMS — resolve before send

| # | Item | Who | Blocks |
|---|---|---|---|
| 1 | **80% phrasing.** Approved copy says "80% of brain cells focus on movement." Defensible form: ~80% of the brain's neurons are in the cerebellum (movement). Confirm final wording. | Luis | Primary |
| 2 | ~~School start date~~ **Resolved:** Tuesday 2026-08-11, per Luis's shipped subject line. Residual: confirm the list doesn't span districts with different start dates. | Luis | Send timing |
| 3 | **Parent dashboard live for every registered parent, with per-practice coach updates and photos actually posted per team.** Claimed in the approved copy; `communication-rules.md` (April) still says "if a parent dashboard exists." | Luis | All three |
| 4 | **Value Guarantee operational status** — wording now "teaching the skills and the passion for the sport" per Luis. Confirm ops honors it; align site footer wording. | Luis | All three |
| 5 | **Suppression list** — `reg_paid` for current season + anyone mid-sequence in Branch A. | Dev / GHL | All three |
| 6 | **Variant B/C school-page claim** — B says the start date is on the school's page; confirm every school page shows dates. | Dev | B |

Resolved by Luis's rewrite (no longer apply): weekly-update day token, registration-minutes claim, retrieval-practice adoption gate, ages line (no age range stated; where grade context is needed anywhere else, it's Elementary / K–5th per the live site — not "ages 6–12").

---

## 6. SEND PLAN

| Touch | Timing | Asset | Segment |
|---|---|---|---|
| 1 | First day of school · 7:00 PM | §2 Primary (approved) | All unregistered |
| 2 | Day 3 · 9:00 AM | §3 Variant B | Non-openers of touch 1 |
| 3 | Day 5 · 6:30 PM | §4 Variant C | All still unregistered |

Clicks that don't complete registration hand off to `popup-funnel-v2/05-abandoned-registration.md`; fresh opt-ins enter the lead funnel. Read results on registrations, not opens. If touch 3 out-converts touch 1, the self-disqualifying-parent segment is the real market.

---

## 7. WHERE THE REST OF THE INTERVIEW ROUTES

- **DRVC girl / "aren't we DRVC?" (Q6, Q16)** → organic + in-season Week 4 email. Consent-gated (minor).
- **Mila (Q26, Q45)** → organic + re-enrollment story.
- **Sculpture arc (Q6, Q17)** → school-outreach deck.
- **Q30 parent phrases** ("always a chance to start again," "we can always give a bit more," "losing is also winning") → in-season parent emails.
- **Q29/Q41/Q46 growth signals** → observation cues in the per-practice update, so parents know what to watch for and ask about.
- **Q25 (why yelling doesn't correct)** → coach training + founder content.
- **Named methods (Q18)** → internal only: coach training and curriculum. Not the site, not ads, not parent email — per §0.3 parents get "a method, not mood."

---
brand: Discipline-Rift
area: communication
subarea: evidence
note_type: source-transcript
status: active
canonical: false
used_for_ai: true
source_type: verbatim-extraction
source_reference: "Extracción read-only 2026-11-23 (agente Claude). Nombres/correos/teléfonos de padres e hijos removidos. Fuente: local"
owner: Luis
last_updated: 2026-11-23
sensitivity: internal
hub_role: leaf
audience: parent
channel: [email]
up:
  - "[[01-Brands/Discipline-Rift/02-Communication/Communication-Home]]"
related:
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Marketing-Email-Language-Guide]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Campaigns/DR-Marketing-Email-History-Index]]"
---

# DR outbound email: local-source extraction (verbatim)

Extracted 2026-11-23. Read-only pass over the Trellis-Brain vault, the Trellis repo (`/Users/cberrio04/Documents/CLAUDE CODE`, including git history), the DR repo (`/Users/cberrio04/Documents/DISCIPLINERIFT/disciplinerift`), DR auto-memory, and ~/Downloads and ~/Desktop.

**Important finding:** `domains/content/discipline-rift/` (the campaigns, the email-html kit and popup-funnel-v2) **no longer exists on disk** in the Trellis repo. It is in git history only (last commit `a78b5c7`, 2026-08-11). It was extracted read-only to `scratchpad/git/domains/content/discipline-rift/`. The `brand-kit/email/dr-boilerplate-ghl.html` path cited in the vault is also missing on disk.

Legend for STATUS: **SENT** = evidence it went to parents · **LIVE-AUTO** = live automation that is sending now · **APPROVED** = Luis approved, not proven sent · **DRAFT** = never approved or shipped · **RULE** = a wording or structure rule · **TRANSACTIONAL** = operational, use for voice reference only.

---

## 1. Inventory

| # | File | What it is | Date | Status |
|---|---|---|---|---|
| 1 | `DISCIPLINERIFT/disciplinerift/supabase/functions/_shared/email-templates.ts` → `parentGuideHtml()` + `send-parent-guide/index.ts` | "Here you go! 3-minute Parent Guide": the lead-magnet email (newsletter/popup opt-in) | code last changed 2026-11-04; seen in info@ Sent 2026-06-25 | **LIVE-AUTO / SENT** |
| 2 | `Trellis-Brain/.../03-Evidence/Founder-Voice/email-sent-analysis-2026-06-30.md` §A1 | Same Parent Guide email as captured from the Sent folder; also has a faculty cold-outreach template | extracted 2026-06-30 | **SENT** (evidence) |
| 3 | git `a78b5c7:domains/content/discipline-rift/email-html/2026-08-back-to-school.html` | Back-to-school primary, GHL-ready HTML build (the "verified reference build") | 2026-08-10 | **SENT** (shipped subject 2026-08-11; Luis's ChatGPT HTML is the true ground truth and was never archived) |
| 4 | `Trellis-Brain/.../02-Communication/Campaigns/DR-First-Week-Of-School-Campaign-2026-08.md` (= git `campaigns/2026-08-first-week-of-school-email.md`) | First-week-of-school campaign: approved primary + Variants B/C + **Luis's 5 rules** | last_updated 2026-08-10 | Primary **APPROVED**; B/C **DRAFT** (pending Luis's read); §0 **RULE** |
| 5 | `Trellis-Brain/.../Campaigns/DR-Email-Rewrite-Retrospective-2026-08.md` | Analysis of Luis's rewrite: what he cut and added | 2026-08-10 | **RULE** |
| 6 | `Trellis-Brain/.../02-Communication/DR-Parent-Email-Template.md` | Binding house-list drafting contract (10 slots, 230-word cap) | 2026-08-10, assets resolved 2026-08-25 | **RULE** (canonical) |
| 7 | `Trellis-Brain/.../02-Communication/DR-Email-Design-Spec.md` §5.2, §5.9, §6, §9, §10, §10.1, §11 | Render contract + copy rules + pre-send checklist | 2026-08-25 | **RULE** |
| 8 | `DISCIPLINERIFT/disciplinerift/docs/emails/campaign-unregistered-attended-winter26-{andover,baldwin-park,hamlin}.html` + `ghl-unregistered-attended-winter26.html` | "X is not registered for volleyball yet" (attended practice without registering) | sent 2026-10-30 (3/3 via info@) | **SENT** |
| 9 | `.../docs/emails/campaign-winter-pinecrest-avalon-days.html` | Winter re-enroll: "Flag Football Mondays, Tennis Tuesdays" (correction + spots) | sent 2026-10-26 (22 recipients, dashboard) | **SENT** |
| 10 | `.../docs/emails/campaign-winter-pinecrest-avalon-soccer.html` | Winter re-enroll: "Soccer starts Thursday" | sent 2026-10-27 (22/22 via Composio Gmail) | **SENT** |
| 11 | `.../docs/emails/campaign-youre-in-{isai-deerwood,marcella-sunblaze}-oct8.html` | "You're in for Fall 2026" (mid-season add) | 2026-10-08 | **SENT** (transactional-ish) |
| 12 | `.../docs/emails/campaign-season-cancel-low-registration.html` | Season canceled due to low registration | 2026-10-26 | **SENT**, TRANSACTIONAL |
| 13 | `.../docs/emails/campaign-{storm,rainy,weather,makeup,practice-on,no-practice,delayed,correction,tournament,cancel-week}-*.html` (~25 files) + `faculty-*.html` | Operational one-off parent/faculty campaigns | 2026-09-30 → 2026-11-20 | **SENT**, TRANSACTIONAL (not transcribed; same shell/sign-off as #8–#10) |
| 14 | `email-templates.ts` → `waitlistInviteHtml()` + `waitlist-invite/index.ts` | "You're invited to register for {team}" | live since 2026-08-18 (manual invite) | **LIVE-AUTO** |
| 15 | `email-templates.ts` → `seasonReminderHtml()` / `seasonReminderSubject()` | 15/7/1-day season-start reminders | live 2026-09-01 | **LIVE-AUTO**, TRANSACTIONAL |
| 16 | `Trellis-Brain/.../ClickUp-Verbatim/WEEKLY-N8N/09…14-*.md` | Weekly practice-eve emails, Weeks 1–6 (Luis's own final draft 2026-08-31) | 2026-08-31 | TRANSACTIONAL (Luis-written) |
| 17 | `Trellis-Brain/.../Templates/Operational-Email-Library.md` + `ClickUp-Verbatim/03,04,05` | 15/7/1-day reminder copy rewrites (n8n era) | 2026-08-31 | TRANSACTIONAL (superseded in production by #15) |
| 18 | `Trellis-Brain/.../Sequences/DR-Lead-Magnet-Sequence.md` | 6-email lead-magnet sequence (guides + SIBLING code) | 2026-07-23 | **DRAFT** |
| 19 | `Trellis-Brain/.../Sequences/DR-Registration-Sequence.md` (Branch B R1–R3) | Cart-recovery emails/SMS | 2026-07-23 | **DRAFT** (a real GHL abandonment automation exists; its copy is not stored locally) |
| 20 | git `a78b5c7:.../popup-funnel-v2/03-lead-funnel.md` | Lead funnel v2: guide delivery + 10% code + SMS + 72h close | 2026-08-11 | **DRAFT** ("Draft v1 for review") |
| 21 | git `a78b5c7:.../popup-funnel-v2/03-sequence-a…, 04-sequence-b…, 05-abandoned-registration.md, 01-popup.md, 02-lead-magnet.md, 00-audit-live-v1.md` | 30-day nurture branches, abandoned-registration and popup specs; the audit describes the live v1 funnel | 2026-08-04 → 08-11 | **DRAFT** (00 = audit of live v1) |
| 22 | git `a78b5c7:.../dr-comms-rewrite-prompt.md`, `dr-marketing-context-from-qa.md`; git `69be6e6:.agents/product-marketing-context.md` | Language contract, banned words, claim rule, structural rules S1–S10 | 2026-07-09 → 08-11 | **RULE** (partly superseded by #4–#7) |
| 23 | `Trellis-Brain/.../02-Communication/Marketing-Language-Library.md` | Keyword buckets + excluded terms (ClickUp KEYWORDS - ADS / MARKETING) | 2026-05-21 | **RULE** |
| 24 | `Trellis-Brain/.../02-Communication/communication-rules.md` | Voice rules, subject-line rules, signature, "what DR is not" | authored 2026-04-21, verified 2026-08-27 | **RULE** (older; partly superseded) |
| 25 | `Trellis-Brain/.../00-Brand-Core/Voice-and-Tone.md` | Voice posture, avoid list, cultural refrains | 2026-09-17 | **RULE** |
| 26 | `Trellis-Brain/.../02-Communication/DR-Parent-Communication-Philosophy.md` | Luis's parent message, verbatim (2026-09-15/16 dictation) | 2026-09-17 | **RULE** |
| 27 | `Trellis-Brain/.../02-Communication/DR-Communication-Audit-2026-08-04.md` §6 | Canon conflicts (fun-first, pricing, trial, age, SMS, syntax) | 2026-08-04 | **RULE** (context) |
| 28 | `Trellis-Brain/02-Meetings/2026-10-29 SyncUp DR Executives (26677).md` | Luis: emails should read as written by the coach; app-adoption cadence D1/D3/D6 email, D9 SMS, D12 "last chance" | 2026-10-29 | **RULE** / decision |
| 29 | `DISCIPLINERIFT/disciplinerift/docs/proposals/2026-11-23-app-download-campaign.md` | Draft copy for the "Download the app" campaign (D1–D12) | 2026-11-23 | **DRAFT** (today; pending Luis) |
| 30 | `Trellis-Brain/.../00-Brand-Core/offers-evidencia.md` l.73 | Fragment from ClickUp "Volleyball Registration Campaign — Finalized Content": "It was only $129 for a six-week season…" | observed 2026-10-21 | fragment only (full page is in ClickUp, not local) |
| 31 | DR memory: `project-dr-winter26-sms-invite.md`, `project-dr-pinecrest-soccer-winter-send.md`, `project-dr-unreg-attended-winter26.md`, `project-dr-refund-promo-registered.md` | Send records + Fall→Winter SMS line | Oct–Nov 2026 | **SENT** (records) |
| 32 | `Trellis-Brain/.../03-Evidence/Founder-Voice/bot-training/01-PARENTS.md` | Luis's real 1:1 parent replies | 2026 | voice reference (not marketing) |
| 33 | `Trellis-Brain/.../02-Communication/fall-campaign-and-content-strategy-2026.md` | Fall angle: "Don't know what to do this year? Try sports." | 2026-10-16 | **RULE** / decision |

**Not found locally (gaps):**
- **The GHL-built marketing campaigns.** Memory says they carry "100% refund" and "Value Guarantee" in the footer, but the GHL API has no scope for email templates.
- **The live GHL newsletter-nurture copy.** `dr_ghl_newsletter` only posts to a webhook.
- **The live GHL abandonment copy.**
- **The v1 popup emails at 18h and 40h.** Only the audit's quoted fragments survive: "REGISTER FOR THE SEASON", "Before registration closes, here is the direct link", "Our upcoming season is filling and we finalize rosters soon", signed "From Coach Luis".
- **No old Wix newsletters** anywhere.
- **Nothing relevant in ~/Downloads or ~/Desktop.** The only DR file there, `Mensajes-Coaches-Winter-2026.pdf`, is a coach-message stats report.

---

## 2. Verbatim marketing emails

### 2.1 Parent Guide delivery: LIVE-AUTO / SENT (source #1; same copy as #2, Sent 2026-06-25)

**Subject:** `Here you go! 3-minute Parent Guide`
**From name:** Discipline Rift
**Hero:** Here you go! Your 3-minute Parent Guide
**Hero sub:** From Coach Luis at Discipline Rift

```
Hi {name},

What if this was the season your child did not just participate…
But discovered something about themselves?

The first time they understand a new skill.
The first time they try again after struggling.
The first time they feel like they belong in a group.

Many children stop participating in organized activities before middle school… Not because they lack ability, but because they did not feel supported or capable early on.

Here are five simple ways you can strengthen your child's experience starting this week.

1. Start Every Week with Curiosity
After each session, ask open ended questions:
What felt good today?
What was challenging?
Can you show me something new you practiced?
Curiosity builds reflection. Reflection builds growth.

2. Create a 10 Minute Ritual
Set aside ten minutes twice a week to move together. The goal is connection, not correction. When children associate structured activity with bonding, they stay engaged longer.

3. Celebrate Small Wins
Notice effort, not just results.
Trying again. Staying focused. Listening well.
Confidence grows when progress is seen.

4. Let Them Teach You
Ask your child to explain something they learned. Teaching strengthens understanding and reinforces self belief.

5. Talk About Growth
Have conversations about perseverance, teamwork, and character. These are the qualities that last long after any season ends.

Structured programs can accelerate this growth when they are developmentally appropriate and focused on confidence before competition.

Our upcoming season is designed with that intention:
Small groups.
Intentional coaching.
Progression based learning.
An environment where children feel capable.

If this feels like the right next step for your child:

[REGISTER FOR THE SEASON] → https://www.disciplinerift.com/register
[FIND YOUR SCHOOL] (ghost button) → https://www.disciplinerift.com/register

What if this season everything shifts?   (italic, blue)
```
**Footer note:** This email was sent because you signed up for the Discipline Rift Parent Guide.

> ⚠ This email is still live, but later rules ban much of it. The v1 audit and the rewrite prompt flag: the unsourced "stop… before middle school" stat; the motivational "What if…" framing; the soft outcome (character/belonging) used as the promise; the two competing CTAs; and the magnet adding parent homework. Use it as evidence of what was sent, not as a model.

---

### 2.2 Back-to-school primary: SENT (source #3, the build; the approved copy text is in #4)

**Subject (shipped):** `Back to school this Tuesday. Are you ready?`
**Preview (shipped):** `The supplies are ready. Now what will fill your child's time after 3 PM?`
**Hero:** `DISCIPLINE RIFT` (giant blue wordmark, nothing under it)
**Send plan:** first day of school (Tue 2026-08-11), 7:00 PM ET, all non-registered (suppress `reg_paid`)

```
Hi {{contact.first_name}},

The supply list is done. Shoes, backpack, folders, the new bedtime.

But what else isn't on the list? Maybe sports and physical activity?

Yes — sports are as important as everything else.

[ REGISTER ] → https://disciplinerift.com/

Points for our parents to be mindful of:

1. How their body moves through space.
The coordination between what they see, where they are, and what they do with it. We're seeing larger groups of players behind in motor coordination.

2. What they do the first time something is hard.
At this age, the first conclusion is almost always "I can't do this." What they learn to do next is the part that follows them into the classroom and everywhere else.

Every practice runs on a method, not mood.
We teach the skill until a child who has never touched a ball understands it. We drill it in a format they will actually stay engaged in. Then we play a real game using it.

If a program has no method, your child's development comes down to luck. It depends on whether they happen to get a coach who is good at explaining things.

Easy for you — we will do what is necessary.
No transportation needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school.

And if you ask "How was practice?" and just hear "Fine":
You will receive one update after every practice from the coach with the information that matters, through the parent dashboard — where you can see your child's progress and photos from the court.

Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season.

[ REGISTER ] → https://disciplinerift.com/

Wishing your child a valuable, enriched school year.

Coach Luis
Founder, Discipline Rift
info@disciplinerift.com · (407) 614-7454
```
**Footer:** Value Guarantee · Running at 55 schools in Central Florida / 713 W Yale St, Orlando FL 32804 · (407) 614-7454 / info@disciplinerift.com / Privacy · Terms · Unsubscribe · © Discipline Rift (Torres Rivero LLC)

**How it differs from the approved doc (#4 §2):**
- The doc's subject `The one thing not on the school supply list` and preview `Backpack, shoes, schedule — done. One thing left.` were **replaced** by the shipped ones above.
- The approved line "80% of brain cells focus on movement." is **absent** from the build (its phrasing was an open item).
- Luis made further off-record cuts to his own ChatGPT HTML. That file was never archived.

---

### 2.3 First-week Variant B: DRAFT (source #4 §3; Day 3, 9:00 AM, non-openers; "pending Luis's read")

**Subject:** `Two questions I get every August`
**Preview:** `And the one that actually decides how the season goes.`

```
Hi {{contact.first_name}},

Every August I get the same two questions. How much is it, and when does it start.

Fair questions. The start date for your school is on your school's page. On cost — it's low cost, everything included, and you see the exact number for your school on the payment screen, before you enter a card.

Here's the question almost nobody asks: how do you teach it?

It's the one that decides what your child actually walks away with. Because without a method, a season comes down to luck — whether your child happens to get a coach who is good at explaining things.

Ours is simple to say and hard to do:

Teach. Break the skill down until a child who has never touched a ball understands it.

Drill. Repeat it in a format they'll actually stay engaged in, with correction.

Play. A real game using the exact thing they just learned, so it lands before they go home.

Same structure every week, at every school, grouped by age — because a kindergartner and a fifth grader do not learn or play the same way. A first-timer starts from zero. A player who already knows the sport keeps growing, because the teaching is tiered, not one-size.

No transportation needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school.

Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season.

[ REGISTER ]([REGISTER_LINK])

Coach Luis
Founder, Discipline Rift
info@disciplinerift.com · (407) 614-7454
```

### 2.4 First-week Variant C: DRAFT (source #4 §4; Day 5, 6:30 PM, all still unregistered)

**Subject:** `If your child isn't "the sporty one"`
**Preview:** `The player who surprises our coaches most started off to the side.`

```
Hi {{contact.first_name}},

If you're reading this thinking my kid isn't really a sports kid — I want to tell you which player surprises our coaches the most.

It isn't the one who shows up already good.

It's the one who spends the first couple of practices standing slightly outside the group. Quiet. Not sure they want to be there. And then somewhere in the middle of the season, they're the one demonstrating the drill for everybody else.

That happens often enough that we plan for it.

Here's what usually happens in between. The first time a skill doesn't work, almost every child this age reaches the same conclusion: I can't do this. What we teach next is most of the point of the whole thing — you can try again, you can ask for help, you can use the correction the coach just gave you. A child who learns to ask for help in a gym is learning something that has very little to do with the gym.

The season is built so a child starting from zero can get there — and so a player who already knows the sport keeps growing. The teaching is tiered, not one-size.

No transportation needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school.

And when you ask about practice, you'll know what to ask about: the coach sends an update after every practice through the parent dashboard, with your child's progress and photos from the court.

Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season.

[ REGISTER ]([REGISTER_LINK])

Coach Luis
Founder, Discipline Rift
info@disciplinerift.com · (407) 614-7454
```

---

### 2.5 "Not registered yet" (attended without registering): SENT 2026-10-30 (source #8; GHL template version)

**Subject:** `{{contact.unreg_kid}} is not registered for volleyball yet` (sent example: `Cassidy is not registered for volleyball yet`)
**Preview:** `{{contact.unreg_kid}} attended practice this week. Here is the Winter schedule and the link to register.`
**Eyebrow/hero:** DISCIPLINE RIFT / **Almost on the roster.** / {kid} is not registered for volleyball yet / {school}

```
Hi {{contact.first_name}},

Your child {{contact.unreg_kid}} attended volleyball practice this week and has not been registered for the Winter season yet.

Whenever possible, please head to our website, disciplinerift.com, and register {{contact.unreg_kid}} for the team, ideally before the next practice on {{contact.unreg_next_practice}}.

Winter Season Schedule
{{contact.unreg_day_time}}            e.g. "Mondays, 3:15–4:15 PM"
{{contact.unreg_dates}}               e.g. "Oct 26 – Dec 7 (no practice Nov 23, Thanksgiving week)"
Practices: {{contact.unreg_practice_list}}   e.g. "Oct 26, Nov 2, Nov 9, Nov 16, Nov 30, Dec 7"

[ Register {{contact.unreg_kid}} ] → {{contact.unreg_link}}  (disciplinerift.com/register?schoolId=N)

If you have any questions, please let us know. Just reply here or call (407) 614-7454.

See you at practice!

Coach Luis
Founder, Discipline Rift
```
**Footer (all Oct–Nov campaigns):** DISCIPLINE RIFT / Discipline Rift · Torres Rivero LLC / 713 W. Yale Street, Orlando, FL 32804 / info@disciplinerift.com · (407) 614-7454 · www.disciplinerift.com
(Memory: the structure is Luis's ("estructura del jefe"), with a dated schedule added.)

### 2.6 Winter re-enroll, Pinecrest Avalon (days correction + spots): SENT 2026-10-26 (source #9)

**Subject:** `Pinecrest Avalon Winter: Flag Football Mondays, Tennis Tuesdays`
**Preview:** `We listed the Winter days wrong. Flag Football is on Mondays, Tennis on Tuesdays — and there are still spots.`
**Hero:** DISCIPLINE RIFT / **Winter is on.** / Flag Football Mondays · Tennis Tuesdays / Pinecrest Avalon Elementary School

```
Hi {PARENT_FIRSTNAME},

Quick correction: we listed the Winter days wrong earlier. Here are the real days — and there are still spots open.

Flag Football
Every Monday, 3:15–4:15 PM
Started Oct 26 · 12 spots left

Tennis
Every Tuesday, 3:15–4:15 PM
Starts Oct 27 · 3 spots left

Team meets in the Lobby at 2:45 PM. All gear is provided.

[ Save a spot ] → https://disciplinerift.com/register?schoolId=29

Questions? Just reply here or call (407) 614-7454.

See you at practice!

Coach Luis
Founder, Discipline Rift
```
**Footer line:** You are receiving this because your child played {TEAM_NAME} with us in Fall 2026.

### 2.7 Winter re-enroll, Pinecrest Avalon Soccer: SENT 2026-10-27 to 22 (10 Fall families who had not re-registered + 12 waitlist) (source #10)

**Subject:** `Pinecrest Avalon Winter: Soccer starts Thursday`
**Preview:** `Kindergarten through 5th grade. Team meets in the Lobby at 2:45 PM, all gear provided.`
**Hero:** DISCIPLINE RIFT / **Winter is on.** / Soccer starts this Thursday / Pinecrest Avalon Elementary School

```
Hi {PARENT_FIRSTNAME},

{INTRO}            (personalized per recipient: names the kids for Fall families; the variants were not saved)

Soccer
Every Thursday, 3:15–4:15 PM
Oct 29 – Dec 10 (no practice Nov 26) · Kindergarten–5th grade · {SPOTS} spots left

Team meets in the Lobby at 2:45 PM. All gear is provided.

[ Save a spot ] → https://disciplinerift.com/register?schoolId=29

Questions? Just reply here or call (407) 614-7454.

See you at practice!

Coach Luis
Founder, Discipline Rift
```

### 2.8 Fall→Winter SMS invite: SENT 2026-10-24 to 224 parents (source #31; from memory, Luis's line)

```
Hi {first}! {SMS Kids} {SMS Verb: isn't/aren't} registered yet for the next {SMS Sport} season, starting next week!
```

### 2.9 Waitlist invite: LIVE-AUTO (source #14)

**Subject:** `You're invited to register for ${teamName}`
**Hero:** You're invited to register! / A spot is open on {team}

```
Hi {name},        (fallback "Hi there,")

Good news — a spot is available on {team} ({sport}), and we'd love to have your child join us.

Tap below whenever you're ready to complete your registration.

[ REGISTER NOW ]
If the button doesn't work, paste this link into your browser: {url}

What happens next
1. Tap the button above to open your registration.
2. Confirm your details and complete checkout.
3. Your child's spot on {team} is confirmed. Done.

Spots are filled as families register, so we recommend completing yours when you get a chance. Questions? Just reply to this email.
```
**Footer:** You're receiving this because you joined the waitlist for {team} at Discipline Rift.
(Code comment rule: "no seat is being held and the link never expires, so the copy carries no deadline, no countdown and no scarcity.")

### 2.10 "You're in" (mid-season add): SENT 2026-10-08 (source #11, Marcella example)

**Subject:** `You're in for Fall 2026` · **Preview:** `Marcella is on the roster. Here's what's left of the season.`

```
Hi {PARENT_FIRSTNAME},
Marcella is now on the current season's volleyball team. Here's what's left of Fall 2026:
🏐 Remaining practices
Tomorrow, Friday, October 9th · 3:15–4:15 PM
Friday, October 16th · 3:15–4:15 PM
Last practice of the season
Practices are on campus right after school. No transportation needed.
Winter 2026: Marcella is already registered. Winter practices start Friday, October 30th.
Questions? Just reply here or give us a call.
[CALL (407) 614-7454]
See you on the court!
Coach Luis
Founder, Discipline Rift
```

---

### 2.11 Drafts never confirmed sent (verbatim kept short; full files cited)

#### a) Lead-Magnet Sequence: DRAFT 2026-07-23 (source #18), signed "The Discipline Rift Team", syntax `{UPPERCASE}`

| # | Timing | Subject | Preview |
|---|---|---|---|
| 0 | immediately (+ SMS) | Here's your guide, {PARENT_FIRST_NAME} 👇 | Plus a few more we think you'll want. |
| 1 | +1 day | The one question to ask after every practice | Works even on a rough day. |
| 2 | +2 days | 4 red flags a youth program is overpromising | We'd rather lose your business than oversell. |
| 3 | +4 days | Is a program actually built for your kid's age? | A 6-question checklist. |
| 4 | +6 days (+ SMS) | See if Discipline Rift is at your school | On campus, right after class. Beginner-friendly. |
| 5 | +8 days | Seasons are filling near you | A quick nudge before spots go. |

Email 5 body (verbatim):
```
Hi {PARENT_FIRST_NAME},

Quick one. Our seasons run on the school calendar, and teams fill on a first-come basis — once a team's full, that's it until next season.

If you've been thinking about it, now's the moment to grab a spot:
[ Find your school & register ] → {SCHOOL_SEARCH_URL}

Two kids? Use code SIBLING for 10% off the second registration.

No pressure either way — we'll keep sending you useful stuff for parents whether you register now or later.

The Discipline Rift Team

{UNSUBSCRIBE_URL}
```
Email 4 body (verbatim):
```
Hi {PARENT_FIRST_NAME},

Here's the simplest version of what we do:

Your child learns a sport — volleyball, tennis, or pickleball — right at their own school, in the hour after class. Trained coaches. Beginner-friendly to advanced. A season structured so you can actually see progress, tier by tier. No transportation needed — our coaches handle everything from dismissal, on campus.

The only thing that matters right now: is your school on the list?

[ Find your school ] → {SCHOOL_SEARCH_URL}

If it is, registration takes a couple of minutes. If it's not, reply and tell us your school — we're adding new ones every season.

The Discipline Rift Team

{UNSUBSCRIBE_URL}
```
Email 4 SMS: `Discipline Rift: want to see if we're at your child's school? Search here 👉 {SCHOOL_SEARCH_URL}` / `On campus, after class, beginner-friendly. Reply STOP to opt out.`
(Emails 0–3 are in the file; they carry the Parent Guides 1–4 from `Templates/Parent-Guides-Library.md`.)

#### b) Cart recovery R1–R3: DRAFT 2026-07-23 (source #19)

- **R1** (+1h) Subject `You're almost done — {STUDENT_FIRST_NAME}'s spot is held` · Preview `Finish in under a minute.`
  ```
  Hi {PARENT_FIRST_NAME},
  You started registering {STUDENT_FIRST_NAME} for {SPORT} at {SCHOOL_NAME} — you're one step from done. We're holding the spot for you.
  [ Finish registration ] → {REGISTER_URL}
  If something came up or you have a question, just reply — happy to help.
  The Discipline Rift Team
  ```
- **R2 SMS** (+24h): `Discipline Rift: {STUDENT_FIRST_NAME}'s spot for {SPORT} at {SCHOOL_NAME} is still open, but teams are filling for the season.` / `Finish here (takes <1 min): {REGISTER_URL}` / `Reply STOP to opt out.`
- **R3** (+72h) Subject `Last call for {STUDENT_FIRST_NAME}'s spot` · Preview `We'll release the hold soon.`
  ```
  Hi {PARENT_FIRST_NAME},
  We've been holding {STUDENT_FIRST_NAME}'s spot for {SPORT} at {SCHOOL_NAME}, but the season is filling and we'll need to release it soon.
  If you still want in:
  [ Complete registration ] → {REGISTER_URL}
  A reminder of why parents choose us: it's on campus, right after school, beginner-friendly, and we actually teach the sport. If we don't deliver, you get a 100% refund, any time during the season.
  If now isn't the right time, no problem — we'll be here next season.
  The Discipline Rift Team
  ```
  (The popup-v2 review flagged R2/R3 as non-compliant: vague scarcity and the wrong signature.)

#### c) Lead funnel v2: DRAFT (source #20), signed "From Coach Luis / Discipline Rift / info@disciplinerift.com / (407) 614-7454"

- **T0** (immediately) `Here it is: the hour your child calls "good"` · Preview `One practice, start to finish, block by block.`
  ```
  Hi {{contact.first_name}},
  Here is the guide.
  It is one practice at a Discipline Rift season, written out from the bell to pickup. What we teach in each block, why the structure never changes, and the things your coach writes down that your child is never going to mention at dinner.
  It takes about six minutes to read. There is nothing in it for you to do.
  [ Read the guide ] → [GUIDE_URL]
  One thing worth knowing while you read it: the sport running at your child's school changes by campus and by season. When you are ready, the registration page opens with a school search so you can see what is on offer at yours.
  ```
- **T1** (23h) `The difference between watching kids and teaching them` · Preview `Plus something to use before Sunday.`. Root problem ("no method… depends on luck"), Luis quote **"If a child enters a place where there is no clear method, everything depends on luck."**, 10% `[DISCOUNT_CODE]`, guarantee "No claim window, no fine print about how many practices your child attended."
- **T2 SMS** (24h): `Hi {{contact.first_name}}, Coach Luis here. I sent you an email about an hour ago with a code in it for your child's season. Worth opening before it runs out. Reply STOP to opt out.`
- **T3** (72h) `Your code runs out tomorrow` · Preview `And a last thought before the season fills.`. Includes "The child who surprises our coaches most is almost never the athletic one…" and the P.S. "If the timing is wrong this season, just reply and tell me. I will make sure you hear about the next one first."
- Full copy: `scratchpad/git/domains/content/discipline-rift/popup-funnel-v2/03-lead-funnel.md` lines 113–290.

#### d) popup-funnel-v2 branch sequences: DRAFT (source #21), subjects only (full copy in the scratchpad git extract)

- **A (school covered):**
  - `Your Parent Guide — and yes, we're at {{contact.child_school}}`
  - `The part parents ask about first: dismissal`
  - `If your child has never played {{contact.season_sport}}`
  - `Who's actually standing on that court with your kid`
  - `What a season costs you — in money and in weeks`
  - `What "progress you can see" actually looks like`
  - `{{contact.child_school}} registration closes [REGISTRATION_CLOSE_DATE]`
  - `Week 3 of a Discipline Rift season`
  - `The version to forward to your partner`
  - `Last call for {{contact.child_school}}`
  - `[SEASON_SPORT_AT_SCHOOL] is back at {{contact.child_school}}`
  - `Closing tonight — last call for {{contact.child_school}}`
- **B (school not covered):**
  - `We're not at {{contact.child_school}} yet — here's what happens now`
  - `Quick check on your child's school`
  - `Honest answer about {{contact.child_school}}`
  - `The Season Guide — and what to ask any after-school program`
  - `{{contact.nearest_dr_sport}} is running at {{contact.nearest_dr_school}}`
  - `The fastest way to get us into {{contact.child_school}}`
  - `Who's actually running the practice`
  - `Something for the wait`
  - `Which sport actually fits your child`
  - `Where things stand with {{contact.child_school}}`
  - `Update on your request for {{contact.child_school}}`
  - `Five questions worth asking any after-school program`
  - `Registration just opened across our schools — worth a re-check`
  - `Still want to hear when we reach {{contact.child_school}}?`
  - `It's happening — Discipline Rift is coming to {{contact.child_school}}`
  - `{{contact.child_school}} is open for next season`
- **05 (abandoned registration):**
  - `One step left on {{contact.child_first_name}}'s registration — everything is saved`
  - `What is the one thing holding you back?`
  - `If it is the timing, we can split it`
  - `{{contact.child_school}} — {{contact.season_sport}} starts [SEASON_START_DATE]`
  - `Closing this out — but the door stays open`
  - `Everything that is in the season (and the guarantee behind it)`
  - `Who is actually coaching {{contact.child_first_name}}`
  - `Tell me the one thing and I will answer it`
  - `No, we are not going to charge you for making an account`
  - `A few fields left on {{contact.child_first_name}}'s registration`
  - `What one Discipline Rift practice actually looks like`
  - `Yes — we run {{contact.season_sport}} at {{contact.child_school}}`
  - `How the after-school part actually works`
  - `One season. That is the whole decision.`
  - `Your card did not go through — nothing was charged`
  - `{{contact.child_first_name}}'s registration is still saved`
- Some of these drafts break later rules: proof stacks, invented-urgency patterns and "registration closes". The parent-email template says these cold-funnel rules "must never leak into house-list emails".

#### e) App-download campaign: DRAFT 2026-11-23 (source #29)

D1 subject `The Discipline Rift app is here` · Preview `Messages from your coach, practice reminders and your schedule in one place.`; signed Coach Luis; same HTML shell as 2.7. The rest of the file is today's working draft.

---

### 2.12 TRANSACTIONAL voice reference

**Season-start reminders (live code, #15):**
- Subjects: `15 days until {team} starts` · `One week until {team} starts` · `{Sport} starts tomorrow`.
- Heroes: "15 days to go." / "One week to go." / "Tomorrow."
- Lede: "There are 15 days left until the start of {team}. Make sure to remind your child about the practices. Here is the complete schedule."
- 15-day CTA line: "Questions before day one? Message Coach {coach} directly."
- 1-day line: "Please send a water bottle, athletic shoes, and comfortable athletic clothes."
- Sign-off: **"See your child on the court!" / "— The Discipline Rift Team"**.

**Weekly practice-eve emails (Luis's final draft 2026-08-31, #16), subjects Week 1→6:**
1. `[Player First Name]'s First [Sport] Practice Is Tomorrow`
2. `Tomorrow, We're Building on What They Learned in [Sport]`
3. `[Sport] Gets More Challenging Tomorrow`
4. `Tomorrow, We Start Seeing [Sport] Differently`
5. `It's Time to Put Everything Together in [Sport]`
6. `How Far They've Come in [Sport]. Final Practice Tomorrow`

All six sign off "Discipline Rift Coaching Team".

Week 1 body excerpt:
```
[Player First Name]'s first DR [Sport] practice of the [Season] season is tomorrow.
This first week is all about getting started. Coach [Coach Name] will introduce themselves and begin teaching the foundational skills and movements [Player First Name] will build on throughout the season.
Tomorrow, players will:
- Watch Coach [Coach Name] demonstrate skills and movements.
- Practice those movements through drills and games.
- Learn where those skills appear in game-like situations.
- Begin connecting individual movements to the game itself.
…
Please have [Player First Name] bring a water bottle, athletic shoes, and comfortable athletic clothes.
If you have any questions, you can contact Coach [Coach Name] through the Parent Dashboard.
We're excited to get [Player First Name] started tomorrow.
```
Week 6 lines worth reusing:
- "Our goal isn't only for [Player First Name] to leave knowing more about [Sport]. We want them to leave wanting to keep playing it."
- "Thank you, [Parent First Name], for allowing Coach [Coach Name] and Discipline Rift to be part of [Player First Name]'s [Season] season."

**Low-registration cancel (#12):** "Our program is built to guarantee both fun and learning, and we require a minimum number of players to properly run our activities, curriculum, and programming." Signed "Thank you for your understanding, / Coach Luis / Discipline Rift".

**Footer taglines approved for operational mail:** "Teaching developmental skills and inspiring passion for sport" (Luis wants it standardized) · "Developing young players in volleyball, tennis, pickleball, and flag football".

**Luis 1:1 parent replies (#32)** repeat one pattern: "Hi {first}! … you can register here: https://disciplinerift.com/register. Thanks for reaching out — Luis Torres".

---

## 3. Verbatim rules on wording, banned words and structure

### 3.1 Luis's 5 rules (First-Week campaign §0, 2026-08-09, "binding for all DR parent-facing marketing")

1. **Never diagnose the reader's child, never imply practice is boring.** The attention-gap point ("hold attention on something that isn't entertaining") was cut entirely — not reworded, cut. It confirms a parent's private insecurity ("my child will get distracted") and sells a dull product in the same breath. If a developmental point can't be stated without either effect, it doesn't ship.
2. **Never position as beginner-only.** "Most of our players have never played the sport" tells the family of a returning or experienced player this isn't where they grow — it trades retention for acquisition. A first-timer can start from zero AND a returning player keeps developing; when experience level comes up at all, that's the frame.
3. **Method as fact, not lecture.** Parents never hear method names (retrieval practice, blocked practice, serial practice). "We have a method that does X" — teach, drill, play, not luck — is the ceiling of detail. The science stays internal (coach training, curriculum docs).
4. **The dashboard feeds the parent-child conversation. It never replaces it.** The child answering "fine" is not a reason to stop asking — it's the reason to give the parent the coach's perspective, so they can ask more and deeper questions. Any copy implying "you won't have to ask" is wrong. Parents, players, and coaches communicating clearly is the point; the dashboard is how the parent walks in informed.
5. **One email, few points, chosen hard.** The first draft was an essay. Pick the points most valuable to parents and stop. His finalized version also cuts: the fear frame (replaced with a positive one), the proof stack (55 schools / Level 2 / supervised — trust lives on the site and later touches), all urgency mechanics (deadlines, tier-ladder placement, "the team forms without them," registration-minutes), the age line, and founder editorializing. Close warm, not with a squeeze.

**Ruling on CTAs:** **one unique action, rendered twice** — a Register button after the hook and one at the end. This supersedes "exactly one CTA button per email" as previously written; the rule was always about competing actions, not button count.

**§0.1 production learnings (verbatim points):**
- "Subject style ruling: calendar-anchored, plain, direct question."
- "Placement rule for the gap frame: the after-school-gap framing is allowed in subject/preview *as an open question* — never in the body as fear."
- "Copy compresses at design stage ('everything else: 80%'). Approval doesn't freeze copy; write lines that survive halving."
- "He designs by reacting to renders… his iteration grain is one element per message → HTML must be block-deletable."
- "Luis's homepage CTA was an explicit instruction, not an oversight."

**Retrospective (#5):** "Luis edits to protect relationships; the draft was written to win arguments." "When Luis adds, it's evidence or warmth. When Luis cuts, it's persuasion." Word count went from ~490 to ~230. Proof points went from 5 to 0 and urgency lines from 4 to 0.

### 3.2 Parent Email Template (house list), binding (#6)

- **Sender model:** "Write as Coach Luis talking to a parent who already knows the school — not as a marketer persuading a skeptic."
- **Slots, in order:**
  1. Greeting `Hi {{contact.first_name}},`
  2. Hook: 2–3 short lines, plain, situational, positive (a question is fine; no fear)
  3. **REGISTER #1**
  4. 2–3 points for parents (1 bold line + 1–2 sentences each; universal to the age, never a diagnosis)
  5. Method, not mood (teach → drill → play + the luck line; no method names)
  6. Easy for you (convenience line verbatim)
  7. Visibility (per-practice coach update + dashboard; "more to go on when you ask")
  8. Guarantee (verbatim)
  9. **REGISTER #2**
  10. Warm close + signature ("Never a deadline squeeze.")
- "Not every email uses every slot — cut slots before shrinking them. **Never add slots.**"
- **Caps:** "Target 150–200 words; 230 is the ceiling." "One idea per slot." "One unique CTA, rendered exactly twice… Label `REGISTER`."
- **Destination:** Luis shipped the homepage; the funnel's entry is /register. "Build with whatever Luis states per send; do not silently 'correct' his stated URL."
- **Subject rule:** "Preview extends, never repeats."
- **Zero:** "dollar figures, method names, proof stacks… urgency mechanics, age-range lines, beginner-only positioning, banned vocabulary."
- "Cold pop-up nurture… rules must never leak into house-list emails."
- **Chain:** "draft → five-rules check → Claude builds GHL-ready HTML → Luis reacts to the RENDER → QA → GHL". Each render ships "one proposed 3–6 word hero phrase" (he accepted "Movement belongs on the list"). "Archive the shipped HTML per send."

### 3.3 Locked phrases (verbatim)

- **Convenience:** "No transportation needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school." Never "no driving" or "no pickup", because parents still pick up.
- **Guarantee (current Luis wording):** "Our value is teaching the skills and the passion for the sport. If we do not deliver it, you receive a 100% refund at any time during the season."
  - Older wording: "Our value is the teaching. If we don't deliver it, you get a 100% refund, any time during the season."
  - Live-site wording: "if we don't deliver the value, real teaching and real progress".
- **Price:** "Low cost — everything included." No dollar figure anywhere outside checkout. "10% off" was judged acceptable because "a percentage does not reveal a price". SIBLING = 10% off the second registration (draft).
- **Method:** "Every practice runs on a method, not mood." / "If a program has no method, your child's development comes down to luck."
- **Audience line:** "Elementary · K through 5th" (not "ages 6–12"). "Beginner-friendly to advanced."
- **Sanctioned proof only:** "Running at 55 schools across Central Florida" + founder Luis Torres. "Never fabricate a testimonial or a stat."
- **Signature (house list):** `Coach Luis / Founder, Discipline Rift / info@disciplinerift.com · (407) 614-7454`. Oct–Nov sends: `See you at practice! / Coach Luis / Founder, Discipline Rift`. The older drafts' "The Discipline Rift Team" was rejected for marketing.
- **Footer:** Discipline Rift · Torres Rivero LLC · 713 W. Yale Street, Orlando, FL 32804 · info@disciplinerift.com · (407) 614-7454 · www.disciplinerift.com. The design spec adds "Value Guarantee · Running at 55 schools in Central Florida" and an unsubscribe link.
- **Language:** English-only to parents (EN/ES toggle removed; "en inglés, igual que todos los correos a padres").

### 3.4 Banned words and claim rules

- **Design spec §9:** "Banned on parent-facing emails: *fun-first, elite, high-performance, next level, serious athlete, future champion, tryouts*, and athlete-development-as-the-central-promise." "Teaching leads. 'We actually teach' is the anchor of every asset. Confidence, friends, and discipline are byproducts, never the promise." "No trial." "Tier = season."
- **Rewrite prompt §5:**
  - USE: season · on-campus · after-school · we actually teach · beginner-friendly to advanced · skill development · structured practice · coach-led · trained coaches · Tier System · tier progression · predictable schedule · pickup/dismissal · weekly updates · right at their school
  - BANNED: "next level" · "compete at the next level" · "serious athlete" · "elite" · "high performance" · "future champion" · "transform your child" · "unlock" · "tryouts" · "fun-first" (undersells the teaching) · "no driving" · "no pickup"
  - CLAIM RULE: "confidence, friends, belonging, character, discipline, sportsmanship may appear only as byproducts… NEVER the main promise, a headline, or the thing a CTA sells." Examples of v1 breaking it: "found their place," "it builds belief," "discovered something about themselves."
  - "Never invent a statistic." v1's "most kids quit activities by age 11" was banned; write `[NEEDS SOURCE: ...]` instead.
- **Marketing context (Q&A):** avoid "College, scholarships, exposure, pathways" (Q53, explicitly refused), "Anything that frames the child as at risk", and character claims as the promise. Real coach phrases available as copy: "Go" · "Keep going" · "Just one more" · "You're one step away" · "That was awesome".
- **Voice-and-Tone avoid list:** generic agency language · empty hype · AI buzzwords · all-caps subject lines or shouting punctuation · "unlock your potential" · soft generic CTAs · long over-explanations. Operating rule: "If the voice would not feel right in a one-on-one conversation between Luis and a parent he respects, it doesn't belong on a DR asset."
- **Marketing-Language-Library "Excluded — DO NOT USE":**
  - human rights · equity toolkit · Children's Rights (generic) · immigrant children · government raids of parks
  - private equity (as primary frame) · growing influence of technology · reshaping the youth sport landscape
  - disjointed landscape / fragmented / uncoordinated
  - municipal budgets cut / local recreation programs suffered / private providers flourished
  - range of sources · casual sport offerings buoyed participation · recovered / rebound in participation
- **How to use the library:** "Choose one parent outcome… one pain… convenience as the unique unlock… trust only if the asset has room… Always end with a clear next-step (avoid soft generic CTAs)." The contrast phrases (Cat. 10) include "on-campus = less logistics", "structured season, simple commitment" and "kids start — and stay — in sports".
- **communication-rules §1/§8/§12 (older, 2026-04):**
  - "Confidence through clarity — parents want to know what happens next, not be motivated"
  - "Avoids: hype language, vague promises, 'unleash your child's potential'"
  - Emoji "minimal — only in email subject lines or banners"
  - Subject "under 55 characters"; "Preview text should extend the subject, not repeat it"; "Use student first name where available"
  - "Not a motivational newsletter… Not a high-pressure sales channel… Not elite-athlete positioning"
- **Waitlist code rule:** no deadline, countdown or scarcity when no seat is actually held.
- **Urgency (rewrite prompt S5):** "Urgency must be real — anchored to a named date." v1's "filling up / rosters finalize soon" is banned. The Oct sends used real spot counts ("12 spots left", "3 spots left") and real next-practice dates.
- **Luis 2026-10-29:** rewrite emails so they "sound as if written by the coach, very precise and understandable at a glance" ("muy precisos y entendibles de un vistazo").
- **Parent Philosophy (Luis verbatim):**
  - Core message: "Convenient enough to start. Fun enough to love. Structured enough to learn. Deep enough to continue. Flexible enough to pursue further if they want."
  - Progress language: "What we worked on → What improved → What comes next". "Practice went great today!" is not DR voice.
  - "Retention should not depend only on: Discounts. Promotions. Convenience. Marketing."
- **Fall 2026 angle:** "Don't know what to do this year? Try sports." Do not frame school summer-camp footage as DR's own camp.

### 3.5 Known conflicts between rules (resolve before writing)

- **"fun-first":** banned by the design spec, the rewrite prompt and the product-marketing context ("undersells the teaching"), yet still listed under "Words DR Prefers" in Voice-and-Tone and in Marketing-Language-Library Cat. 1. **The newer and more specific rule wins: banned.**
- **Price:** "no dollar figures" (all current rules) vs. the ClickUp "Volleyball Registration Campaign — Finalized Content" fragment "It was only $129 for a six-week season" (#30) and Money-Model's "$129".
- **Age:** "K through 5th" (design spec, latest) vs. "6–12" (rewrite prompt, PMC).
- **CTA count:** "one CTA" (rewrite prompt S1, design spec §6) vs. Luis's ruling of one action rendered twice (latest).
- **CTA label:** "REGISTER" (spec) vs. "Save a spot" / "Register {kid}" in the Oct sends.
- **Signature:** "The Discipline Rift Team" (communication-rules §11, reminders) vs. "Coach Luis, Founder" (all marketing since August).
- **Proof:** design spec §9 allows "55 schools" vs. Luis's rule 5, which keeps the proof stack out of house-list emails (it lives in the footer).

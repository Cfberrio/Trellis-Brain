---
brand: Discipline-Rift
area: communication
subarea: sequences
note_type: sequence
status: ready
used_for_ai: true
sensitivity: internal
owner: Luis
last_updated: 2026-08-04
sequence: coach-lifecycle
audience: coach
channel: [email, whatsapp]
related_notes:
  - "[[../DR-Communication-Engine]]"
  - "[[../DR-Communication-Audit-2026-08-04]]"
  - "[[../../00-Brand-Core/DR-Brand-Audit-2026-08-04]]"
---

# DR Coach Communication Chain

Every message DR sends a coach, from application through season close. **New chain** — before this, coaches received exactly one automated message: a reminder that they'd failed to log a session.

- **Voice:** warm, appreciative, operationally precise. Read back the specifics. Thank them every time. State the next step. Personal messages sign as **Luis Torres, Founder**; system messages sign as **Discipline Rift Operations**.
- **Channel rule:** email carries the lifecycle. The **WhatsApp group** carries in-season daily/weekly directives (manual, already in practice). No SMS.
- **Merge syntax:** `{UPPERCASE}` canonical per [[../DR-Communication-Engine]].
- **Escalation guard:** C2 (declined), and anything touching pay, termination, or discipline, is **draft-and-flag for a human** — never auto-send. Per `AI-Customer-Service-Instructions/06-escalation-rules.md`.

---

## A. Recruiting & onboarding

| # | Step | Email | Trigger |
|---|---|---|---|
| C0 | Application received | *We got your application, {FIRST_NAME} — here's what happens next* | Coach application submitted |
| C1 | Moving forward — book the interview | *Next step: a short call about coaching with DR* | Application approved for interview |
| C2 | Not moving forward | *An update on your DR coaching application* | Application declined — **human review before send** |
| C3 | Offer + onboarding checklist | *Welcome to Discipline Rift — three things to complete* | Offer extended and accepted |
| C4 | Assignment confirmed | *Your season assignment: {SCHOOL_NAME}, {SPORT}* | Coach matched to a team |

## B. In-season

| # | Step | Email | Trigger |
|---|---|---|---|
| C5 | Week-before prep | *{SPORT} at {SCHOOL_NAME} starts {FIRST_PRACTICE_DATE}* | 7 days before first session |
| C6 | Weekly session plan (×6) | *Week {N}: {WEEK_FOCUS} — your plan* | Start of each season week |
| C7 | Session record reminder | *Today's session at {SCHOOL_NAME} isn't logged yet* | Session not submitted by 8 PM ET |
| C8 | Schedule change / cancellation | *Change to {SCHOOL_NAME} {SPORT} — {CHANGE_DATE}* | Session changed or cancelled |
| C9 | Mid-season check-in | *Week 3 check-in — how's the group?* | Start of week 3 |

## C. Season close

| # | Step | Email | Trigger |
|---|---|---|---|
| C10 | Season close + next season | *Season's done — thank you, and what's next* | Final session logged |

---

# Full copy

## C0 — Application received · Email

Replaces the live template that has been sending **"Hi name,"** to every applicant since January. Adds a real timeline and states the standard, so the applicant self-selects before DR spends review time.

**Subject:** We got your application, {FIRST_NAME} — here's what happens next

```
Hi {FIRST_NAME},

Thanks for applying to coach with Discipline Rift.

We run after-school sports seasons on campus at 55 schools across Central Florida —
volleyball, tennis, pickleball, and flag football, for kids 6 to 12. Most of them are
starting from zero. Our job is to actually teach them the sport.

What happens next:
1. We review your application — within 5 business days.
2. If there's a fit, we'll reach out to schedule a short call.
3. Selected coaches complete a background check and our coach training before the season.

What we look for: coaches who can hold a group's attention, teach one thing well rather
than five things badly, and treat a nervous 7-year-old the same way they'd treat a
confident 12-year-old.

If that sounds like how you coach, you'll like it here.

Questions in the meantime? Just reply to this email.

— The Discipline Rift Coaching Team
info@disciplinerift.com · (407) 614-7454
```

---

## C1 — Moving forward · Email

**Subject:** Next step: a short call about coaching with DR

```
Hi {FIRST_NAME},

Good news — we'd like to talk. Your application stood out.

The call is about 20 minutes. We'll walk through how a DR season actually runs, the
schools and sports we're staffing this season, and what your availability looks like.
Come with questions.

[ Pick a time ] → {SCHEDULING_URL}

If none of those times work, reply with a couple that do and we'll make it happen.

Talk soon,
Luis Torres
Founder, Discipline Rift
```

---

## C2 — Not moving forward · Email · **human review required**

Currently DR sends nothing, which means every declined applicant is left waiting indefinitely. Silence is a level-2 pairing: applicants talk, and coaches move between programs in a small local market.

**Subject:** An update on your DR coaching application

```
Hi {FIRST_NAME},

Thank you for applying to coach with Discipline Rift, and for the time you put into it.

We're not moving forward with your application for this season. It's a limited number of
positions against the schools and sports we're staffing right now, and that's the main
constraint.

If you'd like us to keep your application on file for next season, just reply and say so —
we'd be glad to.

Either way, thank you for your interest in the work.

— The Discipline Rift Coaching Team
```

> **Do not automate this send.** Draft it, route to a human, send manually. Per escalation rules, hiring decisions are never auto-communicated.

---

## C3 — Offer + onboarding checklist · Email

**Subject:** Welcome to Discipline Rift — three things to complete

```
Hi {FIRST_NAME},

Welcome to the team. We're glad to have you.

Three things before you can be assigned to a school:

1. Background check — Level 2, required for every DR coach on a campus.
   [ Start it here ] → {BACKGROUND_CHECK_URL}

2. Coach training — how a DR practice is structured, the callout system, and how we
   group players by stage rather than just age.
   [ Access training ] → {TRAINING_URL}

3. Availability + paperwork — days you can work, blackout dates, and your onboarding forms.
   [ Complete here ] → {ONBOARDING_URL}

Once all three are done, we'll match you to a school and a sport and send your assignment.

A note on what you're walking into: every practice is 60 minutes and every minute is
planned. You'll get a written plan each week — the skill focus, the cue, the drills, and
the reason behind them. You won't be improvising.

Questions at any point, reply here.

Luis Torres
Founder, Discipline Rift
```

---

## C4 — Assignment confirmed · Email

**Subject:** Your season assignment: {SCHOOL_NAME}, {SPORT}

```
Hi {FIRST_NAME},

You're set. Here's your assignment for the season:

📍 School: {SCHOOL_NAME}, {SCHOOL_LOCATION}
🏐 Sport: {SPORT}
📅 Season: {SEASON_START_DATE} – {SEASON_END_DATE}
🕒 Practice: {PRACTICE_SCHEDULE}
👥 Roster: {ROSTER_COUNT} players, grades {GRADE_RANGE}
🤝 Program director: {DIRECTOR_NAME} — {DIRECTOR_PHONE}

Your dashboard has the roster, the weekly plans, and session logging:
[ Coach Dashboard ] → {COACH_DASHBOARD_URL}

You'll get the Week 1 plan seven days before the first practice, and a plan every week
after that.

{DIRECTOR_NAME} is your first call for anything on the ground — a locked gate, a missing
player, a parent question you'd rather not field alone.

Glad to have you at {SCHOOL_NAME}.

Luis Torres
Founder, Discipline Rift
```

---

## C5 — Week-before prep · Email

**Subject:** {SPORT} at {SCHOOL_NAME} starts {FIRST_PRACTICE_DATE}

```
Hi {FIRST_NAME},

First practice is one week out.

📅 {FIRST_PRACTICE_DATE}, {FIRST_PRACTICE_TIME}
📍 {SCHOOL_NAME} — check in at {CHECK_IN_POINT}
👥 {ROSTER_COUNT} players on your roster

Before day one:
• Read the Week 1 plan — it's in your dashboard now. → {COACH_DASHBOARD_URL}
• Arrive 15 minutes early. Dismissal is the part that goes wrong when you're rushed.
• Confirm your equipment bag: {EQUIPMENT_LIST}
• Know how the students get to you — {DISMISSAL_FLOW}

Day one is the one that decides your season. Most of these kids have never played
{SPORT}. Learn names, keep everyone moving, and send them home having touched the ball
more times than they expected.

You're ready. See you out there.

Luis Torres
Founder, Discipline Rift
```

---

## C6 — Weekly session plan · Email × 6

The parallel to the parent weekly email, and the biggest structural gap this chain closes. Parents get six touchpoints of belief; coaches get six touchpoints of execution. Same week, same skill, both sides aligned.

**Subject:** Week {WEEK_NUMBER}: {WEEK_FOCUS} — your plan

```
{FIRST_NAME} — Week {WEEK_NUMBER} at {SCHOOL_NAME}.

Focus: {WEEK_FOCUS}
Cue of the week: "{WEEK_CUE}"
Theme: {WEEK_THEME}

One cue. Say it every rep. Do not add a second one — they'll hold one and lose both.

The plan: → {WEEK_PLAN_URL}

Execute:
• {EXECUTION_POINT_1}
• {EXECUTION_POINT_2}
• {EXECUTION_POINT_3}

Log the session before you leave the campus. Parents get their weekly update off your
log, and it names the same skill you just taught — so when a parent asks their kid about
{WEEK_FOCUS} tonight, the kid has an answer.

Self-check before you walk out:
• Did every player touch the ball more than they stood still?
• Did they leave better than they walked in?

Execute.

— Discipline Rift Operations
```

**Per-sport variable fill** — pull `{WEEK_FOCUS}`, `{WEEK_CUE}`, `{WEEK_THEME}` from [[DR-Sport-Week-Banks]]. The parent email for the same week draws from the same row. One source, two audiences.

---

## C7 — Session record reminder · Email

Upgrade of the one coach template that exists. Three changes: a real subject line, the school named, and the reason stated — a coach who knows the log feeds the parent email logs it.

**Subject:** Today's session at {SCHOOL_NAME} isn't logged yet

```
Hi {FIRST_NAME},

Today's {SPORT} session at {SCHOOL_NAME} hasn't been submitted yet.

[ Log the session ] → {COACH_DASHBOARD_URL}

It takes about two minutes: attendance, what you covered, anything a parent should know.

Why it matters: attendance drives the note we send parents when a player misses, and your
session record feeds the weekly parent update. If it's not logged, parents hear nothing.

Thanks for closing it out.

— Discipline Rift Operations
info@disciplinerift.com · (407) 614-7454
```

> **Fix before ship:** the live version sends a raw Vercel preview URL (`dash-board-coaches-whpv.vercel.app`). Move the dashboard to a DR subdomain and set `{COACH_DASHBOARD_URL}` to it.

---

## C8 — Schedule change / cancellation · Email

**Subject:** Change to {SCHOOL_NAME} {SPORT} — {CHANGE_DATE}

```
Hi {FIRST_NAME},

Change to your schedule:

{CHANGE_DETAIL}
(e.g., "Practice on Fri Sep 19 is cancelled — the gym is being used for a school assembly."
 or "Practice moves to 3:45 PM starting Oct 3.")

{MAKEUP_DETAIL}   (makeup session date, or "no makeup — the season shifts one week later")

Parents have been notified directly — you don't need to message them.

Questions, reply here or call {DIRECTOR_NAME} at {DIRECTOR_PHONE}.

— Discipline Rift Operations
```

**Rule:** DR notifies the parents, not the coach. A coach fielding logistics is a coach not preparing a practice, and it breaks the promise made to schools that DR handles parent communication.

---

## C9 — Mid-season check-in · Email

The two-way one. Everything else in this chain talks at the coach; this asks. It is also the earliest point DR can catch a season going sideways while there is still time to fix it.

**Subject:** Week 3 check-in — how's the group?

```
Hi {FIRST_NAME},

Halfway through at {SCHOOL_NAME}. Quick check-in — reply to this one, it goes to a person.

Three questions:
1. Who's struggling? Any player you'd want a second set of eyes on.
2. What's not working? Drill, timing, space, equipment, dismissal — anything.
3. What do you need from us?

Also: if you've got a moment worth showing — a kid who couldn't serve in week 1 and can
now — tell us. Those are the stories we want to be able to tell.

Thanks for the work you're putting in.

Luis Torres
Founder, Discipline Rift
```

---

## C10 — Season close + next season · Email

**Subject:** Season's done — thank you, and what's next

```
Hi {FIRST_NAME},

That's a season. Thank you.

{ROSTER_COUNT} kids at {SCHOOL_NAME} finished {SPORT} with you, and most of them started
knowing nothing about it. That's the whole job, and you did it.

Two things to close out:
1. Final session logs and tier assessments — due {ASSESSMENT_DEADLINE}.
   [ Complete in dashboard ] → {COACH_DASHBOARD_URL}
2. Equipment return — {EQUIPMENT_RETURN_DETAIL}

Next season starts {NEXT_SEASON_START}. If you want to come back — and we hope you do —
let us know your availability:
[ Availability for next season ] → {AVAILABILITY_URL}

Coaches who return are how a program stops being a collection of sessions and starts
being something a school counts on. The kids ask for their coach by name.

Thanks again.

Luis Torres
Founder, Discipline Rift
```

---

## Implementation notes

- **C6 is the load-bearing message.** It ties the coach's week to the parent's week. Without it, the parent weekly email describes a skill the coach may not have taught that week — which is worse than sending nothing.
- **C2 never auto-sends.** Hiring outcomes route to a human. Draft only.
- **C7 replaces the current live coach reminder.** Do not run both.
- **C9 replies go to a monitored inbox**, not a no-reply. If nobody reads them, do not send it — an ignored "what do you need?" is worse than no question.
- **WhatsApp stays manual.** This chain is the email backbone; the daily WhatsApp directives layer on top and are written by operations. Build the 6-message-per-season bank there too so voice stays consistent across coaches (per [[../communication-rules]] §10).
- **Roster and director data** must exist in the coach record before C4 can fire. `[CONFIRM — owner: dev]`

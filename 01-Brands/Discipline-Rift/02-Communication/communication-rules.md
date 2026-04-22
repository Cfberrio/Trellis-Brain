# Discipline Rift — Communication Rules

**Last updated:** 2026-04-21
**Brand:** Discipline Rift (DR)
**Scope:** All parent-facing, coach-facing, and internal automated communications — email and messaging.
**Automation platform:** n8n
**Audience segments:** Parents, Coaches (operational), Coach applicants

---

## 1. Brand Voice

DR communicates differently depending on who it's talking to. Two distinct voices operate simultaneously.

### Parent-facing voice
- Warm, organized, trustworthy
- Confidence through clarity — parents want to know what happens next, not be motivated
- Never casual to the point of unprofessional; never formal to the point of cold
- Uses child's name and parent's name to feel personal
- Short paragraphs, clear structure, easy to scan on mobile
- Emoji use: minimal — only in email subject lines or banners where it reinforces energy (soccer ball, volleyball, calendar)
- Avoids: hype language, vague promises, "unleash your child's potential" constructions
- Sounds like a reliable coordinator who actually shows up

**Tone example (parent):**
> "Hi [Parent], just a quick heads-up — [Student]'s first volleyball session is this Friday. Here's what to expect and what to bring."

### Coach-facing voice (operational, internal)
- Direct, energetic, no filler
- Assumes accountability — coaches are treated as professionals
- Tactical + motivational in the same message
- Uses sport metaphors naturally, not forced
- Consistent structure: frame the day/week → tactical point → motivational anchor → execution expectations → self-check
- Emoji used more freely as cues/bullets, not decoration

**Tone example (coach):**
> "Week 4. Energy matters more than perfection right now. Three things to execute before you walk out today: [list]. Coaches who execute small things consistently are the ones who build lasting programs."

### Coach application voice
- Professional, encouraging, action-clear
- Confirms the application was received, sets expectations on next steps
- Should NOT read like a form auto-reply — must feel like a real organization responded

---

## 2. Audience Segments

| Segment | Who | Channel | Voice |
|---|---|---|---|
| Parents | Paying adults, kids 6–12 | Email | Warm, organized, trustworthy |
| Coaches (active) | On-payroll session coaches | WhatsApp group | Direct, tactical, motivational |
| Coach applicants | Inbound coach applications | Email | Professional, encouraging |
| Students | Kids (indirect — communicated through parents) | Not direct | N/A |

---

## 3. n8n Variable Reference

All dynamic content in DR automations uses n8n JSON variable syntax. These differ from GHL syntax used in OEV.

| Variable | What it contains | Example output |
|---|---|---|
| `{{ $json.firstname }}` | Parent first name | Maria |
| `{{ $json.lastname }}` | Parent last name | Gonzalez |
| `{{ $json.name }}` | Full name (student or contact, context-dependent) | Sofia Gonzalez |
| `{{ $json.studentfn }}` | Student first name | Sofia |
| `{{ $json.parentfn }}` | Parent first name (explicit) | Maria |
| `{{ $json.email }}` | Contact email address | maria@example.com |
| `{{ $json.team }}` | Team or sport assigned | Volleyball |
| `{{ $json.scheduleHtml }}` | HTML-formatted session schedule block | (rendered table) |
| `{{ $json.otp }}` | One-time password for authentication | 482910 |

**Rules for variable use:**
- Always use `{{ $json.variable }}` — double curly braces, `$json.` prefix
- Never use bare field names like `json.name` or `name` without delimiters
- Test all variables before activation in n8n — empty fallback values should be configured where possible
- `scheduleHtml` renders as HTML — ensure the email template is HTML-enabled, not plain text

---

## 4. Email Templates — Documented

### Email 01 — OTP (One-Time Password / Authentication)

**Type:** Transactional
**Trigger:** User requests access code (portal login, registration verification)
**Channel:** Email only
**Audience:** Parents

**Subject:** Your Discipline Rift Verification Code
**Template pattern:**
```
Hi {{ $json.firstname }},

Your one-time verification code is:

[OTP CODE — large, centered]
{{ $json.otp }}

This code expires in [X] minutes.
If you didn't request this, ignore this email.

— The Discipline Rift Team
```

**Notes:**
- No fluff — OTP emails should be as short as possible
- Code should be visually prominent (large text or button style)
- Expiry time must be accurate — confirm with n8n workflow TTL setting
- Do not add marketing content to OTP emails

---

### Email 02 — Registration Confirmation

**Type:** Transactional
**Trigger:** Successful student registration
**Channel:** Email only
**Audience:** Parent

**Subject:** You're registered! Here's what's next for {{ $json.studentfn }}
**Template pattern:**
```
Hi {{ $json.parentfn }},

{{ $json.studentfn }} is officially registered for [Sport/Season Name].

Here's what you confirmed:
- Sport: {{ $json.team }}
- Season dates: [start] – [end]
- Schedule: {{ $json.scheduleHtml }}
- Location: [School/Venue Name]

What to expect next:
- You'll receive a reminder [X days] before the first session
- Coaches will confirm session details closer to the start date
- [Any pre-season instructions — e.g., check-in process, what to bring]

Questions? Reply to this email or contact us at [contact info].

See you on the field,
The Discipline Rift Team
```

**What works:**
- Confirms decision immediately — reduces post-registration doubt
- `scheduleHtml` block removes ambiguity about dates
- "What to expect next" section reduces inbound questions

**Improvement opportunities:**
- Add a parent dashboard link so they can log in and review their registration
- Include a single next action CTA button: "View Your Registration" → dashboard URL
- Consider adding a "What to bring to the first session" section here instead of waiting for the reminder — fewer emails, more useful

---

### Email 03 — 30-Day Session Reminder

**Type:** Operational / Reminder
**Trigger:** 30 days before first session
**Channel:** Email only
**Audience:** Parent

**Subject:** 30 Days Until {{ $json.studentfn }}'s Season Starts 🗓️
**Template pattern:**
```
Hi {{ $json.parentfn }},

Just a heads-up — {{ $json.studentfn }}'s [Sport] season starts in 30 days.

Here's the schedule one more time:
{{ $json.scheduleHtml }}

[Any prep reminders — registration docs, what to bring, first day process]

See you soon,
The Discipline Rift Team
```

**⚠️ Bug flagged:**
The current template displays **"1-Day Reminder"** in the email header/banner. This is a copy-paste error from Email 05. The banner and any internal header text must be updated to reflect "30-Day Reminder" before this sequence is live.

**Notes:**
- At 30 days, the parent's main need is confirmation that it's still happening + a schedule refresh
- Keep short — this is not an onboarding email, it's a signal to start planning
- Do not repeat content already covered in Email 02

---

### Email 04 — 7-Day Session Reminder

**Type:** Operational / Reminder
**Trigger:** 7 days before first session
**Channel:** Email only
**Audience:** Parent

**Subject:** One Week Away — What {{ $json.studentfn }} Needs to Know
**Template pattern:**
```
Hi {{ $json.parentfn }},

{{ $json.studentfn }}'s [Sport] season starts in one week.

Session details:
{{ $json.scheduleHtml }}

Before the first session:
- [What to bring — shoes, water bottle, etc.]
- [Arrival instructions — where to drop off]
- [Any first-day check-in process]

Coaches are ready. See you there.

The Discipline Rift Team
```

**⚠️ Bug flagged:**
Same copy-paste issue as Email 03 — current template displays **"1-Day Reminder"** in the header/banner. Must be corrected to "7-Day Reminder."

**What works:**
- Logistical detail is appropriate here — parents are planning their week
- Arrival/drop-off instructions reduce first-day friction

**Improvement opportunities:**
- Add a coach introduction line: "Your coach for this season is [Coach Name]." — reduces first-day anxiety for new parents
- If coach info isn't available at 7 days, placeholder should still be in the template for when it's wired up

---

### Email 05 — 1-Day Session Reminder

**Type:** Operational / Reminder
**Trigger:** 1 day before first session (or each session if recurring)
**Channel:** Email only
**Audience:** Parent

**Subject:** Tomorrow's the day! {{ $json.studentfn }}'s session is [Day] 🏐
**Template pattern:**
```
Hi {{ $json.parentfn }},

Reminder — {{ $json.studentfn }} has a session tomorrow.

📅 When: [Day], [Time]
📍 Where: [Location / Campus]
👕 What to bring: [list]

See you there,
The Discipline Rift Team
```

**Notes:**
- This template is the correct original — the 30-day and 7-day versions should reference this as the source but update timing language
- 1-day reminders should be short and scannable — parents read these on phones during the day
- Emoji usage appropriate here — acts as visual anchors in a short message

---

### Email 06 — Coach Session Reminder

**Type:** Operational / Internal
**Trigger:** Before scheduled session
**Channel:** Email (to coach)
**Audience:** Coach

**Subject:** Session Reminder — [Sport], [Day]
**Template pattern:**
```
Hi {{ $json.name }},

You have a session scheduled for tomorrow.

📅 [Day], [Time]
📍 [Location]
👥 Team: {{ $json.team }}

Please confirm attendance by replying to this email or updating in the coach dashboard.

— Discipline Rift Operations
```

**⚠️ Bug flagged:**
Current template uses `json.name` without template syntax delimiters. In n8n, this will render literally as `json.name` in the sent email — not the coach's actual name. Must be corrected to `{{ $json.name }}`.

**Improvement opportunities:**
- Add dashboard link: "View your full schedule at [coach dashboard URL]"
- Add a session prep reminder relevant to the sport (e.g., "Bring training plan, arrive 10 minutes early")
- Consider adding team roster count or key notes if available from n8n data

---

### Email 07 — Parent Attendance Note

**Type:** Operational / Communication
**Trigger:** After session — sent to parent when student was marked absent or had a note
**Channel:** Email only
**Audience:** Parent

**Subject:** A Note About {{ $json.studentfn }}'s Session Today
**Template pattern:**
```
Hi {{ $json.parentfn }},

We wanted to follow up about today's session for {{ $json.studentfn }}.

[Attendance note / coach observation — dynamic content]

If you have questions or need to make up a session, reply here or contact your coach directly.

The Discipline Rift Team
```

**Notes:**
- This is a sensitive email — tone must remain supportive, not punitive
- Avoid language that could read as accusatory toward parents ("We noticed your child was absent again")
- Dynamic note content should be reviewed before automating — coach notes fed through n8n need a quality filter
- If automation is not ready, this should be a manual send rather than a broken automated one

---

### Email 08 — Coach Application Confirmation

**Type:** Transactional
**Trigger:** Coach application form submitted
**Channel:** Email only
**Audience:** Coach applicant

**Subject:** We got your application — here's what happens next
**Template pattern:**
```
Hi {{ $json.firstname }},

Thanks for applying to coach with Discipline Rift.

We've received your application and will review it within [X business days].

What happens next:
1. Our team reviews your application
2. If there's a fit, we'll reach out to schedule an interview
3. Selected coaches complete our onboarding process

In the meantime, feel free to reply to this email with any questions.

Talk soon,
The Discipline Rift Team
```

**⚠️ Bug flagged:**
Current template body opens with **"Hi name,"** — the `{{ $json.firstname }}` variable is not wired up. This will send literally as "Hi name," to every applicant. Must be connected to the correct n8n field before activation.

**What works:**
- Numbered next-steps section sets clear expectations — reduces follow-up emails from applicants
- Tone is professional without being cold

**Improvement opportunities:**
- Add a specific timeline (e.g., "within 5 business days") instead of a placeholder
- Consider linking to a coach resources page or FAQ if one exists — reduces inbound questions
- Add a line about what makes a successful DR coach to reinforce brand standards during application stage

---

## 5. Volleyball Parent Email Sequence — 6-Week Nurture

**Type:** Relationship / Retention nurture
**Trigger:** Parent enrolled in volleyball program
**Audience:** Parents of volleyball students
**Cadence:** Weekly (one per week, Weeks 1–6)
**Channel:** Email only
**Goal:** Keep parents informed, engaged, and bought in throughout the season — reduce churn, increase re-enrollment

### Sequence Overview

| Email | Timing | Purpose |
|---|---|---|
| Week 1 | Day of or day after first session | Welcome + first impression |
| Week 2 | Week 2 | Season momentum + what's being worked on |
| Week 3 | Week 3 | Mid-season check-in / skills spotlight |
| Week 4 | Week 4 | Recognition + social proof moment |
| Week 5 | Week 5 | Building toward end of season |
| Week 6 | Final week | Season closing + re-enrollment / next steps |

---

### Week 1 — Welcome to the Season

**Subject:** {{ $json.studentfn }}'s first session is done — here's how it went
**Body pattern:**
```
Hi {{ $json.parentfn }},

Week 1 is officially underway.

This week, coaches focused on:
- [Skill or drill introduced]
- [Team warm-up / getting-to-know-you activity]
- [First baseline activity]

What to watch for at home:
[1 simple parent observation cue — e.g., "Ask them what their coach's name is."]

See you next week,
The Discipline Rift Team
```

**Why this works:** Closes the loop on the first session, gives parents a conversation starter with their child, and sets a cadence early.

---

### Week 2 — Building Momentum

**Subject:** Week 2: What {{ $json.studentfn }} is working on
**Body pattern:**
```
Hi {{ $json.parentfn }},

We're two weeks in and the energy has been great.

This week's focus:
- [Skill progression from Week 1]
- [New drill or team activity]

Coaches are tracking early progress on [specific skill]. By Week 4, most students will see a noticeable improvement here.

Keep it up,
The Discipline Rift Team
```

**Notes:** Sets a forward-looking milestone so parents feel like they're part of a progression, not just attending sessions.

---

### Week 3 — Skills Spotlight

**Subject:** Halfway there — what the coaches are seeing
**Body pattern:**
```
Hi {{ $json.parentfn }},

We're at the midpoint of the season and coaches wanted to share what they're seeing.

[Coach observation — general pattern for the group, or a specific skill note]

A reminder of what's coming in the second half:
- [Remaining milestones]
- [Any events, showcases, or team challenges]

{{ $json.studentfn }} is right on track.

The Discipline Rift Team
```

**Notes:** "Right on track" is a deliberate reassurance line for parents who wonder if their child is doing okay. If personalization is possible, this line should be conditional.

---

### Week 4 — Recognition Moment

**Subject:** Something we noticed about {{ $json.studentfn }}
**Body pattern:**
```
Hi {{ $json.parentfn }},

Week 4 is when we really start to see athletes come into their own.

[Positive recognition — can be general, e.g., "consistency has improved across the board" or personalized if data allows]

This week, coaches are working on:
- [Skill detail]

You're investing in something that matters. We see it.

The Discipline Rift Team
```

**Notes:** This is the emotional anchor email in the sequence. It doesn't need to be complicated — it needs to make the parent feel the investment was worth it.

---

### Week 5 — Final Stretch

**Subject:** One week left — here's what to expect for the finale
**Body pattern:**
```
Hi {{ $json.parentfn }},

Final week is coming up. Here's what's planned:

[End-of-season activity or showcase detail]
[Date, time, location if applicable]

Coaches will also be completing [tier/progress assessments] this week.

{{ $json.studentfn }} should be proud of this season.

See you at the finish,
The Discipline Rift Team
```

**Notes:** Logistics-forward because parents need to plan attendance for any end-of-season event. CTA if applicable: "Save the date: [event details]."

---

### Week 6 — Season Close + Re-enrollment

**Subject:** Season's done — here's what's next for {{ $json.studentfn }}
**Body pattern:**
```
Hi {{ $json.parentfn }},

The season is officially wrapped.

[Summary of what was accomplished — general or personalized]

{{ $json.studentfn }}'s progress:
[Tier level achieved or skill summary if tracked]

What's next:
[Next season details — dates, sport, registration link]
[Early registration note or incentive if applicable]

It's been a great season. Hope to see you again.

The Discipline Rift Team
[Registration CTA button: "Register for Next Season"]
```

**What works:**
- Ends with a forward-looking CTA when parent sentiment is highest (end of a positive season)
- Progress summary reinforces the value of the investment before the ask

**Improvement opportunities:**
- If tier progression is tracked, this email should include a personalized progress note — not just generic copy
- Re-enrollment offer should have a deadline to create urgency ("Early registration closes [date]")
- Consider adding a brief 1-question NPS or satisfaction survey here — feedback capture when relationship is strongest

---

## 6. Coach Internal Communication — WhatsApp Patterns

Coach communications happen in a WhatsApp group (coach-only, internal). Messages are sent by operations/head staff (Maria Jose Gonzalez pattern observed). These are NOT automated — they are manually crafted daily or weekly messages.

### Observed Message Pattern

All observed coach messages follow this consistent structure:

```
[Day/Week anchor — sets the frame]

[Tactical point — one specific technique, skill cue, or session directive]

[Motivational anchor — a principle or mindset framing, sometimes a quote]

[Execution expectations — 2–3 specific things to do today]

[Self-check questions — 1–2 questions for the coach to reflect on]

[Closing line — brief, charged]
```

### Real-life example structure (reconstructed pattern):

> **Thursday — Week 4**
>
> Energy in the room this week matters more than perfection. Athletes are hitting a wall — your job is to reset the room before they know they need it.
>
> Today: warm-up sets the tone. Don't rush it. 3 things:
> - [Specific drill or cue]
> - [Engagement tactic]
> - [Execution reminder]
>
> Ask yourself before you walk out: Did they leave better than they walked in? Did I communicate the why behind the drill?
>
> Execute.

### Template for future coach daily messages:

```
[Day], [Week anchor if applicable]

[1-sentence frame — what matters most today or this week]

[Tactical point — specific, actionable, 1–3 sentences]

[Principle or motivational anchor — not generic, tied to where the season is]

Execute [2–3 specific tasks]:
- [Task 1]
- [Task 2]
- [Task 3 if applicable]

Self-check:
- [Question 1]
- [Question 2 if applicable]

[Closing line — 2–5 words, charged]
```

### Voice rules for coach messages:
- Write to a professional who knows the sport — no over-explaining
- One message per day maximum — more dilutes impact
- Tactical + motivational in the same message, not separate
- Never corporate. Never vague inspiration without a specific execution tie.
- Emoji use as bullet points or emphasis is appropriate — not decoration
- Close with a short charged line, not a long affirmation

### What to avoid in coach messages:
- Generic motivational quotes without operational grounding
- Long walls of text with no scannable structure
- Asking coaches to do things that weren't set up properly in advance (operational failures in a motivational message erode trust)
- Mixed signals — message should align with what was communicated in session planning

---

## 7. Channel Logic

| Message type | Channel | Who sends | Automated? |
|---|---|---|---|
| OTP / Auth | Email | System | Yes |
| Registration confirmation | Email | System | Yes |
| 30-day reminder | Email | System | Yes |
| 7-day reminder | Email | System | Yes |
| 1-day reminder | Email | System | Yes |
| Coach session reminder | Email | System | Yes |
| Parent attendance note | Email | System (with coach input) | Partial |
| Coach application confirmation | Email | System | Yes |
| Weekly volleyball parent sequence | Email | System | Yes |
| Coach daily directives | WhatsApp group | Manual (operations staff) | No |

**Rule:** No DR communication currently uses SMS as a primary channel. If SMS is added, it must be treated as a supplemental channel for time-sensitive operational alerts only (same-day cancellations, location changes) — not for marketing or sequence nurture.

---

## 8. Subject Line Patterns

Observed and recommended subject line constructions for DR:

| Pattern | Example | Use for |
|---|---|---|
| Action + student name | "{{ $json.studentfn }}'s first session is done" | Post-session updates |
| Countdown | "One week away — what {{ $json.studentfn }} needs to know" | Reminders |
| Curiosity / specificity | "Something we noticed about {{ $json.studentfn }}" | Recognition emails |
| Direct statement | "We got your application — here's what happens next" | Transactional |
| Milestone | "Season's done — here's what's next" | Season close |

**Subject line rules:**
- Use student first name where available — it's the parent's primary reference point
- Specificity beats generic (not "Your reminder" — instead "Tomorrow's session for Sofia")
- Emoji used sparingly and only when it signals the content (🗓️ for dates, 🏐 for volleyball)
- Keep under 55 characters for mobile preview
- Preview text should extend the subject, not repeat it

---

## 9. Known Bugs — Action Required Before Production

These bugs exist in current DR templates and must be fixed before any sequence goes live.

| # | Email | Bug | Fix required |
|---|---|---|---|
| 1 | Email 03 — 30-Day Reminder | Banner/header displays "1-Day Reminder" | Update header text to "30-Day Reminder" |
| 2 | Email 04 — 7-Day Reminder | Banner/header displays "1-Day Reminder" | Update header text to "7-Day Reminder" |
| 3 | Email 06 — Coach Session Reminder | Variable written as `json.name` (no delimiters) | Change to `{{ $json.name }}` |
| 4 | Email 08 — Coach Application Confirmation | Body opens with "Hi name," | Wire `{{ $json.firstname }}` to the opening salutation |

**Priority:** All four should be fixed before activating any automated sequence. Bug #3 and #4 will produce visibly broken emails in production.

---

## 10. Improvement Recommendations

### Template standardization
- Establish a header/banner naming convention and use a shared component — the copy-paste bug in emails 03/04 happened because headers were manually duplicated. Use a template variable or shared block for email type labels.
- All emails should have a fallback value for first name variables: `{{ $json.parentfn | default: "there" }}` — so broken variable data doesn't produce blank salutations.

### Coach dashboard integration
- Emails 06 (coach reminder) and the weekly volleyball sequence should link to the coach dashboard (`https://dash-board-coaches-whpv.vercel.app/`) for schedule management and session confirmation.
- If a parent dashboard exists, all parent-facing emails should carry a consistent "View in dashboard" link.

### Sequence timing audit
- Confirm that the 30-day, 7-day, and 1-day reminders are not all firing for every session in a multi-session season — that would overwhelm parents. Define whether reminders fire only for the first session or for each session.
- The 6-week volleyball sequence assumes weekly cadence. If sessions are cancelled or rescheduled, the sequence needs a pause/resume trigger in n8n — otherwise parents receive week 3 content when they're still on week 1.

### Re-enrollment flow
- Week 6 email has a re-enrollment CTA, but there's no defined sequence for parents who click it but don't complete registration. Consider a 2–3 email abandoned registration sequence triggered off that click.

### Coach communication cadence
- Coach WhatsApp messages are ad hoc. For consistency and quality control, build a message bank for each week of the season — 6 messages per sport per season, written in advance, reviewed once, sent on schedule. This reduces daily writing pressure and maintains voice consistency across coaches.

### Attendance follow-up (Email 07)
- If coach notes are manual input into n8n, add a QA step before send — a coach note that reads "didn't show up" is not the same as a parent-appropriate attendance communication. Either auto-format the note or require a structured input form from coaches.

---

## 11. Signature Block

All DR emails should close consistently:

```
The Discipline Rift Team
[Contact email if applicable]
disciplinerift.com
```

For coach-specific emails, the sender name may be adjusted to feel more personal:
```
Coach [Name]
Discipline Rift
```

For coach application emails:
```
The Discipline Rift Coaching Team
[Recruitment contact if applicable]
```

---

## 12. What Discipline Rift Communication Is Not

To maintain voice clarity:

- Not a motivational newsletter — transactional and operational emails should be functional, not inspirational
- Not a B2B communication — parent-facing content should feel warm and personal, not professional and formal
- Not a high-pressure sales channel — any re-enrollment asks should feel like a natural next step, not a conversion push
- Not interchangeable with CTS or OEV voice — DR is youth sports and energy, not hospitality or event venue logistics
- Not elite-athlete positioning — communications should reflect the actual offer: fun-first, beginner-friendly, coach-led

---

*This file is the source of truth for all Discipline Rift automated and manual communications. Updates to sequences, variables, or voice rules should be reflected here first.*

---
brand: Discipline-Rift
area: communication
subarea: evidence
note_type: source-transcript
status: active
canonical: false
used_for_ai: true
source_type: verbatim-extraction
source_reference: "Extracción read-only 2026-11-23 (agente Claude). Nombres/correos/teléfonos de padres e hijos removidos. Fuente: ghl-gmail"
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

# Discipline Rift — historical outbound marketing emails (GHL + Gmail)

Collected 2026-11-23, read-only. Parent/child names, parent emails/phones and contact IDs removed ([parent], [child], [email], [phone]). Tracking URLs shortened (query strings stripped). Text is verbatim from the sent HTML converted to plain text; `[img: …]` marks image alt text; `[url]` after a word is the link target of that word/button.

## Sources and access notes

- GHL: `/emails/builder` (templates) and `/emails/schedule` (campaign list) return 401 "token is not authorized for this scope" with GHL_PRIVATE_KEY_DR, so saved templates (incl. the Feb-2026 intern template "DR EMAILS") could NOT be read. `/locations/{id}/templates` returned 0 templates; `/campaigns/` returned 0. Workaround: `/conversations/messages/export?channel=Email` (every email GHL actually sent, 38,014 messages, Jan–Nov 2026). Grouped by subject; one representative (most-sent) copy per email below. Earliest GHL email: 2026-01-29 (test); first real campaign 2026-02-15.
- GHL workflows present (names only): DR | Webhook - Newsletter Lead; Registration Abandoned (draft); Registration Paid (Registered); Season Start Reminder; Weekly Practice Reminder; Parent Absence; Parent/Coach New Messages; Coach Missing Session Record; Tag-trigger variants (Nov 2026); "Email on Lead Abandonment" (May 2026).
- Gmail (info@disciplinerift.com via Composio): search + full bodies OK. Some queries (`label:promotions`-style / drafts variants) hit 403 "restricted scope" on metadata for part of the pages; the rest worked. `from:leadconnectorhq OR from:msgsndr` returned 0. Wix-era (2022–2023) Shoutout blasts survive only as quoted text inside parent replies; those bodies were recovered from the quote (marked).

## 1. Inventory

### 1a. GHL (sent via GHL / Mailgun, from luis@ / coachluis@ / info@disciplinerift.com)

| # | Source | Name / subject | First sent | Last sent | Sends | Sender | Type |
|---|---|---|---|---|---|---|---|
| G1 | GHL campaign | No school tomorrow! Important information | 2026-02-15 | 2026-02-15 | 1768 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G2 | GHL campaign | After school time can be wasted... we fix that | 2026-02-20 | 2026-02-20 | 1699 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G3 | GHL workflow | Here you go! 3-minute Parent Guide | 2026-02-23 | 2026-11-22 | 520 | Discipline Rift <luis@disciplinerift.com> | Workflow: Newsletter Lead (email 1) |
| G4 | GHL workflow | Sports: This is where most parents hesitate | 2026-02-23 | 2026-10-23 | 206 | Discipline Rift <luis@disciplinerift.com> | Workflow: Newsletter Lead (email 2) |
| G5 | GHL workflow | Last chance to secure your child's spot this season | 2026-02-26 | 2026-10-23 | 189 | Discipline Rift <luis@disciplinerift.com> | Workflow: Newsletter Lead (email 3) |
| G6 | GHL campaign | Sports after Spring Break? One Week Away | 2026-03-15 | 2026-03-15 | 18 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G7 | GHL campaign | Stressed from Spring break? Time to take action | 2026-03-16 | 2026-03-16 | 1829 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G8 | GHL campaign | It's time. Last Season of the year | 2026-03-19 | 2026-03-19 | 1824 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G9 | GHL campaign | Ready for tomorrow? | 2026-03-22 | 2026-03-22 | 1826 | Discipline Rift <luis@disciplinerift.com> | Campaign |
| G10 | GHL workflow | Nos hemos dado cuenta de que te has perdido nuestras novedades | 2026-05-05 | 2026-05-05 | 3 | Discipline Rift <luis@disciplinerift.com> | Workflow: re-engagement (ES) |
| G11 | GHL workflow | Finish your registration | 2026-05-26 | 2026-06-19 | 110 | Discipline Rift <luis@disciplinerift.com> | Workflow: Registration Abandoned (1) |
| G12 | GHL workflow | Second Attempt | 2026-05-27 | 2026-06-20 | 109 | Discipline Rift <luis@disciplinerift.com> | Workflow: Registration Abandoned (2) |
| G13 | GHL workflow | Final Email | 2026-05-29 | 2026-06-22 | 108 | Discipline Rift <luis@disciplinerift.com> | Workflow: Registration Abandoned (3) |
| G14 | GHL campaign | Discipline Rift: Next Steps | 2026-07-31 | 2026-07-31 | 13 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G15 | GHL campaign | Back to school this Tuesday, are you ready? | 2026-08-09 | 2026-08-18 | 2236 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G16 | GHL campaign | First week is done. Is your child ready? | 2026-08-16 | 2026-08-18 | 2214 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G17 | GHL campaign | Long weekend! Volleyball starts this week | 2026-09-05 | 2026-09-05 | 2187 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G18 | GHL campaign | Happy Labor Day! Volleyball is here | 2026-09-07 | 2026-09-08 | 1974 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G19 | GHL campaign | Next sports season is here. [child] isn't registered yet | 2026-10-04 | 2026-10-05 | 1473 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G20 | GHL campaign | Good things come to an end! isn't registered for next season | 2026-10-11 | 2026-10-11 | 2331 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G21 | GHL campaign | season is coming to an end. | 2026-10-18 | 2026-10-18 | 2262 | Discipline Rift <info@disciplinerift.com> | Campaign |
| G22 | GHL campaign | practices begin this week at . There may still be room! | 2026-10-26 | 2026-10-26 | 1451 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G23 | GHL campaign | Practice is Happening as Scheduled | 2026-11-02 | 2026-11-02 | 20 | Discipline Rift <coachluis@disciplinerift.com> | Campaign |
| G24 | GHL workflow | 7-day: We're seven days away from VOLLEYBALL HILLCREST! | 2026-09-03 | 2026-10-23 | 355 | Discipline Rift <info@disciplinerift.com> | Workflow: Season Start Reminder (7-day) |
| G25 | GHL workflow | 1-day: Volleyball is tomorrow! | 2026-09-07 | 2026-11-02 | 621 | Discipline Rift <info@disciplinerift.com> | Workflow: Season Start Reminder (1-day) |
| G26 | GHL workflow | [child]'s First Volleyball Practice Is Tomorrow | 2026-09-01 | 2026-11-02 | 547 | Discipline Rift <info@disciplinerift.com> | Workflow: Season Start Reminder (first practice) |
| G27 | GHL workflow | Tomorrow, We Start Seeing Volleyball Differently | 2026-09-01 | 2026-10-27 | 358 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder (wk1) |
| G28 | GHL workflow | Volleyball Gets More Challenging Tomorrow | 2026-09-01 | 2026-11-10 | 549 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder |
| G29 | GHL workflow | Tomorrow, We're Building on What They Learned in Volleyball | 2026-09-01 | 2026-11-05 | 640 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder |
| G30 | GHL workflow | It's Time to Put Everything Together in Volleyball | 2026-09-01 | 2026-11-03 | 290 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder |
| G31 | GHL workflow | How Far They've Come in Volleyball. Final Practice Tomorrow | 2026-09-01 | 2026-11-10 | 356 | Discipline Rift <info@disciplinerift.com> | Workflow: Weekly Practice Reminder (final) |
| G32 | GHL workflow | A note about [child]'s session | 2026-09-01 | 2026-11-20 | 411 | Discipline Rift <info@disciplinerift.com> | Workflow: Parent Absence |

Excluded from GHL (operational, not marketing): coach/parent new-message notifications, "Still waiting: unread message", coach session-record reminders, receipts/invoices, staff campaigns to coaches (Meet the Families, Coaching Resources, DR Team Fall Schedule, Required: Review Annual Schedule, private-lesson availability), practice-canceled notices, test sends. Per-school duplicates of the season-start and weekly reminders (tennis/pickleball/soccer/flag football variants) exist with the same structure; only the volleyball version is reproduced.

### 1b. Gmail (info@disciplinerift.com)

| # | Source | Subject | Date | Sender | Type |
|---|---|---|---|---|---|
| M1 | Gmail | Re: Last 2 Week to Register - Sign up Today! | 2022-10-13 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M2 | Gmail | Re: Limited Time Christmas Offer - Sign up today! | 2022-12-20 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M3 | Gmail | Re: Registrations Now Open - Sign up today! | 2022-12-13 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M4 | Gmail | Re: Late Spring Registrations now open - Don't miss out!! | 2023-02-10 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M5 | Gmail | Re: Limited Time Offer Ends Today! - Sign Up Now! | 2023-01-02 | [parent reply quoting DR blast] | Wix Shoutout blast (recovered from reply quote) |
| M6 | Gmail | Re: Programs Start Next Week - Register Today! | 2023-01-11 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M7 | Gmail | Re: Last week To Sign Up - Don't Miss out! | 2023-01-10 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M8 | Gmail | Re: Limited Spots Available - Don't Miss Out! | 2022-10-26 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M9 | Gmail | Re: Late Fall Registrations - Sign up Today! | 2022-10-18 | [parent reply quoting DR blast] | Wix Shoutout blast (recovered from reply quote) |
| M10 | Gmail | Re: School Starts Tomorrow-Register Today!!! | 2023-08-09 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M11 | Gmail | Re: Tennis and Volleyball Camps Now Available!! - DR Sports & Athletics | 2023-04-13 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M12 | Gmail | Re: Season Update - DR Sports & Athletics | 2022-12-05 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M13 | Gmail | Re: Looking forward to seeing you at WINDERMERE ELEMENTARY VOLLEYBALL | 2022-09-01 | Discipline Rift <info@disciplinerift.com> | Wix Shoutout blast (recovered from reply quote) |
| M14 | Gmail | Updated Schedule Late Spring Season - DR Sports & Athletics | 2023-04-13 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M15 | Gmail | Welcome to DRVC Pre-Season - Your Journey Begins Tomorrow! 10U LIME | 2024-03-11 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M16 | Gmail | Congratulations! Volleyball Club Team Placement | 2024-03-03 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M17 | Gmail | First Day of Volleyball - Week 1 with DR Sports & Athletics | 2025-04-10 | Discipline Rift <info@disciplinerift.com> | Weekly season update (2025) |
| M18 | Gmail | Volleyball Week 2 with DR Sports & Athletics | 2025-04-17 | Discipline Rift <info@disciplinerift.com> | Weekly season update (2025) |
| M19 | Gmail | Last Week of Volleyball with DR Sports & Athletics | 2025-05-07 | Discipline Rift <info@disciplinerift.com> | Weekly season update (2025) |
| M20 | Gmail | DRVC Volleyball Tryouts – This Saturday! | 2025-05-28 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M21 | Gmail | Tomorrow - Fall Season Discipline Rift | 2025-09-15 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M22 | Gmail | Practice is today! Orangewood Tennis | 2025-08-20 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M23 | Gmail | Reminder:  VOLLEYBALL INDEPENDENCE Starts tomorrow! | 2025-11-04 | info@disciplinerift.com | Season start reminder |
| M24 | Gmail | Reminder: VOLLEYBALL WATER SPRING Starts in 7 days! | 2026-01-19 | info@disciplinerift.com | Season start reminder |
| M25 | Gmail | DR Tennis Spring Season | 2025-11-11 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M26 | Gmail | Eagle Creek Afterschool Clubs Spring Semester | 2025-11-18 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M27 | Gmail | Prueba Newsletter | 2025-11-24 | DisciplineRift <info@disciplinerift.com> | Newsletter test send |
| M28 | Gmail | Prueba Newsletter 5 | 2025-11-24 | DisciplineRift <luis@disciplinerift.com> | Newsletter test send |
| M29 | Gmail | Their Health won’t wait for “Later” - Spring Season | 2025-12-06 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M30 | Gmail | Spring Volleyball - Discipline Rift | 2026-01-08 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M31 | Gmail | Spring Pickleball Season 🥒  Dates & Flyer | 2026-01-08 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M32 | Gmail | Registration | 2025-12-22 | info@disciplinerift.com | Promo / announcement |
| M33 | Gmail | No school tomorrow! Important information | 2026-02-15 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M34 | Gmail | After school time can be wasted... we fix that | 2026-02-20 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M35 | Gmail | 6255 New Independence Pkwy, Winter Garden, FL 34787 Season Ended Last Week – New Registration Now Open | 2026-03-03 | info@disciplinerift.com | Weekly season update (2025) |
| M36 | Gmail | Stressed from Spring break? Time to take action | 2026-03-16 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M37 | Gmail | Thank You for Coming Today | 2026-03-17 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M38 | Gmail | It's time. Last Season of the year | 2026-03-19 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M39 | Gmail | Ready for tomorrow? | 2026-03-22 | Discipline Rift <luis@disciplinerift.com> | GHL campaign copy (received) |
| M40 | Gmail | THANK YOU from UCF Knight Shadow & Summer 2026 info! | 2026-03-26 | [parent reply quoting DR blast] | Promo / announcement |
| M41 | Gmail | Season Update? Prep for Fall | 2026-05-04 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M42 | Gmail | Preparing you for the DR Fall Season | 2026-07-28 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M43 | Gmail | Back to school this Tuesday, are you ready? | 2026-08-09 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M44 | Gmail | First week is done. Is your child ready? | 2026-08-16 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M45 | Gmail | Long weekend! Volleyball starts this week | 2026-09-05 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M46 | Gmail | Happy Labor Day! Volleyball is here | 2026-09-07 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M47 | Gmail | Volleyball Starts Thursday! | 2026-09-08 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M48 | Gmail | [child] is all set for Volleyball at Hamlin Elementary School - Fall 2026 schedule | 2026-09-16 | <info@disciplinerift.com> | Welcome / confirmation |
| M49 | Gmail | You're all set — [child]'s Fall 2026 Volleyball team is confirmed | 2026-09-21 | <info@disciplinerift.com> | Welcome / confirmation |
| M50 | Gmail | Next sports season is here. [child] isn't registered yet | 2026-10-04 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M51 | Gmail | Good things come to an end! isn't registered for next season | 2026-10-11 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M52 | Gmail | season is coming to an end. | 2026-10-18 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M53 | Gmail | Here you go! 3-minute Parent Guide | 2026-10-23 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M54 | Gmail | One week until VOLLEYBALL INNOVATION starts | 2026-10-23 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M55 | Gmail | Volleyball starts tomorrow | 2026-10-25 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M56 | Gmail | practices begin this week at . There may still be room! | 2026-10-26 | Discipline Rift <coachluis@disciplinerift.com> | GHL campaign copy (received) |
| M57 | Gmail | Winter Flag Football at Pinecrest Avalon has spots open | 2026-10-26 | Discipline Rift <info@disciplinerift.com> | Promo / re-enroll |
| M58 | Gmail | Pinecrest Avalon Winter: Flag Football Mondays, Tennis Tuesdays | 2026-10-26 | <info@disciplinerift.com> | Promo / re-enroll |
| M59 | Gmail | Pinecrest Avalon Winter: Soccer starts Thursday | 2026-10-27 | Discipline Rift <info@disciplinerift.com> | Season start reminder |
| M60 | Gmail | [child] is not registered for volleyball yet | 2026-10-30 | Discipline Rift <info@disciplinerift.com> | Promo / re-enroll |
| M61 | Gmail | Hope Prep Girls' 15U Volleyball / 2027 Season Dates | 2026-11-12 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M62 | Gmail | Summer Camp Schedule - July 20–24 | 2026-07-19 | Discipline Rift <info@disciplinerift.com> | Promo / announcement |
| M63 | Gmail | You're in! [child]'s Fall 2026 practice schedule | 2026-10-08 | <info@disciplinerift.com> | Welcome / confirmation |

## 2. Verbatim text — GHL

### G1. No school tomorrow! Important information
- Type: Campaign · GHL source: campaign · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-02-15 → 2026-02-15 · 1768 sends

```text
SUBJECT: No school tomorrow! Important information

Here's what you need to know

Discipline Rift

Parent!, no class tomorrow — Presidents’ Day

Since kids are out, it’s the perfect time to lock in the last season of the year (right after school, on campus).

REGISTER HERE [https://www.disciplinerift.com/register]

[#1] [#2][img: previous][img: previous]

[img: next][img: next]

Quick heads-up:

There’s no class tomorrow because of Presidents’ Day.
This is the moment to get your child locked in for the last season of the year.

This time I’m writing to you as the founder of Discipline Rift.
This whole year being in schools and seeing housands of students
I’ve learned that kids fear being judged,
they walk in unsure, worried they’ll mess up.

THAT’S WHAT WE FIX WITH SPORTS

Coaches teach the basics first, then increase difficulty through short, guided play! So kids build confidence fast.

Here’s what you’ll notice:

They miss, laugh, reset, and try again.. because it feels safe to keep going.

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://www.disciplinerift.com/register]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://www.disciplinerift.com/register]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G2. After school time can be wasted... we fix that
- Type: Campaign · GHL source: campaign · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-02-20 → 2026-02-20 · 1699 sends

```text
SUBJECT: After school time can be wasted... we fix that

LAST season of the year is here

Discipline Rift

Coach Luis here!

After school can go either way.
Time can be wasted… or it can be used for something better.

Backpacks drop. Energy is still there.
They just need somewhere to put it.

Spring registration is here, kids stay on campus and step straight into movement: small groups, supportive coaches, and games that ease learning.

REGISTER HERE [https://www.disciplinerift.com/register]

No pressure.
No “you should already know this.”

Just a place where trying, missing, and trying again is normal.

And something shifts quickly.

You’ll hear laughter instead of frustration.
You’ll notice them asking when the next practice is.

That’s what we care about most.

Spring is the last time to start.

Register before teams get full for Spring

We’d love to have your family join us.

Coach Luis -
Founder, Discipline Rift

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://www.disciplinerift.com/register]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://www.disciplinerift.com/register]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G3. Here you go! 3-minute Parent Guide
- Type: Workflow: Newsletter Lead (email 1) · GHL source: workflow · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-02-23 → 2026-11-22 · 520 sends

```text
SUBJECT: Here you go! 3-minute Parent Guide

Here you go! 3-minute Parent Guide
From Coach Luis at Discipline Rift

Hi ${name},
What if this was the season your child did not just participate...
But discovered something about themselves?
The first time they understand a new skill.
The first time they try again after struggling.
The first time they feel like they belong in a group.
Many children stop participating in organized activities before middle school... Not because they lack ability, but because they did not feel supported or capable early on.
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
REGISTER FOR THE SEASON [https://services.msgsndr.com/urls/l/Kn5zvTgqj]
FIND YOUR SCHOOL [https://services.msgsndr.com/urls/l/Kn5zvTgqj]

What if this season everything shifts?

From Coach Luis
Discipline Rift
📧 info@disciplinerift.com
📞 [phone]

This email was sent because you signed up for the Discipline Rift Parent Guide.

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G4. Sports: This is where most parents hesitate
- Type: Workflow: Newsletter Lead (email 2) · GHL source: workflow · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-02-23 → 2026-10-23 · 206 sends

```text
SUBJECT: Sports: This is where most parents hesitate

Secure Your Child's Spot
From Coach Luis at Discipline Rift

Hi {Name},
If you already know your child would benefit from structure, you can secure a spot now:
REGISTER YOUR CHILD HERE [https://services.msgsndr.com/urls/l/2Uf6yxhOrq]

Time matters.
These elementary years are when habits form.
When identity forms.
When confidence either grows or shrinks.

If you have been considering it, this is the time to act.
The right environment does not just fill afternoons.
It builds belief.

From Coach Luis
Discipline Rift
📧 info@disciplinerift.com
📞 [phone]

This email was sent because you signed up for the Discipline Rift Parent Guide.

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G5. Last chance to secure your child's spot this season
- Type: Workflow: Newsletter Lead (email 3) · GHL source: workflow · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-02-26 → 2026-10-23 · 189 sends

```text
SUBJECT: Last chance to secure your child's spot this season

Before Registration Closes
From Coach Luis at Discipline Rift

Hi [object Object],
Before registration closes, here is the direct link:
SECURE YOUR SPOT [https://services.msgsndr.com/urls/l/VQ_j7-UPle]

Protect the experience.
Protect the child's confidence.
Protect the quality of the group.
That requires commitment to timing.

Seasons move quickly. Childhood moves faster.
If you are ready to give your child a structured space to grow this season, now is the moment.
We would love to have your family join us.
SECURE YOUR SPOT [https://services.msgsndr.com/urls/l/VQ_j7-UPle]

From Coach Luis
Discipline Rift
📧 info@disciplinerift.com
📞 [phone]

This email was sent because you signed up for the Discipline Rift Parent Guide.

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G6. Sports after Spring Break? One Week Away
- Type: Campaign · GHL source: campaign · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-03-15 → 2026-03-15 · 18 sends

```text
SUBJECT: Sports after Spring Break? One Week Away

What happens after spring break? Sports

Discipline Rift

Coach Luis here!

As spring break begins, spring sports are now just one week away.

For parents, the real win is not just helping kids get better. It is helping them want to come back.

Because if kids do not want to return, progress never even starts.

REGISTER HERE [https://www.disciplinerift.com/register]

Discipline Rift

That is why our program is built around fun-first, beginner-friendly sessions that happen right after school, on campus.

We teach the sport step by step, at a pace kids can enjoy, so they leave smiling and excited to do it again.

One after-school practice per week

No club lifestyle

No weekends taken over

Spring season is coming up quickly, and spots are limited per team.

REGISTER HERE [https://www.disciplinerift.com/register]

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://www.disciplinerift.com/register]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://www.disciplinerift.com/register]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G7. Stressed from Spring break? Time to take action
- Type: Campaign · GHL source: campaign · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-03-16 → 2026-03-16 · 1829 sends

```text
SUBJECT: Stressed from Spring break? Time to take action

Last season of the year.. limited spots per team

Discipline Rift

Hi! Coach Luis here

As spring break begins, our last sports season of the year is just one week away.

THE real win is not just helping kids get better. It is helping them want to come back.

Because if kids do not want to return, progress never even starts.

REGISTER HERE [https://link.msgsndr.com/email-tracking/e8a152ab15e?…]

Discipline Rift

That is why our program is built around fun-first, beginner-friendly sessions that happen right after school, on campus.

We teach the sport step by step, at a pace kids can enjoy, so they leave smiling and excited to do it again.

One after-school practice per week

No club lifestyle

No weekends taken over

Spring season is coming up quickly, and spots are limited per team.

REGISTER HERE [https://link.msgsndr.com/email-tracking/e8a152ab15e?…]

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://link.msgsndr.com/email-tracking/e8a152ab15e?…]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://link.msgsndr.com/email-tracking/e8a152ab15e?…]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G8. It's time. Last Season of the year
- Type: Campaign · GHL source: campaign · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-03-19 → 2026-03-19 · 1824 sends

```text
SUBJECT: It's time. Last Season of the year

Is your child not focusing? Season starts next week

Quynh, it's time.
Time to focus, time for the last sports season of the year.

Is your child not focusing? It might not be what you think.

Many kids struggle with attention, but maybe it's not always about their ability to focus.

We just need a method that adapts to their energy levels. Our practice method is high-energy, engaging, and dynamic.

We use interactive drills to keep them involved. When they are engaged, they can do it.

AND this spring is the our last season of the year

REGISTER HERE [https://link.msgsndr.com/email-tracking/335a0e8c5d5?…]

We teach the sport step by step, at a pace kids can enjoy, so they leave excited to do it again.

One after-school practice per week

No club lifestyle

No weekends taken over

SPRING SEASON STARTS NEXT WEEK

REGISTER HERE [https://link.msgsndr.com/email-tracking/335a0e8c5d5?…]

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://link.msgsndr.com/email-tracking/335a0e8c5d5?…]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://link.msgsndr.com/email-tracking/335a0e8c5d5?…]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G9. Ready for tomorrow?
- Type: Campaign · GHL source: campaign · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-03-22 → 2026-03-22 · 1826 sends

```text
SUBJECT: Ready for tomorrow?

Season is starting tomorrow! Sports ARE here

, ready for tomorrow?

Season starts tomorrow.

Spring season is here. Last season of the year.

Sports are not just about learning the game. They teach kids how to handle tough moments, value the small details, and keep growing without needing perfection.

They also learn to be part of something bigger than themselves, contribute to a team, and help others reach the goal together.

That is why this season matters.

REGISTER HERE [https://link.msgsndr.com/email-tracking/0dbd18d3ff8?…]

We teach the sport step by step, at a pace kids can enjoy, so they leave excited to do it again.

One after-school practice per week

No club lifestyle

No weekends taken over

SPRING SEASON STARTS NEXT WEEK

REGISTER HERE [https://link.msgsndr.com/email-tracking/0dbd18d3ff8?…]

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://link.msgsndr.com/email-tracking/0dbd18d3ff8?…]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://link.msgsndr.com/email-tracking/0dbd18d3ff8?…]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G10. Nos hemos dado cuenta de que te has perdido nuestras novedades
- Type: Workflow: re-engagement (ES) · GHL source: workflow · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-05-05 → 2026-05-05 · 3 sends

```text
SUBJECT: Nos hemos dado cuenta de que te has perdido nuestras novedades

Hola [parent],

Hemos notado que recientemente cambiaste a la etapa 'abandoned' en nuestro pipeline de newsletter. Queremos asegurarnos de que no te pierdas las últimas noticias y ofertas exclusivas que tenemos preparadas para ti.

Si hay algo que podamos hacer para mejorar tu experiencia o si tienes alguna pregunta, no dudes en contactarnos. Nos encantaría contar contigo nuevamente y ayudarte a aprovechar todos los beneficios de nuestra comunidad.

Gracias por estar con nosotros.

Saludos cordiales,

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G11. Finish your registration
- Type: Workflow: Registration Abandoned (1) · GHL source: workflow · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-05-26 → 2026-06-19 · 110 sends

```text
SUBJECT: Finish your registration

https://services.msgsndr.com/urls/l/a97iQPPZIV

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G12. Second Attempt
- Type: Workflow: Registration Abandoned (2) · GHL source: workflow · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-05-27 → 2026-06-20 · 109 sends

```text
SUBJECT: Second Attempt

https://services.msgsndr.com/urls/l/k9UHHNsVwN

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G13. Final Email
- Type: Workflow: Registration Abandoned (3) · GHL source: workflow · From: Discipline Rift <luis@disciplinerift.com> · Sent 2026-05-29 → 2026-06-22 · 108 sends

```text
SUBJECT: Final Email

https://services.msgsndr.com/urls/l/rJ2a9ARSBnI

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G14. Discipline Rift: Next Steps
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-07-31 → 2026-07-31 · 13 sends

```text
SUBJECT: Discipline Rift: Next Steps

Coach Angelise,
What we do as coaches matters. Through sports, we have the opportunity to help children become more active, confident, disciplined, and connected.
Please save the following dates:
August 5
Flyers and Supplies Pickup
5:00 PM to 9:00 PM
Discipline Rift Headquarters
3847 E Colonial Dr
Orlando, FL 32803
August 6
Meet the Families Events
Approximately 8:00 AM to 6:00 PM
Coaches will receive an AM + PM assignment with their school location and time frames.
August 29
Annual DR Training Day (conference day for our coaches)
8:00 AM to 2:00 PM
Arrival at 7:45 AM
Discipline Rift Headquarters
3847 E Colonial Dr
Orlando, FL 32803
Save DR Training Day to your calendar [https://calendar.google.com/calendar/event?…]
Please let us know about any scheduling conflicts as soon as possible.

We look forward to preparing together and creating a meaningful season for every player under our guidance.
Discipline Rift
www.disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G15. Back to school this Tuesday, are you ready?
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-08-09 → 2026-08-18 · 2236 sends

```text
SUBJECT: Back to school this Tuesday, are you ready?

The supplies are ready, but what is your child doing after school?

Discipline Rift

Hi [parent],

The supply list is done. Shoes, backpack, folders, the new bedtime.

But what else isn't on the list? Maybe sports and physical activity?

Yes, sports are as important as everything else: 80% of brain cells focus on movement.

Volleyball • Tennis • Pickleball • Flag Football

REGISTER [https://link.msgsndr.com/email-tracking/dfd43397e45?…]

POINTS FOR OUR PARENTS TO BE MINDFUL OF

What matters this school year

1. How their body moves through space.

The coordination between what they see, where they are, and what they do with it. We're seeing larger groups of players behind in motor coordination.

2. What they do the first time something is hard.

At this age, the first conclusion is almost always, "I can't do this." What they learn to do next is the part that follows them into the classroom and everywhere else.

3. Every practice runs on a method, not a mood.

We teach the skill until a child who has never touched a ball understands it. We drill it in a format they will actually stay engaged in. Then, we play a real game using it.

If a program has no method, your child's development comes down to luck. It depends on whether they happen to get a coach who is good at explaining things.

4. Easy for you. We will do what is necessary.

No transportation is needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school.

5. If you ask, "How was practice?" and just hear, "Fine."

You will receive one update after every practice from the coach with information that matters (not just a bunch of nonsense) through the parent dashboard, where you can see your child's progress and photos from the court.

BUILT FOR THE SCHOOL WEEK

Easy for you. Intentional for them.

✓

Six weeks of coached practice

✓

On your child's campus, immediately after dismissal

✓

No transportation needed

✓

Beginner-friendly to advanced

Our value is teaching the skills and a passion for the sport.

VALUE GUARANTEE

If we do not deliver it, you receive a 100% refund at any time during the season.

REGISTER [https://link.msgsndr.com/email-tracking/dfd43397e45?…]

Low cost — everything included.

Wishing your child a valuable, enriched school year.

Coach Luis

Founder, Discipline Rift

Running at 55 schools across Central Florida

DISCIPLINE RIFT

Value Guarantee · Running at 55 schools in Central Florida

713 W Yale St, Orlando, FL 32804 · [phone] [tel: 14076147454]

info@disciplinerift.com [mailto:info@disciplinerift.com] ·
disciplinerift.com [https://link.msgsndr.com/email-tracking/dfd43397e45?…]

Privacy · Terms · © 2026 Discipline Rift (Torres Rivero LLC)

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G16. First week is done. Is your child ready?
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-08-16 → 2026-08-18 · 2214 sends

```text
SUBJECT: First week is done. Is your child ready?

Sports after school happen right at their school

Discipline Rift

Registration is open for after-school sports at your child's school.

Volleyball • Tennis • Pickleball • Flag Football

Hi [parent],

The first week of school is done.

Your child's time after school should be intentional.

REGISTER [https://link.msgsndr.com/email-tracking/85ebb347098?…]

They need a place to begin and develop.

One of our parents told me that her daughter, Valeria, had never been very athletic.

She signed her up for after-school volleyball anyway.

Valeria started as a complete beginner.

She practiced once a week.

Right at her own school.

I know another activity can sound like another drive, another schedule, and another problem for a parent to solve.

That was not the case for her mom.

She did not have to pick Valeria up and drive her somewhere else. Our coaches came directly to the school.

Over time, she developed skills.

Not because she was already athletic.

Because she started.

Her mom could also reach the coach directly through the parent dashboard whenever she needed something. No going through admin staff.

Six weeks. Once a week. $129.

Click below, search for your child's school, and register.

REGISTER [https://link.msgsndr.com/email-tracking/85ebb347098?…]

START HERE

Give them a place to begin.

✓

A six-week season for $129

✓

Practice once a week, right after class

✓

No transportation needed

✓

Direct coach messaging through the parent dashboard

Search for your child's school and complete registration.

A place to begin. A place to develop.

Coach Luis

Founder, Discipline Rift

Running at 55 schools across Central Florida

DISCIPLINE RIFT

Value Guarantee · Running at 55 schools in Central Florida

713 W Yale St, Orlando, FL 32804 · [phone] [tel: 14076147454]

info@disciplinerift.com [mailto:info@disciplinerift.com] ·
disciplinerift.com [https://link.msgsndr.com/email-tracking/85ebb347098?…]

Privacy · Terms · © 2026 Discipline Rift (Torres Rivero LLC)

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G17. Long weekend! Volleyball starts this week
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-09-05 → 2026-09-05 · 2187 sends

```text
SUBJECT: Long weekend! Volleyball starts this week

Monday is Labor Day. Then the volleyball team starts at your school.

The long weekend ends Monday.

Volleyball starts this week.

A volleyball team at your child's elementary school.

Elementary • K through 5th • Beginner-friendly to advanced • No transportation needed

REGISTER [https://link.msgsndr.com/email-tracking/85cad8f927a?…]

Hi [parent],

This is a long weekend. Enjoy it.

Then the school week gets real, and the hours between dismissal and dinner with your family start filling up.

Your child's time after school should be intentional.

Your child does not need to already be athletic.

They need a team to begin and develop on.

Take advantage of the first week. Search for your child's school and claim their spot.

Three things about the volleyball team

On campus.

No transportation needed.

Volleyball practice happens right on your child's school campus, immediately after dismissal.

A method, not a mood.

We actually teach.

Our coaches train and prepare to teach the skills the right way, so every child has a real place to begin and develop.

You can ask.

If "How was volleyball?" only gets you "Fine," you still have a real answer.

In the parent dashboard, you can see progress and team photos, receive updates, and message the coach directly.

THIS VOLLEYBALL SEASON

Six weeks on a volleyball team.

One practice a week, right after school.

✓

Volleyball on your child's campus

✓

Beginner-friendly to advanced

✓

Parent dashboard and coach updates

✓

No transportation needed

LOW COST. EVERYTHING INCLUDED.

100% refund, any time during the season.

If we don't deliver the value—real teaching and real progress—you receive a full refund.

REGISTER [https://link.msgsndr.com/email-tracking/85cad8f927a?…]

Search for your child's school and claim the spot.

Running at 55 schools across Central Florida, teaching passion and discipline.

Wishing your child a valuable, enriched school year.

Coach Luis

Founder, Discipline Rift

Discipline Rift

Value Guarantee · Running at 55 schools in Central Florida

713 W Yale St, Orlando, FL 32804 · [phone] [tel: 14076147454]

info@disciplinerift.com [mailto:info@disciplinerift.com] ·
disciplinerift.com [https://link.msgsndr.com/email-tracking/85cad8f927a?…]

Privacy · Terms · © 2026 Discipline Rift (Torres Rivero LLC)

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G18. Happy Labor Day! Volleyball is here
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-09-07 → 2026-09-08 · 1974 sends

```text
SUBJECT: Happy Labor Day! Volleyball is here

Last day of the weekend, First day of the volleyball is this week!

Last day of the long weekend.

Time to get your child on the team.

Elementary • K through 5th • Beginner-friendly to advanced • No transportation needed

REGISTER [https://link.msgsndr.com/email-tracking/a1950d0665e?…]

Hi ,

Happy Labor Day! What is your family doing today? Today, you have the whole day.

Tomorrow they go back. What happens after school?

The screens are not a plan. A team is.

We have a place where your child can begin and develop.

Right at school.

Volleyball practice happens on campus. No transportation needed.

They get to learn, not just spend time.

Our coaches have been training and preparing to coach the right way.

You can ask.

On the parent dashboard, you can see progress and team photos, receive updates, and message the coach directly.

SEASON STARTS TOMORROW

Six weeks on a volleyball team.

One practice a week, right after school.

✓

Volleyball on your child's campus

✓

Beginner-friendly to advanced

✓

Parent dashboard and coach updates

✓

No transportation needed

LOW COST. EVERYTHING INCLUDED.

100% refund, any time during the season.

REGISTER [https://link.msgsndr.com/email-tracking/a1950d0665e?…]

Search for your child's school and claim the spot before tomorrow.

The largest sports program in schools across Central Florida, teaching passion and discipline.

Enjoy the rest of the holiday. See you on the court tomorrow.

Coach Luis

Founder, Discipline Rift

Discipline Rift

Value Guarantee · Running at 55 schools in Central Florida

713 W Yale St, Orlando, FL 32804 · [phone] [tel: 14076147454]

info@disciplinerift.com [mailto:info@disciplinerift.com] ·
disciplinerift.com [https://link.msgsndr.com/email-tracking/a1950d0665e?…]

Privacy · Terms · © 2026 Discipline Rift (Torres Rivero LLC)

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G19. Next sports season is here. [child] isn't registered yet
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-10-04 → 2026-10-05 · 1473 sends

```text
SUBJECT: Next sports season is here. [child] isn't registered yet

Hi ,

isn't on the team for next season yet.

The second quarter is almost here, and the next season starts with it.

Search for your child's school and register → [https://link.msgsndr.com/email-tracking/74f5f5e77ca?…]

Teams are now open for volleyball, tennis, pickleball, soccer, and flag football.

The weather is cooling down. This is the perfect time to practice.

On their own campus. No transportation needed.

Real coaching. Our coaches have been training and preparing to teach the skills the right way. Beginner friendly to advanced.

You can ask. See progress and team photos on the parent dashboard, and message the coach directly.

Low cost. Everything included. If we do not deliver real teaching and real progress, you receive a 100% refund at any time during the season.

The hours between the bell and dinner will get filled by something. Give a team, a coach, and a skill to build.

Search for your child's school and register → [https://link.msgsndr.com/email-tracking/74f5f5e77ca?…]

Coach Luis

Founder, Discipline Rift

P.S. We care about giving a place to begin and develop. We hope to see you next season.

Discipline Rift · 713 W Yale St, Orlando, FL 32804

You are receiving this because you requested information from Discipline Rift or registered with us previously.

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G20. Good things come to an end! isn't registered for next season
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-10-11 → 2026-10-11 · 2331 sends

```text
SUBJECT: Good things come to an end! isn't registered for next season

The current season is almost over. Their progress does not have to stop with it.

Hi ,

is a place to grow.

You have heard that from other sports programs.

But I mean that we actually teach and players grow. Here is how.

Our coaches do not simply keep players busy.

REGISTER FOR NEXT SEASON → [https://link.msgsndr.com/email-tracking/7103c989041?…]

We use chunking to teach skills and instructions.

We explain them. We demonstrate them. Players practice them.

Then they use them while playing .

This gives something real to remember.

They can compare how they played at the beginning of the season with how they play now.

They can feel the difference.

They may still make mistakes.

They may still lose points or games.

But underneath that, they know:

I could not do this before.
Now I can.

That is confidence built from evidence.

Instead of feeling like they are failing, they have proof that they are improving.

But one season is not enough.

Progress needs repetition.

Skills need continued coaching.

Relationships with teammates and coaches need time.

Next season continues what has already started.

The skills. The relationships. The discipline. The belief that they can improve when they keep working.

is not registered for next season yet.

That progress is possible because you, , made the decision to give a place to begin.

Now give them a place to continue.

Six weeks. One practice each week.

Right after school. On campus.

No transportation needed.

Low cost. Everything included.

100% refund at any time during the season.

REGISTER FOR NEXT SEASON → [https://link.msgsndr.com/email-tracking/7103c989041?…]

Search for your child's school and secure their place on the next team.

Coach Luis

Founder, Discipline Rift

P.S. We are coaches who actually teach.

Discipline Rift · 713 W Yale St, Orlando, FL 32804

You are receiving this because you requested information from Discipline Rift or registered with us previously.

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G21. season is coming to an end.
- Type: Campaign · GHL source: campaign · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-10-18 → 2026-10-18 · 2262 sends

```text
SUBJECT: season is coming to an end.

The next season starts in one week. Keep building on what they started.

Hi ,

Sports matter more than we sometimes realize.

REGISTER FOR THE NEXT SEASON → [https://link.msgsndr.com/email-tracking/6c8a09b5c9a?…]

Why?

Because of the hours they fill.

Once the school bell rings, those hours can be spent in front of a screen.

Or they can be spent with a coach, a team, and a skill to develop.

For the past several weeks, has spent that time learning .

Practicing skills. Making mistakes. Listening to a coach. Trying again.

Now, the season is coming to an end.

But the development should not end with it.

One season introduces the skills. Continuing gives the repetition and coaching needed to keep developing them.

The next season starts in one week.

REGISTER FOR THE NEXT SEASON → [https://link.msgsndr.com/email-tracking/6c8a09b5c9a?…]

Next season does not repeat this one. Players build on the skills they started and learn how to connect them during play.

Same team environment. Same campus. More time for the coach to teach and for to improve.

No transportation needed. Our coaches handle everything on campus from dismissal until practice ends.

If we do not deliver real teaching and real progress, you receive a 100% refund at any time during the season.

CONTINUE WITH → [https://link.msgsndr.com/email-tracking/6c8a09b5c9a?…]

Coach Luis

Founder, Discipline Rift

P.S. has already started. Now, give them the opportunity to keep developing.

Discipline Rift · 713 W Yale St, Orlando, FL 32804

You are receiving this because you requested information from Discipline Rift or registered with us previously.

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G22. practices begin this week at . There may still be room!
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-10-26 → 2026-10-26 · 1451 sends

```text
SUBJECT: practices begin this week at . There may still be room!

New skills, new challenges, and purposeful progression for .

Hi ,

The new season starts this week at .

There is still room for to join the team and begin the season on time.

REGISTER → [https://link.msgsndr.com/email-tracking/25211b6603f?…]

Skill progression starts with the first practice. Last season established the foundation. This season, our coaches add the next layer of skills and connect those skills during play.

Variability makes skills usable. We change the distance, target, movement, timing, pressure, and decisions within each activity. Players learn how to use the same skill in different situations instead of repeating the same drill.

Every practice will look different. will experience new challenges, games, and practice conditions compared with last season.

The activities change, but the teaching method remains consistent: we explain the skill, demonstrate it, let players practice it, and then apply it in play.

Starting this week matters. The first practice establishes the starting skill and prepares players for the next layer. Joining later means entering after the progression has already begun.

Easy for you. No transportation needed. Our coaches handle everything on campus from dismissal until practice ends.

You will see the progression. After every practice, the coach posts an update to your parent dashboard with the skill taught, the progress made, and what the team will work on next.

If we do not deliver real teaching and real progress, you receive a 100% refund at any time during the season.

REGISTER FOR → [https://link.msgsndr.com/email-tracking/25211b6603f?…]

We look forward to helping continue developing this season.

Coach Luis

Founder, Discipline Rift

P.S. The progression begins this week. Register before the first practice.

Discipline Rift · 713 W Yale St, Orlando, FL 32804

You are receiving this because you requested information from Discipline Rift or registered with us previously.

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G23. Practice is Happening as Scheduled
- Type: Campaign · GHL source: campaign · From: Discipline Rift <coachluis@disciplinerift.com> · Sent 2026-11-02 → 2026-11-02 · 20 sends

```text
SUBJECT: Practice is Happening as Scheduled

Hi [parent],
We want to confirm that today's practice will move forward as scheduled.
Despite the incoming storm, we are proceeding with practice for your child's team.
Practice Details:
Date: Today

Time: Regular practice time

Location: Pavillion

We will continue monitoring weather conditions and notify you if anything changes.
We look forward to seeing our players at practice!
Stay safe,
Discipline Rift

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G24. 7-day: We're seven days away from VOLLEYBALL HILLCREST!
- Type: Workflow: Season Start Reminder (7-day) · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-03 → 2026-10-23 · 355 sends

```text
SUBJECT: 7-day: We're seven days away from VOLLEYBALL HILLCREST!

Water, a snack for before practice, and comfortable clothes to play in.

DISCIPLINE RIFT

Hi [parent],

We're seven days away from VOLLEYBALL HILLCREST!

Make sure to remind your child about practice: they'll need water, a snack for before practice, and comfortable clothes to play in.

SCHEDULE

Fri, Sep 11, 2026
3:15 PM – 4:15 PM

Practice 1

Fri, Sep 18, 2026
3:15 PM – 4:15 PM

Practice 2

Fri, Sep 25, 2026
3:15 PM – 4:15 PM

Practice 3

Fri, Oct 2, 2026
3:15 PM – 4:15 PM

Practice 4

Fri, Oct 9, 2026
3:15 PM – 4:15 PM

Practice 5

Fri, Oct 16, 2026
3:15 PM – 4:15 PM

Practice 6

Coach: Paula Marrero

See your child on the court!

Discipline Rift Team

DISCIPLINE RIFT

Teaching developmental skills and inspiring passion for sport

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G25. 1-day: Volleyball is tomorrow!
- Type: Workflow: Season Start Reminder (1-day) · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-07 → 2026-11-02 · 621 sends

```text
SUBJECT: 1-day: Volleyball is tomorrow!

We're very excited to see them at practice.

DISCIPLINE RIFT

Volleyball is tomorrow!

Hi [parent],

We're very excited to see [child] at practice.

SCHEDULE

Wed, Sep 9, 2026
2:15 PM – 3:15 PM

Practice 1

Wed, Sep 16, 2026
2:15 PM – 3:15 PM

Practice 2

Wed, Sep 23, 2026
2:15 PM – 3:15 PM

Practice 3

Wed, Sep 30, 2026
2:15 PM – 3:15 PM

Practice 4

Wed, Oct 7, 2026
2:15 PM – 3:15 PM

Practice 5

Wed, Oct 14, 2026
2:15 PM – 3:15 PM

Practice 6

Team: VOLLEYBALL PINECREST AVALON

Coach: Agostina Fontana

See you on the court!

Discipline Rift Team

DISCIPLINE RIFT

Developing young players in volleyball, tennis, pickleball, and flag football

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G26. [child]'s First Volleyball Practice Is Tomorrow
- Type: Workflow: Season Start Reminder (first practice) · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-01 → 2026-11-02 · 547 sends

```text
SUBJECT: [child]'s First Volleyball Practice Is Tomorrow

This first week is all about getting started.

DISCIPLINE RIFT

First Practice

Hi [parent],

Volleyball starts tomorrow.

[child]'s first DR Volleyball practice of the Fall 2026 season is tomorrow.

This first week is all about getting started. Coach Ilaria Vouriotis will introduce themselves and begin teaching the foundational skills and movements [child] will build on throughout the season.

Tomorrow, players will

•

Watch Coach Ilaria Vouriotis demonstrate skills and movements.

•

Practice those movements through drills and games.

•

Learn where those skills appear in game-like situations.

•

Begin connecting individual movements to the game itself.

As players become comfortable, Coach Ilaria Vouriotis will add variations and new challenges for those who are ready to take the skill one step further.

The goal is for [child] to understand the movements, begin performing them correctly, and start seeing how they connect to Volleyball.

PRACTICE DETAILS

Player

[child]

Team

VOLLEYBALL HAMLIN

Coach

Ilaria Vouriotis

Day

Wednesday

Schedule

2:15 PM – 3:15 PM

Location

16145 Silver Grv Blvd, Winter Garden, FL 34787

Please have [child] bring a water bottle, athletic shoes, and comfortable athletic clothes.

If you have any questions, you can contact Coach Ilaria Vouriotis through the Parent Dashboard.

MESSAGE YOUR COACH [https://www.disciplinerift.com/parent/messages]

www.disciplinerift.com/parent/messages [https://www.disciplinerift.com/parent/messages]

We're excited to get [child] started tomorrow.

Discipline Rift Coaching Team

DISCIPLINE RIFT

Developing young players in volleyball, tennis, pickleball, and flag football

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G27. Tomorrow, We Start Seeing Volleyball Differently
- Type: Workflow: Weekly Practice Reminder (wk1) · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-01 → 2026-10-27 · 358 sends

```text
SUBJECT: Tomorrow, We Start Seeing Volleyball Differently

This week, we're going deeper into awareness.

DISCIPLINE RIFT

Practice Tomorrow

Hi [parent],

Seeing Volleyball differently.

[child]'s DR Volleyball practice is tomorrow.

This week, we're going deeper into awareness. Helping players understand not only what they are doing, but what is happening around them while they play.

Coach Ranya Mahmouki will continue reinforcing the skills [child] learned while increasingly asking players to recognize when, where, and why those skills should be used.

Tomorrow, players will work on

•

Becoming more aware of their body position and movement.

•

Recognizing teammates and opponents around them.

•

Understanding when and where previously learned skills should be used.

•

Seeing how individual decisions affect the rest of the team.

•

Responding positively to mistakes, challenges, and teammates.

•

Applying their skills in increasingly game-like situations.

For players ready for more, Coach Ranya Mahmouki will increase the number of decisions they need to make and vary the situations in which their skills must be used.

This is also where we go deeper into the mindset of being a player: effort, communication, teamwork, resilience, and learning how to respond when things do not go perfectly.

The goal is for [child] to begin thinking like a Volleyball player, not simply performing individual movements.

PRACTICE DETAILS

Player

[child]

Team

VOLLEYBALL PANTHER LAKE

Coach

Ranya Mahmouki

Day

Wednesday

Schedule

2:15 PM – 3:15 PM

Location

10151 Summerlake Groves St, Winter Garden, FL 34787

Questions about tomorrow's practice? Message your coach anytime through your Parent Dashboard.

MESSAGE YOUR COACH [https://www.disciplinerift.com/parent/messages]

www.disciplinerift.com/parent/messages [https://www.disciplinerift.com/parent/messages]

Tomorrow is another opportunity for [child] to understand Volleyball at a deeper level.

Discipline Rift Coaching Team

DISCIPLINE RIFT

Developing young players in volleyball, tennis, pickleball, and flag football

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G28. Volleyball Gets More Challenging Tomorrow
- Type: Workflow: Weekly Practice Reminder · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-01 → 2026-11-10 · 549 sends

```text
SUBJECT: Volleyball Gets More Challenging Tomorrow

This week is about advancement.

DISCIPLINE RIFT

Practice Tomorrow

Hi [parent],

Volleyball gets more challenging.

[child]'s DR Volleyball practice is tomorrow.

At this point in the Fall 2026 season, we're moving beyond simply introducing movements. This week is about advancement.

Coach Ilaria Vouriotis will continue reviewing the skills players have learned while challenging them to become more precise, coordinated, and confident using them.

Tomorrow, players will

•

Retrieve and demonstrate previously learned skills.

•

Go deeper into the details that improve each movement.

•

Work on movement, coordination, timing, and technique.

•

Begin combining different skills instead of always practicing them separately.

•

Apply those skills in changing and less predictable situations.

Sometimes a player is only one adjustment away from succeeding. Moving a little faster, getting into position sooner, or changing one small part of their technique.

Coach Ilaria Vouriotis will help [child] recognize those moments, make the adjustment, and continue working through them.

For players ready for the next level, Coach Ilaria Vouriotis will add more variability by changing combinations, movements, decisions, and situations so they continue being challenged.

The goal is for [child] to start seeing how the different skills of Volleyball connect instead of experiencing each one in isolation.

PRACTICE DETAILS

Player

[child]

Team

VOLLEYBALL HAMLIN

Coach

Ilaria Vouriotis

Day

Wednesday

Schedule

2:15 PM – 3:15 PM

Location

16145 Silver Grv Blvd, Winter Garden, FL 34787

Questions about tomorrow's practice? Message your coach anytime through your Parent Dashboard.

MESSAGE YOUR COACH [https://www.disciplinerift.com/parent/messages]

www.disciplinerift.com/parent/messages [https://www.disciplinerift.com/parent/messages]

We're excited to see [child] take another step forward tomorrow.

Discipline Rift Coaching Team

DISCIPLINE RIFT

Developing young players in volleyball, tennis, pickleball, and flag football

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G29. Tomorrow, We're Building on What They Learned in Volleyball
- Type: Workflow: Weekly Practice Reminder · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-01 → 2026-11-05 · 640 sends

```text
SUBJECT: Tomorrow, We're Building on What They Learned in Volleyball

This week is about recalling what they learned and building from it.

DISCIPLINE RIFT

Practice Tomorrow

Hi [parent],

Building on what they learned.

[child]'s DR Volleyball practice is tomorrow.

This week is about recalling what players learned and building from it. Before introducing the next layer, Coach Daylen Moss will challenge [child] to bring back the movements and skills they worked on last week.

Tomorrow, players will

•

Recall and repeat previously learned movements.

•

Reinforce the technique and small details that make those movements work.

•

Continue applying those skills through drills and game-like situations.

•

Begin learning new, related skills that connect to what they already know.

For players who are ready for more, Coach Daylen Moss will add variations that require them to perform skills in new ways, combine movements, or respond to changing situations.

The goal is for [child] to remember what they learned, perform it more consistently, and use that foundation to keep progressing in Volleyball.

PRACTICE DETAILS

Player

[child]

Team

VOLLEYBALL WEDGEFIELD

Coach

Daylen Moss

Day

Monday

Schedule

3:15 PM – 4:15 PM

Location

3835 Bancroft Blvd, Orlando, FL 32833

Please have [child] bring a water bottle and arrive ready to practice.

If you have any questions, you can contact Coach Daylen Moss through the Parent Dashboard.

MESSAGE YOUR COACH [https://www.disciplinerift.com/parent/messages]

www.disciplinerift.com/parent/messages [https://www.disciplinerift.com/parent/messages]

We're excited to see [child] back tomorrow.

Discipline Rift Coaching Team

DISCIPLINE RIFT

Developing young players in volleyball, tennis, pickleball, and flag football

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G30. It's Time to Put Everything Together in Volleyball
- Type: Workflow: Weekly Practice Reminder · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-01 → 2026-11-03 · 290 sends

```text
SUBJECT: It's Time to Put Everything Together in Volleyball

This week is about making everything stick.

DISCIPLINE RIFT

Practice Tomorrow

Hi [parent],

Putting it all together.

[child]'s DR Volleyball practice is tomorrow.

As we approach the end of the Fall 2026 season, this week is about making everything [child] learned stick.

Over the past several weeks, players have worked on skills, movement, coordination, decision-making, teamwork, and understanding how Volleyball works.

Now Coach Ilaria Vouriotis will bring those pieces together.

Tomorrow, players will

•

Revisit and reinforce skills from throughout the season.

•

Combine multiple skills during drills and games.

•

Continue improving movement, coordination, timing, and technique.

•

Make more decisions without immediately relying on the coach.

•

Apply what they know in increasingly game-like situations.

Players who have progressed further will continue receiving additional challenges, combinations, and variability rather than simply repeating what they have already mastered.

At this point, we want the learning to increasingly belong to [child].

The goal is for [child] to perform skills, recognize situations, and make decisions with greater independence. Without Coach Ilaria Vouriotis always having to tell them exactly what comes next.

By the end of this week, we want [child] to have a stronger understanding of both how to perform the skills and how to play Volleyball.

PRACTICE DETAILS

Player

[child]

Team

VOLLEYBALL HAMLIN

Coach

Ilaria Vouriotis

Day

Wednesday

Schedule

2:15 PM – 3:15 PM

Location

16145 Silver Grv Blvd, Winter Garden, FL 34787

Questions about tomorrow's practice? Message your coach anytime through your Parent Dashboard.

MESSAGE YOUR COACH [https://www.disciplinerift.com/parent/messages]

www.disciplinerift.com/parent/messages [https://www.disciplinerift.com/parent/messages]

We're excited to see [child] put more of the pieces together tomorrow.

Discipline Rift Coaching Team

DISCIPLINE RIFT

Developing young players in volleyball, tennis, pickleball, and flag football

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G31. How Far They've Come in Volleyball. Final Practice Tomorrow
- Type: Workflow: Weekly Practice Reminder (final) · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-01 → 2026-11-10 · 356 sends

```text
SUBJECT: How Far They've Come in Volleyball. Final Practice Tomorrow

This last week is about bringing everything together.

DISCIPLINE RIFT

Final Practice

Hi [parent],

Look how far they've come.

[child]'s final DR Volleyball practice of the Fall 2026 season is tomorrow.

This last week is about bringing everything together: playing, recognizing progress, and celebrating how far the team has come.

Coach Ilaria Vouriotis will bring back favorite drills, activities, and games from throughout the season and give players plenty of opportunities to use what they've learned.

Tomorrow, [child] will

•

Revisit favorite drills and games from the season.

•

Bring together skills learned over the past several weeks.

•

Spend more time playing and applying what they know.

•

Use their skills in game-like situations.

•

See how much more comfortable and capable they have become.

The game becomes much more enjoyable when players understand what they're doing and feel capable participating in it.

Tomorrow gives [child] the opportunity to experience Volleyball with skills and knowledge they didn't have when the Fall 2026 season began.

We'll also finish practice by celebrating the team.

Each player will be recognized for the effort and progress they made throughout the season. We'll award certificates, applaud our players, and give them a moment to be proud of what they accomplished together.

That celebration matters to us.

DR is an environment where [child] should feel recognized for their effort, supported by Coach Ilaria Vouriotis and their teammates, and excited about continuing to play Volleyball.

It's also a chance for everyone to look back at where the team started and appreciate how much they've grown together.

Our goal isn't only for [child] to leave knowing more about Volleyball.

We want them to leave wanting to keep playing it.

FINAL PRACTICE

Player

[child]

Team

VOLLEYBALL HAMLIN

Coach

Ilaria Vouriotis

Day

Wednesday

Schedule

2:15 PM – 3:15 PM

Location

16145 Silver Grv Blvd, Winter Garden, FL 34787

Thank you, Jessica, for allowing Coach Ilaria Vouriotis and Discipline Rift to be part of [child]'s Fall 2026 season.

Questions about tomorrow's practice? Message your coach anytime through your Parent Dashboard.

MESSAGE YOUR COACH [https://www.disciplinerift.com/parent/messages]

www.disciplinerift.com/parent/messages [https://www.disciplinerift.com/parent/messages]

We're excited to celebrate with [child] tomorrow.

Discipline Rift Coaching Team

DISCIPLINE RIFT

Developing young players in volleyball, tennis, pickleball, and flag football

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```

### G32. A note about [child]'s session
- Type: Workflow: Parent Absence · GHL source: workflow · From: Discipline Rift <info@disciplinerift.com> · Sent 2026-09-01 → 2026-11-20 · 411 sends

```text
SUBJECT: A note about [child]'s session

Hope [child] is doing well. They were missed at today's practice!

DISCIPLINE RIFT

Attendance Note

Hi [parent],

We missed [child] at practice today for Volleyball, on VOLLEYBALL AUDUBON.

Hope [child] is doing well. They were missed at today's practice!

If you already let us know about the absence, thank you for the heads up. If not, a heads-up in advance helps. We're coaches, not chasing down students before practice starts, so knowing ahead of time means one less thing to track.

Our goal is to keep every player progressing and connected to the team, so thanks for helping us keep everyone accountable.

TODAY'S PRACTICE

Player

[child]

Team

VOLLEYBALL AUDUBON

Sport

Volleyball

Time

3:15 PM – 4:15 PM

Questions about today's practice? Message us anytime through your Parent Dashboard:

MESSAGE US [https://www.disciplinerift.com/parent/messages]

www.disciplinerift.com/parent/messages [https://www.disciplinerift.com/parent/messages]

Hope to see [child] at the next practice!

Discipline Rift

DISCIPLINE RIFT

Teaching developmental skills and inspiring passion for sport

CONTACT

info@disciplinerift.com [mailto:info@disciplinerift.com]

[phone]

713 W. Yale Street, Orlando, FL 32804

If you no longer wish to receive these emails you may unsubscribe [https://services.msgsndr.com/emails/builder/unsubscribe-view/wAEvsOW2yMI8nTHmqIJy/…]
```


## 3. Verbatim text — Gmail

### M1. 2022-10-13 — Re: Last 2 Week to Register - Sign up Today!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 183d1a186d689b88 — (original recovered from quoted text in a reply)

```text
Last 2 Weeks to Register

Sign up Today!

Dear Parent,

Throughout the past 5 weeks, our coaches have been working on techniques such as Passing, Hitting, Serving (Volleyball), and Forehand, Backhand, Serve, and volley (Tennis). We've had the pleasure to introduce new students to not only a new sport but also a new discipline through teaching them introductory level skills along with life lessons that will shape the person they will become in the future, on and off the court.

Our returning players have also been doing an awesome job. I am proud to say that it has been a pleasure seeing how these young players have developed their game and keep improving every season.

With that being said, every player has the opportunity to keep improving and we enable continuous learning by bringing our programs back after every season. We look forward to spreading our influence and giving back to the community by passing on our knowledge to the next generation. Every time a player comes back we can make a greater impact and improve their game.

Programs start the week of October 31st, find the dates and times for each school by clicking the button down below to register now.
*Find your school* <https://shoutout.wix.com/so/9fOFCdZXS/c?…>
*Check out our site* <https://shoutout.wix.com/so/9fOFCdZXS/c?…> Created with *Explore Ascend* <https://www.wix.com/ascend/home?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/9fOFCdZXS/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M2. 2022-12-20 — Re: Limited Time Christmas Offer - Sign up today!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 18530b577c730312 — (original recovered from quoted text in a reply)

```text
Limited Time Christmas Offer - Sign Up Now!

Dear Parent,

With the season now over, we wanted to update you on the the progress we were able to accomplish with all our players. Throughout the season, we were able to start implementing match playing with all of our players to start introducing them into match settings so they can adapt their skills from drills into games.

We will come back in January for more and I hope to see you all coming back for more learning experiences and life lessons to help the next generation of athletes achieve their goals throughout their journey. We have exciting plans for this 2023 and we hope you all get to be there for them!

Volleyball and Tennis programs will start on January 17th.

Please find the dates and times for each schools by clicking the button down below now!

Don't miss our on our limited time offer we are running until the end of the month!

Use code "CHRISTMAS" for 25% off
*Sign Up Now!* <https://shoutout.wix.com/so/98OKmFo05/c?…>
*Check out our site* <https://shoutout.wix.com/so/98OKmFo05/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/98OKmFo05/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*

-- Brenda L. Arroyo Crespo, Ph.D.
```


### M3. 2022-12-13 — Re: Registrations Now Open - Sign up today!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1850c29553567669 — (original recovered from quoted text in a reply)

```text
Spring Season Registrations Now Open - DR Sports & Athletics

Dear Parent,

As we all know, this week is the last week of our programs this year. 2022 has been a great year as we've gotten the opportunity to make an impact in the lives of many young players. The improvement we have seen in all of our players has been immense and we keep working and improving our tennis and volleyball curriculum in order to provide the best lessons we can for the students.

We will come back in January for more and I hope to see you all coming back for more learning experiences and life lessons to help the next generation of athletes achieve their goals throughout their journey. We have exciting plans for this 2023 and we hope you all get to be there for them!

Volleyball and Tennis programs will start on January 17th.

Please find the dates and times for each schools by clicking the button down below now!

Use code "CHRISTMSAS" for a limited time offer and get 15% off from your order!
*Sign up now!* <https://shoutout.wix.com/so/a2OK76Koz/c?…>
*Check out our site* <https://shoutout.wix.com/so/a2OK76Koz/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/a2OK76Koz/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M4. 2023-02-10 — Re: Late Spring Registrations now open - Don't miss out!!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1863b70f827d5a60 — (original recovered from quoted text in a reply)

```text
Late Spring Registrations now open - Don't miss out!!

Dear Parent,

As we get closer to the end of our current season, I wanted to share that over the past few weeks our coaches and young players have been putting in a lot of work and it is paying off. Players have been making progress and our coaches as well as ourselves are very happy to see that the discipline they have embraced has helped them achieve goals such as being more consistent with the serves for some, passing more accurately for others, and hitting winners in the court for other players. I believe that this discipline will not only help them achieve goals within the sport they practice but in the future as well and that is what we strive for.

For our next season, we are planning on having play days, camps and activities outside of school. We will keep everyone updated regarding these activities as it would be really good to have these players being a part of them. If you haven't already, I would suggest subscribing to our newsletter on our website to stay updated regarding news, offers and events.

Please visit our website to find out about dates and times for each school and don't hesitate to contact us if you have any questions or concerns regarding our programs.

See you soon!

Coach Diego / info@disciplinerift.com

Visit our website by clicking the button down below to sign up today!
*Sign Up Now!* <https://shoutout.wix.com/so/17OOs0kl4/c?…>
*Check out our site* <https://shoutout.wix.com/so/17OOs0kl4/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/17OOs0kl4/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M5. 2023-01-02 — Re: Limited Time Offer Ends Today! - Sign Up Now!
- Sender: [parent — original DR blast quoted in their reply]
- Gmail id: 185738e92186875b — (original recovered from quoted text in a reply)

```text
Happy New Year from our Family to Yours!!!

Dear Parent,

I hope you had a great time during this time. We are very excited to start this coming up season in a few weeks. I look forward to being part of all the successes and goals your children achieve this year and we would love for you all to be a part of our success as well.

We are very grateful to have the opportunity to make an impact in your children's life and be a part of their journey. I hope we get to see you all come back and be a part of our journey as well this year.

Warmest wishes,

Coach Diego / info@disciplinerift.com

Don't miss our on our limited time offer we are running until today!

Use code "CHRISTMAS" for 15% off
*Sign Up Now!* <https://shoutout.wix.com/so/a9OLpJ4IM/c?…>
*Check out our site* <https://shoutout.wix.com/so/a9OLpJ4IM/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/a9OLpJ4IM/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M6. 2023-01-11 — Re: Programs Start Next Week - Register Today!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 185a1d3f1a378846 — (original recovered from quoted text in a reply)

```text
Programs Start Next Week - Register Today!

Dear Parent,

I hope you are having a great start to the year and your young players are as well. Our coaches are missing all the young players and can't wait to start this upcoming season next week.

Please remember that all returning players will be placed in the level they finished in last season they play. Our curriculum is structured to improve the player's abilities progressively every season they come back. We have the ability to do this as our coaches split classes into groups in order to work on the skill development of each group depending on their level.

Please visit our website to find out about dates and times for each school and don't hesitate to contact us if you have any questions or concerns regarding our programs starting next week.

See you soon!

Coach Diego / info@disciplinerift.com

Visit our website by clicking the button down below to sign up today!
*Sign Up Now!* <https://shoutout.wix.com/so/75OMXi1NH/c?…>
*Check out our site* <https://shoutout.wix.com/so/75OMXi1NH/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/75OMXi1NH/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M7. 2023-01-10 — Re: Last week To Sign Up - Don't Miss out!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1859d4a8cd0e1278 — (original recovered from quoted text in a reply)

```text
Last Week to Sign up - Don't Miss out!!

Dear Parent,

Quick reminder that our programs will be starting next week and we have a lot of fun planned for our young players this year. We are ready and I know our coaches are as well!

Please visit our website to find out about dates and times for each school and don't hesitate to contact us if you have any questions or concerns regarding our programs.

Warmest wishes,

Coach Diego / info@disciplinerift.com

Visit our website by clicking the button down below to sign up today!
*Sign Up Now!* <https://shoutout.wix.com/so/12OMN5bki/c?…>
*Check out our site* <https://shoutout.wix.com/so/12OMN5bki/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/12OMN5bki/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M8. 2022-10-26 — Re: Limited Spots Available - Don't Miss Out!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 184157033196e56f — (original recovered from quoted text in a reply)

```text
Limited Spots Available - Don't Miss Out!

Dear Parent,

We are a less than a week out from starting our Winter Season and schools are getting filled up really fast!

Returning players will have a blast as they will be adapting and learning from our different levels on our curriculum. Every season we have a goal to improve not just our players but ourselves too and bring the best we have to the young players that learn and look up from us.

Programs start next week, find the dates and times for each school by clicking the button down below to register now.
*Sign up now!* <https://shoutout.wix.com/so/22OGKkwI5/c?…>
*Check out our site* <https://shoutout.wix.com/so/22OGKkwI5/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/22OGKkwI5/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M9. 2022-10-18 — Re: Late Fall Registrations - Sign up Today!
- Sender: [parent — original DR blast quoted in their reply]
- Gmail id: 183eb657b6d95f59 — (original recovered from quoted text in a reply)

```text
Don't Miss out on the Fun - Sign up Today!

Everyday we get closer to the end of our season but that doesn't mean we are stopping.

At Discipline Rift we believe that practice makes permanent and because of that we just opened our registrations for our upcoming Season starting the week of the 31st.

This season we will be leveling up our players and improving the skills our experienced coaches have been teaching them in both Volleyball and Tennis. Be on the lookout for emails regarding future play days and mini tournaments we are planning. Click the button down below to register now!!

Find your school<https://shoutout.wix.com/so/2aOEjmFfB/c?…> [https://static.wixstatic.com/media/aee59c_49fb538bdfc54478af…] [https://static.wixstatic.com/media/aee59c_19f37cf96f2f4b7980…] Check out our site [https://images.wixstatic.com/media/b49ee3_dd9b1a8812ae411384…] <https://shoutout.wix.com/so/2aOEjmFfB/c?…> Created with [https://static.wixstatic.com/media/b49ee3_e3831b3e6e844c01ad…] Explore Ascend<https://www.wix.com/ascend/home?…>   You've received this email because you are a subscriber of this site<https://shoutout.wix.com/so/2aOEjmFfB/c?…
```


### M10. 2023-08-09 — Re: School Starts Tomorrow-Register Today!!!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 189dc32d44781a8e — (original recovered from quoted text in a reply)

```text
School Starts Tomorrow-Register Today!!!

Dear Parent,

The moment we've all been waiting for is finally here! and I wouldn't want you to miss out on this season. As summer comes to an end, we're thrilled that our fall season is just around the corner. Programs will be starting the week of September 11th and we can't wait to see you all coming back!

We strongly encourage you to subscribe to our newsletter via our website, in order to remain up-to-date with all the latest news, offers, and events related to our camps and programs. You can subscribe by visiting us at: https://www.disciplinerift.com/.

See you soon!

Coach Diego / info@disciplinerift.com

Sign Up Today

by clicking the button down below!
*Sign up Now!* <https://shoutout.wix.com/so/d9OdQW_-c/c?…>
*Check out our site* <https://shoutout.wix.com/so/d9OdQW_-c/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/d9OdQW_-c/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*

-- Luis Torres
```


### M11. 2023-04-13 — Re: Tennis and Volleyball Camps Now Available!! - DR Sports & Athletics
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1877a7c9e57b22f0 — (original recovered from quoted text in a reply)

```text
Tennis and Volleyball Camps Now Available!! - DR Sports & Athletics

Dear Parent,

With our current season now approaching the end and also being the last one for this current school year until the fall, I believe it is necessary for players to stay consistent and keep practicing the skills we have been doing the whole school year. To facilitate this, we are pleased to announce that we will be offering both Volleyball and Tennis camps this summer for all of our players.

These camps will prioritize intensity and proficiency, as we will be limiting registration to a smaller number of players. This will enable our experienced coaches to provide individualized attention and guidance, allowing each player to develop their skills on a deeper level and reach their full potential.

We strongly encourage you to subscribe to our newsletter via our website, in order to remain up-to-date with all the latest news, offers, and events related to our camps and programs. You can subscribe by visiting us at: https://www.disciplinerift.com/.

See you soon!

Coach Diego / info@disciplinerift.com

Click the Sign Up button down below to register today!
*Sign Up Now!* <https://shoutout.wix.com/so/dfOTrycPM/c?…>
*Check out our site* <https://shoutout.wix.com/so/dfOTrycPM/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/dfOTrycPM/c?…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M12. 2022-12-05 — Re: Season Update - DR Sports & Athletics
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 184e320ec5a25a73 — (original recovered from quoted text in a reply)

```text
Season Update - DR Sports & Athletics

Dear Parent,

The past 4 weeks have been amazing and we wanted to share the progress with you. Despite having a second hurricane interrupting our season, we have managed to add more time every class we have had since then which has been so helpful because the extra time has allowed us to spend more time in drills and focus on improving basic skills. In addition, our more advanced players have been focusing on using these skills in competitive match setting among themselves during our classes which they have been enjoying a lot.

Overall, I have really enjoyed this season and I look forward to our last two weeks before we are done for the year. Please feel free to ask us any questions or concerns you may have, I will be happy to answer them.

Kind regards,

-Diego Rivero

[phone] / info@disciplinerift.com

*Play Now!* <https://shoutout.wix.com/so/a7OJRMbil/c?…>
*Check out our site* <https://shoutout.wix.com/so/a7OJRMbil/c?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/a7OJRMbil/c?…
```


### M13. 2022-09-01 — Re: Looking forward to seeing you at WINDERMERE ELEMENTARY VOLLEYBALL
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 182fb3a8849895ad — (original recovered from quoted text in a reply)

```text
Looking forward to seeing you at WINDERMERE ELEMENTARY VOLLEYBALL
*Contact Us* <https://shoutout.wix.com/so/tr/b5a3a22c-315b-4504-b164-9b9dc…>

Share on social

[image: Share on Facebook] <https://shoutout.wix.com/so/tr/b5a3a22c-315b-4504-b164-9b9dc…>

*Check Out My Website* <https://shoutout.wix.com/so/tr/b5a3a22c-315b-4504-b164-9b9dc…> Created with *Explore Ascend* <https://www.wix.com/ascend/home?…>
*You've received this email because you are a subscriber of this site <https://shoutout.wix.com/so/tr/b5a3a22c-315b-4504-b164-9b9dc…>.*
*If you feel you received it by mistake or wish to unsubscribe, please click here <https://www.wixapis.com/email-marketing/v1/email-subscriptio…>.*
```


### M14. 2023-04-13 — Updated Schedule Late Spring Season - DR Sports & Athletics
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1877af9a7254a074

```text
Dear Coach {{Name}},

We hope all is well, please find the updated schedule for our current season attached as we have made some changes according to availability changes and requests from the team.

Please let me know if we can help with anything else,

Have a great day!

Luis Torres
Owner & Founder
Discipline Rift

www.disciplinerift.com [http://www.disciplinerift.com/]

[phone] [tel:(407)+276-3234]
```


### M15. 2024-03-11 — Welcome to DRVC Pre-Season - Your Journey Begins Tomorrow! 10U LIME
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 18e2ad8beeb928b6

```text
Good evening,

We hope you had a great weekend!

We are beyond excited to kick off our practices tomorrow, and we're looking forward to seeing the energy and passion each player brings to the team. Here's a quick rundown of what you need to know:

+ Check-In: Please arrive and check in with your player, {{Name}}, 5-10 minutes before practice begins. This helps us start on time and ensures every minute of practice is used effectively.

+ Practice Schedule: Club practice will be from 5:00 PM to 7:00 PM. We've planned a dynamic session to get our season started on the right foot!

+ Stay Informed: We will be sharing important updates and instructions to keep you in the loop.

+ Gear and Preparation: Make sure {{Name}} comes prepared with the necessary gear, water, and a lot of energy. We believe in starting strong and maintaining that momentum!

#Communication is Key: We value open communication with our DRVC family. Please don't hesitate to reach out if you have any questions and/or feedback.

Once again, welcome to the DRVC Family! We look forward to an outstanding Pre-Season

See you at our gym!

713 W Yale St, Orlando, FL 32804

[https://mysignature.io/?…]Luis Torres Co-Founder
info@disciplinerift.com [mailto:info@disciplinerift.com]
www.disciplinerift.com [https://www.disciplinerift.com]
[phone] [tel:(407)+614-7454]
[https://www.instagram.com/disciplinerift] [https://www.facebook.com/disciplinerift]

[https://mysignature.io/editor/?…]
```


### M16. 2024-03-03 — Congratulations! Volleyball Club Team Placement
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 18e01edfb57c2a1b

```text
Dear Coach {{Name}},

Please find the attached file, it contains the updated version of the schedule with the changes based on the days off that some coaches needed. Please make sure you look through it and make sure everything is correct. If you coach with someone else on one of your days, the first name that shows will be the head coach that day and the second name that shows will be the assistant coach that day.

Please let me know if you have any questions or concerns, we look forward to a great season.

Diego Rivero
Owner & Founder
Discipline Rift

www.disciplinerift.com [http://www.disciplinerift.com/]

[phone] [tel:(407)+276-3234]
```


### M17. 2025-04-10 — First Day of Volleyball - Week 1 with DR Sports & Athletics
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1961fb50b6d4138d

```text
Good morning {{Name}}!
We’re excited to kick off our new volleyball season today! To start things off on the right foot, we’ll focus on developing the fundamentals by working on passing and setting while reinforcing teamwork.
All while creating a fun and engaging environment for the players.

Our goal is to foster an enjoyable and productive atmosphere that inspires a love for the sport and encourages growth.
Reminders:
Class runs from 3:15 PM to 4:15 PM.

Students will be sent by their teachers to meet their coach.

After class, students will be taken to their aftercare location or parents in the car rider line. Please notify us only if your child’s pick-up method has changed!

We’re excited to begin this journey with your child and look forward to a season filled with development, teamwork, and fun!
Feel free to reach out if you have any questions or need support.

Season Schedule: Please mark your calendars with the following dates
Thursday, April 10th
Thursday, April 17th
Thursday, April 24th
Thursday, May 1st
Thursday, May 8th
Thursday, May 15th
Best,

[https://www.instagram.com/disciplinerift]

Luis Torres
Founder
DR Sports & Athletics

[phone] [tel:(407)+614-7454]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.com/]

713 W Yale St, Orlando, FL 32804
```


### M18. 2025-04-17 — Volleyball Week 2 with DR Sports & Athletics
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19644558647130e0

```text
Hey {{Name}}!
We’re back on the court today for Week 2 of volleyball with DR Sports & Athletics, and yes—we’re reviewing passing and setting again. Why? Because these skills are essential. They’re the foundation of every play, every rally, and every win.
This week, we’re going deeper. Players will be working on:
Footwork — developing movement that supports quick and accurate positioning

Calling the ball — building clear communication and confident decision-making

Teamwork — reinforcing the habits that help players trust and rely on each other

We’re not just going through the motions. We’re helping each athlete level up with purpose and precision.
Reminders:
Students will be sent by their teachers to meet their coach

Class runs from 3:15 PM to 4:15 PM

After class, students will be taken to aftercare or the car rider line

Please notify us of any changes to your child’s dismissal plan

Season Schedule:
Thursday, April 10th

✔️
Thursday, April 17th

✔️
Thursday, April 24th
Thursday, May 1st
Thursday, May 8th
Thursday, May 15th

We’re excited to keep building momentum this week. Let’s make it a strong Wednesday.

Best,

[https://disciplinerift-dot-yamm-track.appspot.com/2Gh513KuIF…]

Luis Torres
Founder
DR Sports & Athletics

[phone] [https://disciplinerift-dot-yamm-track.appspot.com/2yMYPzPXEI…]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift-dot-yamm-track.appspot.com/21uwm6wyuO…]

713 W Yale St, Orlando, FL 32804
```


### M19. 2025-05-07 — Last Week of Volleyball with DR Sports & Athletics
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 196abb81d8f90225

```text
Hey {{Name}}!

Today marks the final session (Week 6) of our Volleyball season at DR Sports & Athletics, and we are so proud of everything our players have accomplished over these past several weeks. From learning how to serve and rotate to working as a team, each athlete has shown incredible growth, effort, and discipline.
To celebrate, we’ll be hosting a short closing ceremony during today’s session. Players will receive a certificate of completion, and we’ll enjoy a donut treat together to close out the season on a high note.
Important Reminder:

Today is not an early release day – volleyball will run at the regular time from 3:15 PM to 4:15 PM.
Season Schedule (Wednesdays):

Wednesday, April 2

Wednesday, April 9

Wednesday, April 16

Wednesday, April 23

Wednesday, April 30

Wednesday, May 7 – Final Session and Celebration

Thank you for your support throughout the season. It's been a joy coaching your children and watching them grow in skill and confidence. We hope to see many of them back for future seasons and even more volleyball fun.

Best regards,

[https://www.instagram.com/disciplinerift]

Luis Torres
Founder
DR Sports & Athletics

[phone] [tel:(407)+614-7454]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.com/]

713 W Yale St, Orlando, FL 32804
```


### M20. 2025-05-28 — DRVC Volleyball Tryouts – This Saturday!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1971430d2a99b379

```text
Hey {{Name}}!

Just a quick reminder that your child is ready for the DRVC Volleyball Tryouts this Saturday, May 31st!

Time: 9:00 AM – 11:00 AM
Location: 713 W Yale St, Orlando, FL 32804
Dedicated Coaches
Growth-Centered Environment
A True Volleyball Family
At DRVC, we’re not just building volleyball skills, we’re nurturing teamwork, discipline, and leadership in a space that feels like home.

So, remember your weekend plans, and come ready for a morning of energy, effort, and cool people!

See you Saturday,

[https://www.instagram.com/disciplinerift]

Luis Torres
Founder
DR Sports & Athletics

[phone] [tel:(407)+614-7454]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.com/]

713 W Yale St, Orlando, FL 32804
```


### M21. 2025-09-15 — Tomorrow - Fall Season Discipline Rift
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1994b01279abafa8

```text
Hi Coach {{Name}},
1. New: Arrival/Start Times Shown on Schedule

We’ve updated the master schedule to include arrival and start times for each practice so it’s easier to visualize the flow.

Format: arrival / start–end

Example: 2:45 / 3:15–4:15

Arrival = when students report to the meeting area and coach check-in begins.

Start–End = active practice window.

Please plan to be on campus by the arrival time to park, manage dismissal and check-ins smoothly.

2. Head Coaches: Starting tomorrow, please use the DR Coaches Dashboard to check students in at every practice and submit final attendance by 5PM.

If attendance isn’t recorded, we have no way to confirm who was or wasn’t present—and with hundreds of children across our programs, accurate records are a safety requirement.
+ this is also a way for you to have the most updated roster (sometimes parents register late)

Dashboard link: https://dash-board-coaches-whpv.vercel.app/ [https://dash-board-coaches-whpv.vercel.app/]

Log in with: the same email we use for our daily communications to you.

Save it: add the link to your browser favorites or phone home screen.

iOS (Safari): Share button → Add to Home Screen

Android (Chrome): ⋮ menu → Add to Home Screen

+ What you can do in the DR Coach dashboard

Pull up your team(s) and check in students as they arrive.

Load final attendance before you leave campus.

+++ Pro tips:

Preload rosters on your phone before entering the school.

If the site won’t load on campus, use the PDF roster emailed by the morning:

Take a screenshot of the roster on your phone before arrival.

Mark attendance on the screenshot during practice.

Enter it into the dashboard as soon as you have service.

If you need help

Can’t log in? Reply to this email from the same address you use for coach comms and include a brief description (screenshots help).

Accountability reminder: Leaving attendance blank will be treated as a safety/compliance issue. Please build this step into your practice flow.

Thanks for keeping our kids safe and our standards high. Let’s have an amazing season!

[https://www.instagram.com/disciplinerift]

Luis Torres
Founder
DR Sports & Athletics

[phone] [tel:(407)+614-7454]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.com/]

713 W Yale St, Orlando, FL 32804
```


### M22. 2025-08-20 — Practice is today! Orangewood Tennis
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 198c8737ab20703c

```text
Good morning {{Name}},

We’re excited to let you know that our Tennis Season kicks off today, Wednesday, August 20th!

Players will head straight to the courts after school. Practice runs from 3:30 PM to 4:30 PM. Please make sure your player comes prepared with comfortable athletic wear and a water bottle.

We’re looking forward to a great season of growth, teamwork, and fun!

See you on the courts this afternoon,

[https://www.instagram.com/disciplinerift]

Luis Torres
Founder
DR Sports & Athletics

[phone] [tel:(407)+614-7454]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.com/]

713 W Yale St, Orlando, FL 32804
```


### M23. 2025-11-04 — Reminder:  VOLLEYBALL INDEPENDENCE Starts tomorrow!
- Sender: info@disciplinerift.com
- Gmail id: 19a4c9d6493da9f9

```text
Discipline Rift
1‑Day Reminder for VOLLEYBALL INDEPENDENCE

Hi [parent],
There is one day left until the start of VOLLEYBALL INDEPENDENCE.
Make sure to remind your child about the practices! Here’s the complete schedule:
SCHEDULE

Tue, Nov 4, 2025, 3:15 PM – 4:15 PM

Tue, Nov 11, 2025, 3:15 PM – 4:15 PM

Tue, Nov 18, 2025, 3:15 PM – 4:15 PM

Tue, Dec 2, 2025, 3:15 PM – 4:15 PM

Tue, Dec 9, 2025, 3:15 PM – 4:15 PM

See your child on the court!
— Discipline Rift Team
Discipline Rift - Youth Sports Development
Developing Young Athletes in Volleyball, Tennis, & Pickleball

info@disciplinerift.com [mailto:info@disciplinerift.com] • [phone]
```


### M24. 2026-01-19 — Reminder: VOLLEYBALL WATER SPRING Starts in 7 days!
- Sender: info@disciplinerift.com
- Gmail id: 19bd7e68a2c6f061

```text
Discipline Rift
1‑Day Reminder for VOLLEYBALL WATER SPRING

Hi [parent],
There are seven days left until the start of VOLLEYBALL WATER SPRING.
Make sure to remind your child about the practices! Here’s the complete schedule:
SCHEDULE

Mon, Jan 26, 2026, 3:15 PM – 4:15 PM

Mon, Feb 2, 2026, 3:15 PM – 4:15 PM

Mon, Feb 9, 2026, 3:15 PM – 4:15 PM

Mon, Feb 16, 2026, 3:15 PM – 4:15 PM

Mon, Feb 23, 2026, 3:15 PM – 4:15 PM

Mon, Mar 2, 2026, 3:15 PM – 4:15 PM

See your child on the court!
— Discipline Rift Team
Discipline Rift - Youth Sports Development
Developing Young Athletes in Volleyball, Tennis, & Pickleball

info@disciplinerift.com [mailto:info@disciplinerift.com] • [phone]

---

This email was sent automatically with n8n [https://n8n.io/?…]
```


### M25. 2025-11-11 — DR Tennis Spring Season
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19a74227e4de6501

```text
Hi Mrs. Bennet! Hope you're having a blessed week

Hope you’re doing well!

Could you share the spring dates you'd like to plan for Tennis? Only if you already know the start/end dates, and any blackout/holiday weeks, that would help me finalize the spring schedule

Also, we sent the invoice for this fall season to you just now. I’m happy to send it directly to your bookkeeper as well, would you like me to copy or forward it to Heather Russell ([email] [mailto:[email]]) ?

Take care,

[https://www.instagram.com/disciplinerift]

Luis Torres
Founder
DR Sports & Athletics

[phone] [tel:(407)+614-7454]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.com/]

713 W Yale St, Orlando, FL 32804
```


### M26. 2025-11-18 — Eagle Creek Afterschool Clubs Spring Semester
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19a96f84f274f45b

```text
Hi Ms. Lamos,

Thank you so much for reaching out and for your warm message. We truly
value our partnership with Eagle Creek Elementary and would love to
continue offering our afterschool sports program for the upcoming
spring semester.

I am confirming our intent to return for spring and will proceed with
submitting our request through Facilitron as you advised.

Looking forward to another great season at Eagle Creek!

Best regards,
Discipline Rift • info@disciplinerift.com • [phone] • disciplinerift.com
```


### M27. 2025-11-24 — Prueba Newsletter
- Sender: DisciplineRift <info@disciplinerift.com>
- Gmail id: 19ab3c2536bf94db — List-Unsubscribe header present

```text
Discipline Rift

View in browser [https://disciplinerift.com/api/email-marketing/unsubscribe/n…]

REGISTER FOR SEASON STARTING TOMORROW

Life is a question only each person can answer. We help every child search for their own.

At first, everything in sports feels new. The shots don't land, the ball flies too far, the body gets tired, and the mind starts to doubt.

Right there, in the middle of trying, change begins. Sometimes you win, other times you learn — and learning is also a way of winning.

With every serve, every fall, and every laugh after a mistake, kids discover something bigger than results: discipline isn't perfection — it's choosing not to give up when things don't go as planned.

That's finding your Rift: the moment you decide to keep going, even when it's hard, even when it takes time.

Why join this season?

Broader skill base through varied practice.

Supportive coaching and steady progress.

Age-appropriate challenge that builds confidence.

Register Now [https://www.disciplinerift.com/register]

Use code DISCIPLINE at checkout.

info@disciplinerift.com [mailto:info@disciplinerift.com]
• [phone]

© 2025 Discipline Rift

Discipline Rift

713 W Yale St

Orlando, FL 32804

Unsubscribe from newsletter [https://disciplinerift.com/api/email-marketing/unsubscribe/a…]
```


### M28. 2025-11-24 — Prueba Newsletter 5
- Sender: DisciplineRift <luis@disciplinerift.com>
- Gmail id: 19ab78be75d43b66 — List-Unsubscribe header present

```text
Discipline Rift

View in browser [https://disciplinerift.com/api/email-marketing/unsubscribe/n…]

REGISTER FOR SEASON STARTING TOMORROW

Life is a question only each person can answer. We help every child search for their own.

At first, everything in sports feels new. The shots don't land, the ball flies too far, the body gets tired, and the mind starts to doubt.

Right there, in the middle of trying, change begins. Sometimes you win, other times you learn — and learning is also a way of winning.

With every serve, every fall, and every laugh after a mistake, kids discover something bigger than results: discipline isn't perfection — it's choosing not to give up when things don't go as planned.

That's finding your Rift: the moment you decide to keep going, even when it's hard, even when it takes time.

Why join this season?

Broader skill base through varied practice.

Supportive coaching and steady progress.

Age-appropriate challenge that builds confidence.

Register Now [https://www.disciplinerift.com/register]

Use code DISCIPLINE at checkout.

luis@disciplinerift.com [mailto:luis@disciplinerift.com]
• [phone]

© 2025 Discipline Rift

Discipline Rift

123 Main Street, Suite 100

Orlando, FL 32801

Unsubscribe from newsletter [https://disciplinerift.com/api/email-marketing/unsubscribe/a…]
```


### M29. 2025-12-06 — Their Health won’t wait for “Later” - Spring Season
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19af10474fac6479 — List-Unsubscribe header present

```text
Another season of screens.. or a season of sports? You choose for this January.

Can't see this message? View in browser [https://disciplinerift.wixsite.com/so/2dPhmzJLf/c?…]

This week many of your children say they want to be back on court next season… and many of them even asked if they can bring a friend

They feel stronger. They feel included.
Right now, they’re the ones asking to stay active.

The only thing they can’t do is register themselves.
This is the moment where habits either keep going… or quietly fade away.

They will show you by bringing home their certificate
2. Their smiles and stories about what we did

Spots are limited so we can keep groups small and focused, especially if they’re bringing a friend :) being stronger together

BUTTON TO REGISTER [https://disciplinerift.wixsite.com/so/2dPhmzJLf/c?…]

Thank you for choosing an active, healthy path for your child this year. They’ll remember who made that possible.

SPRING REGISTRATION OPEN
(Volleyball • Tennis • Pickleball)
-week of Jan 19-

Go register before (literally) next year..

info@disciplinerift.com [https://disciplinerift.wixsite.com/so/2dPhmzJLf/c?…]
[phone] [https://disciplinerift.wixsite.com/so/2dPhmzJLf/c?…]

This email was sent from this site [https://disciplinerift.wixsite.com/so/2dPhmzJLf/c?…].

If you no longer wish to receive this email, change your email preferences here [https://disciplinerift.wixsite.com/my-site-4/_manage-consent…].
```


### M30. 2026-01-08 — Spring Volleyball - Discipline Rift
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19b9f407ee7b39a0

```text
Hi Ms. Taylor! Happy almost Friday

We're coming soon! Officially scheduled to start the week of January 19th through February 23rd

Could you please share the attached volleyball flyer with your families so they can begin registering?

Our goal for this season is not just to teach volleyball skills, but to provide a structured safe place where they can learn and build life skills, teamwork, and lifelong discipline right on campus.

We’re excited to get started!

[https://disciplinerift-dot-yamm-track.appspot.com/2Nwuj3atzr…]

Luis Torres
Founder
Discipline Rift

[phone] [https://disciplinerift-dot-yamm-track.appspot.com/2DcxWzAFu3…]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift-dot-yamm-track.appspot.com/2t6lfXtx7K…]

713 W Yale St, Orlando, FL 32804
```


### M31. 2026-01-08 — Spring Pickleball Season 🥒  Dates & Flyer
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19b9f45c7d1b5a4b

```text
Hi Ms. Lott, Happy New Year!

I hope you had a wonderful break :)

We are getting ready to kick off our Spring Pickleball season on campus! We are scheduled to run for 6 weeks on Thursdays
Here are the specific dates for this 6-week session:
January 22

January 29

February 5

February 12

February 19

February 26

Could you please share the attached flyer with your families so they can register?

We’re excited to get the students back out on the courts (or rather, the car loop!) to build on the skills they learned last year.
Take care,

[https://www.instagram.com/disciplinerift]

Luis Torres
Founder
Discipline Rift

[phone] [tel:(407)+614-7454]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.com/]

713 W Yale St, Orlando, FL 32804
```


### M32. 2025-12-22 — Registration
- Sender: info@disciplinerift.com
- Gmail id: 19b47a142ba8abea

```text
Thank you for reaching out regarding registration.

You can register for our upcoming seasons and programs using the following link: https://disciplinerift.com/register

If you have any questions about specific teams, schedules, or need help with the registration process, please let me know which team or sport you are interested in and I’ll be happy to provide more details.

Best regards, 
Luis Torres 
Founder, Discipline Rift 
📧 info@disciplinerift.com 
📞 (407) -614-7454
```


### M33. 2026-02-15 — No school tomorrow! Important information
- Sender: Discipline Rift <luis@disciplinerift.com>
- Gmail id: 19c632eae78ff9bf — List-Unsubscribe header present

```text
Here's what you need to know

Discipline Rift

Parent!, no class tomorrow — Presidents’ Day

Since kids are out, it’s the perfect time to lock in the last season of the year (right after school, on campus).

REGISTER HERE [https://email.admin.disciplinerift.com/c/eJx0U8tyqzgU_BqxSwo…]

[#1] [#2]

Quick heads-up:

There’s no class tomorrow because of Presidents’ Day.
This is the moment to get your child locked in for the last season of the year.

This time I’m writing to you as the founder of Discipline Rift.
This whole year being in schools and seeing housands of students
I’ve learned that kids fear being judged,
they walk in unsure, worried they’ll mess up.

THAT’S WHAT WE FIX WITH SPORTS

Coaches teach the basics first, then increase difficulty through short, guided play! So kids build confidence fast.

Here’s what you’ll notice:

They miss, laugh, reset, and try again.. because it feels safe to keep going.

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://email.admin.disciplinerift.com/c/eJx0U8tyqzgU_BqxSwo…]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://email.admin.disciplinerift.com/c/eJx0U8tyqzgU_BqxSwo…]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0k0lz4joUhX-NvEv…]
```


### M34. 2026-02-20 — After school time can be wasted... we fix that
- Sender: Discipline Rift <luis@disciplinerift.com>
- Gmail id: 19c7d5688b608682 — List-Unsubscribe header present

```text
LAST season of the year is here

Discipline Rift

Coach Luis here!

After school can go either way.
Time can be wasted… or it can be used for something better.

Backpacks drop. Energy is still there.
They just need somewhere to put it.

Spring registration is here, kids stay on campus and step straight into movement: small groups, supportive coaches, and games that ease learning.

REGISTER HERE [https://email.admin.disciplinerift.com/c/eJx0U01zozgU_DVwSwo…]

No pressure.
No “you should already know this.”

Just a place where trying, missing, and trying again is normal.

And something shifts quickly.

You’ll hear laughter instead of frustration.
You’ll notice them asking when the next practice is.

That’s what we care about most.

Spring is the last time to start.

Register before teams get full for Spring

We’d love to have your family join us.

Coach Luis -
Founder, Discipline Rift

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://email.admin.disciplinerift.com/c/eJx0U01zozgU_DVwSwo…]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://email.admin.disciplinerift.com/c/eJx0U01zozgU_DVwSwo…]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0k09v6jgUxT-Ns2s…]
```


### M35. 2026-03-03 — 6255 New Independence Pkwy, Winter Garden, FL 34787 Season Ended Last Week – New Registration Now Open
- Sender: info@disciplinerift.com
- Gmail id: 19cb44b29cc97d5f

```text
Hello, Leslie

Here's some information about Linda's participation in VOLLEYBALL INDEPENDENCE.

Hi [parent],
Our previous Volleyball season officially ended last week, so there is no practice today.
Registration for the upcoming season is now open, beginning the week of March 24
Spots in the team are limited and filled on a registration priority.
Secure your child’s spot here:
👉 https://disciplinerift.com/register
If you have any questions, simply reply to this email.
Best,
Coach Luis
Founder, Discipline Rift
info@disciplinerift.com
[phone]

Coach
Ranya Mahmouki

Location
6255 New Independence Pkwy, Winter Garden, FL 34787

School
Independence Elementary School
```


### M36. 2026-03-16 — Stressed from Spring break? Time to take action
- Sender: Discipline Rift <luis@disciplinerift.com>
- Gmail id: 19cf8e27e565aee7 — List-Unsubscribe header present

```text
Last season of the year.. limited spots per team

Discipline Rift

Hi! Coach Luis here

As spring break begins, our last sports season of the year is just one week away.

THE real win is not just helping kids get better. It is helping them want to come back.

Because if kids do not want to return, progress never even starts.

REGISTER HERE [https://email.admin.disciplinerift.com/c/eJx0U013syoY_DW4a4-…]

Discipline Rift

That is why our program is built around fun-first, beginner-friendly sessions that happen right after school, on campus.

We teach the sport step by step, at a pace kids can enjoy, so they leave smiling and excited to do it again.

One after-school practice per week

No club lifestyle

No weekends taken over

Spring season is coming up quickly, and spots are limited per team.

REGISTER HERE [https://email.admin.disciplinerift.com/c/eJx0U013syoY_DW4a4-…]

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://email.admin.disciplinerift.com/c/eJx0U013syoY_DW4a4-…]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://email.admin.disciplinerift.com/c/eJx0U013syoY_DW4a4-…]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0k81u6joUhZ_GmbV…]
```


### M37. 2026-03-17 — Thank You for Coming Today
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19cfd88a3eb59695

```text
{{Name}}, It was awesome to have you go through this piloting process of our franchise modelHope that we were also able to add value to you from the experience
We’ll be reviewing your insights along with the emails and feedback we received from you. Your input is valuable as we continue refining this model and improving the journey to license.
Like I said earlier, I encourage you to write a LinkedIn post so others can learn from your experience and what stood out to you throughout the day. If you do, make sure to tag us.
Discipline Rift
Instagram: https://www.instagram.com/disciplinerift/ [https://www.instagram.com/disciplinerift/]
Facebook: https://www.facebook.com/disciplinerift/ [https://www.facebook.com/disciplinerift/]
LinkedIn: https://www.linkedin.com/company/disciplinerift/ [https://www.linkedin.com/company/dr-sports-athletics/]
TikTok: https://www.tiktok.com/@disciplinerift [https://www.tiktok.com/@disciplinerift]
Also, I wanted to share a gift with you. This link includes Alex Hormozi’s books and resources:
https://drive.google.com/drive/folders/1hgzcckGo8XNF8mfdczy3PWTeyKoDQyyo?… [https://drive.google.com/drive/folders/1hgzcckGo8XNF8mfdczy3…]
Please use this wisely and do not share it. Please treat it appropriately.
Also, feel free to stay in contact with me directly. My number is [phone]. You can text me or reply here anytime.
We may have some internship opportunities opening for the summer, so if that’s something you’d be interested in, feel free to text me or reply to this email and let me know.
Thank you again for being part of it.

[https://www.instagram.com/disciplinerift]

Luis Torres
Founder
Discipline Rift

[phone] [tel:(407)+614-7454]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.com/]

713 W Yale St, Orlando, FL 32804
```


### M38. 2026-03-19 — It's time. Last Season of the year
- Sender: Discipline Rift <luis@disciplinerift.com>
- Gmail id: 19d07efac951c07f — List-Unsubscribe header present

```text
Is your child not focusing? Season starts next week

Erika, it's time.
Time to focus, time for the last sports season of the year.

Is your child not focusing? It might not be what you think.

Many kids struggle with attention, but maybe it's not always about their ability to focus.

We just need a method that adapts to their energy levels. Our practice method is high-energy, engaging, and dynamic.

We use interactive drills to keep them involved. When they are engaged, they can do it.

AND this spring is the our last season of the year

REGISTER HERE [https://email.admin.disciplinerift.com/c/eJx0U8tS8zgXfBp5B6W…]

We teach the sport step by step, at a pace kids can enjoy, so they leave excited to do it again.

One after-school practice per week

No club lifestyle

No weekends taken over

SPRING SEASON STARTS NEXT WEEK

REGISTER HERE [https://email.admin.disciplinerift.com/c/eJx0U8tS8zgXfBp5B6W…]

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://email.admin.disciplinerift.com/c/eJx0U8tS8zgXfBp5B6W…]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://email.admin.disciplinerift.com/c/eJx0U8tS8zgXfBp5B6W…]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0k1FzujgUxT9NeGs…]
```


### M39. 2026-03-22 — Ready for tomorrow?
- Sender: Discipline Rift <luis@disciplinerift.com>
- Gmail id: 19d17a804a06e9b2 — List-Unsubscribe header present

```text
Season is starting tomorrow! Sports ARE here

Erika, ready for tomorrow?

Season starts tomorrow.

Spring season is here. Last season of the year.

Sports are not just about learning the game. They teach kids how to handle tough moments, value the small details, and keep growing without needing perfection.

They also learn to be part of something bigger than themselves, contribute to a team, and help others reach the goal together.

That is why this season matters.

REGISTER HERE [https://email.admin.disciplinerift.com/c/eJx0U01z8ioY_TVk1w4…]

We teach the sport step by step, at a pace kids can enjoy, so they leave excited to do it again.

One after-school practice per week

No club lifestyle

No weekends taken over

SPRING SEASON STARTS NEXT WEEK

REGISTER HERE [https://email.admin.disciplinerift.com/c/eJx0U01z8ioY_TVk1w4…]

Right after school, on campus.

Small groups. Trained coaches.

Register now so you don’t miss the last season of the year.

REGISTER NOW [https://email.admin.disciplinerift.com/c/eJx0U01z8ioY_TVk1w4…]

If the button doesn’t work, copy/paste this link:

https://www.disciplinerift.com/register [https://email.admin.disciplinerift.com/c/eJx0U01z8ioY_TVk1w4…]

Discipline Rift • K–5 • On-campus, right after school

713 W Yale St, Orlando, FL 32804 • [phone] • info@disciplinerift.com

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0k9tzqjoYxf-a8NY…]
```


### M40. 2026-03-26 — THANK YOU from UCF Knight Shadow & Summer 2026 info!
- Sender: [parent — original DR blast quoted in their reply]
- Gmail id: 19d2b371163f36d1

```text
Discipline RIft Team,

Thank you so much for hosting UCF students during the Spring Break 2026 Knight Shadow experience. The thank-you notes have been pouring in, and one thing is certain, your organization made this a valuable and impactful experience for our
students.

We truly appreciate the time and care you took to engage with the students in meaningful ways that opened their eyes to new and different possibilities within their majors. Your commitment to mentorship makes a lasting difference!

We are excited to share that the SUMMER 2026 Knight Shadow sessions are scheduled for
Tuesday, Aug. 4 & Wednesday, Aug. 5.

If you are interested in hosting students again for the summer session, registration is now open. You can access the registration at this link:
SUMMER 2026 EMPLOYER REGISTRATION [https://ucf.qualtrics.com/jfe/form/SV_3t6yBSHmpec1c0K]

Important dates to note:

·
Employer registration closes: May 22.

·
Student matches released: July 8th

·
Logistics email to students due by: July 13th

If you are interested in participating in an Employer Virtual Information session, they will be held on Zoom on these dates:

April 8 from 12:00-1:00 ET

May 6 from 12:00-1:00 ET

May 15 from 12:00-1:00 ET

Employer Info Session zoom link: https://ucf.zoom.us/j/2292969594 [https://ucf.zoom.us/j/2292969594].

Thank you for making my first Knight Shadow experience as the Program Manager so wonderful. Your participation and engagement are what make this program such a valuable opportunity for UCF students.

Go Knights! Charge On!!

Marika Koch, Assistant
Director

Knight Shadow Program Manager & Service-Learning Lead

Experiential Learning | Division
of Student Success and Well-Being

UNIVERSITY OF CENTRAL FLORIDA

[phone] | academicsuccess.ucf.edu/explearning [https://academicsuccess.ucf.edu/explearning/]

[https://ucf.joinhandshake.com/login] [https://twitter.com/ucf_el?…]
[https://www.facebook.com/ucfel/]
[https://www.instagram.com/ucf_el/]

4123 Pictor Ln, Orlando, FL 32816

Kenneth G. Dixon Career Development Center

Orlando, FL 32816

Please note: Florida
has a very broad open records law (F.S. 119). Emails may be subject to public disclosure.
```


### M41. 2026-05-04 — Season Update? Prep for Fall
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19df348670af8b63

```text
Hi Ms. Taylor! Happy Monday,I wanted to let you know that our spring season has officially ended! We will no longer have practices for the 2025-2026 school year..
We appreciate your support throughout the season and for allowing us to serve your students on campus and make sports available to families contributing to the 63x30 initiative [https://disciplinerift.yatrack2.com/2Pbq2ogTyHxsowLGVWJhrMPE…]
A few quick updates and requests for the fall:
Facility Reservations
Facility reservations have already been sent for the fall season.
Fall Season Start Date
We are currently scheduled to start the week of August 31st.
Meet the Teacher Event
We’re looking forward to joining you for the Meet the Teacher event. Once you have the information, please send it our way so we can plan accordingly.
Support From Our Side
We would love to participate, connect with families, and continue adding value to your school. Please let us know if you need help with anything from our side.
Thank you again! We wish you a wonderful summer

[https://disciplinerift.yatrack2.com/2g2fPBu3vpyIE29H1fVcwen7…]

Luis Torres
Founder
Discipline Rift

[phone] [https://disciplinerift.yatrack2.com/2uMmFiY3n06FzTKVPnjJhmyW…]

info@disciplinerift.com [mailto:info@disciplinerift.com]

disciplinerift.com [https://disciplinerift.yatrack2.com/2OXOHZL0qTPmqK7TvQ6q9Gt2…]

713 W Yale St, Orlando, FL 32804
```


### M42. 2026-07-28 — Preparing you for the DR Fall Season
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19fa9c4959afeccb

```text
Coach Kessa Lazar,Welcome to the Discipline Rift Fall season!
We’re excited to have you on the team and look forward to seeing you on the court this Fall.
Please review and save the following important dates:
1. August 5: Flyers and Supplies Pickup
Time: 5:00 PM to 9:00 PM
Location: Discipline Rift Offices
3847 E Colonial Dr
Orlando, FL 32803
Please stop by during this time to pick up the flyers and supplies needed for your Meet the Families event.
If you cannot make it on August 5, reply with your availability as soon as possible so we can arrange to meet with you directly before August 6.
2. August 6: Meet the Families Events
Event window: Approximately 8:00 AM to 6:00 PM
Coaches will be assigned either an AM or PM time slot at one of our partner schools.
Your assigned location, arrival time, and event details will be shared this weekend. Please keep your schedule open until your assignment is confirmed.
3. August 29: Annual DR Training Day
Training time: 8:00 AM to 12:00 PM
Arrival time: 7:45 AM
Location: Discipline Rift Offices
3847 E Colonial Dr
Orlando, FL 32803
This is the same location as the August 5 supplies pickup.
Our annual Training Day is designed to develop our coaching skills, strengthen the DR method, align expectations, and prepare everyone for the upcoming seasons.
Save the date: Add DR Training Day to your calendar [https://disciplinerift.yatrack2.com/24pcFJilA7Ppy_N6MH5-UPOl…]
Dress code: Business casual
Please bring:
A notebook

Pen or pencil

Attendance at all events is encouraged to fulfill our responsibility to actually teach as coaches.

Please reply to confirm that you received this email and that we can count on you for both required dates. Include any scheduling conflicts in your response.
Looking forward to seeing you on the court!
Discipline Rift
```


### M43. 2026-08-09 — Back to school this Tuesday, are you ready?
- Sender: Discipline Rift <coachluis@disciplinerift.com>
- Gmail id: 19fe8c49fd42bc24 — List-Unsubscribe header present

```text
The supplies are ready, but what is your child doing after school?

Discipline Rift

Hi [parent],

The supply list is done. Shoes, backpack, folders, the new bedtime.

But what else isn't on the list? Maybe sports and physical activity?

Yes, sports are as important as everything else: 80% of brain cells focus on movement.

Volleyball • Tennis • Pickleball • Flag Football

REGISTER [https://email.admin.disciplinerift.com/c/eJx0VMty6jgU_Bp5M5W…]

POINTS FOR OUR PARENTS TO BE MINDFUL OF

What matters this school year

1. How their body moves through space.

The coordination between what they see, where they are, and what they do with it. We're seeing larger groups of players behind in motor coordination.

2. What they do the first time something is hard.

At this age, the first conclusion is almost always, "I can't do this." What they learn to do next is the part that follows them into the classroom and everywhere else.

3. Every practice runs on a method, not a mood.

We teach the skill until a child who has never touched a ball understands it. We drill it in a format they will actually stay engaged in. Then, we play a real game using it.

If a program has no method, your child's development comes down to luck. It depends on whether they happen to get a coach who is good at explaining things.

4. Easy for you. We will do what is necessary.

No transportation is needed. Everything is handled by our coaches from the moment of dismissal, on campus, right after school.

5. If you ask, "How was practice?" and just hear, "Fine."

You will receive one update after every practice from the coach with information that matters (not just a bunch of nonsense) through the parent dashboard, where you can see your child's progress and photos from the court.

BUILT FOR THE SCHOOL WEEK

Easy for you. Intentional for them.

✓
Six weeks of coached practice

✓
On your child's campus, immediately after dismissal

✓
No transportation needed

✓
Beginner-friendly to advanced

Our value is teaching the skills and a passion for the sport.

VALUE GUARANTEE

If we do not deliver it, you receive a 100% refund at any time during the season.

REGISTER [https://email.admin.disciplinerift.com/c/eJx0VMty6jgU_Bp5M5W…]

Low cost — everything included.

Wishing your child a valuable, enriched school year.

Coach Luis

Founder, Discipline Rift

Running at 55 schools across Central Florida

DISCIPLINE RIFT

Value Guarantee · Running at 55 schools in Central Florida

713 W Yale St, Orlando, FL 32804 · [phone] [tel: 14076147454]

info@disciplinerift.com [mailto:info@disciplinerift.com] ·
disciplinerift.com [https://email.admin.disciplinerift.com/c/eJx0VMty6jgU_Bp5M5W…]

Privacy · Terms · © 2026 Discipline Rift (Torres Rivero LLC)

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0VEuTsjwT_TVhN1O…]
```


### M44. 2026-08-16 — First week is done. Is your child ready?
- Sender: Discipline Rift <coachluis@disciplinerift.com>
- Gmail id: 1a00b1e5ad53d802 — List-Unsubscribe header present

```text
Sports after school happen right at their school

Discipline Rift

Registration is open for after-school sports at your child's school.

Volleyball • Tennis • Pickleball • Flag Football

Hi [parent],

The first week of school is done.

Your child's time after school should be intentional.

REGISTER [https://email.admin.disciplinerift.com/c/eJx0VMlyszgYfBpxmUo…]

They need a place to begin and develop.

One of our parents told me that her daughter, Valeria, had never been very athletic.

She signed her up for after-school volleyball anyway.

Valeria started as a complete beginner.

She practiced once a week.

Right at her own school.

I know another activity can sound like another drive, another schedule, and another problem for a parent to solve.

That was not the case for her mom.

She did not have to pick Valeria up and drive her somewhere else. Our coaches came directly to the school.

Over time, she developed skills.

Not because she was already athletic.

Because she started.

Her mom could also reach the coach directly through the parent dashboard whenever she needed something. No going through admin staff.

Six weeks. Once a week. $129.

Click below, search for your child's school, and register.

REGISTER [https://email.admin.disciplinerift.com/c/eJx0VMlyszgYfBpxmUo…]

START HERE

Give them a place to begin.

✓
A six-week season for $129

✓
Practice once a week, right after class

✓
No transportation needed

✓
Direct coach messaging through the parent dashboard

Search for your child's school and complete registration.

A place to begin. A place to develop.

Coach Luis

Founder, Discipline Rift

Running at 55 schools across Central Florida

DISCIPLINE RIFT

Value Guarantee · Running at 55 schools in Central Florida

713 W Yale St, Orlando, FL 32804 · [phone] [tel: 14076147454]

info@disciplinerift.com [mailto:info@disciplinerift.com] ·
disciplinerift.com [https://email.admin.disciplinerift.com/c/eJx0VMlyszgYfBpxmUo…]

Privacy · Terms · © 2026 Discipline Rift (Torres Rivero LLC)

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0VE2TsjoT_TVhN1O…]
```


### M45. 2026-09-05 — Long weekend! Volleyball starts this week
- Sender: Discipline Rift <coachluis@disciplinerift.com>
- Gmail id: 1a073560a56796bc — List-Unsubscribe header present

```text
Monday is Labor Day. Then the volleyball team starts at your school.

The long weekend ends Monday.

Volleyball starts this week.

A volleyball team at your child's elementary school.

Elementary • K through 5th • Beginner-friendly to advanced • No transportation needed

REGISTER [https://email.admin.disciplinerift.com/c/eJx0k013ujgYxT8NbOb…]

Hi [parent],

This is a long weekend. Enjoy it.

Then the school week gets real, and the hours between dismissal and dinner with your family start filling up.

Your child's time after school should be intentional.

Your child does not need to already be athletic.

They need a team to begin and develop on.

Take advantage of the first week. Search for your child's school and claim their spot.

Three things about the volleyball team

On campus.

No transportation needed.

Volleyball practice happens right on your child's school campus, immediately after dismissal.

A method, not a mood.

We actually teach.

Our coaches train and prepare to teach the skills the right way, so every child has a real place to begin and develop.

You can ask.

If "How was volleyball?" only gets you "Fine," you still have a real answer.

In the parent dashboard, you can see progress and team photos, receive updates, and message the coach directly.

THIS VOLLEYBALL SEASON

Six weeks on a volleyball team.

One practice a week, right after school.

✓
Volleyball on your child's campus

✓
Beginner-friendly to advanced

✓
Parent dashboard and coach updates

✓
No transportation needed

LOW COST. EVERYTHING INCLUDED.

100% refund, any time during the season.

If we don't deliver the value—real teaching and real progress—you receive a full refund.

REGISTER [https://email.admin.disciplinerift.com/c/eJx0k013ujgYxT8NbOb…]

Search for your child's school and claim the spot.

Running at 55 schools across Central Florida, teaching passion and discipline.

Wishing your child a valuable, enriched school year.

Coach Luis

Founder, Discipline Rift

Discipline Rift

Value Guarantee · Running at 55 schools in Central Florida

713 W Yale St, Orlando, FL 32804 · [phone] [tel: 14076147454]

info@disciplinerift.com [mailto:info@disciplinerift.com] ·
disciplinerift.com [https://email.admin.disciplinerift.com/c/eJx0k013ujgYxT8NbOb…]

Privacy · Terms · © 2026 Discipline Rift (Torres Rivero LLC)

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0VM2SsjobvBrYzRQ…]
```


### M46. 2026-09-07 — Happy Labor Day! Volleyball is here
- Sender: Discipline Rift <coachluis@disciplinerift.com>
- Gmail id: 1a07e498255cb584 — List-Unsubscribe header present

```text
Last day of the weekend, First day of the volleyball is this week!

Last day of the long weekend.

Time to get your child on the team.

Elementary • K through 5th • Beginner-friendly to advanced • No transportation needed

REGISTER [https://email.admin.disciplinerift.com/c/eJx0VE93ujgU_TRhM-f…]

Hi [parent],

Happy Labor Day! What is your family doing today? Today, you have the whole day.

Tomorrow they go back. What happens after school?

The screens are not a plan. A team is.

We have a place where your child can begin and develop.

Right at school.

Volleyball practice happens on campus. No transportation needed.

They get to learn, not just spend time.

Our coaches have been training and preparing to coach the right way.

You can ask.

On the parent dashboard, you can see progress and team photos, receive updates, and message the coach directly.

SEASON STARTS TOMORROW

Six weeks on a volleyball team.

One practice a week, right after school.

✓
Volleyball on your child's campus

✓
Beginner-friendly to advanced

✓
Parent dashboard and coach updates

✓
No transportation needed

LOW COST. EVERYTHING INCLUDED.

100% refund, any time during the season.

REGISTER [https://email.admin.disciplinerift.com/c/eJx0VE93ujgU_TRhM-f…]

Search for your child's school and claim the spot before tomorrow.

The largest sports program in schools across Central Florida, teaching passion and discipline.

Enjoy the rest of the holiday. See you on the court tomorrow.

Coach Luis

Founder, Discipline Rift

Discipline Rift

Value Guarantee · Running at 55 schools in Central Florida

713 W Yale St, Orlando, FL 32804 · [phone] [tel: 14076147454]

info@disciplinerift.com [mailto:info@disciplinerift.com] ·
disciplinerift.com [https://email.admin.disciplinerift.com/c/eJx0VE93ujgU_TRhM-f…]

Privacy · Terms · © 2026 Discipline Rift (Torres Rivero LLC)

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0VEuTsjob_DVhN1O…]
```


### M47. 2026-09-08 — Volleyball Starts Thursday!
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a0817fbceb86080

```text
Hello Ms. , Hope you're great!

Volleyball starts this Thursday. We will be proceeding with the season, however could you share our flyer one more time with your families as we want to bring awareness to the program.

We appreciate your partnership and look forward to an amazing season!
```


### M48. 2026-09-16 — [child] is all set for Volleyball at Hamlin Elementary School - Fall 2026 schedule
- Sender: <info@disciplinerift.com>
- Gmail id: 1a0ab3daad5a33f1

```text
DISCIPLINE RIFT

You're in for Fall!

[child] has been moved to the Fall 2026 season.

Hi [parent], as requested, your registration for VOLLEYBALL HAMLIN at Hamlin Elementary School now applies to the current Fall 2026 season. Your payment stays the same — nothing else to do on your end. Here is the schedule.

Team Information

Student
[child]

Team
VOLLEYBALL HAMLIN · Fall 2026

Coach
Ilaria Vouriotis

School
Hamlin Elementary School

Location
16145 Silver Grv Blvd, Winter Garden, FL 34787

Meeting Spot
Cafeteria at 1:45 PM

Pickup
3:15 PM at the Cafeteria

Practice Schedule

Wednesday, September 16, 2026

2:15 PM – 3:15 PM

Hamlin Elementary School

Wednesday, September 23, 2026

2:15 PM – 3:15 PM

Hamlin Elementary School

Wednesday, September 30, 2026

2:15 PM – 3:15 PM

Hamlin Elementary School

Wednesday, October 7, 2026

2:15 PM – 3:15 PM

Hamlin Elementary School

Wednesday, October 14, 2026

2:15 PM – 3:15 PM · Last practice of the season

Hamlin Elementary School

Coach: Ilaria Vouriotis · Location: 16145 Silver Grv Blvd, Winter Garden, FL 34787

Schedule shown in Miami timezone (EST/EDT)

Before the first practice

• What to bring: comfortable athletic clothes, sneakers, and a water bottle. We provide all the gear — nets, balls, and drill equipment.

• Let the school know: please tell the front office that [child] is staying after school on Wednesdays for Discipline Rift Volleyball.

• Pickup: 3:15 PM at the Cafeteria, same spot where the team meets.

Questions? Simply reply to this email — we read every message.
See you on the court!

DISCIPLINE RIFT

Discipline Rift · Torres Rivero LLC

713 W. Yale Street, Orlando, FL 32804

info@disciplinerift.com · [phone] · www.disciplinerift.com

You're receiving this because [child] is registered for a Discipline Rift program at Hamlin Elementary School.
```


### M49. 2026-09-21 — You're all set — [child]'s Fall 2026 Volleyball team is confirmed
- Sender: <info@disciplinerift.com>
- Gmail id: 1a0c571d3ac7a173

```text
96

DISCIPLINE RIFT

You're all set for Fall 2026!

[child]'s team has been updated

Hi there,

Good news — [child] is now enrolled in the Fall 2026 Volleyball season at Tildenville Elementary. No action is needed on your end; [child]'s spot is confirmed and payment is already on file.

Student[child]

TeamVolleyball – Tildenville

SeasonFall 2026

SchoolTildenville Elementary School

LocationCafeteria

CoachValeria Chirico

Remaining practices

Monday, Sep 283:15 – 4:15 PM

Monday, Oct 53:15 – 4:15 PM

Monday, Oct 193:15 – 4:15 PM

Note: Oct 12 has no practice (season break).

What to bring: comfortable athletic clothes, closed-toe sneakers, and a water bottle. Practice takes place at the school's cafeteria — please have [child] ready for pickup right after 4:15 PM.

Questions? Just reply to this email and we'll help right away.

See you on the court!

The Discipline Rift Team

DISCIPLINE RIFT

Discipline Rift, LLC · Orlando, FL

You're receiving this because [child] is enrolled in a Discipline Rift season.
```


### M50. 2026-10-04 — Next sports season is here. [child] isn't registered yet
- Sender: Discipline Rift <coachluis@disciplinerift.com>
- Gmail id: 1a108643d08fa033 — List-Unsubscribe header present

```text
Hi [parent],

isn't on the team for next season yet.

The second quarter is almost here, and the next season starts with it.

Search for your child's school and register → [https://email.admin.disciplinerift.com/c/eJx0k01zsjoUxz8N7Nq…]

Teams are now open for volleyball, tennis, pickleball, soccer, and flag football.

The weather is cooling down. This is the perfect time to practice.

On their own campus. No transportation needed.

Real coaching. Our coaches have been training and preparing to teach the skills the right way. Beginner friendly to advanced.

You can ask. See progress and team photos on the parent dashboard, and message the coach directly.

Low cost. Everything included. If we do not deliver real teaching and real progress, you receive a 100% refund at any time during the season.

The hours between the bell and dinner will get filled by something. Give a team, a coach, and a skill to build.

Search for your child's school and register → [https://email.admin.disciplinerift.com/c/eJx0k01zsjoUxz8N7Nq…]

Coach Luis

Founder, Discipline Rift

P.S. We care about giving a place to begin and develop. We hope to see you next season.

Discipline Rift · 713 W Yale St, Orlando, FL 32804

You are receiving this because you requested information from Discipline Rift or registered with us previously.

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0VMmSszwSfBq4dQd…]
```


### M51. 2026-10-11 — Good things come to an end! isn't registered for next season
- Sender: Discipline Rift <coachluis@disciplinerift.com>
- Gmail id: 1a12d2ec4612e769 — List-Unsubscribe header present

```text
The current season is almost over. Their progress does not have to stop with it.

Hi [parent],

is a place to grow.

You have heard that from other sports programs.

But I mean that we actually teach and players grow. Here is how.

Our coaches do not simply keep players busy.

REGISTER FOR NEXT SEASON → [https://email.admin.disciplinerift.com/c/eJx0k01zgjoYhX8N7Np…]

We use chunking to teach skills and instructions.

We explain them. We demonstrate them. Players practice them.

Then they use them while playing .

This gives something real to remember.

They can compare how they played at the beginning of the season with how they play now.

They can feel the difference.

They may still make mistakes.

They may still lose points or games.

But underneath that, they know:

I could not do this before.
Now I can.

That is confidence built from evidence.

Instead of feeling like they are failing, they have proof that they are improving.

But one season is not enough.

Progress needs repetition.

Skills need continued coaching.

Relationships with teammates and coaches need time.

Next season continues what has already started.

The skills. The relationships. The discipline. The belief that they can improve when they keep working.

is not registered for next season yet.

That progress is possible because you, Erika, made the decision to give a place to begin.

Now give them a place to continue.

Six weeks. One practice each week.

Right after school. On campus.

No transportation needed.

Low cost. Everything included.

100% refund at any time during the season.

REGISTER FOR NEXT SEASON → [https://email.admin.disciplinerift.com/c/eJx0k01zgjoYhX8N7Np…]

Search for your child's school and secure their place on the next team.

Coach Luis

Founder, Discipline Rift

P.S. We are coaches who actually teach.

Discipline Rift · 713 W Yale St, Orlando, FL 32804

You are receiving this because you requested information from Discipline Rift or registered with us previously.

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0VM2SsrwavBrYzRQ…]
```


### M52. 2026-10-18 — season is coming to an end.
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a151442255da97d — List-Unsubscribe header present

```text
The next season starts in one week. Keep building on what they started.

Hi [parent],

Sports matter more than we sometimes realize.

REGISTER FOR THE NEXT SEASON → [https://email.ops.disciplinerift.com/c/eJx0k013qjoYhX8NzE4Xv…]

Why?

Because of the hours they fill.

Once the school bell rings, those hours can be spent in front of a screen.

Or they can be spent with a coach, a team, and a skill to develop.

For the past several weeks, has spent that time learning .

Practicing skills. Making mistakes. Listening to a coach. Trying again.

Now, the season is coming to an end.

But the development should not end with it.

One season introduces the skills. Continuing gives the repetition and coaching needed to keep developing them.

The next season starts in one week.

REGISTER FOR THE NEXT SEASON → [https://email.ops.disciplinerift.com/c/eJx0k013qjoYhX8NzE4Xv…]

Next season does not repeat this one. Players build on the skills they started and learn how to connect them during play.

Same team environment. Same campus. More time for the coach to teach and for to improve.

No transportation needed. Our coaches handle everything on campus from dismissal until practice ends.

If we do not deliver real teaching and real progress, you receive a 100% refund at any time during the season.

CONTINUE WITH → [https://email.ops.disciplinerift.com/c/eJx0k013qjoYhX8NzE4Xv…]

Coach Luis

Founder, Discipline Rift

P.S. has already started. Now, give them the opportunity to keep developing.

Discipline Rift · 713 W Yale St, Orlando, FL 32804

You are receiving this because you requested information from Discipline Rift or registered with us previously.

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://email.ops.disciplinerift.com/c/eJx0VE2TsjwW_TVh112QA…]
```


### M53. 2026-10-23 — Here you go! 3-minute Parent Guide
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a16acc454384e27

```text
DISCIPLINE RIFT

Here you go! Your 3-minute Parent Guide

From Coach Luis at Discipline Rift

Hi [parent],

What if this was the season your child did not just participate…
But discovered something about themselves?

The first time they understand a new skill.
The first time they try again after struggling.
The first time they feel like they belong in a group.

Many children stop participating in organized activities before middle school… Not because they lack ability, but because they did not feel supported or capable early on.

Here are five simple ways you can strengthen your child’s experience starting this week.

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

REGISTER FOR THE SEASON [https://www.disciplinerift.com/register]

FIND YOUR SCHOOL [https://www.disciplinerift.com/register]

What if this season everything shifts?

DISCIPLINE RIFT

Discipline Rift · Torres Rivero LLC

713 W. Yale Street, Orlando, FL 32804

info@disciplinerift.com · [phone] · www.disciplinerift.com

This email was sent because you signed up for the Discipline Rift Parent Guide.
```


### M54. 2026-10-23 — One week until VOLLEYBALL INNOVATION starts
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a16a23f11c4b760

```text
DISCIPLINE RIFT

One week to go.

VOLLEYBALL INNOVATION is about to start.

Coach Daylen Moss will be leading the season.

Hi [parent],

There are seven days left until the start of VOLLEYBALL INNOVATION. Make sure to remind your child about the practices. Here is the complete schedule.

Practice Schedule

Fri, Oct 30, 2026
3:15 PM – 4:15 PM
Practice 1
Fri, Nov 6, 2026
3:15 PM – 4:15 PM
Practice 2
Fri, Nov 13, 2026
3:15 PM – 4:15 PM
Practice 3
Fri, Nov 20, 2026
3:15 PM – 4:15 PM
Practice 4
Fri, Dec 4, 2026
3:15 PM – 4:15 PM
Practice 5
Fri, Dec 11, 2026
3:15 PM – 4:15 PM
Practice 6

Coach: Daylen Moss · Season: Winter 2026

Cancelled practices are already excluded. Times shown in Miami timezone (EST/EDT).

See your child on the court!

— The Discipline Rift Team

DISCIPLINE RIFT

Discipline Rift · Torres Rivero LLC

713 W. Yale Street, Orlando, FL 32804

info@disciplinerift.com · [phone] · www.disciplinerift.com

You are receiving this because your child is enrolled in a Discipline Rift season.
```


### M55. 2026-10-25 — Volleyball starts tomorrow
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a1746f26d561cfd

```text
DISCIPLINE RIFT

Tomorrow.

Maliah start Volleyball tomorrow.

VOLLEYBALL TILDENVILLE · Coach Luis Torres

Hi [parent],

There is one day left until the start of VOLLEYBALL TILDENVILLE. Make sure to remind your child about the practices. Here is the complete schedule.

Practice Schedule

Mon, Oct 26, 2026
3:15 PM – 4:15 PM
Practice 1
Mon, Nov 2, 2026
3:15 PM – 4:15 PM
Practice 2
Mon, Nov 9, 2026
3:15 PM – 4:15 PM
Practice 3
Mon, Nov 16, 2026
3:15 PM – 4:15 PM
Practice 4
Mon, Nov 30, 2026
3:15 PM – 4:15 PM
Practice 5
Mon, Dec 7, 2026
3:15 PM – 4:15 PM
Practice 6

Coach: Luis Torres · Season: Winter 2026

Cancelled practices are already excluded. Times shown in Miami timezone (EST/EDT).

Please send a water bottle, athletic shoes, and comfortable athletic clothes.

MESSAGE YOUR COACH [https://www.disciplinerift.com/parent/messages]

See your child on the court!

— The Discipline Rift Team

DISCIPLINE RIFT

Discipline Rift · Torres Rivero LLC

713 W. Yale Street, Orlando, FL 32804

info@disciplinerift.com · [phone] · www.disciplinerift.com

You are receiving this because your child is enrolled in a Discipline Rift season.
```


### M56. 2026-10-26 — practices begin this week at . There may still be room!
- Sender: Discipline Rift <coachluis@disciplinerift.com>
- Gmail id: 1a17592dd1cb1ffe — List-Unsubscribe header present

```text
New skills, new challenges, and purposeful progression for .

Hi [parent],

The new season starts this week at .

There is still room for to join the team and begin the season on time.

REGISTER → [https://email.admin.disciplinerift.com/c/eJx0k8tyqzgYhJ8Gdie…]

Skill progression starts with the first practice. Last season established the foundation. This season, our coaches add the next layer of skills and connect those skills during play.

Variability makes skills usable. We change the distance, target, movement, timing, pressure, and decisions within each activity. Players learn how to use the same skill in different situations instead of repeating the same drill.

Every practice will look different. will experience new challenges, games, and practice conditions compared with last season.

The activities change, but the teaching method remains consistent: we explain the skill, demonstrate it, let players practice it, and then apply it in play.

Starting this week matters. The first practice establishes the starting skill and prepares players for the next layer. Joining later means entering after the progression has already begun.

Easy for you. No transportation needed. Our coaches handle everything on campus from dismissal until practice ends.

You will see the progression. After every practice, the coach posts an update to your parent dashboard with the skill taught, the progress made, and what the team will work on next.

If we do not deliver real teaching and real progress, you receive a 100% refund at any time during the season.

REGISTER FOR → [https://email.admin.disciplinerift.com/c/eJx0k8tyqzgYhJ8Gdie…]

We look forward to helping continue developing this season.

Coach Luis

Founder, Discipline Rift

P.S. The progression begins this week. Register before the first practice.

Discipline Rift · 713 W Yale St, Orlando, FL 32804

You are receiving this because you requested information from Discipline Rift or registered with us previously.

Unsubscribe

If you no longer wish to receive these emails you may unsubscribe [https://email.admin.disciplinerift.com/c/eJx0VMtyszoTfBrYJQU…]
```


### M57. 2026-10-26 — Winter Flag Football at Pinecrest Avalon has spots open
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a179a1953436bc8

```text
Hi [parent],
You joined the waitlist for Flag Football at Pinecrest Avalon this fall. That team filled up. The Winter season at the same school has spots open.
Every Monday after school, 3:15–4:15 PM (team meets in the lobby at 2:45)
6 practices, October 26 – December 7 (no practice November 23)
All gear provided: flags, footballs, cones
$129 for the season
Spots are first come, first served, so register soon if Mondays work for you.
Register for Winter Flag Football [https://disciplinerift.com/register?…]
Questions? Just reply to this email.
The Discipline Rift Team
```


### M58. 2026-10-26 — Pinecrest Avalon Winter: Flag Football Mondays, Tennis Tuesdays
- Sender: <info@disciplinerift.com>
- Gmail id: 1a178ee4d6322897

```text
We listed the Winter days wrong. Flag Football is on Mondays, Tennis on Tuesdays — and there are still spots.

DISCIPLINE RIFT

Winter is on.

Flag Football Mondays · Tennis Tuesdays

Pinecrest Avalon Elementary School

Hi [parent],

Quick correction: we listed the Winter days wrong earlier. Here are the real days — and there are still spots open.

Flag Football

Every Monday, 3:15–4:15 PM

Started Oct 26 · 12 spots left

Tennis

Every Tuesday, 3:15–4:15 PM

Starts Oct 27 · 3 spots left

Team meets in the Lobby at 2:45 PM. All gear is provided.

Save a spot [https://disciplinerift.com/register?…]

Questions? Just reply here or call [phone].

See you at practice!

Coach Luis
Founder, Discipline Rift

DISCIPLINE RIFT

Discipline Rift · Torres Rivero LLC

713 W. Yale Street, Orlando, FL 32804

info@disciplinerift.com · [phone] · www.disciplinerift.com

You are receiving this because your child played FLAG FOOTBALL PINECREST AVALON with us in Fall 2026.
```


### M59. 2026-10-27 — Pinecrest Avalon Winter: Soccer starts Thursday
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a17de4522403070

```text
Kindergarten through 5th grade. Team meets in the Lobby at 2:45 PM, all gear provided.

DISCIPLINE RIFT

Winter is on.

Soccer starts this Thursday

Pinecrest Avalon Elementary School

Hi [parent],

Winter soccer at Pinecrest Avalon starts this Thursday, October 29. We’d love to have Magdalena and Nikolaos back, and there are still spots open.

Soccer

Every Thursday, 3:15–4:15 PM

Oct 29 – Dec 10 (no practice Nov 26) · Kindergarten–5th grade · 8 spots left

Team meets in the Lobby at 2:45 PM. All gear is provided.

Save a spot [https://disciplinerift.com/register?…]

Questions? Just reply here or call [phone].

See you at practice!

Coach Luis
Founder, Discipline Rift

DISCIPLINE RIFT

Discipline Rift · Torres Rivero LLC

713 W. Yale Street, Orlando, FL 32804

info@disciplinerift.com · [phone] · www.disciplinerift.com

You are receiving this because your child played soccer at Pinecrest Avalon with us in Fall 2026.
```


### M60. 2026-10-30 — [child] is not registered for volleyball yet
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a18dd8eeb132348

```text
[child] attended practice this week. Here is the Winter schedule and the link to register.
DISCIPLINE RIFT
Almost on the roster.
[child] is not registered for volleyball yet
Andover Elementary School
Hi [parent],
Your child [child] attended volleyball practice this week and has not been registered for the Winter season yet.
Whenever possible, please head to our website, disciplinerift.com [https://disciplinerift.com/register?…], and register [child] for the team, ideally before the next practice on Monday, Nov 2.
Winter Season Schedule
Mondays, 3:15–4:15 PM
Oct 26 – Dec 7 (no practice Nov 23, Thanksgiving week)
Practices: Oct 26, Nov 2, Nov 9, Nov 16, Nov 30, Dec 7

Register [child] [https://disciplinerift.com/register?…]
If you have any questions, please let us know. Just reply here or call [phone].
See you at practice!
Coach Luis
Founder, Discipline Rift

DISCIPLINE RIFT
Discipline Rift · Torres Rivero LLC
713 W. Yale Street, Orlando, FL 32804
info@disciplinerift.com · [phone] · www.disciplinerift.com
```


### M61. 2026-11-12 — Hope Prep Girls' 15U Volleyball | 2027 Season Dates
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 1a1d00ee6a7d147f

```text
Hi Ms. Daniels!

Hope you're great! I'm following up on our Developmental Girls' 15U Volleyball Team. Here are our proposed dates for 2027:

- Season 1: January 28 – March 4
- Season 2: March 25 – April 29 (Tentative)
- Practices: Thursdays after school from 3:15-4:15.
- Games: One game towards Week 6 of each season
- Tournaments: March 6th and April 31st

Could you confirm whether these dates work with your school calendar, particularly spring break.

Once confirmed, we can finalize the schedule and move forward with registration!

Regarding registrations, we can create a customized flyer with a dedicated QR code for families to register. 10% of proceeds will go back to the school as a donation in appreciation of facility use and our continued partnership.

Hope to hear from you soon!

Best,
Discipline Rift
```


### M62. 2026-07-19 — Summer Camp Schedule - July 20–24
- Sender: Discipline Rift <info@disciplinerift.com>
- Gmail id: 19f7b3185e8d92cd

```text
Hi coaches,I hope you’re doing well! This is a reminder of the schedule for Week 7 of our summer programming, taking place July 20–24.
Monday, July 20
St. Mary Magdalen Catholic School — Volleyball
Time: 10:00 AM
Head Coach: Yassine, Sebastian
142 E. Swoope Avenue
Winter Park, FL 32789
Orangewood Christian School — 1:00–4:00 PM
Tennis: Sebastian
Pickleball: Yassine
1221 Trinity Woods Lane
Maitland, FL 32751
Tuesday, July 21–Friday, July 24
Orangewood Christian School — 1:00–4:00 PM
Tennis: Sebastian or Yassine
Pickleball: Sebastian or Yassine
1221 Trinity Woods Lane
Maitland, FL 32751
Kessa will also be joining us at Orangewood throughout the week to shadow and assist you coaches.
Please let me know if you have any questions or scheduling concerns. Thank you again for your help, and we’re looking forward to a great week!
Take care,
Luis Torres
Founder
Discipline Rift
```


### M63. 2026-10-08 — You're in! [child]'s Fall 2026 practice schedule
- Sender: <info@disciplinerift.com>
- Gmail id: 1a11c20c162dbf4d

```text
[child] is on the roster. Here's what's left of the season.

DISCIPLINE RIFT

You're in!

[child] is on the Fall 2026 roster

Volleyball · Deerwood Elementary School

Hi [parent],

[child] is now on the current season's volleyball team with Arlo. Here's what's left of Fall 2026:

🏐 Remaining practices

Monday, October 12th · No practice

Monday, October 19th · 3:15–4:15 PM
Last practice of the season

Same time and spot on campus as Arlo. No transportation needed.

Questions? Just reply here or give us a call.

CALL [phone] [tel:+14076147454]

See you on the court!

Coach Luis
Founder, Discipline Rift

DISCIPLINE RIFT

Discipline Rift · Torres Rivero LLC

713 W. Yale Street, Orlando, FL 32804

info@disciplinerift.com · [phone] · www.disciplinerift.com

You are receiving this because your child is enrolled in VOLLEYBALL DEERWOOD at Deerwood Elementary School.
```

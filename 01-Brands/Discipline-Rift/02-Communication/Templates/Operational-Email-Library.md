---
brand: Discipline-Rift
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-8437 (Developer/DR/EMAILS) pages 8cqnrff-6557, 6577, 6617, 6637, 6597, 6657, 6677, 6697"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# DR Operational Email Library

## Parent
- [[01-Brands/Discipline-Rift/02-Communication/Communication-Home|DR Communication Home]]

## Related
- [[01-Brands/Discipline-Rift/02-Communication/Templates/Parent-Communication-Volleyball-Season|Parent Communication — Volleyball Season]]
- [[01-Brands/Discipline-Rift/02-Communication/Templates/School-Outreach-Email-Templates|School Outreach Email Templates]]
- [[01-Brands/Discipline-Rift/06-DNA/Conversion|DR Conversion]]

## Purpose

Canonical operational email templates used across the registration → reminder → attendance flow. These are **automation templates** (live in n8n / GHL workflows). Use this note as the source of truth before editing any live template.

## Template index

| # | Template | Trigger | Channel |
|---|---|---|---|
| 1 | OTP Email | Account verification | Transactional |
| 2 | Registration Confirmation | Payment processed | Transactional |
| 3 | 30-Day Reminder | 30 days pre-season | Reminder |
| 4 | 7-Day Reminder | 7 days pre-season | Reminder |
| 5 | 1-Day Reminder | 1 day pre-season | Reminder |
| 6 | Coach Session Reminder | Daily — session not logged | Coach ops |
| 7 | Parent Assistance (no-show) | Student missed practice | Attendance |
| 8 | Coach Application Confirmation | Coach applied | Recruiting |

## 1. OTP Email

> **DISCIPLINE RIFT**
> Encouraging students to find their discipline and sport
>
> **Welcome to Discipline Rift!**
> Thank you for joining the Discipline Rift community. We're excited to have you with us!
>
> **Verification Code:**
> `{{ .Token }}`
>
> Use this code to verify your account.
> This code will expire in 24 hours for security purposes.

## 2. Registration Confirmation

> **DISCIPLINE RIFT**
> ✅ Registration Successful!
>
> Your payment has been processed successfully.
>
> **PAYMENT CONFIRMATION**
> Amount: $`${AMOUNT}`
> Payment confirmed on: `${DATE}`
>
> **STUDENT INFORMATION**
> Full Name: `${STUDENT_FIRST_NAME} ${STUDENT_LAST_NAME}`
> Grade: `${GRADE}`
> Emergency Contact: `${EMERGENCY_CONTACT_NAME}`
> Emergency Phone: `${EMERGENCY_PHONE}`
>
> **TEAM INFORMATION**
> Team Name: `${TEAM_NAME}`
> School: `${SCHOOL_NAME}`
> Location: `${SCHOOL_LOCATION}`
> Price: `${TEAM_PRICE}`
> Description: `${TEAM_DESCRIPTION}`
>
> **PRACTICE SCHEDULE**
> `${PRACTICE_OCCURRENCES}`
> Coach: `${COACH_NAME}`
> Location: `${LOCATION}`
> Schedule shown in Miami timezone (EST/EDT)
>
> ---
> Discipline Rift
> Support: info@disciplinerift.com
> Phone: (407) 614-7454
> Web: www.disciplinerift.com

## 3. 30-Day Reminder

> Hi `{{ $json.firstname }}`,
>
> There are 30 days left until the start of `{{ $json.name }}`.
>
> Make sure to remind your child about the practices! Here's the complete schedule:
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> See your child on the court!
> — Discipline Rift Team
>
> Discipline Rift - Youth Sports Development
> Developing Young Athletes in Volleyball, Tennis, & Pickleball
> Contact: info@disciplinerift.com — (407) 614-7454

## 4. 7-Day Reminder

> Hi `{{ $json.firstname }}`,
>
> There are seven days left until the start of `{{ $json.name }}`.
>
> Make sure to remind your child about the practices! Here's the complete schedule:
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> See your child on the court!
> — Discipline Rift Team

## 5. 1-Day Reminder

> **Discipline Rift — 1-Day Reminder for `{{ $json.name }}`**
>
> Hi `{{ $json.firstname }}`,
>
> There is **one day** left until the start of **`{{ $json.name }}`**.
>
> Make sure to remind your child about the practices! Here's the complete schedule:
>
> **SCHEDULE**
> `{{ $json.scheduleHtml }}`
>
> See your child on the court!
> — Discipline Rift Team

## 6. Coach Session Reminder

> **Discipline Rift — Session Record Reminder**
>
> Hello `{{ $json.name }}`,
>
> We noticed that today's session has not been submitted in the Coach Dashboard.
>
> Please log in and complete the session information so we can keep attendance and session records up to date.
>
> Go to Coach Dashboard: https://dash-board-coaches-whpv.vercel.app/
>
> Thank you!
> Contact: info@disciplinerift.com — (407) 614-7454

## 7. Parent Assistance (Attendance Note)

> **Discipline Rift — Attendance Note**
>
> Hi `{{ $json.parentfn }}`,
>
> We missed `{{ $json.studentfn }}` at practice today for `{{ $json.team }}`.
>
> We know things come up — schedules change, rides run late, or something at school pops up. If there was any issue getting to practice today, just let us know so we can note it on our end.
>
> Our goal is to keep every player progressing and feeling part of the team, so thanks for helping us keep attendance up to date.
>
> You can reply to this email or reach us here if you need to update anything about today's session.
>
> See you at the next practice!
> Discipline Rift

## 8. Coach Application Confirmation

> Hi `[name]`,
>
> Thanks for applying to be a coach at Discipline Rift!
>
> Our mission is to help young players grow through humility, perseverance, and adaptability — and we're excited you want to be part of that journey.
>
> We'll review your application and reach out soon if it's a fit.
>
> Until then, learn more about our coaching culture through our social media channels.
>
> – The DR Team
> info@disciplinerift.com

## Operating rules

- **Voice anchor:** "humility, perseverance, adaptability" (per Coach Application).
- **Standard sign-off:** Discipline Rift — info@disciplinerift.com — (407) 614-7454.
- **Tone:** warm, operational, parent-friendly. Never marketing-pushy.
- **Template merge fields:** match GHL / n8n payload — confirm field names before changing.
- **Image attachments:** banner image attached to each (`https://t9017418223.p.clickup-attachments.com/...`). Keep brand banner consistent across all 8 templates.

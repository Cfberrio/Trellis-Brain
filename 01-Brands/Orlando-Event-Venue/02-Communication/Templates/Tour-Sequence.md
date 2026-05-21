---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-4977 (Developer/OEV/EMAILS WEBSITE) page 8cqnrff-11917 (TOURS)"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# OEV Tour Sequence

## Parent
- [[01-Brands/Orlando-Event-Venue/02-Communication/Communication-Home|OEV Communication Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Booking-Calendar-Sequence|Booking Calendar Sequence]]
- [[01-Brands/Orlando-Event-Venue/06-DNA/Conversion|OEV Conversion]] (Tour Handoff SOP)

## Sequence map

### Public-facing flow
| # | Step | Channel |
|---|---|---|
| 01 | Tour confirmed | Email only |
| 02 | Tour reminder (day of) | Email + SMS |
| 03 | 1-hour reminder | SMS only |
| 04 | Tour follow-up | Email only |

### Internal admin flow
| # | Step | Channel |
|---|---|---|
| 05 | 1-hour admin reminder | SMS only |

## 01. Tour Confirmed — Email Only

**Subject:** Tour Confirmed | Orlando Event Venue
**Preview:** Your venue tour is scheduled. Here's what to expect and how to access the space.

> Hi `{{first_name}}`,
>
> Your tour at **Orlando Event Venue** has been scheduled. We look forward to showing you the space.
>
> **Tour Details**
> Date: `{{tour_date}}`
> Time: `{{tour_time}}`
> Location: Orlando Event Venue
> Address: 3847 E Colonial Dr, Orlando, FL 32803
>
> During your tour, you'll get a full walkthrough of the venue and have the chance to ask questions about pricing, layout, availability, and booking. The tour typically takes about **15–20 minutes**.
>
> **Quick Reminders**
> - Maximum capacity: **90 guests**
> - Free parking available on-site
> - No alcohol or hard liquor allowed on premises
>
> **Arrival & Access**
> When you arrive at Colonial Town Center, look for the **GLOBAL sign with 3847 displayed**.
>
> If the venue is locked when you arrive, please use these access steps:
>
> **1. Locate the Entrance** — Door on left side of building.
> **2. Get the Key from the Lockbox** — Black lockbox with touchscreen keypad. Tap screen to wake, enter code: **03302026**. Open lockbox, retrieve magnetic key.
> **3. Unlock the Door** — Tap magnetic key on sensor (right side of door). Return key to lockbox immediately + close it.
> **4. Enter the Venue** — Once inside, wait in front area; our team will meet you shortly.
>
> Need to reschedule? Reply to this email or call **(407) 974-5979**.
>
> Looking forward to meeting you,
> Orlando Event Venue Team
> 3847 E Colonial Dr, Orlando, FL 32803
> orlandoeventvenue@gmail.com — (407) 974-5979

## 02. Tour Reminder (Day Of) — Email

**Subject:** Your Tour Is Today | Orlando Event Venue
**Preview:** A quick reminder for today's tour, including arrival and access instructions.

> Hi `{{first_name}}`,
>
> This is a friendly reminder that your tour at **Orlando Event Venue** is scheduled for today.
>
> **Tour Details**
> Time: `{{tour_time}}`
> Location: 3847 E Colonial Dr, Orlando, FL 32803
>
> **Arrival & Access**
> Look for the **GLOBAL sign with 3847 displayed** at Colonial Town Center.
>
> If locked: door on left → black lockbox keypad → code **03302026** → retrieve key → tap on sensor (right of door) → return key to lockbox → wait in front area.
>
> If you have any questions or need to reschedule, reply or contact orlandoeventvenue@gmail.com / (407) 974-5979.
>
> Orlando Event Venue Team

## 02. Tour Reminder (Day Of) — SMS

> Hi `{{first_name}}` — this is a reminder that your Orlando Event Venue tour is scheduled for today at `{{tour_time}}`.
> Please arrive at 3847 E Colonial Dr, Orlando, FL 32803 and look for the GLOBAL sign with 3847.
> If the venue is locked, use the lockbox code: **03302026**.
> Questions? Reply here or call 407-974-5979.

## 03. 1-Hour Reminder — SMS Only

> Hi `{{first_name}}` — your Orlando Event Venue tour starts in 1 hour.
> Please look for the GLOBAL sign with 3847 at 3847 E Colonial Dr. If needed, use the lockbox code: **03302026**.
> Reply here if you need help finding the entrance.

## 04. Tour Follow-Up — Email Only

**Subject:** Thank You for Touring Orlando Event Venue
**Preview:** Thanks for visiting. If you'd like to move forward, you can book directly here.

> Hi `{{first_name}}`,
>
> Thank you for taking the time to tour **Orlando Event Venue** with us. We enjoyed meeting you and hope the walkthrough helped you get a clear feel for the space.
>
> **Venue Highlights**
> - Up to **90 guests**
> - **90 chairs + 10 tables**
> - Prep kitchen
> - Two bathrooms
> - Free parking
> - No catering restrictions
>
> **Pricing**
>
> **Hourly Rate**
> $140/hour
> 4-hour minimum
>
> **Daily Special**
> $899/day
> 24-hour access
>
> **Cleaning Fee**
> $199 per reservation
>
> **Ready to book?**
> Reserve directly here:
> https://orlandoeventvenue.org/book
>
> If you have any questions before booking, just reply to this email.
>
> Best,
> Luis Torres
> Manager
> Orlando Event Venue
> orlandoeventvenue@gmail.com — (407) 974-5979
> 3847 E Colonial Dr, Orlando, FL 32803

## 05. Internal Admin Reminder — SMS Only

> Hi — reminder that a venue tour is scheduled in 1 hour.
> Name: `{{first_name}} {{last_name}}`
> Time: `{{tour_time}}`
> Phone: `{{phone}}`
> Email: `{{email}}`
> Location: Orlando Event Venue
> 3847 E Colonial Dr, Orlando, FL 32803
> Please be ready to receive the guest.

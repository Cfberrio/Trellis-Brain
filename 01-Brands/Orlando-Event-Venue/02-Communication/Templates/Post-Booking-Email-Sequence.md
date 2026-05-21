---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-4977 page 8cqnrff-22637 (Developer / OEV / EMAILS WEBSITE / BOOKING CALENDAR)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
related_systems:
  - ghl
  - website
hub_role: leaf
---

# Post-Booking Email Sequence

## Parent
- [[../Communication-Home|OEV Communication Home]]

## Related
- [[../OEV-Communication-Manual|OEV Communication Manual]]
- [[../../06-DNA/Fulfillment|OEV Fulfillment]]
- [[../../06-DNA/Conversion|OEV Conversion]]
- [[../../05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]

## Purpose
Canonical 10-step post-booking email + SMS sequence — from deposit received through final review request. All customer-facing communication uses these exact templates.

## SMS Placement (which steps get SMS too)
| Step | Email | SMS |
|---|---|---|
| 01. Payment confirmation | ✅ | — |
| 02. Booking confirmed | ✅ | — |
| 03. Remaining balance due | ✅ | ✅ |
| 04. Final payment received | ✅ | — |
| 05. 30-day reminder | ✅ | — |
| 06. 7-day reminder | ✅ | — |
| 07. 1-day reminder | ✅ | ✅ |
| 08. 1-hour reminder | ✅ | ✅ |
| 09. Post-event Guest Report | ✅ | ✅ |
| 10. Review request | ✅ | — |

## Variables Used
- `{{contact.first_name}}` / `{{contact.full_name}}`
- `{{contact.oev_reservation_number}}`
- `{{contact.oev_event_type}}`
- `{{contact.oev_event_date}}`
- `{{contact.oev_booking_type}}`
- `{{contact.oev_number_of_guests}}`
- `{{contact.oev_balance_amount}}`
- `{{contact.oev_balance_link_expires_at}}`
- `{{contact.oev_balance_payment_url}}`
- `{{booking.reservation_number}}`
- Website-side: `${firstName}`, `${booking.*}`, `${formattedDate}`, `${timeRange}`, etc.

## Signature Block (use on every email)
```
Orlando Event Venue Team
407-974-5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr Orlando, FL 32803
```

---

## 01 — Payment Confirmation (Website) — Email

**Subject:** Orlando Event Venue — Deposit Received
**Preview:** We received your 50% deposit. Our team will review your booking and follow up within 24 hours.

```
Hi {{contact.first_name}},

Thank you for choosing Orlando Event Venue.

We've received and secured your 50% deposit. Our team will now review your booking details and follow up within approximately 24 hours.

Booking Details
Reservation #: {{contact.oev_reservation_number}}
Event Type: {{contact.oev_event_type}}
Event Date: {{contact.oev_event_date}}
Booking Type: {{contact.oev_booking_type}}

What Happens Next
Within 24 hours, our team will review your booking details, including timing, capacity, and venue readiness.

Please do not send invitations yet until this review is complete. This helps prevent confusion in case any details need to be adjusted.

Your remaining balance will be due 15 days before your event. We'll send you a secure payment link and reminder emails when it's time.

If you need to update anything in the meantime, simply reply to this email and our team will help.

[Signature]
```

---

## 02 — Booking Confirmed (GHL) — Email

**Subject:** Your Event Is Confirmed | Orlando Event Venue
**Preview:** Your date is locked in. Here's what to expect next.

```
Hi {{contact.first_name}},

Your booking is confirmed, and your event date is now locked in.

We're already preparing behind the scenes to help your event run smoothly.

What's Included
Capacity: Up to 90 guests
Seating + Tables: 10 tables + 90 chairs
Amenities: Prep kitchen + 2 full bathrooms

What Happens Next
Your remaining balance is due 15 days before your event. We'll send a secure payment link and reminders before the due date.

Your access instructions will be emailed 1 day before your event so you have the most accurate arrival details right before your booking.

If your guest count, timing, or event needs change, reply to this email and we'll update your booking with you.

Quick Reference
Reservation #: {{contact.oev_reservation_number}}
Event Type: {{contact.oev_event_type}}
Date: {{contact.oev_event_date}}
Guest Count: {{contact.oev_number_of_guests}}
Booking Type: {{contact.oev_booking_type}}

[Signature]
```

---

## 03 — Remaining Balance Reminder (GHL) — Email + SMS

### Email
**Subject:** Remaining Balance Due | Orlando Event Venue
**Preview:** Your remaining balance is due. Your secure payment link is below.

```
Hi {{contact.first_name}},

This is a friendly reminder that your remaining event balance is now due.

Remaining Balance
Amount Due: {{contact.oev_balance_amount}}
Payment Link Expires: {{contact.oev_balance_link_expires_at}}

Pay Securely Here
{{contact.oev_balance_payment_url}}

What to Expect
Once payment is completed, your booking will update automatically.

If you have already paid, no further action is needed.

If anything looks incorrect or you need help, reply to this email and we'll take care of it quickly.

Thank you again — we look forward to hosting you soon.

[Signature]
```

### SMS
```
Hi {{contact.first_name}} — your remaining balance for Orlando Event Venue is now due.

Your secure payment link has been emailed to you. Please complete payment before the link expires.

Questions? Reply here or call 407-974-5979.
```

---

## 04 — Final Payment Received (Website) — Email

**Subject:** Final Payment Received | Orlando Event Venue
**Preview:** Your booking is now fully paid and confirmed.

```
Hi ${firstName},

Thank you for completing your final payment.

Your booking at Orlando Event Venue is now fully paid and confirmed.

Payment Received
Amount Paid: ${formatCurrency(booking.amount_paid)}

Event Details
Reservation #: ${booking.reservation_number}
Event Date: ${formattedDate}
Event Time: ${timeRange}
Booking Type: ${formattedBookingType}
Guests: ${booking.number_of_guests}
Event Type: ${booking.event_type}

Payment Summary
Total Amount: ${formatCurrency(booking.total_amount)}
Deposit Paid: ${formatCurrency(booking.deposit_amount)}
Balance Paid: ${formatCurrency(booking.balance_amount)}
Status: Fully Paid

If you need to update anything before your event, simply reply to this email.

[Signature]

Please keep this email for your records.
```

---

## 05 — 30-Day Reminder (GHL) — Email

**Subject:** 30 Days Until Your Event | Orlando Event Venue
**Preview:** Here's what to expect between now and event day.

```
Hi {{contact.first_name}},

Your event is 30 days away, so this is a good time to review the key details and next steps.

What's Included
Capacity: Up to 90 guests
Seating + Tables: 10 tables + 90 chairs
Amenities: Prep kitchen + 2 full bathrooms

Timeline
15 days before your event: Your remaining balance is due. We'll send a secure payment link and reminders.
1 day before your event: You'll receive your access instructions by email, including entry details and day-of information.

Your Event Details
Reservation #: {{contact.oev_reservation_number}}
Event Type: {{contact.oev_event_type}}
Date: {{contact.oev_event_date}}
Guest Count: {{contact.oev_number_of_guests}}
Booking Type: {{contact.oev_booking_type}}

Important Reminders
If your guest count, timing, or event needs have changed, reply now so we can update your booking.
The venue maximum is 90 guests.
Alcohol, glitter, and confetti are not allowed.

Wi-Fi
Network: GlobalChurch
Password: Orlandoministry

[Signature]
```

---

## 06 — 7-Day Reminder (GHL) — Email

**Subject:** 7 Days Until Your Event | Orlando Event Venue
**Preview:** A quick check-in so you're prepared for event week.

```
Hi {{contact.first_name}},

Your event is now 7 days away, and we're excited to host you.

This is a quick check-in to help you stay prepared and avoid last-minute issues.

Venue Information
Orlando Event Venue
3847 E Colonial Dr, Orlando, FL 32803
Wi-Fi: GlobalChurch
Password: Orlandoministry

What to Expect This Week
Your access instructions will be emailed 1 day before your event. Please check your inbox and spam/junk folder.

Please Confirm Any Updates Now
If your guest count, timing, or event needs have changed, reply to this email now so we can update your booking before event day.

Important Reminders
Maximum occupancy is 90 guests.
Setup and breakdown must stay within your booking window. Late cleanup may result in a $200/hour fee.
Alcohol, drugs, smoking, pets, glitter, confetti, and rice are not allowed.
No nails, staples, residue tape, or open flames unless pre-approved.

[Signature]
```

---

## 07 — 1-Day Reminder (GHL) — Email + SMS

### Email
**Subject:** Your Access Instructions for Tomorrow | Orlando Event Venue
**Preview:** Here are your entry instructions and post-event checkout steps.

```
Hi {{contact.first_name}},

We're excited to host you at Orlando Event Venue.

Below are your access instructions, along with the steps to complete before you leave.

Arrival & Access Instructions

1. Locate the Entrance
Arrive at Colonial Town Center and look for the GLOBAL sign with 3847 displayed.

2. Get the Key from the Lockbox
Facing the GLOBAL sign, go to the door on the left side of the building.
Near the entrance, you'll see a black lockbox with a touchscreen keypad.
Tap the screen to wake it up and enter the code: 03302026
Open the lockbox and retrieve the magnetic key.

3. Unlock the Door
Tap the magnetic key on the sensor on the right side of the door.
After unlocking, return the key to the lockbox immediately and close it.

4. Turn On the Lights
Once inside, locate the remote labeled "Light" on the left wall.
Use the left-side buttons to turn on the lights.
Please return the remote to its original place.

Before You Leave
Turn off all lights using the right-side buttons on the light control pad.
Place all trash bags on the back patio. Do not leave trash bags inside the venue.
Lock the door securely when exiting.
Make sure all personal items are removed.

Guest Report
After your booking ends, please complete your Guest Report to close out your reservation:
https://orlandoeventvenue.org/guest/report/{{contact.oev_reservation_number}}

If you need help at any point, reply to this email and we'll assist as quickly as possible.

[Signature]
```

### SMS
```
Hi {{contact.first_name}} — your access instructions for tomorrow's event have been emailed.

Please review them tonight, and reply here if you need help.

Orlando Event Venue
407-974-5979
```

---

## 08 — 1-Hour Reminder (GHL) — Email + SMS

### Email
**Subject:** Starting in 1 Hour | Orlando Event Venue
**Preview:** Here are your access steps and your post-event checkout reminder.

(Same access instructions as Step 07 — repeated for last-minute confirmation. Add: "Arriving a few minutes early is recommended so you can begin on time and use your full booking window.")

### SMS
```
Hi {{contact.first_name}} — your event starts in 1 hour.

Please use the access instructions already emailed to you. Reply here if you need help.

Orlando Event Venue
407-974-5979
```

---

## 09 — Post-Event Guest Report (Website) — Email + SMS

### Email
**Subject:** Guest Report Needed to Close Out Your Reservation | Orlando Event Venue
**Preview:** There's one final step remaining after your event.

```
Hi {{contact.full_name}},

We hope your event went well.

To officially close out your reservation, please complete your Guest Report.

Complete Your Guest Report Here
https://orlandoeventvenue.org/guest/report/{{booking.reservationnumber}}

This report takes about 2–3 minutes and includes photos or videos of the front door, main area, tables/chairs, bathrooms, and kitchen, plus a few final checkboxes.

After submitting, please reply DONE to this email.

Also, would it be too much to ask for you to complete this review and share your experience? It will only take five minutes:
https://g.page/r/CU-yUA0El90UEAE/review

[Signature]
```

### SMS
```
Hi {{contact.first_name}} — your Guest Report is needed to close out your reservation.

Please complete it here:
https://orlandoeventvenue.org/guest/report/{{booking.reservationnumber}}

We'd love to hear from you! Would it be too much to ask for you to complete this review and share your experience?
https://g.page/r/CU-yUA0El90UEAE/review

We appreciate your time and hope to host you again soon.

Orlando Event Venue
407-974-5979
```

---

## 10 — Review Request — Email

**Subject:** Action Needed Orlando Event Venue
**Preview:** We'd love to hear about your experience.

```
Hi [Name],

Thank you for hosting your event with us.

Would it be too much to ask for you to complete this review and share your experience? It will only take five minutes:

https://g.page/r/CU-yUA0El90UEAE/review

We appreciate your time and hope to host you again soon.

[Signature]
```

---

## Operational Rules

### Timing constraints
- Wi-Fi credentials: communicated ONLY in 30-day + 7-day reminder (NOT earlier — prevents premature use)
- Access instructions: communicated ONLY 1 day before + 1 hour before (NOT in confirmation — prevents pre-booking access)
- Lockbox code: rotated per booking date (currently `03302026` example — should be updated per actual booking)

### Trigger sequence
- Step 01 fires immediately on deposit payment (website event)
- Step 02 fires when admin reviews + confirms (manual trigger or 24h auto)
- Step 03 fires 15 days before event date
- Step 04 fires on remaining-balance payment (website event)
- Step 05 fires 30 days before event date
- Step 06 fires 7 days before event date
- Step 07 fires 1 day before event date
- Step 08 fires 1 hour before event start time
- Step 09 fires when booking window ends
- Step 10 fires 24h after Guest Report submitted (if Google review not detected)

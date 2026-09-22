---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Verbatim copy-paste from ClickUp doc 8cqnrff-4977, page 8cqnrff-11917 (TOURS), fetched 2026-09-21. Replaces the 2026-05-28 in-vault version, which described a different (self-access + video call) tour model that ClickUp no longer matches."
owner: Luis
last_updated: 2026-09-21
sensitivity: internal
related_systems:
  - ghl
  - website
hub_role: leaf
up:
  - "[[01-Brands/Orlando-Event-Venue/02-Communication/Communication-Home]]"
related:
  - "[[01-Brands/Orlando-Event-Venue/02-Communication/OEV-Communication-Manual]]"
  - "[[01-Brands/Orlando-Event-Venue/00-Brand-Core/Rules-and-Fees]]"
  - "[[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Post-Booking-Email-Sequence]]"
  - "[[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Automations]]"
---

# Tour Sequence

## Parent
- [[../Communication-Home|OEV Communication Home]]

## Related
- [[../OEV-Communication-Manual|OEV Communication Manual]]
- [[../../00-Brand-Core/Rules-and-Fees|OEV Rules and Fees]]
- [[Post-Booking-Email-Sequence|Post-Booking Email + SMS Sequence]]
- [[../../05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]

## Source
Verbatim copy-paste from ClickUp doc "OEV TOUR COMMUNICATIONS" (`8cqnrff-4977` / page `8cqnrff-11917`). This is the canonical wording — do not reword outside ClickUp.

> **Model change vs. the previous version of this note:** the tour is a guided phone walkthrough. The guest arrives, calls Luis at 407 974 5979, and Luis lets them in and guides them through the space live on a normal phone call. There is no self-access lockbox flow and no video call for tours, and tours do not use a reservation number or a Tour Page (those belong to booked events only). The earlier "remote self-access + video call" version of this file described a different, unbuilt model — see the ClickUp doc's own "Open question: door code" note below.

```
OEV TOUR COMMUNICATIONS

1. Communication Overview

T01 and T02 send the same SMS. It is written so it reads correctly both a day before and an hour before, and it is set up once and reused in both steps. T01 also sends an email; T02 is SMS only.

The tour is a guided walkthrough. The guest arrives at the venue and calls Luis at 407 974 5979. Luis lets them in, guides them through the space on a normal phone call, explains the venue details and available options, and answers their questions.

Tours do not have a reservation number and do not use a Tour Page. Those belong to booked events only.

2. TOUR CONFIRMATION

After the guest schedules a tour, the confirmation sends immediately.

TC01. SMS Confirmation

Hi {{contact.first_name}}, your tour of Orlando Event Venue is confirmed.

When: {{appointment.start_time}}

Where: 3847 E Colonial Dr, Orlando, FL 32803. Park in the Colonial Town Center plaza and look for the GLOBAL sign with 3847.

This is a guided walkthrough. When you arrive, call Luis at 407 974 5979 and he will let you in and guide you through the venue.

We will send you a reminder the day before and one hour before your tour.

Need to make a change? Call or text 407 974 5979.

Orlando Event Venue

TC01. Email Confirmation

Subject: Your Orlando Event Venue Tour Is Confirmed
Preview: How your guided walkthrough works and where to find us.

Hi {{contact.first_name}},

Your tour of Orlando Event Venue is confirmed.

YOUR TOUR

{{appointment.start_time}}

Orlando Event Venue
3847 E Colonial Dr
Orlando, FL 32803

HOW YOUR TOUR WORKS

This is a guided walkthrough. When you arrive, call Luis at 407 974 5979. He will let you in, guide you through the space, explain the venue details and available options, and answer your questions.

FINDING US

Free parking is available in the Colonial Town Center plaza. The entrance can be easy to miss the first time: look for the GLOBAL sign with 3847, face the sign, and use the door on the left.

During the tour you will be able to walk through the venue, see the included tables, chairs, prep kitchen, bathrooms, and parking, review the available rental and production options, and ask questions about your event.

We will send you a reminder the day before and one hour before your tour.

If you need to reschedule, call or text 407 974 5979.

Luis and the Orlando Event Venue Team

T01. Tour Reminder, 1 Day Before

Channel: SMS and Email
Timing: Approximately 24 hours before the tour

SMS: send the shared reminder SMS above.

Email

Subject: Your Tour Is Tomorrow
Preview: How the tour works and how to find us.

Hi {{contact.first_name}},

Your tour of Orlando Event Venue is tomorrow.

WHEN

{{appointment.start_time}}

WHERE

Orlando Event Venue
3847 E Colonial Dr
Orlando, FL 32803

Free parking is available in the Colonial Town Center plaza. Look for the GLOBAL sign with 3847, face the sign, and use the door on the left.

HOW IT WORKS

When you arrive, call Luis at 407 974 5979. He will let you in, guide you through the venue, explain the available features and services, and answer your questions.

Need to reschedule? Call or text 407 974 5979.

Luis and the Orlando Event Venue Team

T02. Tour Reminder, 8 Hours Before

Channel: SMS only

Hi {{contact.first_name}}, reminder about your tour at Orlando Event Venue

When: {{appointment.start_time}}

Please confirm with "YES" to keep your appintment.

Where: 3847 E Colonial Dr, Orlando, FL 32803. Park in the Colonial Town Center plaza and look for the GLOBAL sign with 3847. The entrance is the door on the left.

When you arrive, call Luis at 407 974 5979 and he will let you in and guide you through the venue.

Need to change the time, or help finding us? Let us know asap.

Orlando Event Venue

T03. Post-Tour Booking Follow-Up

Send only if the guest has not completed a booking.

T03. Email

Channel: Email
Timing: Approximately 1 hour after the tour

Subject: Your Event Planning Kit + A Surprise Inside
Preview: Your free planning resources and $50 OFF Orlando Event Venue.

Hi {{contact.first_name}},

Thank you again for touring Orlando Event Venue.

As promised, here is your free Event Planning Kit to help you organize your budget, setup, timeline, and other important event details:

https://orlandoeventvenue.org/planning-kit

We also have a surprise for you:

Use discount code PLAN50 to receive $50 OFF your Orlando Event Venue rental.

When you are ready, view the available options and secure your date here:

https://orlandoeventvenue.org/book

If you have any questions before booking, call or text me at 407 974 5979. I'm happy to help.

Luis Torres
Orlando Event Venue

T03. SMS

Channel: SMS
Timing: Approximately 3 hours after the tour

Hi {{contact.first_name}}, I sent you an email with your free event planning kit and a special discount code.

Check your inbox for "Your Event Planning Kit + A Surprise Inside."

When you're ready, you can secure your date here:

https://orlandoeventvenue.org/book

Questions? Call or text me at 407 974 5979.

Luis Torres

4. FINAL TOUR SEQUENCE

The guest schedules a tour on the GHL calendar embedded at orlandoeventvenue.org/schedule-tour.
Send the TC01 confirmation by SMS and email, immediately.
Approximately one day before the tour, send the shared reminder SMS and the T01 email.
Approximately one hour before the tour, send the shared reminder SMS again.
The guest arrives and calls Luis at 407 974 5979.
Luis lets the guest in and guides them through the venue on a normal phone call.
Send the T03 email approximately one hour after the tour if no booking has been completed.
Send the T03 SMS approximately three hours after the tour if no booking has been completed.
If the guest books after receiving the T03 email but before the T03 SMS is scheduled, do not send the SMS.

5. BUILD NOTES

Date and time merge field

The tour date and time come from the GHL appointment, using a single merge field:

{{appointment.start_time}}

Do not use appointment.date or appointment.time. Those two fields do not exist in GHL. Any message using them sends with the line blank, which is what happened on the confirmation sent to Ricardo Guevara on 2026-08-04. GHL does not raise an error for an unknown merge field, it simply renders nothing.

GHL has no separate merge fields for date and for time, so the messages above put both on a single "When:" line rather than the previous two-line "Date: / Time:" layout.

Two things to confirm inside GHL before sending:

Confirm the exact field name in the merge field picker. Open the message inside the workflow that already has its appointment trigger set, then use the merge field selector. The picker lists only what is actually available in that context, with the exact name for the current GHL version. If a field does not appear there, it does not exist and no spelling of it will work.
Confirm the message runs in an appointment context. The appointment merge fields are only populated when the automation was triggered by an appointment event, such as Customer Booked Appointment or Appointment Status. If the workflow starts from a tag, from Contact Created, or from any other trigger, there is no appointment attached and the field renders blank even when the name is correct.

Also check how the time renders on the first send: the format and timezone follow the calendar and location settings, not the message.

One reminder SMS, sent twice

T01 and T02 share a single SMS body. Keeping one text instead of two means the reminder wording can never drift apart between the two sends, and it is the reason the message avoids "tomorrow" and "in about an hour": those would be wrong at one of the two send times.

If the copy ever needs to change, change it once and update both workflow steps.

No reservation number and no Tour Page for tours

Tours do not carry a reservation number, and none of the tour messages ask for one.

{{contact.oev_reservation_number}} is a contact custom field populated from a booking snapshot. A tour is not a booking: it exists only in the GHL calendar and never reaches the OEV database. Using that field in a tour message produces one of two wrong results: it renders blank for a guest who has never booked, or it renders the number of an unrelated past booking.

Because the Tour Page was opened by entering that reservation number, the Tour Page is out of the tour flow as well. Access is handled by the guest calling Luis on arrival, which is already how the guided walkthrough works.

Open question: door code

The previous version of this document had the guest opening the venue themselves with a live door code shown on the Tour Page one hour before the appointment. That flow is not built, and without a reservation number there is no way to open such a page.

For now, Luis lets the guest in when they call. If tours should later become self-access, that needs a decision and a separate build: storing tours in the OEV database from a GHL webhook, generating a tour identifier, and building the page with the dynamic code, the same way orlandoeventvenue.org/accesscode works for booked events.

T03 automation notes

T03 contains two communications: one email and one SMS.
Send the T03 email approximately one hour after the tour.
Send the T03 SMS approximately three hours after the tour.
Before sending each communication, confirm that the guest has not completed a booking.
If the guest has already booked, do not send the remaining T03 communication.
The Event Planning Kit lives at orlandoeventvenue.org/planning-kit and is live as of 2026-08-04.
The discount code is PLAN50. The offer must always be written as $50 OFF.
The T03 SMS does not need to include the kit link or discount code itself. Its purpose is to direct the guest to the email containing the Event Planning Kit and $50 OFF offer.
```

## Note
The prior in-vault version of this file (2026-05-28) described a self-access lockbox + video-call tour model. That model is not what ClickUp specifies and, per the ClickUp doc's own "Open question: door code" section, was never built. The block above is the literal, current ClickUp text: a phone-guided walkthrough with no reservation number, no Tour Page, and no video call. If the copy or the tour model changes, update ClickUp first, then re-paste here.

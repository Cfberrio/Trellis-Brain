---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Verbatim copy-paste from ClickUp doc 8cqnrff-4977, page 8cqnrff-31517 (BOOKING), fetched 2026-09-21. Replaces the 2026-05-27 in-vault version, which had drifted from live copy."
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
  - "[[01-Brands/Orlando-Event-Venue/06-DNA/Fulfillment]]"
  - "[[01-Brands/Orlando-Event-Venue/06-DNA/Conversion]]"
  - "[[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Automations]]"
---

# Post-Booking Email + SMS Sequence

## Parent
- [[../Communication-Home|OEV Communication Home]]

## Related
- [[../OEV-Communication-Manual|OEV Communication Manual]]
- [[../../00-Brand-Core/Rules-and-Fees|OEV Rules and Fees]]
- [[../../06-DNA/Fulfillment|OEV Fulfillment]]
- [[../../06-DNA/Conversion|OEV Conversion]]
- [[../../05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]

## Source
Verbatim copy-paste from ClickUp doc "OEV POST BOOKING COMMUNICATIONS" (`8cqnrff-4977` / page `8cqnrff-31517`). This is the canonical wording — do not reword outside ClickUp. Covers internal bookings (I01, I02), external bookings (E01), shared payment/check-in touches (S01, P01, P02, S02, S04, S06), and the standard reference/writing rules.

```
OEV POST BOOKING COMMUNICATIONS
1. Writing Standard
Every message is written to be read once and understood. The tone is warm and direct. It should feel like Luis talking to a host, not a system sending a notice.
We share only what matters at that moment and let the Event Page carry the full detail, so no single message is heavy and nothing important gets buried.
We number a list only when the reader has several things to do or check. Emails close with a reference block. Texts close with the reservation number.
The Event Page at orlandoeventvenue.org/accesscode is the one place that holds access instructions, the live door code, Wifi, venue rules, the Before You Leave checklist, and the Guest Report.
2. Communication Overview

3. Standard Reference Section
Appears at the bottom of every email. It does not interrupt the message.
FOR REFERENCE
Reservation Number:
{{contact.oev_reservation_number}}
Event Date:
{{contact.oev_event_date}}
Event Time:
{{contact.oev_event_start_time}} to {{contact.oev_event_end_time}}
Event Type:
{{contact.oev_event_type}}
Booking Type:
{{contact.oev_booking_type}}
Guest Count:
{{contact.oev_number_of_guests}}
Text messages end only with:
Reservation #{{contact.oev_reservation_number}}
4. Internal Booking Communications
I01. First 50% Received and Under Review
Email | Sent when the first 50% is received
Email subject: We Received Your First Payment
Preview: Your booking is now being reviewed by our team.
Hi {{contact.first_name}},
Thank you. We have received your first fifty percent, and your booking is now with our team for review.
We take a quick look at the timing, guest count, and venue setup to make sure everything about your event will run smoothly, and we will be back in touch within about 24 hours to confirm.
Until you hear from us, please hold off on sending invitations or making any arrangements you cannot get back. And if anything about your event has changed since you booked, just reply here so we review the right details.
In the meantime, you can start getting familiar with your Event Page. It is the one place that will hold everything you need as your date gets closer. That includes your planning details, venue instructions, live door code on event day, the Before You Leave checklist, and your Guest Report:

Enter your reservation number when prompted.
We will reach out the moment your review is complete.
Luis and the Orlando Event Venue Team
407 974 5979
orlandoeventvenue@gmail.com
Followed by the standard reference block in Section 3.
I02. Booking Confirmed
Email | Sent when the booking is approved
Subject: Your Event Is Confirmed
Preview: Your booking is approved. Here is what happens next.
Hi {{contact.first_name}},
Good news. Your event at Orlando Event Venue is approved and officially confirmed. We are looking forward to hosting you.
Your final payment is due fifteen days before your event, and we will email you a secure link when it is time, so there is nothing to do on that front right now.
About a month out, we will check in on the few details that affect how we prepare the space:
Whether alcohol will be served.
Any audio and visual needs.
Any additional services you would like to add.
Everything else is in your hands, so that is all we will ask about.
The most useful thing to do today is save your Event Page. It is the single place that holds your venue instructions, live door code, Wifi, venue rules, the Before You Leave checklist, and your Guest Report:

Enter your reservation number when prompted. Your live door code appears there one hour before your event begins.
If anything changes between now and then, just reply here or call 407 974 5979.
Luis and the Orlando Event Venue Team
Followed by the standard reference block in Section 3.
5. External Booking Communication
E01. Booking Confirmed
Email | Sent when an external booking is received
Subject: Your Orlando Event Venue Booking Is Confirmed
Preview: We have your reservation. Here is what happens next.
Hi {{contact.first_name}},
Your booking at Orlando Event Venue is confirmed, and we are looking forward to hosting you.
Your payment is handled through the company or platform where you reserved, so there is nothing to pay us directly. On our side, we take care of everything about the event itself: your planning, venue access, event day support, closing, and Guest Report.
About a month out, we will check in on the few details that affect how we prepare the space:
Whether alcohol will be served.
Any audio and visual needs.
Any additional services you would like to add.
Everything else is in your hands, so that is all we will ask about.
The most useful thing to do today is save your Event Page. It is the single place that holds your venue instructions, live door code, Wifi, venue rules, the Before You Leave checklist, and your Guest Report:

Enter your reservation number when prompted. Your live door code appears there one hour before your event begins.
Questions or changes? Reply here or call 407 974 5979.
Luis and the Orlando Event Venue Team
Followed by the standard reference block in Section 3.
6. Shared Communications
S01. 30 Day Check In
Email | Sent 30 days before the event
Subject: Let us Confirm a Few Details for Your Event
Preview: A quick check on bar service, audio and visual needs, and additional services.
Hi {{contact.first_name}},
Your event is about one month away. We only need to confirm a few details that could affect what is available to you on event day.
Please reply if anything has changed:
1. Bar Service
Will alcohol be served, or has your original plan changed? All alcohol service must go through Orlando Event Venue. You cannot bring your own alcohol, and you cannot bring your own bartender.
2. Audio and Visual Services
Will you need microphones, a projector, the LED wall, streaming, video calls, or technical support?
3. Additional Services
Would you like to add tablecloths, production support, setup help, or any other venue service?
A couple of things worth remembering: the venue holds up to 90 guests, and you are responsible for setting up and returning the tables and chairs to their original arrangement. Before you leave, all bagged trash goes on the back patio. Our team handles the standard cleaning afterward.
You can review your event information, venue rules, and upcoming instructions on your Event Page any time:

Reply with any changes. If everything is the same, there is nothing you need to do.
Luis and the Orlando Event Venue Team
407 974 5979
Followed by the standard reference block in Section 3.
P01. Remaining Payment Due
Email | Internal bookings only | Sent 15 days before the event
Subject: Your Remaining Payment Is Due
Preview: Complete your final payment with the secure link below.
Hi {{contact.first_name}},
Your remaining balance for your event is now due. You can complete it securely here:
{{contact.oev_balance_payment_url}}
Your balance:
{{contact.oev_balance_amount}}
Due:
{{contact.oev_balance_due_date}}
The link expires on:
{{contact.oev_balance_link_expires_at}}
Please complete it before then to keep your date secured.
As soon as your payment goes through, your booking updates automatically and we will email your receipt along with your final event day details. If you have already paid, you are all set. There is no action needed.
Questions or trouble with the link? Reply here or call 407 974 5979.
Luis and the Orlando Event Venue Team
Followed by the standard reference block in Section 3.
P02. Fully Paid Confirmation
Email | Internal bookings only | Sent when the final payment is received
Subject: Your Event Is Fully Paid
Preview: No further payment is needed. Here is how to get ready.
Hi {{contact.first_name}},
Your final payment is in. Your event is fully paid, and there is nothing more to pay. Thank you.
From here on, everything is about getting ready for event day, and it all lives on your Event Page:

Enter your reservation number when prompted. There you will find:
Your venue access instructions.
Your live door code.
Wifi.
The venue rules.
Your Before You Leave checklist.
Your Guest Report.
Your door code appears one hour before your event begins.
We will stay in touch as your date approaches. You will get a quick check in seven days out, a preparation reminder the day before, and your full access instructions one hour before you start.
Please make sure whoever arrives first also has your Event Page link and reservation number.
Luis and the Orlando Event Venue Team
407 974 5979
Followed by the standard reference block in Section 3.
S02. 7 Day Final Check In
SMS | Sent 7 days before the event
Hi {{contact.first_name}}, your event is one week away.
If anything has changed with your bar service, audio and visual needs, or any additional services, reply here and we will take care of it.
If everything is the same, reply CONFIRMED and you are set.
Reservation #{{contact.oev_reservation_number}}
S04. Event Access
Email and SMS | Sent 1 day before the event
Email
Email subject: Your Event Access Page
Preview: Your door code and complete entry instructions will be available on your Event Page.
Hi {{contact.first_name}},
Your event is tomorrow.
Your door code and complete instructions for entering the venue are available only on your Event Page:

Enter your reservation number when prompted.
Your Event Page includes:
Your live door code when it becomes available.
Complete instructions for entering the venue.
Wifi information.
The venue rules.
Your Before You Leave checklist.
Your Guest Report.
Your live door code will appear on the page one hour before your event begins.
Please make sure whoever arrives first has the Event Page link and your reservation number.
Need help? Call or text 407 974 5979.
Luis and the Orlando Event Venue Team
Followed by the standard reference block in Section 3.
SMS
Hi {{contact.first_name}}, your event is tomorrow.
Your live door code and complete entry instructions will be available only on your Event Page:

Enter your reservation number when prompted. Your door code will appear one hour before your event begins.
Please make sure whoever arrives first has the link and your reservation number.
Need help? Call or text 407 974 5979.
Reservation #{{contact.oev_reservation_number}}
S06. Guest Report and Review
Email and SMS | Sent 1 hour after the event starts
Email
Email subject: Thank You for Hosting. One Quick Step to Close Out Your Event
Preview: Submit your Guest Report and tell us how it went.
Hi {{contact.first_name}},
Thank you for choosing Orlando Event Venue, and thank you for trusting us to host your event. It genuinely means a lot.
Now that your reservation has ended, there is one last step: your Guest Report. It is how we confirm the venue was closed out properly, and it takes about two minutes on your Event Page:

Before you submit, just make sure:
Everyone has left.
The lights are off.
The trash is on the back patio with nothing left inside.
The tables and chairs are back in their original arrangement.
The prep kitchen and both bathrooms are checked.
Your personal items and equipment are cleared.
The entrance is locked.
Then upload a few quick photos. The report shows you exactly which ones.
Your reservation stays open until we receive it, so please complete it while you are still on site if you can.
One more thing. If your event went well, an honest Google review is the single biggest way you can help future hosts find us. We would be grateful:

Thank you again for hosting with us.
Luis and the Orlando Event Venue Team
407 974 5979
Followed by the standard reference block in Section 3.
SMS
Hi {{contact.first_name}}, thank you for hosting with us!
Your reservation has ended, so there is one last step: your Guest Report. It takes about two minutes and confirms the venue was closed out:

And if it went well, an honest review means the world to us:

Reservation #{{contact.oev_reservation_number}}
```

## Note
This file previously carried an older (2026-05-27) in-vault paraphrase of this sequence, which had drifted from what ClickUp actually says (different subjects, different step numbering, different wording throughout). That version is gone. The block above is the literal ClickUp text, unedited. If the copy needs to change, change it in ClickUp first, then re-paste here.

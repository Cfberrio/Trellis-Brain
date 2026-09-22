---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Verbatim copy-paste from ClickUp doc 8cqnrff-4977, page 8cqnrff-11737 (LEAD SEQUENCE), fetched 2026-09-21. Replaces the HOST100-era version of this note, superseded 2026-08-04 by the Event Planning Kit / PLAN50 offer."
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
  - "[[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home]]"
  - "[[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Tour-Sequence]]"
  - "[[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Post-Booking-Email-Sequence]]"
  - "[[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Lead-Magnet-Event-Planning-Kit]]"
---

# Pop-Up Lead Magnet Sequence

## Parent
- [[../Communication-Home|OEV Communication Home]]

## Related
- [[../OEV-Communication-Manual|OEV Communication Manual]]
- [[../../00-Brand-Core/Brand-Home|OEV Brand Home]]
- [[Tour-Sequence|Tour Sequence]]
- [[Post-Booking-Email-Sequence|Post-Booking Email + SMS Sequence]]
- [[../../01-Systems/Marketing/Lead-Magnet-Event-Planning-Kit|Lead Magnet — Event Planning Kit]]

## Source
Verbatim copy-paste from ClickUp doc "OEV Lead Magnet System" / "OEV LEAD MAGNET COMMUNICATIONS AND EVENT PLANNING KIT" (`8cqnrff-4977` / page `8cqnrff-11737`), fetched 2026-09-21. This is the **current, active** offer (Event Planning Kit + PLAN50), replacing the old HOST100 sequence this file used to hold. This is the canonical wording — do not reword outside ClickUp.

> **Developer note carried over from ClickUp:** OEV-LM-S04 and all customer-facing expiration language must remain disabled until PLAN50 can expire separately for each contact and the expiration can be enforced during checkout. Per [[../../01-Systems/Marketing/Lead-Magnet-Event-Planning-Kit|Lead Magnet — Event Planning Kit]], per-contact PLAN50 expiry is **not implemented** — the coupon is currently a shared code with no per-lead expiry window.

```
OEV Lead Magnet System
PART 3: LEAD COLLECTION FORM
5. Final Popup Copy

6. Form Fields

OEV LEAD MAGNET COMMUNICATIONS AND EVENT PLANNING KIT
1. Message Timeline

Important Developer Note
OEV-LM-S04 and all customer-facing expiration language must remain disabled until PLAN50 can expire separately for each contact and the expiration can be enforced during checkout.

2. CONFIRMATION SCREEN
Headline
Your Event Planning Kit + $50 OFF Are on the Way
Message
Check your email and text for your Event Planning Kit and your code for $50 OFF your venue rental.
Already know your date? Only 50% of total is needed to book.
Questions or did not receive the kit? Call or text 407 974 5979.
Confirmation Screen Requirements
Do not include an "Open My Event Planning Kit" button.
Do not include an "Open My Email" button.
Do not add a button that suggests the customer can open an email from the confirmation screen.
The customer should be told to check their email and text for the kit and $50 OFF.
A booking button may remain as a separate secondary action.
A tour button may remain once the final tour-booking URL is confirmed.
Optional Secondary Actions

3. ACTUAL EMAILS AND SMS MESSAGES
OEV-LM-E01 — IMMEDIATE EMAIL
Subject: Your Event Planning Kit + $50 OFF
Preview Text: Your planning checklist and PLAN50 are ready.
Hi {{contact.first_name}},
Welcome, and thank you. Your Event Planning Kit is ready.
We are a local nonprofit venue built for events of up to 90 guests. The kit covers your planning timeline, budget, room layout, and the small things hosts often forget, including serving spoons, ice, and extra trash bags.
Open your kit here:
{{kit_url}}
You will also receive PLAN50:
Code: PLAN50
Offer: $50 OFF your venue rental
Use: Enter the code during checkout
When you are ready to hold your date, begin here:
{{booking_url}}
Your date is held after the first 50 percent is received. Our team will then review the timing, guest count, and setup before sending a separate confirmation.
Questions? Reply to this email or call or text 407 974 5979.
Luis and the Orlando Event Venue Team
407 974 5979
orlandoeventvenue.org
orlandoeventvenue@gmail.com
3847 E Colonial Dr, Orlando, FL 32803
Email Actions

OEV-LM-S01 — IMMEDIATE SMS
Hi {{contact.first_name}}, Orlando Event Venue here. Your Event Planning Kit is ready on your email. Use PLAN50 for $50 OFF your venue rental. When you are ready, begin your booking here: {{booking_url}}. Questions? Reply or call 407 974 5979.

OEV-LM-E02 — 24 hr
Subject: A Quick Note From Luis, and Your Kit
Preview Text: A few helpful venue details and a simple way to see the space.
Hi {{contact.first_name}},
Luis here. I hope the Event Planning Kit is helping you get organized.
If you have not opened it yet, you can find it here:
{{kit_url}}
Here are a few venue details to keep in mind:
You may choose your own caterer. Professional caterers must provide proof of insurance. The prep kitchen is for staging and reheating, not cooking.
Free parking is available in the Colonial Town Center plaza.
The room holds up to 90 guests and includes 10 tables and 90 chairs.
Would you like to see the space before deciding?
Book a tour here:
{{tour_url}}
Already know your date? Begin your booking here:
{{booking_url}}
Your date is held after the first 50 percent is received. Our team will then review the timing, guest count, and setup before sending a separate confirmation.
Use PLAN50 for $50 OFF your venue rental.
Reply any time with questions. We are happy to help.
Luis and the Orlando Event Venue Team
407 974 5979
orlandoeventvenue.org
Email Actions

OEV-LM-S02— 24 hr

Hi {{contact.first_name}}, Luis at Orlando Event Venue. Want to see the space before deciding? Book a tour here: {{tour_url}}. Already know your date? Begin your booking: {{booking_url}}. Use PLAN50 for $50 OFF your venue rental.

OEV-LM-E03 — 48 hours after
Subject: Ready to finalize your event?
Preview Text: Use the kit to plan clearly, then hold your date when you are ready.
Hi {{contact.first_name}},
Just checking in.
The Event Planning Kit covers the details hosts need to understand before the event, including the venue rules, planning timeline, room layout, and what to bring.
When you are ready, the first 50 of payment holds your date. Our team will then review and send a separate confirmation.
The remaining balance is due 15 days before the event.
Begin your booking here:
{{booking_url}}
Would you prefer to see the space first?
Book a tour here:
{{tour_url}}
You can also review your Event Planning Kit here:
{{kit_url}}
Use PLAN50 for $50 OFF your venue rental.
Prefer to talk it through? Reply to this email or call or text me at 407 974 5979.
Luis and the Orlando Event Venue Team
407 974 5979
orlandoeventvenue.org
Email Actions

OEV-LM-S04 — 72 hours after

Hi {{contact.first_name}}, $50 OFF your venue rental expires tonight. When you are ready, the first 50 percent boks the venue: {{booking_url}}. Prefer to see the space first? Book a tour: {{tour_url}}. Questions? Reply or call 407 974 5979.

4. ORLANDO EVENT VENUE EVENT PLANNING KIT
ORLANDO EVENT VENUE
Your Event Planning Kit
Everything you need to plan a smooth event in our space, including the small things people often forget.
Orlando Event Venue is a local nonprofit venue built for events of up to 90 guests. You get a clean, private room that you can arrange for your event. You bring the plan, food, decorations, and event details. We provide the space and clear information so nothing catches you off guard.
Keep this kit open on your phone while you plan. You can also print the checklists and worksheets.
Venue Snapshot

1. What We Provide and What You Bring
This is the most important part of the kit. Knowing what is already at the venue will help you avoid unnecessary purchases and last-minute problems.

Important Food Information
You may choose your own caterer.
Professional caterers must provide proof of insurance.
There is no cooking at the venue.
The kitchen is for staging, assembling, and reheating food.
Food should arrive ready to serve or only need warming.
Important Alcohol Information
Alcohol and bartending must be arranged through Orlando Event Venue. Bar packages begin at $18 per guest. Contact the team before purchasing or arranging alcohol.
The Items Most Often Forgotten
If you remember nothing else, remember:
Plates, cups, and utensils
Serving spoons and tongs
Serving bowls, trays, and platters
Tablecloths
Ice
Extra trash bags
2. Your Event Budget
You do not need a complicated spreadsheet. Estimate the main expenses before buying anything, then update the actual amount as you spend.

Planning tip: Keep approximately 10 percent of the budget available for last-minute items.
Use PLAN50 for $50 OFF your venue rental.
3. Your Planning Timeline

Four or More Weeks Before
Begin your booking.
Set a rough guest count. The venue holds up to 90 guests.
Choose your caterer or decide what food you will bring.
Decide whether you need bar service.
Decide whether you need the LED wall or audiovisual services.
Plan for the remaining direct-booking balance, due 15 days before the event.
Your date is held after the first 50 percent is received. OEV will then review the timing, guest count, and setup before sending a separate confirmation.
Two Weeks Before
Confirm the final guest count.
Confirm the caterer and arrival time.
Confirm that a professional caterer has supplied proof of insurance.
Sketch the room and table layout.
Purchase or reserve tableware, linens, and serving pieces.
Review the venue rules before finalizing decorations.
One Week Before
Confirm the event timeline with the caterer and helpers.
Complete the Bring List.
Gather supplies in one location.
Assign people to help with setup and closing.
Two or Three Days Before
Buy ice, drinks, and fresh food.
Charge speakers, lights, phones, and other equipment.
Print the run sheet and table layout.
Pack supplies into labeled boxes or bins.
Day Before
Review the access instructions on your Event Page.
Confirm who will arrive first.
Load the vehicle or place everything by the door.
Rest. The planning is complete.
After the Event
Restore the tables and chairs.
Bag all trash and place it on the back patio.
Turn off the lights.
Confirm that personal items have been removed.
Lock the entrance.
Submit the Guest Report through your Event Page.
4. Complete Bring List
Food and Serving
Serving spoons
Tongs and ladle
Platters, serving bowls, and trays
Cutting board and sharp knife
Can opener and bottle opener
Foil and cling wrap
Containers for leftovers
Warming trays and approved fuel, if needed
Ice and coolers
Paper towels and hand wipes
Tableware
Plates and bowls
Cups for cold drinks
Cups for hot drinks
Forks, knives, and spoons
Napkins
Tablecloths and linens
Centerpieces or table decorations
Drinks
Water
Soft drinks
Juice
Drink dispensers or pitchers
Cups and straws
Extra ice
Bar service arranged with OEV if alcohol will be served
Setup and Decorations
Welcome sign
Table numbers or directional signs
Removable hooks that leave no residue
Approved tape that leaves no residue
Scissors
Markers
Zip ties or twist ties
Extension cord
Power strip
Phone and speaker chargers
Lighter or matches only when flames have been approved in advance
Trash and Closing
OEV handles standard cleaning. You are responsible for bagging the trash, placing it on the back patio, and restoring the tables and chairs.
Extra trash bags
Wipes for quick spills
Containers for leftover food
Helpers assigned for closing
Just in Case
Small first-aid kit
Phone charger
Pen and paper
Safety pins
Small sewing kit
Stain-remover pen
Cash for tips
Printed run sheet
Printed table layout
5. Your Table and Room Plan
You have 10 tables and 90 chairs available.
Start by deciding which tables will not be used for guest seating:
Food and drinks table
Gift, sign-in, or guest-book table
Bar or service table, if needed
Remaining tables for guests
Common Layouts

If round tables are used, estimate approximately 8 to 10 guests per table. Confirm the final plan using the guest count and actual arrangement.
Leave Room For
A clear path to the bathrooms
A clear path to the exit
A line around the food table
An open area for dancing or mingling
The bar area, if bar service is added
Guests using wheelchairs or walkers
Layout Notes

6. Help Every Guest Participate
Keep clear, wide paths for guests using a wheelchair or walker.
Confirm accessible parking and entrance information with OEV.
Do not reserve or block public accessible spaces without authorization.
Service animals are welcome in accordance with applicable law.
Ask guests about food allergies and dietary needs.
Share dietary information with the caterer.
Create a calm area for anyone who may need a short break.
7. Food and Drink Plan
Food

Remember: The kitchen is for staging and reheating. Food should arrive ready to serve or only need warming.
Drinks
Place water and nonalcoholic drinks where guests can reach them.
Plan approximately two drinks per guest during the first hour and one drink per additional hour.
Bring enough cups, straws, pitchers, or dispensers.
Purchase more ice than the initial estimate.
Arrange alcohol and bartending with OEV before the event.
8. Help Guests Find the Venue
The entrance can be easy to miss the first time.
Park in the Colonial Town Center plaza.
Look for the GLOBAL sign with 3847.
Face the GLOBAL sign.
Use the door on the left.
Guest Arrival Checklist
Send the address to guests.
Send the parking instructions on the morning of the event.
Explain that the entrance is beside the GLOBAL sign.
Place a welcome sign near the entrance.
Assign a greeter.
Give the greeter a list of important telephone numbers.
Venue address: 3847 E Colonial Dr, Orlando, FL 32803
OEV telephone number: 407 974 5979
9. Your Day-of Run Sheet
Choose helpers before filling in the schedule.

Event Schedule

Before Guests Arrive
Bathrooms are ready.
Tables and chairs are arranged.
Food and drinks are ready.
Trash bags are installed.
Music, lighting, and equipment are working.
Welcome and directional signs are in place.
Walkways and exits are clear.
Closing Checklist
Complete everything before the reservation ends.
All guests have left.
All trash is bagged and placed on the back patio.
Tables and chairs are returned to their original arrangement.
The prep kitchen is checked.
Both bathrooms are checked.
Personal items and equipment are packed.
Remotes and venue equipment are returned.
All lights are turned off.
The entrance is locked.
The Guest Report is submitted.
In an emergency, call 911. The venue address is 3847 E Colonial Dr, Orlando, FL 32803.
10. The Small Things People Forget
Review this checklist before leaving home.

Also remember:
First-aid kit
Stain-remover pen
Cash for tips
Accessible parking and entrance information
Event Page link
Reservation number
Contact information for the person arriving first
11. Venue Rules to Plan Around
The complete rules will appear on your Event Page after booking.

Cameras and noise sensors help OEV monitor the venue.
READY TO HOLD YOUR DATE?
You have the plan. The next step is holding the space.
Your date is held after the first 50 percent is received. The Orlando Event Venue team will then review the timing, guest count, and setup before sending a separate confirmation.
For direct bookings, the remaining balance is due 15 days before the event.
Use PLAN50 for $50 OFF your venue rental.
Begin your booking:

Questions? Call or text 407 974 5979.
Luis and the Orlando Event Venue Team
orlandoeventvenue.org

FINAL DEVELOPER NOTE
The published Event Planning Kit must not claim that PLAN50 expires in seven days until the expiration can be calculated and enforced separately for each contact.
Once that functionality has been successfully implemented and tested, the closing section of the kit may include:
PLAN50 is available through {{offer_expires_at}}. Your Event Planning Kit is yours to keep.
```

## Note
This file used to hold the HOST100 sequence (SAVE100/SAVE50 before that), superseded 2026-08-04. That old copy is gone — the block above is the current, literal ClickUp text for the PLAN50 / Event Planning Kit offer. If the copy needs to change, change it in ClickUp first, then re-paste here. See [[../../01-Systems/Marketing/Lead-Magnet-Event-Planning-Kit|Lead Magnet — Event Planning Kit]] for the offer-history table and implementation status (per-contact PLAN50 expiry is still not built).

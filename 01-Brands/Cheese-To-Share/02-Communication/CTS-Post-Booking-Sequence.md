# Cheese to Share — Post-Booking Communication Sequence

## Canonical Contact Block

Every email and SMS in this sequence closes with this exact contact info. Do not vary the phone, email, or URL across touchpoints.

```
Cheese To Share
(407) 494-4263
info@cheesetoshare.us
https://www.cheesetoshare.us/
```

Email sign-off: "Warm regards," followed by the contact block above (brand only, no personal name).
SMS sign-off: "Luis, Cheese To Share" — first name + brand only, no phone/email/URL inside the SMS body.

## Sender / Delivery Map

| # | Touchpoint | Channel | Sender |
|---|---|---|---|
| 01 | Booking Confirmed | Email | CTS SMTP (Gmail) |
| 02 | Balance Due | Email + SMS | GHL |
| 03 | Balance Paid | Email | CTS SMTP (Gmail) |
| 04 | Event Week — Final Details | Email | GHL |
| 05 | Day Before | SMS | GHL |
| 06 | Review Request | Email + SMS | GHL |

---

## 01 · BOOKING CONFIRMED — EMAIL ONLY

**Subject:** Your Cheese To Share booking is confirmed — {{contact.cts_event_date}}
**Preview text:** Deposit received. Your date is locked in. The spread is already coming together.

Good morning {{contact.first_name}},

Thank you for booking CTS — we look forward to sharing this one with you.

Your 50% deposit is in, and your date is officially locked in. Behind the scenes, our team is already creating the experience in our heads.

**Your Booking**
Reservation #: {{contact.cts_reservation_number}}
Services: {{contact.cts_services}}
Date: {{contact.cts_event_date}}
Time: {{contact.cts_event_time}}
Address: {{contact.cts_event_address}}
Guest Count: {{contact.cts_guest_count}}

**Payment Summary**
Total: {{contact.cts_total_amount}}
Deposit Paid: {{contact.cts_deposit_amount}}
Remaining Balance: {{contact.cts_balance_amount}}

**Key Dates to Know**
14 days before your event — Remaining balance is due. We'll send a secure payment link and a text reminder.
7 days before your event — Final guest count locks. Increases possible if inventory allows; decreases after this point don't reduce the price.
1 day before your event — You'll get a short text with our setup arrival window.

**What Happens Next**

Every Cheese To Share booking is food + presentation + production + experience.

We're already sourcing your cheeses, confirming the styling pieces, and assigning your dedicated server.

If anything changes on your end (date, guest count, venue), just reply to this email and we'll handle it with you.

A few quick reminders so the day runs clean:

- Outside food cannot be added to the grazing table (if ordered) without prior approval — this is how we protect the presentation.
- Please flag any guest allergies in advance! Even when a dish isn't made with an allergen, trace amounts may be present.
- The venue needs to allow our team access for the full setup window on event day.

We can't wait to share with you!

Warm regards,
Cheese To Share
(407) 494-4263
info@cheesetoshare.us
https://www.cheesetoshare.us/

---

## 02 · BALANCE DUE — EMAIL + SMS

### 02a · Email

**Subject:** Your remaining balance is due — {{contact.cts_event_date}}
**Preview text:** Two weeks out. Your guest count locks in 7 days.

Hi {{contact.first_name}}!

Your event is two weeks away — close enough that we're already thinking about the cheese selection.

Your remaining balance is now due.

**Remaining Balance**
Amount Due: {{contact.cts_balance_amount}}
Payment Link Expires: {{contact.cts_balance_link_expires_at}}

Pay Securely Here → {{contact.cts_balance_payment_url}}

**A Quick Heads-Up**

Your final guest count locks in 7 days ({{contact.cts_guest_count_lock_date}}). If you need to adjust the number of guests, this is the window. Increases are possible if inventory allows; decreases after the lock date don't reduce the price.

**What Happens After Payment**

Once your balance clears, you'll get a quick receipt. Then a final details email about a week out with your setup arrival window, and everything we'll need from your venue on the day.

If anything has changed about your event (date, address, head count), reply to this email and we'll handle it with you.

Warm regards,
Cheese To Share
(407) 494-4263
info@cheesetoshare.us
https://www.cheesetoshare.us/

### 02b · SMS

```
Hi {{contact.first_name}}! Two weeks out from Cheese To Share catering your event. Your remaining balance is now due.
Payment link was sent to your email!
Luis, Cheese To Share
```

---

## 03 · BALANCE PAID — EMAIL ONLY

**Subject:** You're all set for CTS Catering
**Preview text:** Payment received. We'll see you soon.

Hi {{contact.first_name}}!

Thank you! Your final payment is in, and your booking is fully paid.

**Payment Summary**
Reservation #: {{contact.cts_reservation_number}}
Total: {{contact.cts_total_amount}}
Deposit: {{contact.cts_deposit_amount}}
Balance: {{contact.cts_balance_amount}}
Status: Paid in full

About a week before your event, we'll send your final details — setup arrival window, server name, and everything we'll need from your venue on the day.

The spread is yours. We can't wait to bring the experience to you.

Warm regards,
Cheese To Share
(407) 494-4263
info@cheesetoshare.us
https://www.cheesetoshare.us/

---

## 04 · EVENT WEEK — FINAL DETAILS — EMAIL ONLY

**Subject:** Event week: Your Cheese To Share catering details
**Preview text:** Everything we'll need on the day.

Hi {{contact.first_name}}!

One week out. Here's everything in one place.

**Your Event**
Reservation #: {{contact.cts_reservation_number}}
Pillar: {{contact.cts_pillar}} — {{contact.cts_package_tier}}
Date: {{contact.cts_event_date}}
Time: {{contact.cts_event_time}}
Address: {{contact.cts_event_address}}
Final Guest Count: {{contact.cts_guest_count}}

**Your Setup Window**

Our team arrives several hours ahead of your event start time for setup. Production duration is as specified on the website for your package, so the spread is finished, styled, and ready before your first guest walks in.

**What We'll Need From You on the Day**

- A clear surface or area where the grazing table / station / cheeseboard will be.
- Venue access during the full setup window.
- Power access if your package includes lighting or live stations.
- A point of contact on site (you or someone you designate) who can let our team in and answer quick setup questions.

**Quick Reminders**

- Outside food cannot be added to the grazing table without prior approval — it protects the presentation.
- If a guest has an allergy we haven't been told about yet, reply now so we can adjust. Trace amounts of nuts, dairy, gluten, and other allergens may be present.
- Cheese To Share equipment (boards, trays, stands, florals, backdrops, lighting) belongs to us — damage, loss, or stained items are charged at repair or replacement cost.

**If Anything Changes**

Reply to this email or call us at (407) 494-4263. The sooner we know, the cleaner the day runs.

This is the one people will be talking about after — and that's exactly the point.

Warm regards,
Cheese To Share
(407) 494-4263
info@cheesetoshare.us
https://www.cheesetoshare.us/

---

## 05 · DAY BEFORE — SMS ONLY

```
Hi {{contact.first_name}} — tomorrow's the day. Our Cheese To Share team will arrive ahead of time for your {{contact.cts_package_tier}} setup.
If anything's changed about venue access or timing, reply here.
Bringing everything to share with you tomorrow.
Luis, Cheese To Share
```

---

## 06 · REVIEW REQUEST — EMAIL + SMS

### 06a · Email

**Subject:** How was the spread, {{contact.first_name}}?
**Preview text:** Two minutes of your time — and it helps us a lot.

Hi {{contact.first_name}}!

We hope it was the one people are still talking about.

If you have a couple of minutes, we'd love a quick review — it's the single biggest thing that helps people find us for their own moments that matter.

Leave a review here: [REVIEW US button → Google review link]

Thank you for trusting us with your day. We'd love to bring the spread to your next one too.

Warm regards,
Cheese To Share
(407) 494-4263
info@cheesetoshare.us
https://www.cheesetoshare.us/

### 06b · SMS

```
Hi {{contact.first_name}} — hope it was the one people are still talking about!
A quick review helps us a lot: [REVIEW US button → Google review link]
If anything wasn't perfect, reply here and we'll make it right.
Thank you! Luis, Cheese To Share
```

---

## Merge Code Reference (GHL — pending namespace correction)

> ⚠️ Doc uses `{{contact.cts_*}}` prefix but custom fields live in **Opportunity** namespace in GHL. Replace prefix with `{{opportunity.*}}` (or GHL equivalent syntax) at email build time.

| Doc merge code | Source | Notes |
|---|---|---|
| `{{contact.first_name}}` | Contact (native) | OK |
| `{{contact.cts_event_date}}` | opportunity.event_date | ISO raw — needs Date Formatter for human-readable |
| `{{contact.cts_event_time}}` | opportunity.event_start_time | Currently same ISO as event_date — needs formatter |
| `{{contact.cts_event_address}}` | opportunity.event_address | OK |
| `{{contact.cts_guest_count}}` | opportunity.guest_count | OK |
| `{{contact.cts_reservation_number}}` | opportunity.order_number | OK |
| `{{contact.cts_services}}` | **NOT MAPPED** — pending decision (tier + addons concat?) |
| `{{contact.cts_total_amount}}` | opportunity.* | Cents stored — needs Math (cents→dollars) for display |
| `{{contact.cts_deposit_amount}}` | opportunity.deposit_paid_dollars | Cents — needs Math |
| `{{contact.cts_balance_amount}}` | opportunity.balance_due_dollars | Cents — needs Math |
| `{{contact.cts_balance_link_expires_at}}` | opportunity.balance_link_expires_at | ISO — needs Date Formatter |
| `{{contact.cts_balance_payment_url}}` | opportunity.balance_payment_url | OK |
| `{{contact.cts_guest_count_lock_date}}` | **NOT MAPPED** — event_date minus 7d (backend pre-compute or GHL Date Formatter) |
| `{{contact.cts_package_tier}}` | opportunity.tier | OK |
| `{{contact.cts_pillar}}` | **NOT MAPPED** — pending CTS taxonomy clarification |



---

## ADDENDUM — Final Mapping Decisions (2026-05-27)

### Backend now pre-computes display fields

Payload from `supabase/functions/_shared/ghl.ts` includes a `display.*` block with human-formatted values. Use these instead of raw `event.*` / `totals_cents.*` in GHL email/SMS templates.

### Email 04 correction

Remove the `Pillar:` line entirely. Pillar concept is dropped — package tier alone is the only product identifier.

Replace:
```
Pillar: {{contact.cts_pillar}} — {{contact.cts_package_tier}}
```
With:
```
Package: {{opportunity.tier}}
```

### Final Merge Code Reference (use these in GHL)

> Custom fields live in **Opportunity** namespace. Use GHL picker — actual syntax may render as `{{opportunity.custom_field.<key>}}` or `{{contact.opportunity.<key>}}` depending on GHL version. Pick from picker, do not hand-type.

| Doc placeholder | GHL field source | Payload path |
|---|---|---|
| `{{contact.first_name}}` | Contact (native) | `customer.name` (parsed) |
| `{{contact.cts_event_date}}` | opportunity.event_date_display | `display.event_date` |
| `{{contact.cts_event_time}}` | opportunity.event_time_display | `display.event_time` |
| `{{contact.cts_event_address}}` | opportunity.event_address | `event.address` |
| `{{contact.cts_guest_count}}` | opportunity.guest_count | `guest_count` |
| `{{contact.cts_reservation_number}}` | opportunity.order_number | `order_number` |
| `{{contact.cts_services}}` | opportunity.tier | `tier` (use `display.services` for consistency) |
| `{{contact.cts_total_amount}}` | opportunity.total_amount_display | `display.total_amount` |
| `{{contact.cts_deposit_amount}}` | opportunity.deposit_amount_display | `display.deposit_amount` |
| `{{contact.cts_balance_amount}}` | opportunity.balance_amount_display | `display.balance_amount` |
| `{{contact.cts_balance_link_expires_at}}` | opportunity.balance_link_expires_display | `display.balance_link_expires` |
| `{{contact.cts_balance_payment_url}}` | opportunity.balance_payment_url | `balance_payment_url` |
| `{{contact.cts_guest_count_lock_date}}` | opportunity.guest_count_lock_date_display | `display.guest_count_lock_date` |
| `{{contact.cts_package_tier}}` | opportunity.tier | `tier` |
| `{{contact.cts_pillar}}` | **DROPPED** | n/a |

### New GHL custom fields to create (Opportunity namespace)

Existing 14 fields stay. Add 8 new display fields so GHL receives pre-formatted strings:

| Field name (GHL) | Field key | Type | Folder |
|---|---|---|---|
| Event Date (Display) | `event_date_display` | Single Line | CTS Event |
| Event Time (Display) | `event_time_display` | Single Line | CTS Event |
| Event DateTime (Display) | `event_datetime_display` | Single Line | CTS Event |
| Guest Count Lock Date | `guest_count_lock_date_display` | Single Line | CTS Event |
| Balance Link Expires (Display) | `balance_link_expires_display` | Single Line | CTS Payment |
| Total Amount (Display) | `total_amount_display` | Single Line | CTS Payment |
| Deposit Amount (Display) | `deposit_amount_display` | Single Line | CTS Payment |
| Balance Amount (Display) | `balance_amount_display` | Single Line | CTS Payment |

After creating, map them in both **Create Opportunity** (Not Found branch) and **Update Opportunity** (Found branch) actions, sourced from corresponding `display.*` paths in the inbound webhook.

### Email handler routing — final

| Trigger | Channel(s) | Sender | Stage transition | Tag |
|---|---|---|---|---|
| deposit_paid | (Email 01) | CTS SMTP | — (Create at Paid on Not Found) | `deposit-paid` |
| staff_assigned | none | — | → Assigned | `staff-assigned` |
| balance_link | Email 02 + SMS 02b | GHL | — | `balance-link-sent` |
| balance_paid | (Email 03) | CTS SMTP | → Balance Paid | `balance-paid` |
| order_cancelled | none | — | Status → Lost | `cancelled` |
| reminder_7d | Email 04 | GHL | — | `reminder-7d-sent` |
| reminder_1d | SMS 05 | GHL | — | `reminder-1d-sent` |
| event_completed | none | — | → Delivered + Status Won | `completed` |
| post_event_thanks_email | Email 06 + SMS 06b | GHL | — | `review-requested` |
| remarketing_email | (TBD copy) | GHL | — | `remarketing-sent` |

### Deferred / pending

- `remarketing_email` copy — Cristian to draft separately
- SPF/DKIM verification on `info@cheesetoshare.us` for GHL sending domain — Cristian to handle before live tests
- Not Found branch keeps single-action design (Create Opp → END). Webhook delivery reliability relies on CTS retry logic in calling Edge Functions, not on GHL mini-router.

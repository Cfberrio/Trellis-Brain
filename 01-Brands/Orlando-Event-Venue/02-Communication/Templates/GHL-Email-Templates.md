---
brand: Orlando-Event-Venue
area: communication
subarea: templates
note_type: template
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Five GHL templates rebuilt on the OEV email design system 2026-08-26. Source HTML held outside the vault; copy is verbatim from the GHL originals."
owner: Luis
last_updated: 2026-08-26
sensitivity: internal
related_systems:
  - ghl
  - email
hub_role: leaf
tags:
  - oev
  - ghl
  - email
  - templates
---

# OEV GHL Email Templates

## Parent
- [[01-Brands/Orlando-Event-Venue/02-Communication/Communication-Home|OEV Communication Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/02-Communication/Email-Design-System|OEV Email Design System]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Visual-Identity|OEV Visual Identity]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Post-Booking-Email-Sequence|Post-Booking Email Sequence]]
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Access-Codes-and-Guest-Report|Access Codes and Guest Report]]

## Purpose
The five GHL-side emails, rebuilt 2026-08-26 on the OEV email design system. These are the templates GHL sends. The Supabase edge functions are a separate channel documented in [[01-Brands/Orlando-Event-Venue/02-Communication/Email-Design-System|Email Design System]].

**Copy in all five is byte-identical to the GHL originals.** Only HTML and CSS changed. Every visible line was diffed after rebuild.

---

## The Five

| # | Template | Trigger | Accent | Primary CTA |
|---|---|---|---|---|
| 1 | Your Event Is **Confirmed** | Booking approved | `accent` | Event Page link |
| 2 | Your Remaining Payment Is **Due** | Balance due | `amber` on hero, `accent` on button | Complete Final Payment |
| 3 | Let Us Confirm a Few **Details** | ~1 month out | `accent` | Open Your Event Page |
| 4 | Your Event Is **Tomorrow** | 1 day out | `accent` | Open Your Event Page |
| 5 | One Last **Step** | Reservation ended | `accent` | Open Your Event Page |

The bold word is the second line of the two-tone display headline — `ink` over `accent`, mirroring the logo split. Display sizes escalate with urgency: 32px on the balance email, 42px on "Tomorrow", 44px on "One Last Step".

---

## Merge Fields Used

All five carry the standard six-row For Reference block:
`{{contact.oev_reservation_number}}`, `{{contact.oev_event_date}}`, `{{contact.oev_event_start_time}}`, `{{contact.oev_event_end_time}}`, `{{contact.oev_event_type}}`, `{{contact.oev_booking_type}}`, `{{contact.oev_number_of_guests}}`

Plus `{{contact.first_name}}` in every greeting.

Balance email only:
`{{contact.oev_balance_payment_url}}`, `{{contact.oev_balance_amount}}`, `{{contact.oev_balance_due_date}}`, `{{contact.oev_balance_link_expires_at}}`

Day-before email also renders `{{contact.oev_event_start_time}}` inline in the door-code timing paragraph.

---

## GHL-Specific Rules

### Paste into a Custom HTML block, never the rich-text editor
The rich-text editor injects `padding-left: 0px !important` on every element, sometimes eight times on one tag, and forces `font-family: verdana` onto every `<p>`. The originals were carrying roughly 200 of these. That is what made them look broken.

### Buttons need a wrapping `<div>`
GHL strips styles off `<a>` tags on save. Put the button look on a `<div>` — background, `border-radius: 999px`, padding, `box-shadow` — and let the `<a>` inside carry only `display: block` and color. The pill survives; the whole surface stays clickable.

```html
<div style="display:inline-block;background:#0284C7;border-radius:999px;padding:16px 46px;box-shadow:0 4px 12px rgba(2,132,199,.35);text-align:center;">
  <a href="{{merge_field}}" style="display:block;color:#FFFFFF;text-decoration:none;font-size:16px;font-weight:bold;letter-spacing:1.5px;text-transform:uppercase;font-family:Arial,Helvetica,sans-serif;line-height:1;">Label</a>
</div>
```

### Lists must be tables, not `<ul>`
GHL and Outlook both mangle list padding. Render bullets as a two-column table: a 20-22px cell holding `&bull;` in `accent`, and a content cell. Used in the day-before email (6 items) and the closeout email (7 items).

### Numbered lists already in the copy stay in the copy
The one-month check-in reads "1. Bar service", "2. Audio and visual services", "3. Additional services". Those numerals are part of the approved text, so the template does **not** add numeral chips. Adding chips would render "1" twice.

---

## Per-Template Notes

### 2 — Your Remaining Payment Is Due
- `{{contact.oev_balance_amount}}` renders at 38px display italic in `amber`. In the original it was 18px, buried in a table row. It is the number the email exists for.
- The fallback URL sits in a white inset box with a light-blue border, `word-break: break-all`, 11px. Stripe `cs_live_` URLs run ~450 characters and destroy any module that renders them as flowing text.
- A black body module was tried here and rejected. See the rhythm rules in [[01-Brands/Orlando-Event-Venue/02-Communication/Email-Design-System|Email Design System]].

### 4 — Your Event Is Tomorrow
- The whole Event Page block — intro, button, and the six-item list — sits in one `accentDeep` drenched module. The email has one job.
- Contains an em dash and straight quotes around `"Access Not Available Yet"`. Both are in the approved copy and stay. The general OEV writing rule against em dashes does not license editing already-approved text.

### 5 — One Last Step
Two CTAs with deliberate hierarchy:
- **Guest Report** — drenched `accentDeep` module, white button. It blocks reservation closeout, so it wins.
- **Google review** — white module, `accent` button. Present, clearly second.

The Google review link (`https://g.page/r/CU-yUA0El90UEAE/review`) belongs here by design. It also lives on the Event Page and the website homepage. This is the centralized review channel, not an oversight.

---

## Open Item: Duplicate Balance Emails

Template 2 and the Supabase edge function `create-balance-payment-link` send the same message through different channels. If both automations are live, the guest receives two balance-due emails.

Not yet verified which one fires in production. Confirm before enabling template 2.

---

## Copy Drift Warning

[[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Post-Booking-Email-Sequence|Post-Booking Email Sequence]] documents a 2026-05-27 version of the sequence whose copy no longer matches what these five templates send. Subject lines, step numbering, and body text have all moved since.

That note remains the canonical record of *sequence logic* — triggers, channel matrix, operational rules. It is **not** current for *copy*. For copy, the authority is the ClickUp spec doc "OEV POST BOOKING COMMUNICATIONS" and the live templates.

Reconciling the two is an open task.

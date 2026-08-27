---
brand: Orlando-Event-Venue
area: communication
subarea: email
note_type: manual
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "Email rebrand executed 2026-08-26. Source module: OEV-PROJECT/supabase/functions/_shared/email-layout.ts (commit 8a60d20)."
owner: Luis
last_updated: 2026-08-26
sensitivity: internal
related_systems:
  - email
  - ghl
  - website
  - payments
hub_role: leaf
tags:
  - oev
  - email
  - design-system
---

# OEV Email Design System

## Parent
- [[01-Brands/Orlando-Event-Venue/02-Communication/Communication-Home|OEV Communication Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Visual-Identity|OEV Visual Identity]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Language-Rules|OEV Language Rules]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/OEV-Communication-Manual|OEV Communication Manual]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/GHL-Email-Templates|OEV GHL Email Templates]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Post-Booking-Email-Sequence|Post-Booking Email Sequence]]
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Automations|GHL Automations]]

## Purpose
The rendering layer for every guest-facing OEV email. Defines the module vocabulary, the shared code module, and the one rule that governs the whole system.

**This note owns how emails look. It never owns what they say.**

---

## The Governing Rule

> Visible copy must be byte-identical to either the ClickUp spec doc "OEV POST BOOKING COMMUNICATIONS" or the pre-redesign original code. Design carries emphasis. Wording never changes.

This rule exists because it was broken. The first two redesign passes (v1, v2) rewrote marketing copy while restyling — invented headlines, reworded CTAs, added phrases nobody approved. v3 restored every word and kept only the new visual system.

Two pre-approved exceptions, both from before the rebrand:
1. `cancel-booking` contact info: placeholder `(407) 555-0123` / `orlandoglobalministries@gmail.com` replaced with the real venue contacts.
2. Event-type capitalization formatting.

### How to verify you did not drift
Render the template, strip tags, diff the visible text against the source copy. Do not eyeball it, and do not trust a previously-rendered preview file — one stale render harness during the 2026-08-26 pass showed old invented copy while the real source was already correct. The harness lied; the diff did not.

---

## Architecture

Single shared module: `supabase/functions/_shared/email-layout.ts`.

Every edge function imports it and composes an email from builder functions that each return an HTML string. No template engine, no external CSS, no webfonts. Table-based and fully inline-styled for Gmail, Outlook, and Apple Mail.

### Shell
`emailShell({ title, preview, body, ... })` wraps everything: hidden preheader, black header with logo, 600px column of stacked modules, black footer with the contact block.

### Modules
Each returns a full shell row (`<tr><td>...</td></tr>`). Stack them with `gap()` between.

| Builder | Ground | Use |
|---|---|---|
| `heroModule` | `softBlue` | Opening statement. Display type, optional badge |
| `textModule` | White, bordered | Running copy |
| `colorModule` | `accent` drenched | One loud statement, white type |
| `referenceModule` | `softBlue` | The "For Reference" block that closes booking emails |
| `stepsRow` | `accentDeep` | Numbered icon steps |
| `venueCard` | `ink` | Address and directions |

### Type and badges
- `displayTitle(text)` — giant condensed italic uppercase, the identity carrier.
- `displayTitleDuo(top, bottom)` — two-tone, `ink` over `accent`. Mirrors the logo's own ORLANDO / EVENT VENUE split.
- `burst(value)` — solid pill for the one number that matters.
- `ticket(label, value)` — dashed badge for codes the guest must type.
- `numberedList(items)` — big blue numerals beside each item.

### Buttons
`primaryButton`, `invertedButton`, `secondaryButton`, `stackButtons`, `linkButton`.

`linkButton(url)` renders the URL itself as the label — it adds emphasis without inventing a CTA phrase the spec does not contain.

---

## Rhythm Rules

- Modules alternate ground. Never two identical grounds adjacent unless a white module separates them.
- **Black appears only in the header and footer.** A black body module was tried on the balance-due email and rejected: it broke the ritmo of the other templates and read as a different brand.
- Gap between modules is 12px. Radius is 30px on body modules, 22px on the footer, 18px on the header.
- One card depth. Never nest a card inside a card.
- No photography. Type and color carry the design.

## Known Limitation
`fallbackLinks()` hardcodes plural phrasing ("buttons", "these links"). Correct for `send-discount-email`. Wrong for `create-invoice`, `create-addon-invoice`, and `create-balance-payment-link`, whose originals use singular. Those three bypass the helper and inline the singular phrasing directly. Do not "fix" them by routing them through the helper — that would change copy.

## Long URLs
Stripe `cs_live_` checkout URLs run ~450 characters. Rendered as plain text on a colored ground they are unreadable and blow out the module. The pattern: put the URL in a white inset box with a light border, `word-break: break-all`, 11px, accent-colored. High contrast, and it contains the string instead of letting it bleed across the color.

## SMTP Gotcha
`denomailer` 1.6.0's quoted-printable encoder turns whitespace-only lines into a literal `=20` that renders as visible junk. Every template passes through `sanitizeForSmtp()` before `client.send()`, which strips trailing whitespace per line.

**Never minify these templates.** Whitespace *between* tags is semantically significant. Collapsing `>\s+<` glued `<strong>Email:</strong>` to the link that followed it and visually broke the cancellation email during the 2026-08-26 test pass.

---

## Assets
Logo referenced by every email: `https://orlandoeventvenue.org/email/logo-dark.png` — verified live (HTTP 200, `image/png`) on 2026-08-26. It is the only remote asset the system loads.

---

## Migrated Functions

Eleven guest-facing edge functions migrated 2026-08-26:

| Function | Email |
|---|---|
| `send-booking-confirmation` | We Received Your First Payment |
| `send-balance-confirmation` | Your Event Is Fully Paid |
| `send-external-booking-confirmation` | Your Orlando Event Venue Booking Is Confirmed |
| `send-internal-booking-reminders` | Your Event Access Page |
| `send-guest-feedback` | Thank You for Hosting |
| `cancel-booking` | Booking Cancelled |
| `create-invoice` | Invoice |
| `create-addon-invoice` | Additional Services Invoice |
| `stripe-webhook` | Payment Confirmation (customer receipt only) |
| `create-balance-payment-link` | Balance Payment Due |
| `send-discount-email` | Event Planning Kit sequence, E1 / E2 / E3 |

Scope discipline held on two of these:
- `stripe-webhook`: only the customer receipt template changed. The two internal notification templates and **all** webhook logic — signature verification, idempotency, state transitions — were untouched.
- `send-internal-booking-reminders`: only `buildReminderHTML` changed. The GHL plain-text path was untouched.

### Test pass
Thirteen renders sent to the internal inbox 2026-08-26 with `[TEST NN/13]` subject prefixes. All thirteen delivered. **These were local renders with sample data, not sends from deployed functions.**

### Deploy status
Commit `8a60d20` is pushed to `main` and **not published**. Remaining pipeline per the repo's CLAUDE.md: confirm Lovable sync, run the `/pre-deploy` gate, `deploy_project`, then verify with a real `curl` against `orlandoeventvenue.org`.

Reminder that has bitten this repo before: a push does not change production, and `orlandoeventvenue.com` is a parked lander that answers 200 and fools health checks. Verify against `.org`.

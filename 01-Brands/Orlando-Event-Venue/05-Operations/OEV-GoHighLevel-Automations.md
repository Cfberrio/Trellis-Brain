---
brand: Orlando-Event-Venue
area: operations
note_type: manual
status: active
used_for_ai: true
owner: Luis
last_updated: 2026-04-23
sensitivity: internal
---

# OEV GoHighLevel Automations

## Parent
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Operating-System|OEV GoHighLevel Operating System]]

## Related
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-Admin-Command-Center|OEV Admin Command Center]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Communication-Home|OEV Communication Home]]
- [[01-Brands/Orlando-Event-Venue/00-Brand-Core/Brand-Home|OEV Brand Home]]

## Purpose
Documents the confirmed automation workflows and pipeline stage configuration active in GoHighLevel for Orlando Event Venue. This note is the operational reference for what GHL automates — covering lifecycle stage movement, client communication sequencing, payment reminders, and internal notifications.

## Confirmed Pipeline Stages
These are the confirmed stages in the OEV GHL pipeline, in order:

1. Pending
2. Confirmed
3. Pre-Event Ready
4. In Progress
5. Post-Event
6. Closed

## Automation Inventory

### 1. Lifecycle / Pipeline Sync Automation
**What it does:** Syncs and updates lifecycle or pipeline stage as booking status changes.

Confirmed details:
- Trigger tied to OEV lifecycle status changes
- Pipeline and lifecycle stages map the full operational arc from initial booking through event closeout
- Screenshots show stage update / sync behavior
- Specific field names and branch labels are partially unreadable — needs later confirmation

**Certainty level:** Confirmed from screenshots. Exact filter field naming needs confirmation.

---

### 2. Host Report Automation
**What it does:** Sends communication based on where the booking stands relative to the host report step.

Confirmed details:
- Trigger tied to host report step change
- Three confirmed branches:
  - `pre_start` — email action triggered before event begins
  - `during_event` — email action triggered during event window
  - `post_event` — email triggered after event; post_event branch appears to also include an SMS step following the email
- Exact subject lines and message content not confirmed — needs later documentation

**Certainty level:** Branch structure confirmed from screenshots. Message content and exact trigger field conditions partially unreadable.

---

### 3. Balance Payment Reminder Automation
**What it does:** Sends a multi-step reminder sequence when a balance payment is due or outstanding.

Confirmed details:
- Trigger tied to balance payment URL availability or status change
- Sequence tracks attempt count — first, second, and third reminder attempts visible in screenshots
- Both email and SMS are used across the reminder sequence
- Branch logic visible in screenshots but specific wording is partially unreadable in some areas

**Certainty level:** Sequence structure and multi-channel nature confirmed from screenshots. Exact timing intervals and branch wording need later confirmation.

---

### 4. Post-Event Cleaning Report Completed Notification
**What it does:** Triggers an internal notification when the post-event cleaning report is marked complete.

Confirmed details:
- Condition tied to cleaning report completion status
- Fires after post-event logic has run
- Functions as an internal operational notification, not a client-facing message

**Certainty level:** Confirmed from screenshots. Exact recipient and notification channel partially unreadable — needs later confirmation.

---

### 5. Bar Service Vendor Assignment Notification *(to be built)*
**What it does:** Notifies the bar service vendor (a GHL staff account, third-party in reality) when they are assigned to a booking. Mirrors cleaning staff assignment pattern exactly.

**Trigger:** `oev_bar_vendor_assigned` field changes from empty → vendor selected by admin.

**Actions:**
1. Email to bar vendor → event date, time window, package, guest count, client name, venue address
2. SMS to bar vendor → short assignment confirmation with date and time
3. Auto-create task in GHL assigned to bar vendor: **"Contact client — [client first name] — [event date]"**

**Vendor access:** Bar vendor has a limited account in the **Staff Dashboard** (custom built) — not a GHL user account. They see only their assigned bookings and their task queue. They cannot see the pipeline, other clients, or payment records. GHL fires the notification; the Staff Dashboard is where the vendor operates.

**Customer Contacted label/task:**
- GHL auto-creates a task in the Staff Dashboard assigned to the bar vendor: "Contact client — [client name] — [event date]" — due 24 hours after assignment
- Vendor logs into Staff Dashboard, sees the task, contacts the client, marks it complete
- Task completion → GHL trigger fires → field `oev_bar_customer_contacted` flips to `true` → syncs to Admin Dashboard
- Admin sees on the booking record: **`✓ Customer Contacted`** (green) or **`⚠ Awaiting Vendor Contact`** (yellow)
- This label is the coordination confirmation signal. Admin does not need to manually verify.

**Pre-Event Ready gate:** Booking cannot advance to `Pre-Event Ready` in the Admin Dashboard if `oev_bar_package ≠ None` and `oev_bar_customer_contacted = false`.

**Certainty level:** Pattern derived from cleaning staff assignment system. Field names, task bridge between GHL and Staff Dashboard, and trigger logic need confirmation against the actual build.

---

## Notes on Certainty

**Confirmed from user:**
- GHL is used in OEV for email, SMS, pipelines, and operational automations
- Pipeline stages: Pending, Confirmed, Pre-Event Ready, In Progress, Post-Event, Closed
- Host report automation exists with pre_start / during_event / post_event branches
- Balance payment reminder sequence exists
- Post-event cleaning report notification exists

**Confirmed from screenshots:**
- Lifecycle sync automation is active
- Host report branches visible with email actions; post_event branch includes SMS
- Balance reminder sequence shows attempt tracking and multi-channel delivery
- Cleaning report completion triggers an internal notification step

**Visible but partially unreadable — needs later confirmation:**
- Exact filter field names and values in lifecycle sync automation
- Exact subject lines and message body for host report automation
- Exact timing intervals in balance reminder sequence
- Specific branch wording in balance reminder
- Recipient and notification channel for cleaning report notification

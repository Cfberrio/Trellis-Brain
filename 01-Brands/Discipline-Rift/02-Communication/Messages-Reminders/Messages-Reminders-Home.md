---
brand: Discipline-Rift
area: communication
subarea: email
note_type: system
status: active
canonical: true
used_for_ai: true
source_type: curated
sensitivity: internal
hub_role: hub
last_updated: 2026-09-14
up:
  - "[[01-Brands/Discipline-Rift/02-Communication/Communication-Home]]"
down:
  - "[[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Parent-New-Messages-1]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Parent-New-Messages-2]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Coach-New-Messages-1]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Coach-New-Messages-2]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Messages-Reminders-Design-Spec]]"
related:
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Communication-Engine]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library]]"
---

# Messages Reminders — unread dashboard messages (parents + coaches)

**Live since:** 2026-09-11 · **Owner:** backend (Supabase edge functions + pg_cron) · **Sender:** GoHighLevel
**ClickUp:** Discipline Rift doc → NOTIFICATIONS → Messages Reminders

## What it does

Emails a parent or a coach when they have **unread messages in the Discipline Rift dashboard**. Coaches write in the dashboard; most parents never open it. This closes that gap without becoming spam.

## The rules

1. **Maximum two emails per cycle.**
   - **Email 1** — as soon as new unread messages appear (next hourly run).
   - **Email 2** — six *business* hours later, only if still unread. Then silence.
2. **Business hours = 7:00 AM – 9:00 PM Orlando.** The night does not count toward the 6 hours and nothing is sent at night. Example: coach writes Monday 5 PM → Email 1 at 5:05 PM → Email 2 Tuesday 9:05 AM.
3. **"Read" = the person opened that chat in the dashboard.** Opening the dashboard without opening the thread does not count.
4. **A newer message restarts the cycle** (new Email 1). A newer message *while Email 2 is still pending* folds into Email 2 — never two Email 1s an hour apart.
5. **Safety cap: 2 emails per person per rolling 24 h.** A capped email is delayed, never dropped.
6. **Only teams with status `ongoing` or `closed`.** Pre-season (`open`), archived, cancelled teams never notify anyone.
7. **Only messages from the last 7 days** can start a cycle.
8. Same rules for coaches — per coach (head and each assistant have their own read state).

## Schedule

| Job | Runs | Window |
|---|---|---|
| `parent-message-notifications` | every hour at :05 | 7 AM – 8 PM Orlando |
| `coach-message-notifications` | every hour at :10 | 7 AM – 8 PM Orlando |

## GHL workflows (GHL only renders — no logic there)

- `DR | Webhook - Parent New Messages`
- `DR | Webhook - Coach New Messages`

Shape of both:

```
Inbound Webhook  →  Create Contact (email, first name, last name)  →  If/Else stage = 1
                                                                        ├─ Send Email 1
                                                                        └─ Send Email 2
```

**Never add** Wait, Goal, "if opened", tags or contact filters in GHL. Every decision (who, when, which stage, dedupe, cap) is taken in the database and logged in `message_notification_delivery`.

## Merge tags available (`{{inboundWebhookRequest.<field>}}`)

`stage`, `parent_first_name`, `coach_first_name`, `children_names` ("Sofia and Mateo" / "your player"), `children_verb` (is/are), `unread_count`, `messages_word` (message/messages), `parent_count`, `parents_word`, `team_name`, `team_names` ("A and B"), `latest_message_preview`, `latest_message_at`, `teams_html` (table team · coach · unread), `parents_html` (table parent · team · unread).

## The four emails

- [[Parent-New-Messages-1]] — Parent, Email 1 (*New Message*)
- [[Parent-New-Messages-2]] — Parent, Email 2 (*Reminder*, last)
- [[Coach-New-Messages-1]] — Coach, Email 1 (*Coach Inbox*)
- [[Coach-New-Messages-2]] — Coach, Email 2 (*Reminder*, last)

## Where things live

- Templates (HTML): `brand-kit/email/transactional/message-notification-{parent,coach}-{1,2}.html`
- Backend rules: `supabase/functions/_shared/message-notification.ts`
- Spec: `docs/superpowers/specs/2026-09-11-message-notifications-design.md`
- Delivery log (who got what, when, why): table `message_notification_delivery`

## Turn it off

```sql
select cron.unschedule('parent-message-notifications');
select cron.unschedule('coach-message-notifications');
```

Related: [[Communication-Home]] · [[DR-Communication-Engine]] · [[07-Parent-Assistance-N8N]]

---
brand: Discipline-Rift
area: communication
subarea: email
note_type: system
status: active
canonical: false
used_for_ai: true
source_type: curated
sensitivity: internal
hub_role: leaf
last_updated: 2026-09-14
up:
  - "[[01-Brands/Discipline-Rift/02-Communication/Messages-Reminders/Messages-Reminders-Home]]"
related:
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-Email-Design-Spec]]"
---

# Message Notifications — design spec (technical)

Mirror of `disciplinerift/docs/superpowers/specs/2026-09-11-message-notifications-design.md`. Repo copy is the source of truth. Plain-language version: [[Messages-Reminders-Home]].

**Date:** 2026-09-11 · **Status:** LIVE

## Goal

Email a parent or coach when they have unread dashboard messages, without ever sending the same notification twice. Replaces the Vercel cron `send-pending-message-notifications` (disabled 2026-06-24).

## Rules (business, decided by Domis)

1. **Two emails per cycle, maximum.** Stage 1 when new unread messages appear. Stage 2 six *business* hours later if still unread. Then silence.
2. **Business hours:** 07:00–21:00 America/New_York. The 21:00→07:00 gap does not count toward the 6 h, and nothing is sent inside it.
3. **A cycle is anchored to the newest unread message.** Same newest message ⇒ same cycle ⇒ no new email. A newer message ⇒ new cycle ⇒ stage 1 again.
4. **"Read"** = a `message_read_status` row exists for (message, recipient). Opening the dashboard without opening the thread is not "read".
5. **Safety cap:** at most 2 emails per recipient per rolling 24 h. A blocked send is *delayed*, not dropped.
6. **Fold-in:** while stage 1 is sent and stage 2 pending, a newer message does NOT open a new cycle; stage 2 reports everything unread.
7. **Look-back:** only messages created in the last 7 days can start a cycle.
8. Same rules for coaches, per coach (head and each assistant have their own read state and cycle).
9. **Team status allowlist (both roles):** only messages on teams with `status in ('ongoing','closed')` count.

## Unread definitions (mirror the live RPCs, run as service_role)

- Parent P: `message.sender_role='coach' and parent_id=P and deleted_at is null` and no `message_read_status(message_id, parent_id=P)`.
- Coach C: `message.sender_role='parent' and deleted_at is null` and team has a `session` with `coach_id=C or assistant_coach_id=C or assistant_coach_id_2=C` and no `message_read_status(message_id, coach_id=C)`. Coach must be `is_active` and not deleted.

## Data

Table `message_notification_delivery` — event_key unique, pending/sent/rejected/blocked/unknown, claim + finish RPCs, admin-read RLS, service-role writer.

```
event_key        message_notification:<role>:<recipient_id>:<cycle_message_id>:<stage>
recipient_role   'parent' | 'coach'
recipient_id     uuid
cycle_message_id uuid  -- newest unread message when the cycle opened
stage            1 | 2
```

## Decision per recipient (pure, unit-tested)

```
U = unread messages (≤7 days old, team ongoing/closed); if empty → skip
newest = max(created_at) in U
open = latest cycle for recipient with stage1 status='sent'
if open exists and open.stage2 not sent:  cycle = open.cycle_message_id   (fold-in)
else:                                     cycle = newest.id
if not stage1.sent:                      cap(24h) ≥ 2 → skip; else send stage 1
elif not stage2.sent and businessHours(stage1.sent_at, now) ≥ 6h:
                                         cap(24h) ≥ 2 → skip; else send stage 2
else skip
```

## Edge functions

- `parent-message-notifications` → `GHL_PARENT_MESSAGES_WEBHOOK`
- `coach-message-notifications` → `GHL_COACH_MESSAGES_WEBHOOK`
- `_shared/message-notification.ts` (pure core, bun tests), `-dispatch.ts`, `-load.ts`, `-handler.ts`

Auth `x-dr-secret` = `DR_EDGE_SECRET` (vault). Body: `{ dry_run, parent_id | coach_id, limit, now, test_mode }`. `DR_MESSAGE_NOTIFY_TEST_RECIPIENT` + `test_mode` redirects ONE email under a `TEST-OVERRIDE:` key.

## Cron

`parent-message-notifications` `5 * * * *`, `coach-message-notifications` `10 * * * *`, both guarded to Orlando hours 07..20.

## GHL

Inbound Webhook → **Create Contact** (email, first/last name) → If/Else on `stage` → two Send Email nodes. Without the Create Contact step, Send Email has no recipient and dies silently while GHL still answers 200 (learned 2026-09-11).

## Manual ops

```sql
-- invoke like the cron does
select net.http_post(
  url := 'https://hvgcxtawrditxvgvqfxb.supabase.co/functions/v1/parent-message-notifications',
  headers := jsonb_build_object('Content-Type','application/json','x-dr-secret',
    (select decrypted_secret from vault.decrypted_secrets where name='DR_EDGE_SECRET' limit 1)),
  body := jsonb_build_object('dry_run', true), timeout_milliseconds := 120000);
-- read the reply
select status_code, content from net._http_response order by id desc limit 1;
-- health
select recipient_role, stage, status, count(*) from message_notification_delivery
 where created_at > now() - interval '1 day' group by 1,2,3 order by 1,2,3;
```

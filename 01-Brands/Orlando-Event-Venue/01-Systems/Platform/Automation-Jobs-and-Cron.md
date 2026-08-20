---
brand: Orlando-Event-Venue
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "OEV-PROJECT docs/automation/ARQUITECTURA-WEBHOOKS-Y-CRON.md, AUDITORIA-COMUNICACIONES-JULIO-2026.md, SPEC-CINTURONES-SEGURIDAD-COMMS.md, PREVENCION-HOST-REPORT-ISSUE.md"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - oev
  - platform
  - automation
---

# Automation, Jobs and Cron

## Parent
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Platform-Home|OEV Platform Home]]

## Related
- [[01-Brands/Orlando-Event-Venue/01-Systems/Platform/Booking-Status-Model|Booking Status Model]]
- [[01-Brands/Orlando-Event-Venue/05-Operations/OEV-GoHighLevel-Automations|OEV GoHighLevel Automations]]
- [[01-Brands/Orlando-Event-Venue/02-Communication/Templates/Booking-Calendar-Sequence|Booking Calendar Sequence]]

## The rule everyone gets wrong first
**`supabase/config.toml` does not run crons in this project.** The `[functions.x.cron]` blocks are decorative leftovers. The only thing that runs on a schedule is **`pg_cron`**, declared with `cron.schedule(...)` inside a SQL migration.

If a recurring task is added only to `config.toml`, it silently never runs. `config.toml` does control `verify_jwt` per function, and that part is real.

## Three layers, never mixed
| Layer | Job | Examples |
|---|---|---|
| 1. Inbound webhooks | Receive external calls in real time | `stripe-webhook`, `ghl-appointment-webhook`, `ghl-update-booking-status` |
| 2. Job producers (schedulers) | Compute *when* something must happen and write it to `scheduled_jobs` | `schedule-balance-payment`, `schedule-host-report-reminders`, `schedule-guest-feedback` |
| 3. Executors (cron) | Run every N minutes and drain what is due | `process-scheduled-jobs` (every 5 min), `daily-health-check`, `process-recurring-invoices` |

Central idea: **almost nothing executes inline**. An external event schedules future work in a table, and a cron empties it when the time comes. If a function fails, the job stays `pending` and is retried — that is the resilience property.

```
External event (Stripe / GHL)
        ▼
  [inbound webhook] → writes bookings, sends emails
        ▼
  [DB trigger on bookings] (lifecycle → pre_event_ready)
        ▼
  [trigger-booking-automation] → 3 schedulers in parallel
        ├── schedule-balance-payment
        ├── schedule-host-report-reminders
        └── schedule-guest-feedback
                 ▼ INSERT scheduled_jobs (pending, run_at = future)
        [pg_cron every 5 min] → process-scheduled-jobs
                 ▼ runs jobs with run_at <= now()
```

## Inbound webhooks
- **`stripe-webhook`** — the important one. Authenticated by Stripe signature (`stripe-signature` + `STRIPE_WEBHOOK_SECRET`), not by a token. Listens to `checkout.session.completed` (95% of the logic) and `checkout.session.expired`. Routes on `metadata.payment_type`: `deposit`, `balance`, `addon_invoice`, `standalone_invoice`.
- **`ghl-appointment-webhook`** — appointments from GoHighLevel / Google Calendar.
- **`ghl-update-booking-status`** — status sync GHL → OEV, with anti-loop protection so a sync does not bounce back.
- Voice and website-form webhooks feed the same intake.

## Scheduled communications currently live
- Deposit and balance reminders.
- 30-day / 7-day / 1-day client reminders (per booking policy).
- **Host report** chain, with the `post_event` step restored to 1 day before event start.
- **`one_hour_report`** (shipped 2026-07-27): job scheduled at event end minus one hour, flips the flag and syncs to GHL. DST-aware Orlando time; past events are skipped.
- Guest feedback / review request.
- Recurring invoices (`process-recurring-invoices`) — required a missing `pg_cron` job to be registered in June 2026 before recurring invoices actually sent.
- Lead-magnet drip — since 2026-08 both follow-ups are measured from email 1 (18h and 36h) and send at 8 AM Orlando time, not fixed hour offsets. See [[01-Brands/Orlando-Event-Venue/01-Systems/Marketing/Lead-Magnet-Event-Planning-Kit|Lead Magnet — Event Planning Kit]].

## Safety belts (July 2026 comms audit)
The July 2026 communications audit produced a safety-belt spec that is now the operating standard:
- 10-day host-report timeout plus a stale `pending_review` check, so a booking cannot sit forever waiting on a human.
- Reschedule recreates host-report jobs for the new event date instead of leaving orphan jobs on the old one.
- Alerting when a confirmation PDF fails, instead of a silent failure.
- Drip protection so a stalled run cannot fire a burst of emails when it recovers.

## Debugging recipes
- List active crons in the DB, then list `scheduled_jobs` with `status = 'pending'` and `run_at < now()` to find stuck work.
- A job that never appears usually means the producer never fired, which usually means the lifecycle never reached `pre_event_ready`.
- A new recurring task = a new `cron.schedule()` in a new migration. Nothing else works.

## Next step
Anything added to the comms matrix must be recorded here and in [[01-Brands/Orlando-Event-Venue/02-Communication/Communication-Home|OEV Communication Home]] on the same day it ships. The July audit exists because the matrix drifted from reality.

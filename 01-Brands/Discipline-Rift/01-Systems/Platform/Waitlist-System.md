---
brand: Discipline-Rift
area: systems
subarea: platform
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "disciplinerift docs/superpowers/specs/2026-06-26-waitlist-reg4-design.md + commits 2026-06-26 → 2026-08-20 (waitlist series)"
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: child
tags:
  - dr
  - platform
  - waitlist
---

# Waitlist System

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Platform-Home|DR Platform Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Team-Status-and-Season-Model|Team Status and Season Model]]
- [[01-Brands/Discipline-Rift/01-Systems/Platform/Registration-and-Checkout-Flow|Registration and Checkout Flow]]
- [[01-Brands/Discipline-Rift/06-DNA/Conversion|DR Conversion DNA]]

## Problem it solves
A full team used to be a hard stop. The parent left, and DR never learned that demand existed at that school. The waitlist converts a "no" into a captured, contactable, ranked queue.

## How it works now
1. **Join** — a parent on a full team joins the waitlist from the same surface, giving their **full name**, contact and student context.
2. **Freed seat detection** — a database trigger fires when a seat is released (refund, removal, expired hold).
3. **Manual invitation** — an admin invites from the queue. There are **no auto-offers and no held seats**.
4. **Claim** — the invited parent receives a branded claim email and completes registration.
5. **Cron safety net** — a scheduled check catches queues that a trigger missed.

## The key decision: manual, not automatic
The original design offered seats automatically and held them. That was replaced by a **manual invitation flow**. Automatic offers to a stale queue burn the parent's trust when the seat is gone or the season has moved on, and holding seats makes a team look full when it is not. A human deciding who to invite is the correct trade at DR's volume.

## Admin surface
The team waitlist is visible inside **Manage Roster**, alongside parent contact columns and a **refund-and-remove** action. Freeing a seat and inviting the next parent is therefore one screen, not three.

## Security note
`waitlist_invite` is revoked from `PUBLIC`, not only from the named roles. Revoking role-by-role left the function reachable; the fix was to revoke from `PUBLIC` and grant explicitly.

## Out of scope in the MVP
Automatic offers, held seats, per-parent expiry windows, and multi-team queue priority. Do not reintroduce them without a decision that says why the manual flow stopped working.

## Commercial reading
The waitlist is the cheapest demand signal DR has. A school with a persistent queue is the strongest possible argument for adding a second team there — better evidence than any survey.

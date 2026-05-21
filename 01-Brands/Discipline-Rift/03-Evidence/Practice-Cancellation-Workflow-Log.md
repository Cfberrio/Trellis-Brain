---
brand: Discipline-Rift
area: evidence
subarea: communication-workflow
note_type: evidence
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "ClickUp Doc 8cqnrff-11677 page 8cqnrff-16037 (PROCESSES / PARENT SMS & EMAILS — SyncUp recording)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
related_systems:
  - ghl
related_notes:
  - "[[../05-Operations/SOPs/Practice-Cancellation-Comms-SOP|Practice Cancellation Comms SOP]]"
hub_role: leaf
---

# Practice Cancellation Workflow — Log + Recording

## Parent
- [[../05-Operations/SOPs/Practice-Cancellation-Comms-SOP|Practice Cancellation Comms SOP]]

## Related
- [[../02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|GHL Marketing + Registration Automations]]

## Purpose
Captured workflow log from a real practice cancellation event. Source of the canonical [[../05-Operations/SOPs/Practice-Cancellation-Comms-SOP|Practice Cancellation Comms SOP]].

## Source
SyncUp recording — Luis Torres + Yassine Mossadek. Practice cancellation due to weather (lightning/rain) for two schools.

## Event Summary
They cancel today's practices for **Bay Lake** and **Independence** (and confirm **Lakemont** is not practicing). They then walk through the step-by-step process in **GoHighLevel** to update the season end date, generate cancellation email + SMS using **MyGPT / Whisper**, and send them to the right parents.

They fix an error in the generated message (makeup date was wrong, should be **May 5**). They use **Email Campaigns** and **Contacts + Advanced Filters/Tags** to target the correct teams for SMS. The dashboard is unreliable. Parents reply to acknowledge texts. They decide to **call the schools** because at least one parent complained about late notice.

## Topics

### Canceling practices and which teams
Cancel for Bay Lake + Independence (weather/lightning/rain). Lakemont has no practice so no messaging required.

### Updating sessions in GHL
Path: **Manage → Update session**. Set season end date (5/5). Re-enter session time details — the system forces a rewrite.

### Writing parent communication with AI (MyGPT + Whisper)
Copy program details into GPT. Prompt for cancellation email + text including: weather reason, apology, and missed-practice make-up by extending the season.

**Error caught:** GPT suggested makeup date May 12 — corrected to May 5.

### Sending emails via Email Campaigns
Use the "DR team" template. Warn: if you don't re-select the correct team, you might email the prior team's parent list (example: 14 still selected).

### Sending SMS via Contacts + Advanced Filters/Tags
Non-intuitive path:
- Contacts → Filters → Advanced Filters
- Filter by tag (e.g., **late spring 2026** + the school name)
- Select all → More → Send SMS
- Parent count may not match player count due to siblings

### Follow-ups, complaints, calling schools
A parent complains about late notice. Decide next time to text earlier. Realize they still need to **notify/call the schools** for early pickup changes. Split: one person calls Bay Lake, the other calls Independence.

## Action Items Captured From This Event
- Call the schools to notify them (split: Bay Lake + Independence)
- Respond to upset parent with apology + explain storm delay + commit to earlier texts next time
- Ensure all parent messaging is correct (especially makeup date: **May 5**, not May 12) before sending future campaigns

## Insights For SOP
- Dashboard is unreliable — log sends externally
- Wrong team filter risk on Email Campaigns — re-select always
- Sibling-aware parent counts — parent count ≠ player count
- AI-generated dates need verification before send
- Always call schools, not just send SMS, when last-minute changes affect pickup

---
brand: Discipline-Rift
area: operations
subarea: sops
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-11677 page 8cqnrff-11197 (PROCESSES / SMS — EOS Mass Texting)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
related_systems:
  - ghl
related_notes:
  - "[[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|GHL Marketing + Registration Automations]]"
hub_role: leaf
---

# Mass SMS via GHL SOP

## Parent
- [[SOPs-Home|DR SOPs Home]]

## Related
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|GHL Marketing + Registration Automations]]
- [[Practice-Cancellation-Comms-SOP|Practice Cancellation Comms SOP]]

## Purpose
Send end-of-season (EOS) or batch SMS notifications to multiple teams and their parents through GHL using templates + dynamic fields for personalization.

## When To Use
- End-of-season notifications (results, reminders, retention CTAs)
- Cross-team announcements that need to land in parents' SMS
- Time-sensitive operational notices (when email is too slow)

## Workflow

### 1. Pick the team(s)
Identify which teams need the message. Example teams used historically: Panther Lake, Windmir, Pershing, Hemlin, Pinecrest Avalon.

### 2. Open GHL template
Use the existing EOS / DR team template. Verify:
- Dynamic fields populate correctly (parent name, child name, team name, dates, links)
- All necessary links present (registration, season info, etc.)

### 3. Filter to the correct audience
**Path:** Contacts → Filters → Advanced Filters → tag filter (e.g., season tag + school name).

> [!warning] Re-select the correct team before sending. If you don't change the filter, you might accidentally text the prior team's parent list.

> Parent count may not match player count due to siblings.

### 4. Send
**Action:** Select all → More → Send SMS.

### 5. Track recipients
GHL dashboard is currently **unreliable** for tracking who received the message. Workaround:
- Log the send list externally (spreadsheet)
- Watch for replies / opt-outs
- Note any failed sends

## Quality Checklist Before Send
- [ ] Template has all dynamic fields filled
- [ ] All links work
- [ ] Filter set to correct team(s)
- [ ] Re-verify filter (especially if previous send used different team)
- [ ] Spelling / dates / makeup dates verified

## Known Issues To Track
- Tracking of which contacts received messages — improve via external log
- Template + dynamic fields management — keep a master template list

## Improvements Backlog
- Improve recipient tracking
- Ensure all templates include necessary dynamic fields and links before sending
- Continue refining the process for managing templates and recipient lists

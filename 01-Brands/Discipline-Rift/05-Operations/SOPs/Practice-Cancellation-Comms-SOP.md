---
brand: Discipline-Rift
area: operations
subarea: sops
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Synthesized from ClickUp Doc 8cqnrff-11677 page 8cqnrff-16037 (PARENT SMS & EMAILS — practice cancellation workflow log)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
related_systems:
  - ghl
related_notes:
  - "[[Mass-SMS-Via-GHL-SOP]]"
hub_role: leaf
---

# Practice Cancellation Communication SOP

## Parent
- [[01-Brands/Discipline-Rift/05-Operations/SOPs|DR SOPs]]

## Related
- [[Mass-SMS-Via-GHL-SOP|Mass SMS via GHL SOP]]
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|GHL Automations]]

## Purpose
Communicate last-minute practice cancellations (weather, facility, emergency) to parents, coaches, and schools — without dropping the trust ball.

## When To Use
- Weather emergency (lightning, rain, heat advisory)
- Facility issue (lock-out, double-booking, condition unsafe)
- Coach emergency
- Anything that prevents practice within < 24 hours of start

## Workflow

### 1. Identify affected teams
Confirm which teams cancel and which don't. Example: cancel Bay Lake + Independence, but Lakemont has no practice anyway (skip messaging).

### 2. Update GHL session schedule
**Path:** Manage → Update session.
- Set the season end date (e.g., extend to the new makeup date)
- Re-enter session time details (GHL forces a rewrite when changing dates)

### 3. Generate parent communication (email + SMS)
Use MyGPT / Whisper with the program details. Prompt for:
- Cancellation **email** + **text**
- Weather/cause reason
- Apology
- Notice that the missed practice will be **made up by extending the season**

> [!warning] Always verify the makeup date in the generated message before sending. AI has flagged wrong dates historically (e.g., May 12 vs correct May 5).

### 4. Send email via Email Campaigns
**Template:** "DR team" template.

**Verify:** re-select the correct team. If you don't change the filter, you might accidentally email the prior team's parent list.

### 5. Send SMS via Contacts + Advanced Filters
**Path:** Contacts → Filters → Advanced Filters.

**Filter by:** season tag (e.g., "late spring 2026") + school name.

Then: Select all → More → Send SMS.

> Parent count may not match player count due to siblings.

### 6. Notify the school directly (call)
A parent complaint surfaced that schools need to know in person too — especially when:
- Last-minute change affects pickup
- Aftercare flow is impacted
- Multiple parents will reach the school for clarification

**Split:** one person calls each affected school. Confirm with each school's admin.

### 7. Handle parent complaints
A parent complained about late notice. Response approach:
- Apologize
- Explain the storm/cause delay
- Commit to **earlier texts next time**

## Pre-Send Checklist
- [ ] Affected teams identified
- [ ] GHL session end date updated
- [ ] Makeup date verified in template (do not rely on AI's first answer)
- [ ] Correct team filter selected (do not inherit from previous send)
- [ ] Email + SMS sent
- [ ] School called directly
- [ ] Reply-monitoring set up (parents acknowledge texts)

## Recurring Improvements
- Send earlier when weather is forecast in advance (don't wait until last minute)
- Build a "weather alert" decision threshold (e.g., 60% rain forecast 4+ hours before practice → start the cancellation flow)
- Improve dashboard reliability for who received SMS

---
brand: Orlando-Event-Venue
domain: operations
area: tools
subarea: staff-operations-console
note_type: canonical
status: active
source: curated + oev-dna-pdf
canonical: true
last_updated: 2026-04-21
used_for_ai: true
sensitivity: internal
hub_role: child
---

# OEV Staff Operations Console

## Parent
- [[Brand-Home]]
- [[Delivery-Process]]
- [[Support-Process]]

## Children
- [[Quality-Standards]]
- [[Dependencies]]
- [[Required-Inputs]]
- [[Payment-Rules]]
- [[Collection-Process]]
- [[Metrics]]
- [[Constraints]]

## Related
- [[OEV-Admin-Command-Center]]
- [[Onboarding-Process]]
- [[Welcome-Flows]]
- [[Retention]]
- [[KPIs]]
- [[Offers]]
- [[Source-Reconciliation]]

## Strategy References
- [[Process-Reliability]]
- [[Standardization]]
- [[Constraint-Identification]]
- [[Feedback-Loops]]

## Purpose
This note defines what the **staff-side operational console** of Orlando Event Venue should make obvious before, during, and after an event. It is the execution-side translation of the sale.

The job of this tool is not lead conversion. Its job is to ensure that once an event is sold, the room, people, equipment, timing, compliance, and closeout are handled without chaos.

## Core Job Of This Tool
The staff operations console exists to answer five things fast:
- What events are mine today or this week?
- What exactly must be prepared for each event?
- What is still missing or unresolved?
- What must happen on-site and in what order?
- What needs to be recorded or closed out after the event?

## Staff-Side Truth
This tool should represent the execution truth of OEV, which includes:
- event schedule,
- room setup requirements,
- production package needs,
- staffing assignment,
- alcohol/compliance boundaries,
- pre-event readiness,
- incident logging,
- inspection and post-event closeout.

## What The Staff Dashboard Must Make Clear

### A. Upcoming Event Queue
This is the first thing staff should see.

Every event card should immediately answer:
- event date,
- time window,
- event type,
- guest count,
- package level,
- setup complexity,
- assigned staff,
- readiness state,
- unresolved issues.

### B. Event Readiness Status
This should make it impossible for staff to walk into an event blind.

Each booking should clearly show whether these are complete:
- final date/time confirmed,
- room layout confirmed,
- add-ons confirmed,
- production requirements confirmed,
- payment cleared enough to proceed,
- rule-sensitive issues flagged,
- pre-event checklist completed,
- owner assigned.

Recommended readiness logic:
- Not Ready
- Waiting On Admin
- Waiting On Client Input
- Waiting On Payment
- Ready For Setup
- Live Event
- Post-Event Inspection Pending
- Closed

### C. Setup / Breakdown Layer
Staff must not infer setup from memory or old text threads.

This section should show:
- required table/chair layout,
- décor/setup services included,
- whether breakdown is included,
- timing windows,
- overtime risk,
- reset expectations,
- room restore standard.

### D. Production / Tech Layer
Because OEV can include AV, LED, streaming, and workshop support, staff should see a separate, explicit technical layer.

This should answer:
- is there a production package,
- which package,
- what equipment is required,
- whether tech staffing is required,
- what testing has to happen before guest arrival,
- whether there is any high-risk technical dependency.

Suggested package logic:
- No Production
- Basic AV
- LED Presentation
- Workshop Broadcast / Streaming

### E. Incident / Exception Layer
This is one of the most valuable pieces.

The staff console should not just show ideal workflows. It should support imperfect reality.

It should make it easy to capture:
- late arrival,
- guest count issue,
- alcohol issue,
- damage concern,
- overtime concern,
- missing payment escalation,
- tech issue,
- staffing issue,
- cleanup/restore issue.

## Staff Workflow By Stage

### 1. Pre-Event Review
Before setup begins, staff should be able to review the event and know:
- what was sold,
- what is required,
- what is not required,
- which promises were made,
- and what must be protected.

### 2. Setup Stage
Staff should see:
- setup start time,
- setup owner,
- furniture layout,
- package-related tech tasks,
- décor or rental tasks,
- finish-by deadline.

### 3. Live Event Stage
During event execution, staff should see:
- primary point of contact,
- event status,
- current issues,
- overtime watch,
- package support responsibilities.

### 4. Breakdown / Reset Stage
This stage should make the following unavoidable:
- restore room,
- remove setup items,
- confirm tech teardown,
- complete inspection,
- log any issue,
- hand off final status.

### 5. Post-Event Closeout
This is where execution becomes data.

After the event, staff should be able to mark:
- inspection complete,
- no issue / issue found,
- fees triggered or not,
- follow-up needed,
- review request ready,
- referral eligibility if applicable.

## What Staff Must Never Have To Guess
A strong staff tool should eliminate guesswork around:
- what package the client bought,
- whether alcohol is allowed,
- whether production support is included,
- whether the event is actually cleared to proceed,
- how the room should look,
- who owns the next step,
- whether a problem must be escalated.

## Required Event Record Structure
Each event should have these blocks available to staff:

### Event Identity
- booking ID
- client name
- event type
- date/time
- guest count

### Execution Requirements
- room layout
- package type
- setup/breakdown service yes/no
- tech requirements
- special notes

### Compliance / Constraint Flags
- alcohol fit
- occupancy fit
- décor restrictions
- timing restrictions
- high-risk notes

### Operational Ownership
- event owner
- setup owner
- tech owner
- inspection owner

### Closeout Fields
- completed on time yes/no
- incident yes/no
- damage yes/no
- extra charges yes/no
- review request eligible yes/no
- referral logic triggered yes/no

## Most Important Staff KPIs
The staff console should make these visible or easy to derive:
- % events moved to Ready For Setup on time
- % events with complete staffing assignment
- % inspections completed same day
- % incidents logged properly
- % post-event closeouts completed without missing data
- repeat issue categories by frequency

## What Claude Should Be Able To Do With This Note
Claude should be able to use this note to:
- design or refine the real staff dashboard,
- identify missing fields,
- turn day-of chaos into checklists,
- suggest SOP improvements,
- map handoff gaps between admin and staff,
- write clearer staff operating standards.

## Failure Modes This Tool Must Catch
- confirmed events without staff assigned
- package sold but execution requirements unclear
- layout/setup unclear before event day
- inspection not done after event
- issues logged in chat but not in system
- event marked “confirmed” but not actually operationally ready
- staff depends on memory instead of system visibility

## Highest-Leverage Improvements This Tool Should Enable
- smoother admin-to-staff handoff
- fewer missed setup details
- fewer day-of surprises
- stronger inspection discipline
- better incident visibility
- better repeatability as volume grows

## What Must Be Added Once Real Staff Dashboard Screenshots/Exports Are Available
This note should be upgraded with the real:
- sections,
- views,
- filters,
- statuses,
- assignment rules,
- checklist logic,
- issue logging pattern,
- closeout workflow.

## Build Standard For This Note
This note is only valuable if it helps the staff side of OEV execute consistently, escalate cleanly, and close each event with less ambiguity.

If it does not reduce operational guesswork, it is not finished.

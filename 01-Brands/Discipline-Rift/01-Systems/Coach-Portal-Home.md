---
brand: Discipline-Rift
area: systems
domain: coach-portal
note_type: canonical
status: active
used_for_ai: true
aliases:
  - DR Coach Dashboard
  - Coach Portal
---

# Coach Portal Home

## Parent
- [[Systems-Home]]

## Related
- [[Parent-App-Home]]
- [[Admin-Operations-App-Home]]
- [[DR-Shared-Entities-and-Integrations]]
- [[DR-Operational-Flows]]
- [[Training-Home]]

## Purpose
This is the coach-facing operating app for Discipline Rift.

Its purpose is to help coaches execute field operations cleanly:
- manage assigned teams
- take attendance by session
- communicate with parents individually or by broadcast
- review unread notifications
- stay aligned with weekly reporting expectations

## User types and access
### Coach
- enters from the main route
- authenticates via email OTP
- sees only assigned teams and sessions
- can take attendance
- can send individual and group messages to parents

### Administrator inside this app
The coach dashboard documentation also includes admin monitoring capabilities inside the same ecosystem:
- global attendance view
- messaging oversight
- coach campaign email tools

That means this system is best understood as a **coach-first operational layer** that also has an admin supervision surface.

## Coach workflow
### 1. Team selection
Coach sees only active or ongoing teams assigned to them.

### 2. Session selection
Once a team is chosen, the app computes upcoming session occurrences from the recurring schedule.

### 3. Attendance mode
Coach marks each student present or absent with immediate save behavior.

### 4. Messaging
Coach can move into messages to communicate with parents individually or by broadcast.

## Core modules
### Dashboard shell
- coach identity
- assigned team count
- notifications icon with unread badge
- logout

### My Teams
- searchable team list
- each item shows team and school/location

### Session selector
- next session instances derived from recurring schedule
- session shows day, date, time, and location

### Statistics panel
Real-time session and team attendance summary:
- enrolled students
- present
- absent
- remaining unmarked

### Attendance pass
Per student:
- full name
- grade
- current status
- present / absent one-click actions
- immediate persistence

### Messaging module
Two main uses:
1. individual parent conversations
2. team-wide broadcasts

Capabilities include:
- real-time messaging
- unread counters
- Enter-to-send
- attachments up to 25MB
- auto-mark read when opening a thread
- group messaging by team
- broadcast history by team

### Notifications
- unread badge on bell icon
- unread summary by conversation
- direct deep-link into exact coach-parent thread

### Weekly reports
Automatic weekly reporting sends attendance summaries by email, including top absences.

## Product interpretation
The Coach Portal is the **field execution layer** of DR.

This is where the program becomes real each day: attendance, parent contact, session discipline, and operational follow-through.

## What Claude should use this note for
Use this note when the task involves:
- coach UX
- attendance workflow
- session-day execution
- coach-parent messaging
- broadcast logic
- coach notifications
- weekly coach reporting

Do not confuse this with the parent app or with the broader internal admin app.

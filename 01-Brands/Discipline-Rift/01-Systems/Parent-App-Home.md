---
brand: Discipline-Rift
area: systems
domain: parent-app
note_type: canonical
status: active
used_for_ai: true
aliases:
  - DR Parent Dashboard
  - Parent Portal
---

# Parent App Home

## Parent
- [[Systems-Home]]

## Related
- [[Coach-Portal-Home]]
- [[Admin-Operations-App-Home]]
- [[DR-Shared-Entities-and-Integrations]]
- [[DR-Operational-Flows]]
- [[Offers]]
- [[Pricing-Logic]]

## Purpose
This is the parent-facing application for Discipline Rift.

Its function is to let families manage and monitor what matters most about their children’s participation:
- active registrations
- practices and schedule
- skills and tier progression
- communication with coaches
- payment history
- individual player detail

## Access model
Parents authenticate through a passwordless OTP flow:
1. parent enters email
2. system sends a 6-digit code
3. parent verifies code
4. parent receives an active session

The app protects dashboard routes automatically and redirects to login if the session is not valid.

## Core navigation
Main sections:
- Home
- My Players
- Skills & Tiers
- Messages
- Schedule
- Payments
- Settings

## What makes this app valuable
This is not just a “dashboard.” It is the **family operating layer** of DR.

It answers these questions for a parent:
- What is happening this week?
- Which child is in which program?
- How is each child progressing?
- When is the next practice?
- What has been paid?
- Did the coach message me?

## Functional modules
### 1. Home
Executive snapshot of the family account:
- practices this week
- active players
- active programs
- unread message alert
- upcoming practices
- active players panel
- quick links to schedule, players, and payments

### 2. My Players
Family roster view:
- one card per child
- active programs
- previous enrollments
- emergency contact details
- empty-state guidance when no children are registered

### 3. Skills & Tiers
Progress tracking by sport:
- current tier per child
- tier navigator
- skill states: not started, in development, consistent
- progress logic connected to attendance and coach-recorded development

### 4. Schedule
Calendar and list modes for all practices:
- monthly view
- list view
- filter by child
- upcoming-only toggle
- practice detail with sport, team, time, school, coach, and time remaining

### 5. Messages
Direct parent ↔ coach communication:
- one conversation per team/coach context
- real-time updates
- unread counters
- automatic read state when opening a conversation

### 6. Payments
Read-only payment history:
- date
- child
- team/program
- amount

### 7. Player profile
Deep view by child:
- basic profile header
- attendance percentage
- coach and school visibility
- sport tabs when enrolled in multiple sports
- current focus by sport
- complete tier navigator

### 8. Coupons
This exists as a management function in the parent-side documentation, but operationally it should be treated as an internal or hybrid admin-facing function, not core parent UX.

### 9. Settings
Reserved for future phases.

## Product interpretation
The Parent App is where DR turns operations into trust.

It gives parents visibility, which reduces confusion and support load. It also makes progress tangible, which supports retention.

## What Claude should use this note for
Use this note when the task involves:
- parent-facing UX
- schedule clarity
- parent communications experience
- message UX
- skills/progress UX
- payment visibility
- family account behavior

Do **not** use this note as the source of truth for internal admin actions such as full registration management, newsletter operations, GHL sync, or full attendance oversight. Those belong to [[Admin-Operations-App-Home]].

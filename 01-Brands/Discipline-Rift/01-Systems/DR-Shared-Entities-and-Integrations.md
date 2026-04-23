---
brand: Discipline-Rift
area: systems
domain: shared
note_type: canonical
status: active
used_for_ai: true
aliases:
  - DR Shared Data Model
  - DR Integrations
---

# DR Shared Entities and Integrations

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Systems-Home|DR Systems Home]]

## Related
- [[Parent-App-Home]]
- [[Coach-Portal-Home]]
- [[Admin-Operations-App-Home]]
- [[DR-Operational-Flows]]

## Why this note exists
The three apps in Discipline Rift are different surfaces of the same business.

This note exists so the vault has one shared source for:
- core entities
- relationships between those entities
- major external services
- system-level interpretation

Without this note, the same data model gets repeated in multiple places.

## Core entities
### School
A physical institution/location where a team operates.

### Team
A program unit linked to a sport and a school.

### Session
A recurring or date-based occurrence tied to team scheduling.

### Staff / Coach
A staff member assigned to teams or sessions.

### Student
An athlete enrolled in programs.

### Parent
A family contact linked to one or more students.

### Enrollment
The relationship that links a student to a team.

### Attendance
A dated presence/absence record tied to a student and session occurrence.

### Message
A communication record between coach and parent, or a broadcast record inside a team context.

### Payment
A financial record connected to enrollments or program participation.

### Coupon / Discount
A pricing override or discount code applied in registration.

### Application
A candidate or applicant record submitted through the public funnel.

### Certificate
A generated completion artifact tied to a student, team, sport, and level.

### Subscriber
An opt-in email recipient for newsletter flows.

## Shared relationships
- A school can have many teams.
- A team belongs to one school and one sport.
- A team has one or more sessions.
- A coach may be assigned to one or more sessions or teams.
- A student can have multiple enrollments over time.
- A parent can be linked to multiple students.
- Attendance is recorded per student per session date.
- Messages live inside a coach-parent-team context.
- Payments tie back to enrollments or program participation.

## Cross-system interpretation
### Parent App depends on
- parent
- student
- enrollment
- payment
- message
- session schedule
- skill/tier progression

### Coach Portal depends on
- coach
- team
- session
- attendance
- parent
- student
- message

### Admin Operations App depends on everything
because it manages the full business layer.

## Main integrations
### Supabase
Used for:
- auth
- data
- storage
- realtime behaviors

### Gmail / SMTP / Workspace relay
Used for:
- campaigns
- newsletters
- reminders

### Twilio
Used for SMS communication.

### GoHighLevel (GHL)
Used as CRM sync destination for parent contact and enrollment context.

### Vercel
Used for deployment and app hosting.

## Use rule
When Claude needs to understand how data moves across the brand, start here first.

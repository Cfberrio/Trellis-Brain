---
brand: Discipline-Rift
area: systems
domain: admin-operations-app
note_type: canonical
status: active
used_for_ai: true
aliases:
  - DR Admin Dashboard
  - DR Internal Dashboard
---

# Admin Operations App Home

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Systems-Home|DR Systems Home]]

## Related
- [[Parent-App-Home]]
- [[Coach-Portal-Home]]
- [[DR-Shared-Entities-and-Integrations]]
- [[DR-Operational-Flows]]
- [[01-Brands/Discipline-Rift/00-Brand-Core/Offers|DR Offers]]

## Purpose
This is the internal admin operating system for Discipline Rift.

It centralizes the core business operations of the organization:
- registrations
- schools
- staff
- discounts
- applications
- campaign communication
- newsletter distribution
- reminders
- certificates
- GHL sync
- cross-school schedule oversight

This is the system that most closely matches what people casually call the “backend,” but functionally it is better described as the **admin operations app**, not backend infrastructure.

## Access model
- authenticated login via email + password
- admin authorization check after login
- authenticated basic users can access limited sections
- admin users access the full operations suite

## Main sections
- Home
- Schedule / Agenda
- Registrations
- Schools
- Staff
- Discount
- Applications
- Email Campaigns
- Newsletter
- Reminders
- Certificates
- GHL Sync

## Operational value by module
### Home
Real-time monitor of sessions happening today:
- all sessions for the day
- team, school, enrolled count, and state
- expandable rows with students

### Schedule / Agenda
Weekly full-calendar operations view:
- all sessions across schools
- event drawer for editing session details
- parent communication directly from session context

### Registrations
The strongest program operations area.

It controls:
- team inventory
- sport and school assignment
- price and capacity visibility
- duplicate/cloning workflows
- session configuration
- enrollments
- roster export

### Schools
School/location management.

### Staff
Coach and administrative personnel management.

### Discount
Coupon management for registration pricing.

### Applications
Review of public candidate submissions and resume downloads.

### Email Campaigns
Targeted parent communication by team using variables and channel choice.

### Newsletter
Mass opt-in communications with preview, test send, batching, and unsubscribe logic.

### Reminders
Attendance-related reminders to coaches and absence notifications to parents.

### Certificates
Client-side certificate generation in ZIP bundles by sport, team, and level.

### GHL Sync
CRM sync for parent contacts and enrollment-related data.

## Product interpretation
This app is the **business control layer** of Discipline Rift.

If the Parent App builds trust and the Coach Portal drives daily execution, the Admin Operations App runs the machine.

## What Claude should use this note for
Use this note when the task involves:
- internal operations
- registrations and roster logic
- schools and staff management
- campaigns and newsletters
- reminders
- certificates
- CRM sync
- admin navigation and permissions

Do not reduce this note to “backend.” It represents an operating application with business workflows, not only technical infrastructure.

---
brand: Discipline-Rift
area: systems
note_type: hub
status: active
used_for_ai: true
aliases:
  - DR Systems Home
---

# Systems Home

## Parent
- [[Brand-Home]]

## Children
- [[Parent-App-Home]]
- [[Coach-Portal-Home]]
- [[Admin-Operations-App-Home]]
- [[DR-Shared-Entities-and-Integrations]]
- [[DR-Operational-Flows]]

## Related
- [[KPIs]]
- [[Offers]]
- [[Pricing-Logic]]
- [[Training-Home]]

## What this section is
This note is the hub for all Discipline Rift product systems.

It separates the brand into 3 real operating surfaces:
1. **Parent App** — what families see and use
2. **Coach Portal** — what coaches use in the field
3. **Admin Operations App** — what internal staff use to run the business

The goal is to prevent product information from getting mixed together. A parent-facing workflow, a coach-facing workflow, and an admin workflow should not live in one giant note.

## Recommended folder structure
```text
01-Systems/
├── Systems-Home.md
├── Parent-App/
│   └── Parent-App-Home.md
├── Coach-Portal/
│   └── Coach-Portal-Home.md
├── Admin-Operations-App/
│   └── Admin-Operations-App-Home.md
└── Shared/
    ├── DR-Shared-Entities-and-Integrations.md
    └── DR-Operational-Flows.md
```

## Naming rule
Do **not** keep notes named `Pasted markdown.md`.

Use names that describe the system clearly:
- `Parent-App-Home.md`
- `Coach-Portal-Home.md`
- `Admin-Operations-App-Home.md`
- `DR-Shared-Entities-and-Integrations.md`
- `DR-Operational-Flows.md`

## How to use this section in Obsidian
- Start here when you need to understand which app or system a workflow belongs to.
- Route Claude here first when the task is about dashboard behavior, flows, access, messaging, attendance, payments, registrations, certificates, or CRM sync.
- From here, jump into the correct app instead of searching the whole vault blindly.

## Graph rule
This note should always stay connected to:
- the 3 app home notes
- the shared systems note
- the operational flows note
- the main brand note

That makes the graph show Discipline Rift as a connected operating system instead of scattered files.

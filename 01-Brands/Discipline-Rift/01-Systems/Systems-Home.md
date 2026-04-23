---
brand: Discipline-Rift
area: systems
note_type: home
status: active
canonical: true
used_for_ai: true
owner: Luis
last_updated: 2026-04-23
sensitivity: internal
hub_role: system-hub
aliases:
  - DR Systems Home
---

# Systems Home

## Parent
- [[01-Brands/Discipline-Rift/00-Brand-Core/Brand-Home|DR Brand Home]]

## Children
- [[01-Brands/Discipline-Rift/01-Systems/Parent-App-Home|DR Parent App Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Coach-Portal-Home|DR Coach Portal Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Admin-Operations-App-Home|DR Admin Operations App Home]]
- [[01-Brands/Discipline-Rift/01-Systems/DR-Shared-Entities-and-Integrations|DR Shared Entities and Integrations]]
- [[01-Brands/Discipline-Rift/01-Systems/DR-Operational-Flows|DR Operational Flows]]

## Related
- [[01-Brands/Discipline-Rift/00-Brand-Core/KPIs|DR KPIs]]
- [[01-Brands/Discipline-Rift/00-Brand-Core/Offers|DR Offers]]
- [[01-Brands/Discipline-Rift/05-Operations/Training/Training-Home|DR Training Home]]

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

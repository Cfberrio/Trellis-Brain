---
brand: Discipline-Rift
area: systems
subarea: ghl-crm
note_type: system
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-16717 page 8cqnrff-19757 (OUTREACH / PIPELINES)"
owner: Luis
last_updated: 2026-05-21
sensitivity: internal
related_systems:
  - ghl
related_notes:
  - "[[Sales-Home]]"
  - "[[School-Outreach-SOP-Public]]"
  - "[[School-Outreach-SOP-Private]]"
hub_role: leaf
---

# GHL CRM Pipeline Spec

## Parent
- [[Sales-Home|DR Sales Home]]

## Related
- [[School-Outreach-SOP-Public|Public Schools Outreach SOP]]
- [[School-Outreach-SOP-Private|Private/Charter Schools Outreach SOP]]
- [[01-Brands/Discipline-Rift/02-Communication/DR-GoHighLevel-Marketing-and-Registration-Automations|GHL Marketing + Registration Automations]]

## Purpose
Three-pipeline structure inside Go High Level for DR school outreach + lead capture. This is the contract Chris (CRM operator) uses to organize school contacts and route opportunities.

## Pipelines

### Pipeline 1 — Orange County 1 — Como Import
**Purpose:** Legacy data from Como (old CRM).

**Use for:**
- Existing Como contacts
- Existing Como school opportunities
- Old follow-ups
- Any school already worked inside Como
- Historical pipeline status

**Goal:** preserve the old pipeline, organized inside GHL.

### Pipeline 2 — Orange County 2 — Public Schools
**Purpose:** Traditional public schools in Orange County.

**Include:** OCPS schools, Elementary schools, K–5 schools, K–8 schools (if they include elementary students), public schools that are not charter/private.

**Exclude:** charter schools, private schools, Pre-K only, Kindergarten-only schools.

### Pipeline 3 — Orange County 3 — Charter + Private Schools
**Purpose:** All schools that are not traditional OCPS public.

**Include:** charter schools, private schools, academies, Christian schools, Montessori schools, independent schools, any school that is public-charter but operates separately from traditional OCPS.

**Reason:** charter and private schools may have different approval processes, decision-makers, facility access, and parent communication rules.

## School Eligibility Rules

### Delete / Do Not Import
- Pre-K only
- Kindergarten only
- Pre-K to Kindergarten
- Preschool only
- Early learning centers
- Childcare centers
- Daycare centers

**Reason:** DR serves mainly K–5; K–8 acceptable if elementary students are included.

### Keep / Import
- K–5
- K–6
- K–8
- 1–5
- 1–8
- PK–5
- PK–8

> [!warning] Do not delete a school just because it includes Pre-K. Delete only if it serves ONLY Pre-K/K and does not include elementary grades.

## Required GHL Custom Fields

### School Information
1. **School Name**
2. **School Type** — Public / Charter / Private / Legacy Como
3. **County** — Orange County
4. **City** — Orlando, Winter Garden, Ocoee, Apopka, Windermere, etc.
5. **School Address**
6. **Grade Range** — K–5, K–8, PK–5, etc.
7. **Eligible for DR?** — Yes / No
8. **Reason Not Eligible** — Pre-K/K only / Too far / Not a school / Duplicate / Other

### Main POC (Point of Contact)
9. **Main POC Name**
10. **Main POC Email**
11. **Main POC Position** — Principal / Assistant Principal / Aftercare Director / Front Desk / PE Teacher / Activities Coordinator / Other
12. **Main POC Phone**
13. **Main POC Extension**

### Secondary Contact (optional)
14. **Secondary POC Name**
15. **Secondary POC Email**
16. **Secondary POC Position**
17. **Secondary POC Phone**
18. **Secondary POC Extension**

### Facility / Logistics
19. **Facility Contact Name**
20. **Facility Contact Email**
21. **Facility Contact Phone**
22. **Preferred Facility Space** — Gym / Pavilion / Field / Cafeteria / Other
23. **Facilitron Required?** — Yes / No / Unknown
24. **Facilitron Status** — Not Started / Submitted / Approved / Denied / Pending School Response
25. **Available Practice Day** — Monday / Tuesday / Wednesday / Thursday / Friday / Unknown
26. **Available Practice Time** — e.g., 3:00–4:00 PM

### Program Interest
27. **Interested Sport** — Volleyball / Tennis / Pickleball / Flag Football / Multiple / Unknown
28. **Primary Sport to Pitch** — Volleyball / Tennis / Pickleball / Flag Football
29. **Season Interest** — Fall / Winter / Spring / Summer / Unknown

## Pipeline Stages (12)

| # | Stage | Description |
|---|---|---|
| 1 | **Low Priority Lead / Imported** | School added but not researched yet |
| 2 | **High Priority Lead / Imported** | School added but not researched yet (higher priority) |
| 3 | **Needs Research** | Missing POC, email, phone, grade range, or school type |
| 4 | **Contact Identified** | Main POC has been found |
| 5 | **First Outreach Sent** | First email or call has been made |
| 6 | **Follow-Up Needed** | No response yet |
| 7 | **Interested** | School replied positively |
| 8 | **Availability Requested** | We asked for day/time/facility availability |
| 9 | **Pending Principal / Admin Review** | They are reviewing internally |
| 10 | **Facility Reservation Submitted** | Facilitron or school reservation submitted |
| 11 | **Approved / Scheduled** | School approved and season can be scheduled |
| 12 | **Not a Fit / Closed Lost** | School declined, no space, wrong age group, or not interested |

## Data Cleanup Rules (for Chris — CRM operator)

### Step 1 — Separate the data
- All old Como records → **Orange County 1 — Como Import**
- Traditional public schools → **Orange County 2 — Public Schools**
- Charter/private schools → **Orange County 3 — Charter + Private Schools**

### Step 2 — Delete non-eligible schools
Delete if grade range is only Pre-K / Kindergarten / Pre-K–K / Preschool / Early Learning / Daycare.

### Step 3 — Keep schools with elementary grades
Keep K–5, K–6, K–8, PK–5, PK–8, 1–5, 1–8.

### Step 4 — Minimum fields before import
1. School Name
2. School Type
3. City
4. Grade Range
5. Main POC Name
6. Main POC Email
7. Main POC Position
8. Phone
9. Extension

If some are missing → move into **Needs Research** stage.

## Final CRM Structure Summary

```
Workspace
├── Pipeline 1: Orange County 1 — Como Import (legacy)
├── Pipeline 2: Orange County 2 — Public Schools (OCPS / public)
└── Pipeline 3: Orange County 3 — Charter + Private Schools (charter, academy, religious, Montessori, independent)
```

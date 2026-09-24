---
brand: Discipline-Rift
area: operations
subarea: sops
note_type: system
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Synthesized from ClickUp list 901710739779 (FLAG PARTNER PROGRAM — practice + injury form submissions)"
owner: Luis
last_updated: 2026-09-17
sensitivity: internal
related_systems:
  - ghl
related_notes:
  - "[[01-Brands/Discipline-Rift/01-Systems/Parent-App-Home|DR Parent App]]"
  - "[[01-Brands/Discipline-Rift/01-Systems/Coach-Portal-Home|DR Coach Portal]]"
hub_role: leaf
up:
  - "[[01-Brands/Discipline-Rift/05-Operations/SOPs/SOPs-Home]]"
related:
  - "[[01-Brands/Discipline-Rift/01-Systems/Parent-App-Home]]"
  - "[[01-Brands/Discipline-Rift/01-Systems/Coach-Portal-Home]]"
  - "[[01-Brands/Discipline-Rift/03-Evidence/Practice-Reports/Flag-Football-2026-Spring]]"
  - "[[01-Brands/Discipline-Rift/02-Communication/Templates/Coach-After-Practice-Parent-Update]]"
  - "[[01-Brands/Discipline-Rift/05-Operations/Training/Method/DR-Training-Philosophy]]"
---

# Practice Report + Injury Form Schema

## Parent
- [[SOPs-Home|DR SOPs Home]]

## Related
- [[01-Brands/Discipline-Rift/01-Systems/Parent-App-Home|DR Parent App Home]]
- [[01-Brands/Discipline-Rift/01-Systems/Coach-Portal-Home|DR Coach Portal Home]]
- [[../../03-Evidence/Practice-Reports/Flag-Football-2026-Spring|Flag Football 2026 Spring Practice Logs (evidence)]]

## Purpose
Field-level specification for the practice report + injury form system that coaches use to capture per-session data. Used by Parent App + Coach Portal.

## Form Fields

### Identification
| Field | Type | Notes |
|---|---|---|
| `Player` | short_text | Athlete name |
| `Date` | date | Session date |
| `Date & Time / Location` | short_text | Session details |

### Practice Report
| Field | Type | Notes |
|---|---|---|
| `Description` | text | Free-form session notes — best win / hardest part / help next time / coach observations |
| `Effort` | (likert 1–5 in practice, capture as int) | Coach rating |
| `Focus` | (likert 1–5) | Coach rating |

### Injury & Care
| Field | Type | Notes |
|---|---|---|
| `Injury & Care` | text | What care was given (e.g., "took him inside, nurse saw him for ice, rested, joined later") |
| `What Happened` | text | Description of incident |
| `Severity` | drop_down | `Near Miss` / `Minor` / `Moderate` / `Severe` |
| `Removed From Practice` | drop_down | `Yes` / `No` |
| `Return-to-Play` | drop_down | `Not Cleared` / `Cleared by Coach` / `Cleared by Nurse` |
| `Parent / Guardian Contact` | drop_down | `Yes` / `No` |

### Media
| Field | Type | Notes |
|---|---|---|
| `Video` | short_text | Link or reference to attached video |
| Attachments | files | Photo + video uploads |

## Capture Workflow
1. Coach opens form on phone (Coach Portal app or web)
2. Selects athlete from roster
3. Fills practice notes (effort, focus, description)
4. If injury: fills Injury & Care section (severity, removed, return-to-play, parent contact)
5. Attaches photo/video if relevant
6. Submits → logged to GHL → visible to parent in Parent App

## Privacy & Sensitivity
- Injury notes are **sensitive**. Restrict access to:
  - The athlete's parent/guardian (view only)
  - Coach + admin (full access)
  - Nurse / medical staff (read only if Return-to-Play involves them)
- Photos of injuries must NOT be shared in any public-facing channel

## Operational Notes
- "Parent Contact = No" + "Severity = Moderate or above" should trigger a manual notification workflow
- "Removed From Practice = Yes" + "Return-to-Play = Not Cleared" → flag for follow-up before next session
- Aggregate per-athlete reports give parents the progress curve they otherwise miss (per Founder Q&A weekly theme — see [[../../03-Evidence/Founder-Voice/Q&A-Weekly-Themes|Founder Q&A Themes]])

## Proposed learning-log fields (2026-09-17 — proposal, not implemented)

Source: Notion change proposal C22 ([[01-Brands/Discipline-Rift/04-Projects/Coach-Hub-Rebuild/DR-Notion-Curriculum-Change-Proposal-2026-09-17|Change Proposal]]) and [[01-Brands/Discipline-Rift/05-Operations/Training/Method/DR-Training-Philosophy|Training Philosophy]] §6. The volleyball week pages already tell coaches to "record a learning log" but no template exists; the free-form `Description` above is where it lands today. If the form is ever extended, keep it **separate from attendance and injury**, one record per team per session (not per player), and small:

| Field | Type | Notes |
|---|---|---|
| `Skill + variant run` | short_text | The actual layer, e.g. "passing → teammate target, predictable feed" |
| `Last reliable rung` | short_text | Where most of the group performed with control |
| `Independent check` | short_text | One CFU observation made *without* a coach prompt; note if catch-support or a cue was used |
| `Regression / progression used` | short_text | What was simplified or which layer was added, for whom |
| `Next retrieval / next layer` | short_text | What next practice starts by retrieving and what the next layer is |
| `One coaching adjustment` | short_text | The one thing the coach will do differently |
| `Parent update sent` | checkbox | The [[01-Brands/Discipline-Rift/02-Communication/Templates/Coach-After-Practice-Parent-Update|after-practice parent update]] went out |

Do not assume the Dashboard supports these until dev confirms; until then coaches put the same content in `Description`. The `Effort` / `Focus` ratings stay per player.

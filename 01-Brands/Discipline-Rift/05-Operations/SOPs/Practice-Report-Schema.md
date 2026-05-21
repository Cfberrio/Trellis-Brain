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
last_updated: 2026-05-21
sensitivity: internal
related_systems:
  - ghl
related_notes:
  - "[[01-Brands/Discipline-Rift/01-Systems/Parent-App-Home|DR Parent App]]"
  - "[[01-Brands/Discipline-Rift/01-Systems/Coach-Portal-Home|DR Coach Portal]]"
hub_role: leaf
---

# Practice Report + Injury Form Schema

## Parent
- [[01-Brands/Discipline-Rift/05-Operations/SOPs|DR SOPs]]

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

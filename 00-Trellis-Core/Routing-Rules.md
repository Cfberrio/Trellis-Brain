---
brand: Trellis-Core
area: system
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
sensitivity: internal
hub_role: root
last_updated: 2026-04-23
---

# Routing Rules

## Parent
- [[00-Trellis-Core/Trellis-Home|Trellis Home]]

## Purpose
This document defines how humans and AI should load context inside the Trellis Brain.

Its purpose is to prevent:
- brand contamination,
- loading the wrong type of notes,
- overloading context with irrelevant material,
- treating folders like knowledge,
- treating evidence like canonical truth,
- starting implementation before retrieving the right context.

## Routing Principle
Load the right context in the right order from the right brand.

Never begin with “search everything.”
Never begin with another brand.
Never begin with evidence if canonical notes exist.
Never begin with folders alone.

## Graph-First Architecture Rule
The Trellis Brain must route through notes, not folders.

Because the graph only connects notes through internal links, routing should prefer hub notes first. Folder structure tells us where things live. Hub notes tell us how things connect.

### Mandatory Hub Notes
At minimum, the system should route through these note types when they exist:
- `Trellis-Home.md`
- `Brand-Home.md`
- `Marketing-Home.md`
- `Sales-Home.md`
- `Communication-Home.md`
- `DNA-Home.md`

### Why This Matters
If the system starts from a hub note, it can:
- load context faster,
- retrieve the right child notes more reliably,
- stay brand-contained,
- and preserve graph connectivity at the same time.

## Brand Isolation Rule
A task must stay inside its active brand unless the user explicitly requests cross-brand comparison, transfer, or adaptation.

Allowed:
- work inside one brand,
- compare two brands only if requested,
- use abstract strategy models from Trellis-Core.

Not allowed by default:
- borrowing evidence from another brand,
- borrowing tone from another brand,
- merging OEV and Reliable Venues context,
- importing CTS language into DR,
- using Trellis Fields voice as default voice for client-facing brands.

## Trellis-Core Rule
`00-Trellis-Core/` is shared infrastructure, not brand memory.

Use Trellis-Core for:
- routing logic,
- metadata rules,
- templates,
- AI instructions,
- abstract strategy models,
- system-level architecture.

Do not use Trellis-Core to store brand-specific voice, offers, objections, or communication examples.

## Canonical Before Evidence Rule
Always prefer canonical notes before evidence.

### Canonical Notes Usually Include
- `Brand-Home`
- `Positioning`
- `Avatar`
- `Offers`
- `Value-Proposition`
- `Voice-and-Tone`
- `Language-Rules`
- `Constraints`
- `Opportunities`
- `KPIs`
- `Communication-Manual`
- `Sales-Process`
- `Pricing-Logic`
- `DNA` notes

### Evidence Usually Includes
- email history,
- WhatsApp messages,
- SMS,
- transcripts,
- call notes,
- voice notes,
- extracted insights,
- good examples,
- anti-examples.

Evidence supports interpretation.
Canonical notes govern execution.

## Parent-Child-Sibling Rule
Every important note should participate in routing through explicit note links.

### Parent Links
Each canonical note should link upward to its nearest hub.

Examples:
- `Positioning` -> `Brand-Home`
- `Sales-Process` -> `Sales-Home`
- `Communication-Manual` -> `Communication-Home`
- `Message` -> `DNA-Home`

### Child Links
Each hub note should link downward to its most important child notes.

Examples:
- `Brand-Home` -> `Positioning`, `Offers`, `Voice-and-Tone`
- `Marketing-Home` -> `Messaging-Strategy`, `Website/Sitemap`, `Campaigns`
- `Communication-Home` -> `Communication-Manual`, `Templates`, `Improvement-Log`

### Sibling Links
Sibling notes should link laterally only when they are operationally related.

Examples:
- `Sales-Messaging` <-> `Sales-Process`
- `Pricing-Logic` <-> `Payment-Rules`
- `Message` <-> `Value-Proposition`

Do not create decorative or random sibling links.

## Home-First Retrieval Rule
When possible, start retrieval at a home note, not a raw child note.

Recommended starting points:
- `Trellis-Home` for system-level tasks
- `Brand-Home` for brand-level tasks
- `Communication-Home` for language and messaging tasks
- `Marketing-Home` for website and content tasks
- `Sales-Home` for conversion and follow-up tasks
- `DNA-Home` for business logic and model tasks

## Default Retrieval Order
Unless the task requires something else, retrieve in this order:
1. active brand
2. relevant hub note
3. relevant canonical child notes
4. relevant systems notes
5. relevant communication notes
6. relevant DNA notes
7. relevant strategy models from Trellis-Core only if needed
8. relevant evidence notes for examples or reality checks
9. archive only if explicitly needed

## Retrieval Order by Task Type
### 1. Communication Tasks
Examples:
- write follow-up email,
- rewrite payment reminder,
- improve coach messaging,
- create support message,
- restructure sales email sequence.

Load in this order:
1. `Brand/02-Communication/Communication-Home.md`
2. `Brand/02-Communication/Manual/Communication-Manual.md`
3. relevant manual notes such as `Sales-Messaging`, `Follow-Up-Messaging`, `Payment-Messaging`
4. `Brand/01-Systems/Sales/` or relevant system folder
5. `Brand/06-DNA/Message.md`
6. `Brand/00-Brand-Core/Voice-and-Tone.md`
7. `Brand/00-Brand-Core/Language-Rules.md`
8. relevant evidence examples
9. strategy models only if the task is also strategic

### 2. Website and Copy Tasks
Examples:
- update landing page,
- change hero section,
- adjust pricing copy,
- create CTA logic,
- improve booking page messaging.

Load in this order:
1. `Brand/01-Systems/Marketing/Marketing-Home.md`
2. `Brand/01-Systems/Marketing/Website/Sitemap.md`
3. `Brand/01-Systems/Marketing/Website/Copy.md`
4. `Brand/00-Brand-Core/Positioning.md`
5. `Brand/00-Brand-Core/Offers.md`
6. `Brand/00-Brand-Core/Value-Proposition.md`
7. `Brand/06-DNA/Message.md`
8. `Brand/02-Communication/Manual/` if wording rules matter
9. relevant evidence or extracted insights
10. strategy models only if offer optimization is needed

### 3. Sales System Tasks
Examples:
- improve follow-up sequence,
- redefine lead handling,
- improve objection logic,
- clarify closing flow.

Load in this order:
1. `Brand/01-Systems/Sales/Sales-Home.md`
2. `Brand/01-Systems/Sales/Sales-Process.md`
3. `Brand/02-Communication/Communication-Home.md`
4. `Brand/02-Communication/Manual/`
5. `Brand/06-DNA/Sales.md`
6. `Brand/06-DNA/Offer.md`
7. `Brand/00-Brand-Core/Objections.md`
8. relevant evidence from `03-Evidence/`
9. strategy models if needed

### 4. Marketing Strategy Tasks
Examples:
- content strategy,
- campaign planning,
- offer framing,
- funnel thinking,
- acquisition ideas.

Load in this order:
1. `Brand/01-Systems/Marketing/Marketing-Home.md`
2. `Brand/01-Systems/Marketing/Messaging-Strategy.md`
3. `Brand/01-Systems/Marketing/Content-Strategy.md`
4. `Brand/00-Brand-Core/Positioning.md`
5. `Brand/00-Brand-Core/Avatar.md`
6. `Brand/00-Brand-Core/Offers.md`
7. `Brand/06-DNA/Message.md`
8. `Brand/06-DNA/Funnel.md`
9. abstract strategy models
10. supporting evidence if needed

### 5. Operations Tasks
Examples:
- create SOP,
- build checklist,
- define QA standard,
- improve handoff,
- structure internal training.

Load in this order:
1. `Brand/05-Operations/`
2. relevant `Home` note or system note inside `01-Systems/`
3. `Brand/00-Brand-Core/Constraints.md`
4. relevant `06-DNA/` notes
5. evidence if needed for pattern extraction

### 6. Evidence Extraction Tasks
Examples:
- classify emails,
- turn voice notes into insights,
- extract objections,
- summarize real support friction.

Load in this order:
1. relevant evidence source in `03-Evidence/`
2. `02-Communication/Communication-Home.md`
3. `02-Communication/Manual/`
4. `00-Brand-Core/Voice-and-Tone.md`
5. `01-Systems/` relevant folder
6. `06-DNA/` relevant notes

The system should use canonical notes to interpret evidence, not the other way around.

### 7. Implementation Tasks
Examples:
- change website copy,
- update automation logic,
- restructure communications,
- modify operational workflows,
- adjust actual system files.

Load in this order:
1. relevant brand hub note
2. relevant canonical notes from the brand
3. relevant system home and child notes
4. communication rules if any output touches language
5. relevant DNA notes that explain core business logic
6. strategy models only if optimization is part of the request
7. evidence only for realism, examples, or anti-pattern detection

No implementation should start before returning a concise implementation brief.

## Required Pre-Implementation Brief
Before Claude Code or any AI implementation layer acts, it must produce a short structured brief including:
- active brand,
- task type,
- hub notes consulted,
- canonical notes consulted,
- supporting evidence consulted,
- constraints detected,
- systems affected,
- implementation objective,
- what should not be changed.

If the brief is weak, incomplete, or crosses brands, stop and reroute.

## Strategy Models Rule
`00-Trellis-Core/Strategy-Models/` is optional support, not default input.

Use strategy models only when the task benefits from abstract commercial optimization such as:
- offer improvement,
- pricing framing,
- objection handling logic,
- retention expansion,
- acquisition logic,
- testing logic,
- leverage decisions.

Do not use strategy models to overwrite brand voice.
Do not use strategy models when the task is purely mechanical.

## Evidence Handling Rule
Evidence should be loaded narrowly and intentionally.

Evidence is useful for:
- examples of how customers actually speak,
- recurring objections,
- proven wins,
- friction patterns,
- anti-examples,
- conversion clues,
- support failure patterns.

Evidence should not be treated as current truth unless it has been explicitly distilled into canonical notes.

## Archive Rule
Archived notes are not part of default retrieval.

Only load `99-Archive/` when:
- the user explicitly requests historical comparison,
- you need to understand why something changed,
- you are tracing prior experiments,
- you are auditing old processes.

## Note Priority Rule
When multiple notes exist, prefer in this order:
1. hub notes
2. manual notes
3. core notes
4. systems notes
5. DNA notes
6. evidence notes
7. archive notes

## Final Routing Rule
The system must route through connected notes, not isolated files and not folder names.

If a note is important enough to guide work, it must be connected.
If a task is important enough to implement, it must first load through the right hub.
If routing starts from the wrong brand, wrong hub, or wrong note type, stop and reroute before acting.

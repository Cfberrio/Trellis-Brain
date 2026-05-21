---
brand: Cross-Brand
area: evidence
subarea: meetings
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
owner: Trellis
last_updated: 2026-05-21
sensitivity: internal
hub_role: system-hub
---

# Meetings — Home

## Parent
- [[../Cross-Brand-Home|Cross-Brand Home]]

## Children
- [[Founder-Sessions/2026-05-21-Founders-Meet|Founder Sessions — most recent]]
- (Individual meeting notes appear below as they are extracted)

## Related
- [[../Synthesis/Synthesis-Home|Synthesis Home]] — recurring themes extracted across meetings

## Purpose
Meeting notes that do not belong to a single brand. Sources include:
- ClickUp AI note-taker output (SyncUp Notes:)
- Ad-hoc meeting docs (`<Name> - <date>`)
- Brand-bound meetings ARE NOT here — those go to the relevant brand's `03-Evidence/` folder

## Naming Convention
All meeting note files use the format:
```
YYYY-MM-DD-<topic>.md
```

Examples:
- `2026-05-21-Founders-Meet.md`
- `2026-05-20-Meeting-Eric.md`
- `2026-05-20-SyncUp-Needs.md`
- `2026-05-18-Sebastian.md`

## Index (filled as meetings are extracted)

### May 2026
- [[Founder-Sessions/2026-05-21-Founders-Meet|2026-05-21 — Founders Meet (equity + vesting + entity split)]]
- [[2026-05-20-SyncUp-Needs-Editor-Specialization|2026-05-20 — SyncUp Needs (editor specialization phasing)]]
- [[2026-05-20-SyncUp-Dev-Portable-Auto|2026-05-20 — SyncUp Dev (minimal stub)]]
- [[../Real-Estate/2026-05-20-Meeting-Eric|2026-05-20 — Meeting Eric (venue software + RevShare)]] *(in Real-Estate/)*
- [[../Real-Estate/2026-05-18-CIG-Property-Management|2026-05-18 — CIG property management + equity]] *(in Real-Estate/)*
- [[../AI-Systems/2026-05-20-Claude-Setup|2026-05-20 — Claude Setup (team onboarding)]] *(in AI-Systems/)*
- DR brand: [[../../Discipline-Rift/03-Evidence/Meetings/2026-05-18-SyncUp-Yassine-Luis-DR-Outreach|2026-05-18 — SyncUp Yassine + Luis (DR school outreach)]]
- DR brand: [[../../Discipline-Rift/03-Evidence/Meetings/2026-05-16-Call-Yassine-Franchise-Commitment|2026-05-16 — Call Yassine (franchise commitment)]]
- OEV brand: [[../../Orlando-Event-Venue/03-Evidence/Meetings/2026-05-18-Sebastian-OEV-Onboarding|2026-05-18 — Sebastian (OEV onboarding)]]
- [[2026-05-04-Nuevo-Flujo|2026-05-04 — Nuevo Flujo (workflow + content strategy)]]

### April 2026 and earlier
- [[../Real-Estate/2026-02-25-RV-x-5th-Floor|2026-02-25 — RV x 5th Floor (venue automation pitch)]] *(in Real-Estate/)*

## Founder Sessions
Recurring founder-level strategic meetings (Trelling, FOUNDERS MEET series) go in `Founder-Sessions/`.

## Extraction Workflow For Each Meeting
1. Read ClickUp doc page content via `clickup_get_document_pages`
2. Identify primary brand(s) referenced
3. If 80%+ brand-specific → route to that brand's `03-Evidence/Meetings/` instead
4. Else → write here with full transcript or summary
5. Extract action items + decisions → log in `../Synthesis/Cross-Brand-Decisions-Log.md`
6. Cross-reference any brand-specific decisions back to the brand's folder

---
brain_note_id: "dest:unknown:af4493044525bfe97aa3d0a538ca6da7"
canonical_key: "unknown/af4493044525bfe97aa3d0a538ca6da7"
brand_id: "unknown"
---
# Tarea: Data model & architecture (extensible to Phase 2)

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The data describes a specific church management system (St. Joseph Connect) involving sacraments, catechists, and rites. While it uses Trellis-standard tech (Supabase, Lovable), it does not align with the specific brands Cheese To Share, Discipline Rift, or Orlando Event Venue, nor is it a core Trellis internal tool.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3etj5v` · [Abrir en ClickUp](https://app.clickup.com/t/86e3etj5v)

**Contenido original**

Core schema in the st.-joseph-connect repo (supabase/migrations). Verified against the code Oct 2.

Core entities built: people, children + guardians, programs (with formation years and groups), terms, sessions, rooms, room bookings, registrations, form definitions, attendance, adults-receiving-sacraments profiles, sacrament paths per group, documents, payments, events, catechist assignments, rites booklets, calendar feeds, audit log.

ERD + review with Luis
Roles & permissions: admin, staff, data manager, catechist, volunteer + access by area (adults receiving sacraments, AFF, youth, children, events, everything)
Row-level security on every table, audit log (Settings → Audit). Backups: Lovable Cloud.
EN/ES: participant pages are bilingual; staff screens are English only
Phase 2 hooks: program kinds for youth, children, young adults, ministries; rooms
Households with two parents: children link to several guardians, but there is no household record
Shared family emails: matched by email + first name, "Data clear" flag
Emmaus server vs walker: stored on each registration from the import; no server form or screen yet
Call campaign log (caller, 3 attempts, outcome)
Rites booklets per year; formation year and groups

_Sincronizado por Brain: 2026-10-03T02:56:50.822Z_

---
brain_note_id: "dest:unknown:d9df054e8f43c575f2fa17c7ba185f6d"
canonical_key: "unknown/d9df054e8f43c575f2fa17c7ba185f6d"
brand_id: "unknown"
---
# Tarea: Radar B — Evaluate Capacitor mobile app for DR (push notifications + offline attendance)

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: Habla de varias marcas (`MULTI_BRAND`)
- reason: `The task primarily focuses on evaluating a mobile app strategy for Discipline Rift (DR), but explicitly includes a research objective to determine if the architecture can support Orlando Event Venue (OEV) and Cheese To Share (CTS) as separate apps.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3aukda` · [Abrir en ClickUp](https://app.clickup.com/t/86e3aukda)

**Contenido original**

Objective
Investigate whether packaging the current DR web app as a native mobile app (iPhone + Android) via Capacitor is worth pursuing, specifically for push notifications on coach-parent messages and offline attendance marking. Also explore whether the same setup could support multiple apps (DR, OEV, etc.) once the first one launches.
Context
Source: Cristian's Radar B, Growth, Week 1 (Sep 18) —

What it is: Package the existing DR web app as an iPhone/Android app using Capacitor. Same backend, same accounts, plus push notifications for coach-parent messages.

What problem it solves: Parents currently don't know when a coach replies unless they manually visit the site. Coaches mark attendance from their phones with unreliable signal. No push today, only email/SMS via GHL.

What we do today: Web responsive + email/SMS notifications from GHL. No push.

Cost: USD $124 first year (Apple + Google developer accounts), zero licensing. Real cost is dev time: 6 phases, and every native UI change goes through app store review. Big unverified risk: if the project depends on server-side rendering, Capacitor can't package it directly and a separate mobile client would need to be built.

Related task:  (Cristian's original cost evaluation)

Cristian's recommendation: Investigate, don't implement yet. Without data on unread messages, the app is cosmetic, not a business case.
To Keep in Mind
Validation first: Before approving anything, measure how many coach-to-parent messages go unread for 24+ hours during Fall 2026. If the number is low, improving the existing SMS notification is cheaper and faster.
SSR risk: Verify whether DR's current stack uses server-side rendering. If it does, Capacitor won't wrap it cleanly, and the scope explodes into building a standalone mobile client.
Multiple apps question (Luis): Once the first Capacitor app ships, can the same architecture produce separate apps for OEV, CTS, or other brands without duplicating the full build pipeline? Research what's shared vs. what's per-app (certificates, store listings, push config, codebase forks).
Store review friction: Every native interface change requires Apple/Google review cycles. Factor this into ongoing maintenance estimates, not just launch cost.

**Comentarios**

- **2026-09-21 · Cristian Berrío**: DR_Mobile_Capacitor_Final_Research.md
- **2026-09-22 · Luis Torres**: Hermano, entremos en llamda a las 10:30 para conversar sobre esto @Cristian Berrío

_Sincronizado por Brain: 2026-10-01T03:13:09.774Z_

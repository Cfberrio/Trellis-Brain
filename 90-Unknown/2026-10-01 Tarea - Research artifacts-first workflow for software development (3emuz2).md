---
brain_note_id: "dest:unknown:62f63d47512a0bca4e314d91348616d8"
canonical_key: "unknown/62f63d47512a0bca4e314d91348616d8"
brand_id: "unknown"
---
# Tarea: Research artifacts-first workflow for software development

## Corrección

marca:
estado: abierta

_Escribe Core, DR, CTS, OEV o descartar después de `marca:`. Brain lo aplica en el siguiente ciclo._

## Fuente

**Por qué está aquí**

- Motivo: La IA no está segura de la marca (`AI_UNSURE`)
- reason: `The document discusses internal software development workflows, specifically integrating Claude Artifacts and Lovable. While it mentions 'Cristian', this is generic developer process research and does not contain specific references to the business domains of Cheese To Share, Discipline Rift, or Orlando Event Venue, nor does it mention Trellis Core specifically.`
- deterministicReason: `BRAND_VALUE_MISSING`
- Fuente: Tarea `86e3emuz2` · [Abrir en ClickUp](https://app.clickup.com/t/86e3emuz2)

**Contenido original**

Objective
Figure out how to integrate Claude Artifacts into our software development workflow so we can visually prototype and iterate on UI/UX before writing production code, then push to Lovable when ready to build.
Context
Right now we go from idea straight to Lovable. The question is whether we can add an artifacts step in between to nail down visuals and interactions first, saving build credits and iteration cycles in Lovable.

Here's what's possible based on current tooling:

Claude Artifacts (free/Pro/Max)
Create interactive UI prototypes, dashboards, mini-apps directly in the Claude chat
Real-time preview panel: see working code instantly as Claude generates it
Iterate with follow-up prompts ("make buttons bigger", "change color scheme", "add a sidebar")
Fork conversations to try different design directions without losing previous versions
Publish and share via link for team review
Copy the code out when ready

Claude Design (newer, higher-fidelity)
Import your codebase/component library so prototypes use your real components and design tokens
Generate screens that match your existing product's look and feel
Export + hand off to Claude Code with full design intent preserved
Great for when you already have a design system and want consistency

Artifacts → Lovable pipeline
Build the visual prototype in Claude Artifacts until the UI feels right
Copy the artifact code and paste into Lovable as the starting point
Or use the Lovable MCP plugin for Claude Code: auto-push to GitHub, auto-deploy to Lovable (3-5x faster than manual)
Lovable has a Claude Code plugin (lovable-claude-code) that syncs changes through GitHub and auto-deploys
There's also a native Lovable connector in Claude that lets you create/iterate/deploy Lovable projects from within Claude

Proposed workflow:
Describe the feature/screen to Claude → get an artifact prototype
Iterate on visuals, layout, interactions through conversation
Share the published artifact link with the team for feedback
Once approved, export the code to Lovable (via copy-paste, GitHub sync, or MCP)
Use Lovable to add backend, auth, database, and deploy
To Keep in Mind
Artifacts are single-page HTML/CSS/JS: great for individual screens and components, not full multi-page apps
Claude Design requires Claude Code v2.1.182+ for the design skill, and v2.1.209+ for MCP connector support
Lovable now has two architectures: new projects (post-April 2026) use TanStack Start (SSR), older ones use Vite SPA. The plugin auto-detects
Some things still need Lovable's Cloud UI directly: new database tables, RLS policies, secrets management
Test this on a small upcoming feature first before changing the whole workflow
Document the process so Cristian and the team can follow it independently

**Comentarios**

- **2026-09-28 · Cristian Berrío**: Research done. Recommendation: use artifacts only as a one-shot visual check for new screens, not as an iteration loop. They burn a huge amount of tokens when you iterate, so they should not be used for every case. Next step is a pilot on one small feature. What I measured I went through our own Claude Code logs. 3 sessions published artifacts, and I isolated the artifact part of each one: A normal work session without artifacts processes about 7.7M tokens in total (median of 195 sessions). The OEV artifact loop alone was about 35 normal sessions. The HTML itself is cheap. 13 publishes added up to about 33K output tokens. The cost comes from iterating: every "make the button bigger" round re-reads the whole conversation (200K to 500K tokens each turn), and screenshots make it heavier. One pass is cheap. A loop is not. Caveat: these numbers are an upper bound because the artifact part of each session includes a bit of other work. They only cover Claude Code, not the claude.ai chat, where the same problem shows up as hitting the plan limit faster. Two assumptions in this task that don't hold Copying artifact code into Lovable. An artifact is one HTML file. Lovable builds in React, Tailwind and shadcn, so it rewrites the code anyway. The useful thing from the artifact is the approved look, not the code. Give Lovable a screenshot and a short spec. Saving Lovable credits. Our August credit audit found Lovable bills for database uptime, which runs whether we build or not (the per-category breakdown is still pending). Build messages do cost credits, but the savings are smaller than the task assumes, and we would be moving the cost to Claude usage. When to use an artifact Use it for: A new screen or flow nobody has seen yet When Luis or a client needs to approve the look before we build Comparing 2 or 3 layout directions Skip it for: Changes to existing DR, OEV or CTS screens. Edit the repo directly, it already has the real components and design tokens. Backend, database, RLS, secrets Copy changes and emails that already have a template How to run it (when it applies) Start a fresh Claude session. Small context keeps every turn cheap. Describe the screen in one message: purpose, user, main action, brand, and the brand colors and fonts. Get one artifact. Share the link for feedback. Maximum 3 feedback rounds. Collect all changes into one message per round, not one change per message. No screenshot verification loops. Once approved, take a screenshot and write a short spec (layout, states, actions, data it needs). Send the screenshot and spec to Lovable (or build it in the repo with Claude Code). Lovable handles backend, auth, database and deploy. Risks If the prototype doesn't get the brand tokens, it drifts from the real product and Lovable has to redo it. Existing apps auto-deploy from GitHub, so any code change there goes through a branch and review, not straight to main.
- **2026-09-29 · Luis Torres**: no lo veo tan efectivo, pensamientos @Cristian Berrío?
- **2026-09-29 · Cristian Berrío**: Honestamente yo nunca utilizo artifact, maybe considero que para las cosas que haces tu, en temas de montar planificacion o cuando quieras realizar un rebranding visual estaria bien usarlo. Como por ejemplo cuando hicimos lo de DR, tu usaste artifact y me ayudo a ver facilmente que era lo que querias hacer
- **2026-09-29 · Cristian Berrío**: Entonces diria usarlo para casos como esos porque consume demasiados tokens

_Sincronizado por Brain: 2026-10-01T17:57:05.696Z_

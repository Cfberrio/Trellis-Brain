---
brand: Cross-Brand
area: reference
note_type: inventory
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp chat workspace (54 channels) — swept 2026-05-21"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# ClickUp Chat Channels — Inventory

## Parent
- [[01-Brands/Cross-Brand/Reference/Reference-Home|Cross-Brand Reference]]

## Related
- [[01-Brands/Cross-Brand/Cross-Brand-Home|Cross-Brand Home]]

## Purpose

Authoritative inventory of all ClickUp chat channels in the Trellis workspace. Per locked PLAN-v2 rule, **only public channels are eligible for sweeps**. DMs + private channels stay out of the vault.

## Sweep policy (locked)

- ✅ Public channels — eligible for content sweep + extraction
- ❌ DMs — never extracted
- ❌ Private channels — never extracted
- ❌ Credentials channel — hard exclude regardless of visibility

## Public channels — by brand / function

### Trellis-Fields (TF)
| Channel | ID | Purpose |
|---|---|---|
| Trellis Fields | `7-9017418223-8` | Main TF channel |
| TF \| Planning 🪵 | `8cqnrff-13937` | TF planning |
| TF \| Content Ideas 🌱 | `8cqnrff-5217` | TF content brainstorm |
| TF \| Content Methods 🪵 | `8cqnrff-15437` | TF content methodology |
| TF \| AI Planning 🌱 | `8cqnrff-16697` | TF AI work |
| Trellis | `6-901708988595-8` | Trellis (newer) |

### Discipline-Rift (DR)
| Channel | ID | Purpose |
|---|---|---|
| DR \| Planning 🏐 | `8cqnrff-12757` | DR planning |
| DR \| Franchise 🏐 | `8cqnrff-9037` | DR franchise expansion (RV proof) |
| DR \| Content Ideas 🏐 | `8cqnrff-1377` | DR content brainstorm |
| Discipline Rift | `6-901708902568-8` | Discipline Rift (newer) |

### Cheese-To-Share (CTS)
| Channel | ID | Purpose |
|---|---|---|
| CTS \| Planning 🧀 | `8cqnrff-13717` | CTS planning |
| CTS \| Content Ideas 🧀 | `8cqnrff-1337` | CTS content brainstorm |
| Cheese To Share | `6-901707720461-8` | CTS (newer) |
| CTS | `4-90174809638-8` | CTS (Director profile) |

### Orlando-Event-Venue (OEV)
| Channel | ID | Purpose |
|---|---|---|
| OEV 𝄡 | `8cqnrff-18117` | OEV operations + comms |

### LT (Lab Trellis / new brand)
| Channel | ID | Purpose |
|---|---|---|
| LT \| Planning 🥼 | `8cqnrff-16017` | LT planning |
| LT \| Content Ideas 🥼 | `8cqnrff-16197` | LT content brainstorm |

### Tech / Dev
| Channel | ID | Purpose |
|---|---|---|
| Dev 💻 | `8cqnrff-2077` | Dev work |
| DEVs | `8cqnrff-8397` | Dev team |
| Developer 💻 | `4-90174810008-8` | Developer profile |
| Tech Support 🤖 | `8cqnrff-12717` | Tech support |
| COMANDOS PARA GITHUB | `8cqnrff-15717` | GitHub commands reference |
| CLAUDE-TRELLIS | `8cqnrff-15617` | Claude usage notes |

### Operations / Cross-team
| Channel | ID | Purpose |
|---|---|---|
| Welcome | `8cqnrff-77` | Workspace intro |
| Annoucements 📢 | `8cqnrff-15117` | Announcements |
| Level Ups 🧩 | `8cqnrff-10337` | Wins / level-ups |
| Community Mgmt 📈 | `8cqnrff-9297` | Community management |
| Coworking 🧠 | `8cqnrff-9077` | Coworking |
| Book Club 📕 | `8cqnrff-9537` | Book club |
| Trellis Merch 👕 | `8cqnrff-17617` | Merch project |
| Planeacion y Estrategia | `6-901708810999-8` | Planning + strategy |
| AI News 🔌 | `8cqnrff-13237` | AI news feed |
| Editing News 📸 | `8cqnrff-13517` | Editing news feed |

### Team members
| Channel | ID | Purpose |
|---|---|---|
| Creators 🪴 | `4-90172390644-8` | Creators team |
| Julián | `5-90174403476-8` | Julián's channel |

### Hard exclude
| Channel | ID | Purpose |
|---|---|---|
| Credentials | `5-90176524940-8` | ❌ **Never extract** (credentials/secrets) |

## Private channels (never extracted)

For audit visibility only. Per locked rule, content is **never** swept from these.

- Needs ⚡️ (`8cqnrff-8037`)
- UPDATES (`8cqnrff-12697`)

## DMs (never extracted)

Multiple direct-message conversations exist in the workspace. Per locked rule, content is **never** swept.

## When to sweep a public channel

A public channel is worth sweeping when:
1. Strategic decision was discussed there (look first in `| Planning` channels).
2. Founder posted a directive that didn't make it to a doc.
3. A brand-defining moment / win / lesson was logged.

Default: **don't** sweep unless looking for something specific. Channels are noisy. Docs + meeting notes carry the canonical signal.

## How to add a new channel to this inventory

1. Pull latest channel list via `mcp__clickup__clickup_get_chat_channels`.
2. Filter to `visibility: PUBLIC`.
3. Add new public channels to the matching brand / function table above.
4. Update `last_updated` frontmatter.

## Total counts (2026-05-21)

- Total channels in workspace: **54**
- Public channels: **~40** (eligible for sweep)
- Private channels: **2** (excluded)
- DMs: **~12** (excluded)
- Credentials channel: **1** (hard exclude)

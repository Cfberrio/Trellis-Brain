# Metadata Standard

## Purpose
This document defines the metadata standard for the Trellis Brain.

Metadata exists to make notes:
- retrievable,
- filterable,
- distinguishable by role,
- safer for AI routing,
- easier to maintain over time.

Use metadata to clarify what a note is, how reliable it is, how current it is, and whether it should be loaded by AI systems.

## Principle
Metadata should stay small, atomic, and machine-readable.

Put business logic in the body of the note, not in metadata.

Metadata helps routing. Body links help the graph.
Do not rely on metadata alone to keep the vault connected.

## Graph Connectivity Rule
If the goal is strong graph connectivity, the body of the note must contain real internal links.

Metadata may help with filtering and routing, but the graph should be designed around explicit links inside sections such as:
- `## Parent`
- `## Children`
- `## Related`
- `## Strategy References`

### Key Rule
A note is not considered structurally complete until:
- its metadata is present,
- its body contains the required internal links for its role,
- and it is discoverable through a hub note.

## Required Rules
### Rule 1
Every canonical note should have metadata.

### Rule 2
Every note used by AI routing should include `brand`, `area`, `note_type`, `status`, and `used_for_ai`.

### Rule 3
Only canonical notes should use `canonical: true`.

### Rule 4
Evidence notes should almost always use `canonical: false`.

### Rule 5
Archived notes should use `status: archived`.

### Rule 6
Do not create custom metadata keys casually. Reuse the shared schema whenever possible.

### Rule 7
Do not use metadata as a substitute for actual note links.

## Core Metadata Schema
These are the standard metadata keys for the vault.

```yaml
brand:
area:
subarea:
note_type:
status:
canonical:
used_for_ai:
source_type:
source_reference:
owner:
last_updated:
sensitivity:
related_systems:
related_notes:
hub_role:
tags:
```

## Field Definitions
### `brand`
The brand this note belongs to.

Allowed values:
- `Trellis-Core`
- `Cheese-To-Share`
- `Discipline-Rift`
- `Orlando-Event-Venue`
- `Reliable-Venues`
- `Trellis-Fields`

Use `Trellis-Core` only for shared infrastructure and abstract models.

### `area`
The top-level functional layer of the note.

Allowed values usually include:
- `brand-core`
- `systems`
- `communication`
- `evidence`
- `projects`
- `operations`
- `dna`
- `strategy-models`
- `system`

### `subarea`
The more specific layer inside the area.

Examples:
- `marketing`
- `sales`
- `website`
- `finance`
- `manual`
- `templates`
- `email`
- `whatsapp`
- `voice-notes`
- `qa`
- `training`

### `note_type`
Defines what kind of note this is.

Recommended values:
- `home`
- `core`
- `manual`
- `template`
- `system`
- `dna`
- `sop`
- `checklist`
- `evidence`
- `insight`
- `project`
- `strategy-model`
- `archive`

### `status`
Defines the operational status of the note.

Allowed values:
- `active`
- `draft`
- `review`
- `deprecated`
- `archived`

Use:
- `active` for current trusted notes,
- `draft` for incomplete notes,
- `review` when the note should not yet be treated as final,
- `deprecated` when replaced but still visible,
- `archived` when no longer part of active retrieval.

### `canonical`
Boolean field.

Allowed values:
- `true`
- `false`

Use `true` only when the note defines current truth.

### `used_for_ai`
Boolean field.

Allowed values:
- `true`
- `false`

Use `false` for notes that should not normally be loaded into AI context.
Examples:
- noisy raw dumps,
- temporary scratch notes,
- irrelevant archived material,
- sensitive internal notes not intended for retrieval.

### `source_type`
Defines where the note came from.

Recommended values:
- `curated`
- `imported`
- `derived`
- `raw`
- `transcript`
- `email`
- `whatsapp`
- `voice-note`
- `call`
- `meeting`
- `ai-generated`

### `source_reference`
Free text or link pointing to the origin.

Examples:
- file path,
- email date,
- call transcript ID,
- imported document name,
- source note link.

If using an internal link in a property, wrap it in quotes.

### `owner`
The human owner or maintainer of the note.

Examples:
- `Luis`
- `Maria`
- `Trellis`
- `Unassigned`

### `last_updated`
Date in ISO format.

Recommended format:
`YYYY-MM-DD`

### `sensitivity`
How sensitive the note is.

Allowed values:
- `public`
- `internal`
- `restricted`

Use:
- `public` for information safe to reuse broadly,
- `internal` for normal business notes,
- `restricted` for notes that should be handled carefully.

### `related_systems`
List of systems affected or referenced.

Examples:
- `website`
- `clickup`
- `ghl`
- `n8n`
- `reporting`
- `email`
- `dashboard`
- `payments`

### `related_notes`
List of strongly connected notes.

Use internal links in quotes.

Example:
```yaml
related_notes:
  - "[[Brand-Home]]"
  - "[[Voice-and-Tone]]"
```

This field helps filtering and context packaging, but it does not replace body links.

### `hub_role`
Defines the structural role of the note in the graph and retrieval system.

Recommended values:
- `root`
- `brand-hub`
- `system-hub`
- `communication-hub`
- `dna-hub`
- `leaf`

Use:
- `root` for `Trellis-Home`,
- `brand-hub` for `Brand-Home`,
- `system-hub` for notes like `Marketing-Home` or `Sales-Home`,
- `communication-hub` for `Communication-Home`,
- `dna-hub` for `DNA-Home`,
- `leaf` for non-hub child notes.

### `tags`
Optional list for lightweight filtering.
Do not use tags as a replacement for structure.

## Minimum Required Metadata by Note Type
### Canonical Core Notes
Use for:
- Brand-Home
- Positioning
- Offers
- Value-Proposition
- Voice-and-Tone
- Language-Rules
- Constraints
- Opportunities
- KPIs

Recommended minimum:
```yaml
brand:
area: brand-core
subarea:
note_type: core
status: active
canonical: true
used_for_ai: true
source_type: curated
owner:
last_updated:
sensitivity: internal
related_systems: []
related_notes: []
hub_role: leaf
```

### Home Notes
Use for:
- Trellis-Home
- Brand-Home
- Marketing-Home
- Sales-Home
- Communication-Home
- DNA-Home

Recommended minimum:
```yaml
brand:
area:
subarea:
note_type: home
status: active
canonical: true
used_for_ai: true
source_type: curated
owner:
last_updated:
sensitivity: internal
related_systems: []
related_notes: []
hub_role:
```

### Communication Manual Notes
Use for:
- Communication-Manual
- Voice-Definition
- Tone-Rules
- Sales-Messaging
- Follow-Up-Messaging
- Support-Messaging
- Payment-Messaging

Recommended minimum:
```yaml
brand:
area: communication
subarea: manual
note_type: manual
status: active
canonical: true
used_for_ai: true
source_type: curated
owner:
last_updated:
sensitivity: internal
related_systems:
  - email
related_notes: []
hub_role: leaf
```

### Systems Notes
Use for:
- Sales-Process
- Lead-Definition
- Follow-Up-Rules
- Pricing-Logic
- Payment-Rules
- Delivery-Process
- Support-Process

Recommended minimum:
```yaml
brand:
area: systems
subarea:
note_type: system
status: active
canonical: true
used_for_ai: true
source_type: curated
owner:
last_updated:
sensitivity: internal
related_systems: []
related_notes: []
hub_role: leaf
```

### DNA Notes
Use for:
- Message
- Offer
- Funnel
- Sales
- Delivery
- Retention
- Metrics

Recommended minimum:
```yaml
brand:
area: dna
subarea:
note_type: dna
status: active
canonical: true
used_for_ai: true
source_type: derived
owner:
last_updated:
sensitivity: internal
related_systems: []
related_notes: []
hub_role: leaf
```

### Evidence Notes
Use for:
- emails,
- SMS,
- WhatsApp,
- transcripts,
- voice notes,
- extracted insights,
- examples,
- anti-examples.

Recommended minimum:
```yaml
brand:
area: evidence
subarea:
note_type: evidence
status: active
canonical: false
used_for_ai: true
source_type:
source_reference:
owner:
last_updated:
sensitivity: internal
related_systems: []
related_notes: []
hub_role: leaf
```

### Archive Notes
Recommended minimum:
```yaml
brand:
area:
subarea:
note_type: archive
status: archived
canonical: false
used_for_ai: false
source_type:
owner:
last_updated:
sensitivity: internal
related_systems: []
related_notes: []
hub_role: leaf
```

## Body Link Standard for Canonical Notes
Metadata is not enough. Canonical notes should also include explicit body links.

### Required Body Sections for Hub Notes
Hub notes should usually include:
- `## Parent`
- `## Children`
- `## Related`

### Required Body Sections for Leaf Notes
Leaf notes should usually include:
- `## Parent`
- `## Related`

### Optional Strategy Link Section
When helpful:
- `## Strategy References`

Example:
```md
## Parent
- [[Brand-Home]]

## Related
- [[Offers]]
- [[Message]]

## Strategy References
- [[Value-Equation]]
```

## Naming Consistency Rule
To improve links, routing, and graph readability:
- use stable note names,
- avoid duplicate canonical note names inside the same brand,
- use explicit brand-specific names for top-level hub notes when needed.

Examples:
- `Orlando Event Venue - Brand-Home`
- `Reliable Venues - Brand-Home`
- `Cheese To Share - Brand-Home`

This is especially important for notes that will be linked from Trellis-Core.

## Final Metadata Rule
Metadata supports routing.
Body links support the graph.
Hub notes support retrieval.

If any of those three layers are missing, the note is not fully integrated into the Trellis Brain.

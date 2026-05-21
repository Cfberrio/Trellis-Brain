---
brand: Trellis-Fields
area: operations
subarea: skool-methods
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-7937 page 8cqnrff-5057 (HERRAMIENTAS SKOOL / How to Set Up Killer Lead Magnets)"
owner: María José
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Lead Magnet Setup — End-to-End SOP

## Parent
- [[../../00-Brand-Core/Brand-Home|TF Brand Home]]
- [[../../01-Systems/Marketing/Lead-Magnet-Strategy|Lead Magnet Strategy]]

## Related
- [[OG-Ideas-And-Virality|OG Ideas + Virality Method]]
- [[../../01-Systems/Marketing/CTA-Formula|CTA Formula]]
- [[../../02-Communication/Hook-Library-TF|TF Hook Library]]

## Purpose
End-to-end workflow for setting up lead magnets + evergreen comment CTAs on Instagram using **ManyChat + Notion + AI**. Reusable across all Trellis brands.

## Phase 1 — Decide What The Lead Magnet Is

Ask the AI (content bot primed with ICP sheet):
> "Based on my ICP sheet, what are the 3 biggest problems my audience is dealing with?"

Example output:
1. Inconsistent client flow and lead generation
2. Content paralysis and burnout
3. No scalable systems to support growth

**Create one lead magnet per pain point.** These become the **core 3 lead magnets** you cycle forever.

## Phase 2 — Build The Lead Magnet (Notion)

For each pain point:

1. Create a new Notion page (or any platform)
2. Title: "How to solve [pain point]"
3. Add icon + branded banner
4. Record a Loom video walking through how to solve the problem
5. Embed Loom + 3-step summary in the page
6. End with CTA: "If you'd like to see how me and my team could implement this for your business, just click below to book in a call"
7. Embed Calendly (or equivalent) below the CTA

Then create a parent page called **"Freebies"** and move all lead magnets inside.

Publish all pages so they're live URLs.

## Phase 3 — Set Up Comment CTA Automation (ManyChat)

### Folder setup
Create folder: `Evergreen Implement CTAs`

### Per lead magnet — create a new automation
1. **Trigger:** User comments on post or reel
2. **Apply to:** All posts or reels
3. **Keyword:** unique 4-char + number combo (e.g., `flow3`, `burnout3`, `scale3`)
   - The number prevents accidental triggering when someone comments a similar word
4. **Comment reply:** "Check DMs fam" / "Gotcha" / "Sent it over"

### DM message setup
Don't ask a qualifying question first — send the resource right away.

Template:
> "Hey [first name]! Here's your authority engine guide. Here's your guide to fix [problem]."

Add a **quick reply button**:
- "Yes, send it over"

When clicked → open website with the Notion lead magnet URL.

### Make it live
- Click "Set Live"
- Test from an alt account by DMing yourself + checking the flow

### Duplicate for each lead magnet
- Duplicate the automation
- Change keyword (e.g., `burnout3` → `scale3`)
- Change website URL
- Change message body to match the new pain point
- Set live

## Phase 4 — Use Forever

After setup, every video uses ONE of the 3 CTA keywords:
- `flow3` / `burnout3` / `scale3`

In the video script, end with: **"Comment [keyword] and I'll send you my free guide on [topic]."**

ManyChat handles the rest. **Never touch ManyChat again** (or at least for quite a while).

## Why This Works (per Hormozi-aligned [[../../01-Systems/Marketing/Lead-Magnet-Strategy|Lead Magnet Strategy]])
1. Solves a small problem (the guide gives real value)
2. Reveals a bigger problem (implementation, scale, integration)
3. Increases desire for main offer (call → "see how me and my team could implement this")

> Never resolve the central problem completely. If you do, there's no reason to buy.

## Quality Checklist
- [ ] 3 core lead magnets created in Notion
- [ ] Each has: title, icon, banner, Loom video, 3-step summary, CTA + Calendly embed
- [ ] All 3 are published as live URLs
- [ ] 3 ManyChat automations created with unique numbered keywords (e.g., `flow3` not `flow`)
- [ ] Each automation tested from an alt account
- [ ] Saved in `Evergreen Implement CTAs` folder
- [ ] CTA in video script matches the keyword exactly

## Anti-Patterns
- ❌ Don't make the keyword too generic (`flow` triggers on "flow of your hair")
- ❌ Don't ask qualifying questions in the first DM (kills momentum)
- ❌ Don't mix CTA types in the same video (only one keyword per video)
- ❌ Don't recreate Notion pages — duplicate them

## Source
Internal training video. Method authored by Trellis Fields team.

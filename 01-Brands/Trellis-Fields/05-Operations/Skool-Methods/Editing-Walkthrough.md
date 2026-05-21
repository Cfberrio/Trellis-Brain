---
brand: Trellis-Fields
area: operations
subarea: skool-methods
note_type: sop
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-7937 page 8cqnrff-5297 (HERRAMIENTAS SKOOL / Editing Walkthrough — Premiere Pro full SOP)"
owner: María José
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Editing Walkthrough — Premiere Pro SOP

## Parent
- [[../../00-Brand-Core/Brand-Home|TF Brand Home]]
- [[../../05-Operations/Team/Team-Roles|TF Team Roles]]

## Related
- [[Lead-Magnets-Setup|Lead Magnet Setup]]
- [[OG-Ideas-And-Virality|OG Ideas + Virality]]

## Purpose
End-to-end Premiere Pro editing SOP for Trellis content (YouTube + reels). Same workflow per piece — minimizes decision fatigue and ensures consistent quality.

## Pre-Production Setup

### Project structure
1. Create new sequence: **HD 1080p**
2. Create bins:
   - `Footage`
   - `Sequences`
3. Drop all source files in `Footage`

### Footage scaling
- If footage = 4K and sequence = 1080p → **scale to 50%** to fit
- If footage already 1080p → scale = 100%

## Step 1 — Audio Fix (Amplify + Hard Limiter)

For every voice clip:
1. **Effects → Amplify** → drag onto clip
   - Edit value: **+15 dB** (or +20 dB for quiet recordings)
2. **Effects → Hard Limiter** → drag onto clip
   - Cut at **-1.5 dB to -3 dB** (matches peak across clips)

> This makes voice clear and consistent across all takes.

Copy these two effects → paste onto every voice clip.

## Step 2 — Transcribe + Text-Based Editing

1. Open **Window → Text panel**
2. Click **Transcript** → transcribe the clip
3. Use transcript to navigate and select sections
4. Highlight unwanted text → **Backspace** to delete (Premiere auto-cuts the video)

> This is dramatically faster than manual scrubbing through video.

### Use case: removing bad takes
- Identify the line read in transcript
- Find the last clean take of the same line
- Cut everything before that take

## Step 3 — Structure The Video

Typical YouTube video structure:
1. **Hook** (A-roll opening)
2. **Loom or value section** (educational tutorial)
3. **Outro** (call to action)

Color-code the timeline:
- Right-click clip → **Label** → choose color
- Use distinct color for Loom/value section so you can visually spot the structure

## Step 4 — Color Grading (Adjustment Layer Method)

### Create adjustment layer
1. New → **Adjustment Layer**
2. Drag onto timeline above all video clips
3. Stretch over entire video

### Apply LUT
1. Open **Lumetri Color**
2. **Basic Correction → Input LUT**
3. For log footage → use **London LOG LUT** (recommended)

### Install custom LUTs (one-time setup)
1. Finder → Applications
2. Right-click Premiere → **Show Package Contents**
3. Contents → Lumetri → Luts → Creative
4. Paste your LUT files here
5. Restart Premiere

### Color adjustments (Basic Correction)
- **Exposure:** +0.3 (slightly brighter)
- **Contrast:** +25
- **Saturation:** ~150 (brings color back into skin)
- **Temperature:** +5 (slight warmth)
- **Tint:** +1 to +2 (slight pink)

## Step 5 — Halation Effect (Cinematic Glow)

1. Duplicate the color-grade adjustment layer
2. Remove the LUT from the duplicate (only effects remain)
3. Add **ASC CDL** effect:
   - Green slope: 0
   - Blue slope: 0
   - Saturation: 0.7
4. Add **Gaussian Blur**:
   - Blurriness: 50–100
5. Change **Blend Mode** of this adjustment layer → **Lighten**
6. Adjust **Opacity** → 50–75% (subtle, not in-your-face)

> Effect: subtle halation around the subject — vintage cinematic glow.

## Step 6 — Optional Glow Layer

1. Duplicate the color-grade layer (again, no LUT)
2. Add **VR Glow** effect:
   - Luma Threshold: 0.5
   - Glow Brightness: 0.5
3. Adjust opacity to taste

## Step 7 — Film Grain Overlay

1. Import a **heavy grain** clip (Dylan John heavy grain, or similar)
2. Drag onto timeline above all layers
3. Unlink + delete the audio
4. Scale down to 50% if 4K
5. Copy and paste end-to-end across entire timeline
6. Select all grain clips → **Nest** (Sequence → Nest)
7. Change blend mode of nested sequence → **Overlay**
8. Opacity → 50%

## Step 8 — Cut Color/Effects Around Loom Section

The Loom video does NOT get color graded (it's already screen-captured native colors).

1. Cut the color-grade adjustment layer at the start of the Loom
2. Cut again at the end of the Loom
3. Delete the middle segment of the adjustment layer

> Result: A-roll has the full color grade + halation + glow + grain. Loom section is left untouched.

## Step 9 — Graphics + B-Roll Overlays (optional)

For graphics:
1. Drop in image (screenshot, result, relevant visual)
2. Move/animate position over timeline section where it's needed
3. Flash up briefly during the line of speech that references it

## Crash Recovery (if Premiere crashes)
If Premiere crashes and you lose progress on reopening the project:

1. Go to the project folder
2. Look for sub-folder: **Adobe Premiere Auto Save**
3. Open the **most recent** auto-save file
4. Most progress should be there

> Lesson: Premiere auto-saves frequently. Don't panic.

## Standard Checklist (every export)
- [ ] Audio: Amplify + Hard Limiter on every voice clip
- [ ] Bad takes removed via transcript editing
- [ ] Color grade applied (adjustment layer with LUT + Basic Correction)
- [ ] Halation effect (optional)
- [ ] Glow effect (optional)
- [ ] Film grain overlay
- [ ] Loom/value section excluded from color grade
- [ ] Subtitles added (always — many viewers no audio)
- [ ] Final review at full playback

## Source
Internal training video. Premiere Pro SOP authored by Trellis Fields team.

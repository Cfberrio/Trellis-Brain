---
brain_note_id: "note:282db3f7-d8fa-4f8e-831a-538821efa365"
canonical_key: "audio-silence-removal-pipeline"
brand_id: "trellis_core"
---
# Audio-Silence-Removal-Pipeline

## Canonical Statement

- **process**: Pipeline for automatic silence removal: 1. Transcribe with Whisper to JSON to identify voice segments. 2. Extract start/end times of voice segments. 3. Use FFmpeg to cut segments. 4. Concatenate segments into a final audio file.
- **rule**: To prevent robotic-sounding cuts, apply padding to segments: subtract 0.1s from start (min 0) and add 0.1s to end for a natural margin.
- **fact**: The pipeline is more precise because it detects voice segments and eliminates everything else, rather than attempting to detect silence directly.

## Evidence Log

- 2026-10-15T07:43:10.615Z — `clickup_doc_page:8cqnrff-13877/8cqnrff-15037`
  - `e1` (source_body): whisper audio.wav --model base --output_format json ... ffmpeg -i audio.wav -ss 0.5 -to 3.2 part1.wav ... ffmpeg -f concat -safe 0 -i list.txt -c copy output.wav
  - `e2` (source_body): Padding (MUY IMPORTANTE) Para que no suene robótico: start = max(0, seg["start"] - 0.1) end = seg["end"] + 0.1 Esto deja un pequeño margen natural.
  - `e3` (source_body): Este pipeline funciona porque: 👉 No detectas silencios directamente 👉 Detectas voz, y todo lo demás se elimina Eso lo hace mucho más preciso.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-13877/8cqnrff-15037`
- Source hash: `79de685d2dbbc837b3a080666972eb122bf4ab9d066526360d229d9d724258d0`
- Observed at: 2026-10-15T07:43:10.615Z
- Agent run: `617769ef-e5d8-4e89-adce-d2c6c1143cac`
- Validation run: `550d8a97-c738-4d2f-bc66-8b991e5f63d2`

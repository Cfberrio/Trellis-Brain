---
brain_note_id: "note:3ff10cd6-94ca-475e-9faa-22b595e16cc6"
canonical_key: "ai-content-engine-workflow"
brand_id: "trellis_core"
---
# AI Content Engine Workflow

## Canonical Statement

- **process**: The AI Content Engine workflow requires three ingredients: business context (constant), data (channel-specific training bank), and prompts (channel-specific instructions).
- **rule**: The system architecture for each brand must follow a four-folder structure: AI assets/ containing business context/, data/, and prompts/.
- **process**: Business context is defined by a 12-question questionnaire covering company purpose, industry, customer transformation, pain points, core offer, and brand voice.
- **rule**: AI should build the template and extract voice/patterns, but the human must always provide the core idea; AI never decides the topic.
- **rule**: Longer and more specific prompts result in tighter, more accurate output, whereas vague prompts produce generic 'AI slop'.

## Evidence Log

- 2026-10-17T07:14:15.551Z — `clickup_doc_page:8cqnrff-20197/8cqnrff-27097`
  - `e1` (source_body): The fix is a workflow, and a workflow is just three ingredients fed to the model every time: business context, data, and prompts.
  - `e2` (source_body): The whole system lives in four folders on the desktop. Build this exactly, once, per brand: AI assets/ ... business context/ ... data/ ... prompts/
  - `e3` (source_body): Hormozi feeds the AI a 12-question business questionnaire before it writes anything. The answers become one file, my_business_context.txt
  - `e4` (source_body): AI builds the template, never the idea. It extracts voice, structure and patterns, then waits. You always feed the idea.
  - `e5` (source_body): Longer and more specific = better output. ... Counter-intuitive: the longer the prompt, the shorter (tighter) the output — because it finally knows exactly what you want.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-20197/8cqnrff-27097`
- Source hash: `90441f0ab051d4f2d8982bb369f1277272abb5e9d119fbced0f0b1d29c1488a6`
- Observed at: 2026-10-17T07:14:15.551Z
- Agent run: `dc9fc4de-1ce0-43d5-a23d-32a73bfe579d`
- Validation run: `604808be-c3d8-4320-a989-ce5e616be442`

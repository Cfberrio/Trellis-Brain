---
brain_note_id: "note:298e5cb4-e42c-4f21-a300-d745b3a2fd8d"
canonical_key: "ai-tooling-installation"
brand_id: "trellis_core"
---
# AI Tooling Installation Guide

## Canonical Statement

- **process**: To install Marketing Skills, add the marketplace using '/plugin marketplace add coreyhaines31/marketingskills' and then run '/plugin install marketing-skills'.
- **process**: To install Caveman for token saving on macOS/Linux/WSL, use the curl command pointing to the JuliusBrussee/caveman install.sh script.
- **process**: To install Caveman on Windows (PowerShell 5.1+), use the 'irm' command pointing to the JuliusBrussee/caveman install.ps1 script.

## Evidence Log

- 2026-10-15T21:37:18.172Z — `clickup_doc_page:8cqnrff-15737/8cqnrff-21157`
  - `e1` (source_body): # Add the marketplace
/plugin marketplace add coreyhaines31/marketingskills

# Install all marketing skills
/plugin install marketing-skills
  - `e2` (source_body): # macOS / Linux / WSL / Git Bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
  - `e3` (source_body): # Windows (PowerShell 5.1+)
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex

## Provenance

- Source: `clickup_doc_page` `8cqnrff-15737/8cqnrff-21157`
- Source hash: `5e66867b4473aefba1d00acf3bb209eeb80e61c8d69241a86390eb1e7f5354d9`
- Observed at: 2026-10-15T21:37:18.172Z
- Agent run: `aa1c5eaf-4554-4c23-bd7d-e13e49c359ea`
- Validation run: `671934a4-2e01-44db-8312-6e06db92e531`

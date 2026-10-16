---
brain_note_id: "note:5221f258-3534-42af-b162-d1f9e76e8531"
canonical_key: "claude-code-mac-installation"
brand_id: "trellis_core"
---
# Claude Code Mac Installation Guide

## Canonical Statement

- **process**: To install Claude Code on Mac, first verify architecture (arm64 vs x86_64), install Apple Command Line Tools via 'xcode-select --install', and set up Homebrew as the primary package manager.
- **process**: Install core dependencies using 'brew install git gh node'. Configure Git global settings and authenticate the GitHub CLI using 'gh auth login' before proceeding to the Claude installation.
- **process**: Install Claude Code using the official native installer: 'curl -fsSL https://claude.ai/install.sh | bash'. Ensure the binary path '$HOME/.local/bin' is added to the shell profile (~/.zshrc or ~/.zprofile).
- **rule**: If the 'claude' command is not found after installation, verify the binary exists in ~/.local/bin and manually source the shell profile or restart the terminal/IDE.

## Evidence Log

- 2026-10-16T17:00:59.596Z — `clickup_doc_page:8cqnrff-18157/8cqnrff-22697`
  - `e1` (source_body): Run: uname -m. If it says: arm64 the Mac is Apple Silicon. If it says: x86_64 the Mac is Intel.
  - `e2` (source_body): Run: xcode-select --install. A popup will appear. Click: Install.
  - `e3` (source_body): Run: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  - `e4` (source_body): Run: brew install git gh node. This installs: git = version control, gh = GitHub CLI, node = JavaScript runtime
  - `e5` (source_body): Run: gh auth login --web --git-protocol https. Choose: GitHub.com, HTTPS, Login with browser.
  - `e6` (source_body): Run the official Claude Code native installer: curl -fsSL https://claude.ai/install.sh | bash. After installation, add Claude to your terminal path: echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc

## Provenance

- Source: `clickup_doc_page` `8cqnrff-18157/8cqnrff-22697`
- Source hash: `99e984ce9a95c046222ce0d42912f766ab6b9a136f3e1af2245abcf80e85fd1a`
- Observed at: 2026-10-16T17:00:59.596Z
- Agent run: `b4ad6cd3-c916-4da6-9450-d2e9679594c0`
- Validation run: `2d887392-c01a-4d4e-a710-6a9d97f1df96`

#!/usr/bin/env bash
# myBrain path-wikilink patch
#
# Problem: myBrain (v1.0.50) indexes frontmatter relation targets by the raw
# wikilink text (e.g. "01-brands/cheese-to-share/00-brand-core/brand-home")
# but looks them up by note basename ("brand-home"). This vault writes every
# `up` / `down` / `related` link with its full folder path, so without this
# patch no note is ever classified as Parent / Child / Friend — everything
# lands in the "undefined" bucket.
#
# Fix: key the anchor cache by the last path segment (the basename), which is
# what the lookup side already uses.
#
# Idempotent. Re-run after every myBrain update (updates overwrite main.js).
# Run from the vault root:  bash 00-Trellis-Core/Obsidian-Config/plugins/mybrain-patch.sh

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
MAIN_JS="$VAULT_ROOT/.obsidian/plugins/mybrain/main.js"

ORIG='let l=u.toLowerCase().normalize("NFC"),p=this.anchorCache.get(l);p||(p=new H(u),'
PATCHED='let l=u.split("/").pop().toLowerCase().normalize("NFC"),p=this.anchorCache.get(l);p||(p=new H(u.split("/").pop()),'

if [[ ! -f "$MAIN_JS" ]]; then
  echo "myBrain not installed ($MAIN_JS missing) — skipping." >&2
  exit 0
fi

if grep -qF "$PATCHED" "$MAIN_JS"; then
  echo "myBrain already patched."
  exit 0
fi

COUNT="$(grep -oF "$ORIG" "$MAIN_JS" | wc -l | tr -d ' ')"
if [[ "$COUNT" != "1" ]]; then
  echo "Expected exactly 1 match of the original snippet, found $COUNT." >&2
  echo "myBrain source changed upstream — patch needs review before applying." >&2
  exit 1
fi

cp "$MAIN_JS" "$MAIN_JS.bak"
python3 - "$MAIN_JS" "$ORIG" "$PATCHED" <<'PY'
import sys
path, orig, patched = sys.argv[1:4]
src = open(path, encoding="utf-8").read()
assert src.count(orig) == 1
open(path, "w", encoding="utf-8").write(src.replace(orig, patched))
PY

echo "myBrain patched. Backup at main.js.bak. Reload the plugin (or restart Obsidian) to apply."

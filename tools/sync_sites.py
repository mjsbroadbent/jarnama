"""Copies the site registry (sites.json) from the irad-persona skill so go.html can send
ad clicks to the advertiser's real site when it is live.

    python3 tools/sync_sites.py [path/to/irad_persona_skill]

Without a path it looks for ../irad_persona_skill next to this repo.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "irad_persona_skill"
data = json.loads((src / "sites.json").read_text(encoding="utf-8"))
out = {"updated": data.get("updated"), "sites": [
    {k: s[k] for k in ("id", "url", "old", "status", "live") if k in s} for s in data["sites"]]}
(ROOT / "sites.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"sites.json: {len(out['sites'])} sites")

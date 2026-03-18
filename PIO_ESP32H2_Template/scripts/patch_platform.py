#!/usr/bin/env python3
from pathlib import Path
import os
import sys

home = Path(os.environ.get("PLATFORMIO_CORE_DIR", Path.home()/".platformio"))
pkg_root = home / "platforms"
candidates = list(pkg_root.glob("espressif32*"))
if not candidates:
    print("Could not find installed platform-espressif32 under", pkg_root)
    sys.exit(1)

patched_any = False
patterns = [
    ('("esp32c3", "esp32c6")', '("esp32c3", "esp32c6", "esp32h2")'),
    ("('esp32c3', 'esp32c6')", "('esp32c3', 'esp32c6', 'esp32h2')"),
]

for plat in candidates:
    for path in plat.rglob("*.py"):
        try:
            txt = path.read_text(encoding="utf-8")
        except Exception:
            continue
        original = txt
        for a, b in patterns:
            txt = txt.replace(a, b)
        if txt != original:
            path.write_text(txt, encoding="utf-8")
            patched_any = True
            print("Patched", path)

if not patched_any:
    print("No matching builder files needed patching, or package layout changed.")
else:
    print("Patch complete. Run: pio run -t clean && pio run")

"""ai-happy-01 entry: copy the prepared image to the output directory.

The image (art.png, a JPEG by its first bytes, which the gate accepts under
the entry.png name) is written byte-identical to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output). Standard library only, no network, no randomness: every
run produces exactly the same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "art.png", OUT_DIR / "entry.png")

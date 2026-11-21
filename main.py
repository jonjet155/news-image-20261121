#!/usr/bin/env python3
"""news-image-20261121 — sum up 21 November 2026's world news in one image.

Standard library only: the grader container installs nothing, so this
program just copies the pre-built entry.png beside it into the output
directory. Run it with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
# Deterministic run: both grader runs must write the same bytes, so
# fail loudly instead of silently shipping a partial copy.
assert (OUT / "entry.png").stat().st_size == (HERE / "entry.png").stat().st_size
assert (OUT / "entry.png").stat().st_size <= 1_048_576

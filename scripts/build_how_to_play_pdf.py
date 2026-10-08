#!/usr/bin/env python3
"""Build the two-page A4 "How to play" PDF from game/print/how-to-play-A4.html.

Headless Edge print-to-pdf, no Python packages needed. Run:

    python game/scripts/build_how_to_play_pdf.py

Output: game/print/how-to-play-A4.pdf
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from build_print_pdf import find_edge

PRINT = Path(__file__).resolve().parent.parent / "print"
SOURCE = PRINT / "how-to-play-A4.html"
OUTPUT = PRINT / "how-to-play-A4.pdf"

if __name__ == "__main__":
    if OUTPUT.exists():
        OUTPUT.unlink()
    subprocess.run(
        [
            find_edge(),
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={OUTPUT}",
            SOURCE.resolve().as_uri(),
        ],
        check=True,
    )
    if not OUTPUT.exists():
        raise SystemExit("Edge did not produce a PDF - check the HTML and the Edge version.")
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size / 1024:.0f} KB)")

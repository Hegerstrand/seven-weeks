#!/usr/bin/env python3
"""Build a standalone PDF of just the "How to Play" leaflet.

Reuses build_print_pdf.py's Markdown renderer (headless Edge print-to-pdf,
no Python packages needed). Run:

    python game/scripts/build_leaflet_pdf.py

Output: game/print/leaflet-how-to-play.pdf
"""
from __future__ import annotations

from pathlib import Path

from build_print_pdf import build

OUTPUT = Path(__file__).resolve().parent.parent / "print" / "leaflet-how-to-play.pdf"

if __name__ == "__main__":
    build(["leaflet-how-to-play.md"], OUTPUT)

#!/usr/bin/env python3
"""Combine every sheet in game/components/*.svg into game/print/game-print-all.pdf.

Headless Edge print-to-pdf, no Python packages needed. Each page keeps the real mm
size of its SVG. Run:

    python game/scripts/build_print_pdf.py
"""
from __future__ import annotations

import os
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENTS = ROOT / "components"
OUTPUT = ROOT / "print" / "game-print-all.pdf"

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_edge() -> str:
    for p in EDGE_CANDIDATES:
        if os.path.exists(p):
            return p
    raise SystemExit("Microsoft Edge not found; add its path to EDGE_CANDIDATES.")


def sheets() -> list[Path]:
    # Underscore-prefixed files are dev-only checks.
    return sorted(p for p in COMPONENTS.glob("*.svg") if not p.name.startswith("_"))


def size_mm(svg: Path) -> tuple[float, float]:
    head = svg.read_text(encoding="utf-8")[:2000]
    w = re.search(r'\bwidth="([\d.]+)mm"', head)
    h = re.search(r'\bheight="([\d.]+)mm"', head)
    if not (w and h):
        raise SystemExit(f"{svg.name}: no width/height in mm on the <svg> element.")
    return float(w.group(1)), float(h.group(1))


def build_html(files: list[Path]) -> str:
    css = ["html,body{margin:0;padding:0}",
           ".sheet{break-after:page;overflow:hidden}",
           ".sheet img{display:block}"]
    body = []
    for i, f in enumerate(files):
        w, h = size_mm(f)
        css.append(f"@page s{i}{{size:{w}mm {h}mm;margin:0}}")
        css.append(f".s{i}{{page:s{i};width:{w}mm;height:{h}mm}}")
        css.append(f".s{i} img{{width:{w}mm;height:{h}mm}}")
        body.append(f'<div class="sheet s{i}"><img src="{f.resolve().as_uri()}"></div>')
    return f"<!doctype html><meta charset=utf-8><style>{''.join(css)}</style>{''.join(body)}"


if __name__ == "__main__":
    files = sheets()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8",
                                     dir=OUTPUT.parent) as tmp:
        tmp.write(build_html(files))
        tmp_path = Path(tmp.name)
    try:
        subprocess.run(
            [find_edge(), "--headless", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={OUTPUT}", tmp_path.as_uri()],
            check=True,
        )
    finally:
        tmp_path.unlink(missing_ok=True)
    if not OUTPUT.exists():
        raise SystemExit("Edge did not produce a PDF.")
    print(f"Wrote {OUTPUT} ({len(files)} pages, {OUTPUT.stat().st_size / 1024:.0f} KB)")

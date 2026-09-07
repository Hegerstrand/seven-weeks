#!/usr/bin/env python3
"""Build one print-ready PDF from every game/components print sheet.

Each SVG becomes its own page in the output PDF, sized to that sheet's own
real mm dimensions (read straight off its <svg width="..mm" height="..mm">
tag) - nothing is scaled, matching the "print at 100%" rule every sheet
already carries. The biggest sheet (board 1) needs A3 paper; everything else
is A4 or smaller, so most home printers can still handle the whole job if fed
manually a page at a time, or send it to a copy shop that does A3.

Requires Microsoft Edge (used headless, via its built-in print-to-pdf) - no
Python packages needed. Run:

    python game/scripts/build_print_pdf.py

Output: game/print/game-print-all.pdf
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

COMPONENTS = Path(__file__).resolve().parent.parent / "components"
OUTPUT = Path(__file__).resolve().parent.parent / "print" / "game-print-all.pdf"

# Physical print/assembly order - matches components/README.md. Update this
# list whenever a sheet is added, renamed, or dropped from components/.
SHEETS = [
    "board-1-FRONT-week-and-project-A3-landscape.svg",
    "board-1-BACK-week-1-the-week-A3-landscape.svg",
    "board-2-FRONT-reality-A4-portrait.svg",
    "board-2-BACK-week-2-reality-A4-portrait.svg",
    "board-3-FRONT-the-team-A4-landscape.svg",
    "board-3-BACK-week-3-the-team-A4-landscape.svg",
    "board-4-FRONT-the-zone-A4-landscape.svg",
    "board-4-BACK-the-zone-A4-landscape.svg",
    "board-4b-the-zone-payoff-127x104mm-A4-landscape.svg",
    "board-3b-standing-281x34mm-A4-landscape.svg",
    "board-person-170x141mm-A4-portrait.svg",
    "cards-activity-63x88mm-A4-portrait.svg",
    "cards-activity-5b-63x88mm-A4-portrait.svg",
    "cards-event-01-09-63x88mm-A4-portrait.svg",
    "cards-event-10-18-63x88mm-A4-portrait.svg",
    "cards-project-63x88mm-A4-portrait.svg",
    "cards-habitus-parts-44x36mm-A4-portrait.svg",
    "leaflet-how-to-play-A4-portrait.svg",
]

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

SIZE_RE = re.compile(r'<svg\b[^>]*\bwidth="([\d.]+)mm"[^>]*\bheight="([\d.]+)mm"')


def find_edge() -> str:
    for path in EDGE_CANDIDATES:
        if Path(path).exists():
            return path
    raise SystemExit("Microsoft Edge not found - install it, or add its path to EDGE_CANDIDATES.")


def read_size_mm(svg_path: Path) -> tuple[float, float]:
    head = svg_path.read_text(encoding="utf-8")[:1000]
    m = SIZE_RE.search(head)
    if not m:
        raise ValueError(f"Couldn't read width/height mm from the <svg> tag of {svg_path.name}")
    return float(m.group(1)), float(m.group(2))


def build_wrapper_html(sheets: list[Path]) -> Path:
    """One HTML page per sheet, each with its own named @page size (CSS Paged
    Media) so Chromium's print-to-pdf emits real per-sheet page sizes instead
    of forcing everything onto one uniform paper size."""
    sizes: dict[str, tuple[float, float]] = {}
    page_rules = []
    body = []
    for svg in sheets:
        w, h = read_size_mm(svg)
        key = f"s{w:g}x{h:g}".replace(".", "_")
        if key not in sizes:
            sizes[key] = (w, h)
            page_rules.append(f"@page {key} {{ size: {w:g}mm {h:g}mm; margin: 0; }}")
        uri = svg.resolve().as_uri()
        body.append(
            f'<div class="sheet" style="page:{key}; width:{w:g}mm; height:{h:g}mm;">'
            f'<img src="{uri}"></div>'
        )
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
* {{ margin:0; padding:0; }}
{chr(10).join(page_rules)}
.sheet {{ page-break-after: always; overflow: hidden; }}
.sheet:last-child {{ page-break-after: auto; }}
.sheet img {{ width:100%; height:100%; display:block; }}
</style></head><body>
{chr(10).join(body)}
</body></html>"""
    out = OUTPUT.parent / "_wrapper.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def main() -> None:
    missing = [s for s in SHEETS if not (COMPONENTS / s).exists()]
    if missing:
        raise SystemExit(f"Missing sheets - update SHEETS in this script: {missing}")

    sheets = [COMPONENTS / s for s in SHEETS]
    wrapper = build_wrapper_html(sheets)
    edge = find_edge()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()

    subprocess.run(
        [
            edge,
            "--headless",
            "--disable-gpu",
            f"--print-to-pdf={OUTPUT}",
            wrapper.resolve().as_uri(),
        ],
        check=True,
    )

    if not OUTPUT.exists():
        raise SystemExit("Edge did not produce a PDF - check the wrapper HTML and Edge version.")
    wrapper.unlink(missing_ok=True)
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size / 1024:.0f} KB, {len(sheets)} pages)")


if __name__ == "__main__":
    main()

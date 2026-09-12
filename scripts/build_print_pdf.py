#!/usr/bin/env python3
"""Build one print-ready PDF from every game/components print sheet.

Each SVG becomes its own page in the output PDF, sized to that sheet's own
real mm dimensions (read straight off its <svg width="..mm" height="..mm">
tag) - nothing is scaled, matching the "print at 100%" rule every sheet
already carries. The biggest sheet (board 1) needs A3 paper; everything else
is A4 or smaller, so most home printers can still handle the whole job if fed
manually a page at a time, or send it to a copy shop that does A3.

The one non-SVG entry, the "How to Play" leaflet, is plain Markdown
(components/specs/leaflet-how-to-play.md) - it's rendered to HTML and
paginated on its own "## Page N of M" headings instead of being read as an
image.

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
SPECS = COMPONENTS / "specs"
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
    "cards-event-19-21-63x88mm-A4-portrait.svg",
    "cards-project-63x88mm-A4-portrait.svg",
    "cards-habitus-parts-44x36mm-A4-portrait.svg",
    "leaflet-how-to-play.md",
]

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

SIZE_RE = re.compile(r'<svg\b[^>]*\bwidth="([\d.]+)mm"[^>]*\bheight="([\d.]+)mm"')
MD_PAGE_RE = re.compile(r"^## Page (\d+) of (\d+).*$", re.MULTILINE)


def find_edge() -> str:
    for path in EDGE_CANDIDATES:
        if Path(path).exists():
            return path
    raise SystemExit("Microsoft Edge not found - install it, or add its path to EDGE_CANDIDATES.")


def resolve_sheet(name: str) -> Path:
    """Markdown sheets live in components/specs/ (they're leaflet source
    text, not SVG specs); everything else is a components/*.svg print sheet."""
    return (SPECS if name.endswith(".md") else COMPONENTS) / name


def read_size_mm(svg_path: Path) -> tuple[float, float]:
    head = svg_path.read_text(encoding="utf-8")[:1000]
    m = SIZE_RE.search(head)
    if not m:
        raise ValueError(f"Couldn't read width/height mm from the <svg> tag of {svg_path.name}")
    return float(m.group(1)), float(m.group(2))


def _inline_md(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    return text


STEP_RE = re.compile(r"^\*\*(\d+\s*·\s*[^*]+)\*\*\s*-\s*(.*)$")
LABEL_DASH_RE = re.compile(r"^\*\*([^*]+)\*\*\s*-\s*(.*)$")
LABEL_ONLY_RE = re.compile(r"^\*\*([^*]+)\*\*$")


def _render_table(rows: list[str]) -> str:
    cells = [r.strip().strip("|").split("|") for r in rows]
    header, rest = cells[0], cells[1:]
    if rest and re.match(r"^\s*:?-+:?\s*$", rest[0][0]):
        rest = rest[1:]
    out = ["<table><thead><tr>"]
    out += [f"<th>{_inline_md(c.strip())}</th>" for c in header]
    out.append("</tr></thead><tbody>")
    for row in rest:
        out.append("<tr>" + "".join(f"<td>{_inline_md(c.strip())}</td>" for c in row) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def _render_paragraph(raw: str) -> str:
    """A numbered "**1 · Title** - body" line becomes a bordered step panel
    (matching the original leaflet's step boxes); a plain "**Label** - body"
    or bare "**Label**" line becomes an unboxed sub-heading, matching how the
    original SVG used mono sub-headers for FINISH THE ROOM / FROM WEEK 2."""
    step = STEP_RE.match(raw)
    if step:
        return f'<div class="step"><h4>{_inline_md(step.group(1))}</h4><p>{_inline_md(step.group(2))}</p></div>'
    label_only = LABEL_ONLY_RE.match(raw.strip())
    if label_only:
        return f'<h4 class="label">{_inline_md(label_only.group(1))}</h4>'
    label_dash = LABEL_DASH_RE.match(raw)
    if label_dash:
        return f'<div class="note"><h4>{_inline_md(label_dash.group(1))}</h4><p>{_inline_md(label_dash.group(2))}</p></div>'
    return f"<p>{_inline_md(raw)}</p>"


def _md_to_html(text: str) -> str:
    """Tiny, dependency-free Markdown -> HTML for the leaflet's own subset:
    headings, paragraphs, bold/italic, blockquotes, lists, tables, rules."""
    lines = text.split("\n")
    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith("### "):
            out.append(f"<h3>{_inline_md(line[4:])}</h3>")
            i += 1
        elif line.startswith("## "):
            out.append(f"<h2>{_inline_md(line[3:])}</h2>")
            i += 1
        elif line.startswith("# "):
            out.append(f"<h1>{_inline_md(line[2:])}</h1>")
            i += 1
        elif line.strip() == "---":
            out.append("<hr>")
            i += 1
        elif line.startswith("> "):
            quote = []
            while i < n and lines[i].startswith("> "):
                quote.append(lines[i][2:])
                i += 1
            out.append('<blockquote class="aside">' + "<br>".join(_inline_md(q) for q in quote) + "</blockquote>")
        elif re.match(r"^\d+\.\s", line):
            items = []
            while i < n and re.match(r"^\d+\.\s", lines[i]):
                items.append(re.sub(r"^\d+\.\s", "", lines[i]))
                i += 1
            out.append("<ol>" + "".join(f"<li>{_inline_md(it)}</li>" for it in items) + "</ol>")
        elif line.startswith("- "):
            items = []
            while i < n and lines[i].startswith("- "):
                items.append(lines[i][2:])
                i += 1
            out.append("<ul>" + "".join(f"<li>{_inline_md(it)}</li>" for it in items) + "</ul>")
        elif line.startswith("|"):
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(_render_table(rows))
        else:
            para = []
            while i < n and lines[i].strip() and lines[i][:1] not in "#>|" and lines[i].strip() != "---" and not lines[i].startswith("- ") and not re.match(r"^\d+\.\s", lines[i]):
                para.append(lines[i])
                i += 1
            out.append(_render_paragraph(" ".join(para)))
    return _wrap_boxes(out)


def _wrap_boxes(blocks: list[str]) -> str:
    """Group each <h3>...</h3> with the blocks that follow it (up to the next
    <h2>/<h3> or the end) into one bordered <section class="box"> - this is
    what makes SETTING UP / WEEK 1 / etc. read as the original's outlined
    boxes instead of a flat wall of text."""
    out = []
    i, n = 0, len(blocks)
    while i < n:
        if blocks[i].startswith("<h3>"):
            section = [blocks[i]]
            i += 1
            while i < n and not blocks[i].startswith(("<h2>", "<h3>")):
                section.append(blocks[i])
                i += 1
            out.append('<section class="box">' + "".join(section) + "</section>")
        else:
            out.append(blocks[i])
            i += 1
    return "\n".join(out)


def render_markdown_pages(md_path: Path) -> list[tuple[float, float, str]]:
    """Split a leaflet Markdown file on its own "## Page N of M" headings -
    everything before the first one (title + intro) stays on page 1 - and
    render each resulting chunk to HTML. Returns (width_mm, height_mm, html)
    per page; page size is fixed A4 portrait, matching the leaflet's own."""
    text = md_path.read_text(encoding="utf-8")
    starts = [m.start() for m in MD_PAGE_RE.finditer(text)]
    boundaries = [0, *starts[1:], len(text)] if starts else [0, len(text)]
    chunks = [text[boundaries[i]:boundaries[i + 1]] for i in range(len(boundaries) - 1)]
    return [(210.0, 297.0, _md_to_html(chunk)) for chunk in chunks]


def build_wrapper_html(sheets: list[Path], wrapper_dir: Path) -> Path:
    """One HTML page per sheet (or per Markdown page), each with its own
    named @page size (CSS Paged Media) so Chromium's print-to-pdf emits real
    per-sheet page sizes instead of forcing everything onto one uniform
    paper size."""
    sizes: dict[str, tuple[float, float]] = {}
    page_rules = []
    body = []

    def page_key(w: float, h: float) -> str:
        key = f"s{w:g}x{h:g}".replace(".", "_")
        if key not in sizes:
            sizes[key] = (w, h)
            page_rules.append(f"@page {key} {{ size: {w:g}mm {h:g}mm; margin: 0; }}")
        return key

    def md_page_key(w: float, h: float) -> str:
        """Its own @page rule, separate from the SVG sheets' margin:0 rule -
        the leaflet needs a real printable margin, set on @page itself so it's
        honoured by the print engine regardless of how the content flows."""
        key = f"md{w:g}x{h:g}".replace(".", "_")
        if key not in sizes:
            sizes[key] = (w, h)
            page_rules.append(f"@page {key} {{ size: {w:g}mm {h:g}mm; margin: 12mm 13mm; }}")
        return key

    for sheet in sheets:
        if sheet.suffix.lower() == ".md":
            for w, h, content_html in render_markdown_pages(sheet):
                key = md_page_key(w, h)
                body.append(f'<div class="sheet md-page" style="page:{key};">{content_html}</div>')
        else:
            w, h = read_size_mm(sheet)
            key = page_key(w, h)
            uri = sheet.resolve().as_uri()
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
.md-page {{
  overflow: visible; height: auto; color: #1a1712;
  font-family: Georgia, "EB Garamond", serif; font-size: 8.6pt; line-height: 1.28;
}}
.md-page h1 {{
  font-family: "IBM Plex Mono", "Courier New", monospace; font-size: 17pt;
  letter-spacing: 2.5px; margin: 0 0 2.5mm; padding-bottom: 2mm;
  border-bottom: .6pt solid #2A2620;
}}
.md-page > h2 {{
  font-family: "IBM Plex Mono", "Courier New", monospace; font-size: 9.5pt;
  letter-spacing: 1.2px; font-weight: normal; color: #4a4436;
  margin: 0 0 3.5mm; padding-bottom: 1.5mm; border-bottom: .4pt solid #2A2620;
}}
.md-page > p {{ font-style: italic; color: #3a352b; margin: -1mm 0 3.5mm; }}
section.box {{
  border: .6pt solid #2A2620; border-radius: 2mm; padding: 3mm 4mm 4mm;
  margin: 0 0 3.5mm;
}}
section.box > h3:first-child {{ margin-top: 0; }}
.md-page h3 {{
  font-family: "IBM Plex Mono", "Courier New", monospace; font-size: 10.5pt;
  letter-spacing: 1.2px; margin: 0 0 2.5mm;
}}
.md-page p {{ margin: 0 0 2mm; }}
.md-page .step {{
  border: .4pt solid #2A2620; border-radius: 1.5mm; padding: 1.8mm 3mm;
  margin: 0 0 2mm;
}}
.md-page .step h4, .md-page .note h4 {{
  font-family: "IBM Plex Mono", "Courier New", monospace; font-size: 8.6pt;
  font-weight: normal; letter-spacing: .5px; margin: 0 0 .8mm;
}}
.md-page .step p, .md-page .note p {{ margin: 0; }}
.md-page .note {{ margin: 0 0 2mm; }}
.md-page h4.label {{
  font-family: "IBM Plex Mono", "Courier New", monospace; font-size: 8.6pt;
  letter-spacing: .8px; margin: 2.5mm 0 1.2mm; color: #3a352b;
}}
.md-page blockquote.aside {{
  margin: 0 0 2mm; padding: 1.2mm 3mm; background: #D9D3C4; border-radius: 1mm;
  font-style: italic; font-size: 8.2pt;
}}
.md-page hr {{ border: none; border-top: .5pt solid #2A2620; margin: 3mm 0; }}
.md-page ol, .md-page ul {{ margin: 0 0 2mm 4.5mm; padding: 0; }}
.md-page li {{ margin-bottom: 1mm; }}
.md-page table {{ border-collapse: collapse; width: 100%; margin: 0 0 2mm; }}
.md-page th, .md-page td {{
  border: .4pt solid #2A2620; padding: 1.6mm 2.5mm; text-align: left;
  font-size: 8.5pt; vertical-align: top;
}}
.md-page th {{ font-family: "IBM Plex Mono", "Courier New", monospace; }}
</style></head><body>
{chr(10).join(body)}
</body></html>"""
    out = wrapper_dir / "_wrapper.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def build(sheet_names: list[str], output: Path) -> None:
    """Render sheet_names (SVGs under COMPONENTS, or .md under SPECS) into one PDF at output."""
    missing = [s for s in sheet_names if not resolve_sheet(s).exists()]
    if missing:
        raise SystemExit(f"Missing sheets: {missing}")

    sheets = [resolve_sheet(s) for s in sheet_names]
    wrapper = build_wrapper_html(sheets, output.parent)
    edge = find_edge()

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    subprocess.run(
        [
            edge,
            "--headless",
            "--disable-gpu",
            f"--print-to-pdf={output}",
            wrapper.resolve().as_uri(),
        ],
        check=True,
    )

    if not output.exists():
        raise SystemExit("Edge did not produce a PDF - check the wrapper HTML and Edge version.")
    wrapper.unlink(missing_ok=True)
    print(f"Wrote {output} ({output.stat().st_size / 1024:.0f} KB, {len(sheets)} sheets)")


def main() -> None:
    build(SHEETS, OUTPUT)


if __name__ == "__main__":
    main()


"""Render proposal.md as a web page for the QATT site.

Usage: python tools/make_html.py [OUT_DIR]     (default: ../qatt/unicode)

Writes OUT_DIR/index.html and the scans of the sources to OUT_DIR/pages, cropped to
the text (a margin of MARGIN pixels on all four sides), which removes the digital
watermark above the text and the page edges. The scans in evidence/ stay as they are.
Page references (evidence/pages/S1-p2.jpg) link to the copied scans; evidence
entries (E07) link to their files in the GitHub repository. Needs markdown-it-py, Pillow and numpy.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import numpy as np
from markdown_it import MarkdownIt
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/qtng/qatt-unicode/blob/main"
DEFAULT_OUT = ROOT.parent / "qatt" / "unicode"

MARGIN = 8        # pixels of paper left around the text
TOP = 100         # the watermark of the Institute lies above this row
INK = 100         # luminance below which a pixel is ink
EDGE = 14         # distance kept from the right edge of the paper (dark edge line)
MIN_INK = 6       # a row or column counts as text with at least this many ink pixels


def crop_to_text(source: Path, target: Path) -> None:
    """Crop a scan to its text with a margin; ignores the watermark and the page edge."""
    image = Image.open(source).convert("RGB")
    grey = np.array(image.convert("L"))
    height, width = grey.shape
    columns = grey[TOP:1400].mean(axis=0)
    paper_right = max(x for x in range(width) if columns[x] < 215) + 1
    ink = grey[TOP:height - EDGE, :paper_right - EDGE] < INK
    rows = np.where(ink.sum(axis=1) >= MIN_INK)[0]
    cols = np.where(ink.sum(axis=0) >= MIN_INK)[0]
    box = (max(int(cols.min()) - MARGIN, 0), max(int(rows.min()) + TOP - MARGIN, TOP),
           min(int(cols.max()) + MARGIN, width), min(int(rows.max()) + TOP + MARGIN, height))
    image.crop(box).save(target, quality=78, optimize=True)

PAGE = """<!DOCTYPE html>
<html lang="en" translate="no">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google" content="notranslate">
  <title>{title}</title>
  <meta name="description" content="Draft Unicode encoding proposal for Quốc Âm Tân Tự (QATT).">
  <link rel="stylesheet" href="/vendor/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="/css/site.css">
  <script src="/js/navigation.js"></script>
  <style>
    body {{ background: #fffdf8; color: #2b2118; }}
    main {{ max-width: 54rem; }}
    h1, h2, h3, h4 {{ font-family: Georgia, "Times New Roman", serif; font-weight: 400; }}
    h2 {{ margin-top: 2.2rem; border-bottom: 1px solid #dccfb2; padding-bottom: .25rem; }}
    a {{ color: #a8362a; }}
    table {{ border-collapse: collapse; margin: 1rem 0; font-size: .9rem; }}
    th, td {{ border: 1px solid #dccfb2; padding: .25rem .5rem; vertical-align: top; }}
    th {{ background: #f7efdc; }}
    .table-wrap {{ overflow-x: auto; }}
    code, pre {{ font-size: .85rem; }}
    pre {{ background: #f7efdc; padding: .75rem 1rem; overflow-x: auto; }}
    .scans {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(8rem, 1fr)); gap: .75rem; }}
    .scans figure {{ margin: 0; text-align: center; font-size: .8rem; }}
    .scans img {{ width: 100%; height: auto; border: 1px solid #dccfb2; }}
  </style>
</head>
<body>
  <main class="container py-4">
{body}
  </main>
</body>
</html>
"""


def slug(text: str) -> str:
    m = re.match(r"(?:([A-D])\.|(\d+(?:\.\d+)*))\s", text)
    if m:
        return "sec-" + (m.group(1) or m.group(2)).replace(".", "-")
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def fix_link(href: str) -> str:
    m = re.fullmatch(r"(?:evidence/)?pages/(S\d-p\d\.jpg)", href)
    if m:
        return f"pages/{m.group(1)}"
    m = re.fullmatch(r"(?:evidence/)?(E\d+[a-z]?\.md)", href)
    if m:
        return f"{REPO}/evidence/{m.group(1)}"
    return href


def scan_gallery() -> str:
    figures = []
    for source in (1, 2):
        for page in range(1, 9):
            name = f"S{source}-p{page}.jpg"
            figures.append(f'<figure><a href="pages/{name}"><img src="pages/{name}" alt="Source {source}, page {page}" loading="lazy"></a>'
                           f"<figcaption>Source {source}, p. {page}</figcaption></figure>")
    return '<div class="scans">' + "".join(figures) + "</div>"


def render(markdown: str) -> str:
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    tokens = md.parse(markdown)
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            token.attrSet("id", slug(tokens[i + 1].content))
        elif token.type == "table_open":
            token.attrSet("class", "table")
        for child in token.children or []:
            if child.type == "link_open":
                child.attrSet("href", fix_link(child.attrGet("href")))
                if (child.attrGet("href") or "").startswith("pages/"):
                    child.attrSet("target", "_blank")
    body = md.renderer.render(tokens, md.options, {})
    body = re.sub(r"<table class=\"table\">", '<div class="table-wrap"><table>', body)
    body = body.replace("</table>", "</table></div>")
    # the scans, after the text of Appendix C
    body = re.sub(r"(<h3 id=\"sec-C\">.*?</p>)", lambda m: m.group(1) + "\n" + scan_gallery(), body, count=1, flags=re.S)
    return body


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    (out / "pages").mkdir(parents=True, exist_ok=True)
    for scan in sorted((ROOT / "evidence" / "pages").glob("S[12]-p[1-8].jpg")):
        crop_to_text(scan, out / "pages" / scan.name)
    markdown = (ROOT / "proposal.md").read_text(encoding="utf-8")
    title = html.escape(re.match(r"# (.*)", markdown).group(1)) + " | Qatt.org"
    (out / "index.html").write_text(PAGE.format(title=title, body=render(markdown)), encoding="utf-8")
    print(f"wrote {out / 'index.html'}")


if __name__ == "__main__":
    main()

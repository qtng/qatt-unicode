"""Render proposal.md as a web page for the QATT site.

Usage: python tools/make_html.py [OUT_DIR]     (default: ../qatt/unicode/draft)

Writes OUT_DIR/index.html, OUT_DIR/evidences/E*.html (one page per evidence entry, plus an
overview) and OUT_DIR/ucd/ (the draft character data), with the images: the 16 pages of both
manuscripts in OUT_DIR/pages, cropped to the text with a margin (this removes the watermark
above the text and the page edges), and the cut-outs of the evidence entries in
OUT_DIR/evidences/images. Needs markdown-it-py, Pillow and numpy.
"""

from __future__ import annotations

import html
import re
import shutil
import sys
from pathlib import Path

import numpy as np
from markdown_it import MarkdownIt
from markdown_it.token import Token
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evidence  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/qtng/qatt-unicode/blob/main"
DEFAULT_OUT = ROOT.parent / "qatt" / "unicode" / "draft"

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
    details.sec {{ border-bottom: 1px solid #dccfb2; }}
    details.sec > summary {{ cursor: pointer; list-style: none; display: flex; align-items: baseline; gap: .6rem; }}
    details.sec > summary::-webkit-details-marker {{ display: none; }}
    details.sec > summary::before {{ content: "\\25B8"; color: #a8362a; transition: transform .15s; }}
    details.sec[open] > summary::before {{ transform: rotate(90deg); }}
    details.sec > summary h2 {{ border-bottom: 0; margin: 1rem 0; flex: 1; }}
    details.sec > :not(summary):last-child {{ margin-bottom: 1.5rem; }}
    main img {{ max-width: 100%; height: auto; border: 1px solid #dccfb2; }}
    code, pre {{ font-size: .85rem; }}
    pre {{ background: #f7efdc; padding: .75rem 1rem; overflow-x: auto; }}
    .anchor {{ margin-left: .4rem; opacity: 0; color: #a8362a; text-decoration: none; vertical-align: -.1em; }}
    .anchor svg {{ width: .75em; height: .75em; fill: currentColor; }}
    h1:hover .anchor, h2:hover .anchor, h3:hover .anchor, h4:hover .anchor, .anchor:focus {{ opacity: 1; }}
    @media (hover: none) {{ .anchor {{ opacity: .45; }} }}
    h1, h2, h3, h4 {{ scroll-margin-top: 4.5rem; }}
  </style>
</head>
<body>
  <main class="container py-4">
{body}
  </main>
  <script>
    // a link to an anchor inside a closed section opens the section
    function openTarget() {{
      const t = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
      for (let d = t && t.closest('details'); d; d = d.parentElement && d.parentElement.closest('details')) d.open = true;
      if (t) t.scrollIntoView();
    }}
    addEventListener('hashchange', openTarget);
    openTarget();
  </script>
</body>
</html>
"""


# the link symbol of Bootstrap Icons (bi-link-45deg)
LINK_ICON = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4.715 6.542 3.343 7.914a3 3 0 1 0 4.243 4.243l1.828-1.829A3 3 0 0 0 '
             '8.586 5.5L8 6.086a1 1 0 0 0-.154.199 2 2 0 0 1 .861 3.337L6.88 11.45a2 2 0 1 1-2.83-2.83l.793-.792a4 4 0 0 1-.128-1.287z"/>'
             '<path d="M6.586 4.672A3 3 0 0 0 7.414 9.5l.775-.776a2 2 0 0 1-.896-3.346L9.12 3.55a2 2 0 1 1 2.83 2.83l-.793.792c.112.42.155.855.128 '
             '1.287l1.372-1.372a3 3 0 1 0-4.243-4.243z"/></svg>')


def slug(text: str) -> str:
    m = re.match(r"(?:([A-D])\.|(\d+(?:\.\d+)*))\s", text)
    if m:
        return "sec-" + (m.group(1) or m.group(2)).replace(".", "-")
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def fix_link(href: str, base: str = "") -> str:
    """Rewrite a link or image source of the Markdown files. base is "" for the proposal and
    "../" for the pages in evidences/ and ucd/."""
    m = re.fullmatch(r"(?:evidence/)?pages/(S\d-p\d\.jpg)", href)
    if m:
        return f"{base}pages/{m.group(1)}"
    m = re.fullmatch(r"(?:evidence/|\./)?(E\d+[a-z]?)\.md(#.*)?", href)
    if m:
        return f"{'evidences/' if not base else ''}{m.group(1)}.html{m.group(2) or ''}"
    if href == "README.md" and base:
        return "index.html"
    return href


def accordion(body: str) -> str:
    """Wrap every section of level 2 in <details>; the first one is open. A link to an anchor
    inside a closed section opens it (script in PAGE)."""
    parts = re.split(r"(?=<h2 id=)", body)
    out = [parts[0]]
    for i, part in enumerate(parts[1:]):
        heading, _, rest = part.partition("</h2>")
        out.append(f'<details class="sec"{" open" if i == 0 else ""}><summary>{heading}</h2></summary>\n{rest}</details>')
    return "".join(out)


def render(markdown: str, base: str = "", fold: bool = False) -> str:
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    tokens = md.parse(markdown)
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            ident = slug(tokens[i + 1].content)
            token.attrSet("id", ident)
            link = Token("html_inline", "", 0)
            link.content = (f'<a class="anchor" href="#{ident}" aria-label="Link to this section" title="Link to this section">'
                            f"{LINK_ICON}</a>")
            tokens[i + 1].children.append(link)
        for child in token.children or []:
            if child.type == "link_open":
                child.attrSet("href", fix_link(child.attrGet("href"), base))
                if "pages/" in child.attrGet("href"):
                    child.attrSet("target", "_blank")
            elif child.type == "image":
                child.attrSet("src", fix_link(child.attrGet("src"), base))
                child.attrSet("loading", "lazy")
    body = md.renderer.render(tokens, md.options, {})
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return accordion(body) if fold else body


def evidence_page(path: Path) -> tuple[str, str]:
    """Title and body of one evidence entry: a table of the header fields, then the text."""
    entry = evidence.parse(path.read_text(encoding="utf-8"))
    sections = ", ".join(f'<a href="../index.html#sec-{x.replace(".", "-")}">{x}</a>' for x in entry["sections"])
    rows = [("Claim", html.escape(entry["claim"])), ("Proposal sections", sections),
            ("Source", html.escape(", ".join(entry["source"]))),
            ("Page", f'<a href="../pages/{entry["source"][0].replace("Source ", "S")}-p{entry["page"]}.jpg" target="_blank">{entry["page"]}</a>'
                     if entry["page"].isdigit() else html.escape(entry["page"])),
            ("Location", html.escape(entry["location"])), ("Status", html.escape(entry["status"]))]
    table = "<table>" + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows if v) + "</table>"
    body = path.read_text(encoding="utf-8").split("---\n", 2)[2]
    head = f'<p><a href="index.html">Evidence</a> · <a href="../index.html">Proposal</a></p>\n<h1>{entry["id"]}</h1>\n'
    return entry["id"], head + table + render(body, "../")


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    (out / "pages").mkdir(parents=True, exist_ok=True)
    for scan in sorted((ROOT / "evidence" / "pages").glob("S[12]-p[1-8].jpg")):
        crop_to_text(scan, out / "pages" / scan.name)
    (out / "evidences" / "images").mkdir(parents=True, exist_ok=True)
    for image in sorted((ROOT / "evidence" / "images").glob("*.png")):
        shutil.copy2(image, out / "evidences" / "images" / image.name)
    markdown = (ROOT / "proposal.md").read_text(encoding="utf-8")
    title = html.escape(re.match(r"# (.*)", markdown).group(1)) + " | Qatt.org"
    (out / "index.html").write_text(PAGE.format(title=title, body=render(markdown, fold=True)), encoding="utf-8")
    (out / "evidences").mkdir(exist_ok=True)
    for stale in (out / "evidences").glob("E*.html"):   # entries that no longer exist
        stale.unlink()
    for path in evidence.entry_files():
        ident, body = evidence_page(path)
        (out / "evidences" / f"{ident}.html").write_text(PAGE.format(title=f"{ident} | Qatt.org", body=body), encoding="utf-8")
    overview = (ROOT / "evidence" / "README.md").read_text(encoding="utf-8")
    index_body = '<p><a href="../index.html">Proposal</a></p>\n' + render(overview, "../")
    (out / "evidences" / "index.html").write_text(PAGE.format(title="Evidence | Qatt.org", body=index_body), encoding="utf-8")
    ucd_out = out / "ucd"
    ucd_out.mkdir(exist_ok=True)
    for name in ("UnicodeData-draft.txt", "Properties-draft.txt", "NamesList-draft.txt"):
        (ucd_out / name).write_text((ROOT / "ucd" / name).read_text(encoding="utf-8"), encoding="utf-8")
    nav = '<p><a href="../index.html">Proposal</a> · <a href="index.html">Draft character data</a> · <a href="questions.html">Questions</a></p>\n'
    for source, target in (("README.md", "index.html"), ("questions.md", "questions.html")):
        body = render((ROOT / "ucd" / source).read_text(encoding="utf-8"), "../")
        body = re.sub(r"<td>(\w+-draft\.txt)</td>", r'<td><a href="\1">\1</a></td>', body)
        body = body.replace('<a href="questions.md">', '<a href="questions.html">').replace("`questions.md`", "questions.html")
        (ucd_out / target).write_text(PAGE.format(title="Draft character data | Qatt.org", body=nav + body), encoding="utf-8")
    print(f"wrote {out / 'index.html'} and {len(evidence.entry_files())} evidence pages")


if __name__ == "__main__":
    main()

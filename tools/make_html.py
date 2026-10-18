"""Render proposal.md as a web page for the QATT site.

Usage: python tools/make_html.py [OUT_DIR]     (default: ../qatt/unicode/draft)

Writes OUT_DIR/index.html, OUT_DIR/evidences/E*.html (one page per evidence entry, plus an
overview) and OUT_DIR/ucd/ (the draft character data). No images are published: the images
of the evidence entries and the links to the scans are dropped, the passages are given as text.
Needs markdown-it-py.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt
from markdown_it.token import Token

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evidence  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/qtng/qatt-unicode/blob/main"
DEFAULT_OUT = ROOT.parent / "qatt" / "unicode" / "draft"

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
    """Rewrite a link of the Markdown files. base is "" for the proposal and "../" for the
    evidence pages in evidences/."""
    m = re.fullmatch(r"(?:evidence/|\./)?(E\d+[a-z]?)\.md(#.*)?", href)
    if m:
        return f"{'evidences/' if not base else ''}{m.group(1)}.html{m.group(2) or ''}"
    if href == "README.md" and base:
        return "index.html"
    return href


def strip_images(markdown: str) -> str:
    """Drop the images of the evidence entries and the links to scans (not published)."""
    markdown = re.sub(r"^!\[[^\]]*\]\([^)]*\)[ \t]*\n?", "", markdown, flags=re.M)
    return re.sub(r"\[([^\]]*)\]\((?:\.\./|evidence/)?(?:pages|images)/[^)]*\)", r"\1", markdown)


def render(markdown: str, base: str = "") -> str:
    markdown = strip_images(markdown)
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
    body = md.renderer.render(tokens, md.options, {})
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return body


def evidence_page(path: Path) -> tuple[str, str]:
    """Title and body of one evidence entry: a table of the header fields, then the text."""
    entry = evidence.parse(path.read_text(encoding="utf-8"))
    sections = ", ".join(f'<a href="../index.html#sec-{x.replace(".", "-")}">{x}</a>' for x in entry["sections"])
    rows = [("Claim", html.escape(entry["claim"])), ("Proposal sections", sections),
            ("Source", html.escape(", ".join(entry["source"]))),
            ("Page", html.escape(entry["page"])),
            ("Location", html.escape(entry["location"])), ("Status", html.escape(entry["status"]))]
    table = "<table>" + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows if v) + "</table>"
    body = path.read_text(encoding="utf-8").split("---\n", 2)[2]
    head = f'<p><a href="index.html">Evidence</a> · <a href="../index.html">Proposal</a></p>\n<h1>{entry["id"]}</h1>\n'
    return entry["id"], head + table + render(body, "../")


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    out.mkdir(parents=True, exist_ok=True)
    markdown = (ROOT / "proposal.md").read_text(encoding="utf-8")
    title = html.escape(re.match(r"# (.*)", markdown).group(1)) + " | Qatt.org"
    (out / "index.html").write_text(PAGE.format(title=title, body=render(markdown)), encoding="utf-8")
    (out / "evidences").mkdir(exist_ok=True)
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

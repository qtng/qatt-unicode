# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```
pip install -r tools/requirements-dev.txt   # pytest, hypothesis, pyyaml, markdown-it-py, pillow, numpy
python -m pytest                            # all tests (about 17 s, 57 tests)
python -m pytest tools/tests/test_qatt_grammar.py::<name>   # one test
```

Regenerate after changing `evidence/` or `tools/qatt_grammar.py` (run from the repo root, in this order):

```
python tools/make_appendix.py    # Appendix B of proposal.md and the evidence overview
python tools/make_crops.py       # evidence cut-outs (evidence/crops.csv)
python tools/make_ucd.py         # draft character data in ucd/
python tools/link_refs.py        # links to evidence ids (E07) and page references (p. 6)
python tools/make_html.py [DIR]  # web pages; default output ../qatt/unicode/draft (the qtng/qatt checkout next to this one)
```

Generated sections of `proposal.md` and the files under `ucd/` and `evidence/` overview come from these scripts: edit the source (`evidence/E*.md`, `corrections.csv`, the grammar) and rerun, do not hand-edit the output.

## Architecture

- `proposal.md` is the specification (the encoding model: every combination written with an explicit joiner, components in reading order). Its open points are marked `[TBD]` and planned in `ROADMAP.md`.
- `tools/qatt_grammar.py` is the reference implementation of that model, in two separate steps: `segment` splits text into clusters with pairwise rules only (UAX #29 style), and `validate_cluster` checks each cluster against the grammar from proposal sections 5 and 6. Ill-formed text must still segment predictably, so do not "repair" pairs in `segment`. The tests in `tools/tests/` check the grammar and the evidence catalogue.
- `evidence/` holds one Markdown file per claim that needs a source citation (`E01`–`E39`, some numbers unused), with images in `evidence/images/` and page scans in `evidence/pages/`. Proposal text cites these ids; `link_refs.py` turns them into links.
- `ucd/` is draft character data (UnicodeData, Properties, NamesList) and the open questions for Unicode experts. It is generated from the grammar by `make_ucd.py`; values the proposal marks `[TBD]` are filled with the most likely value and listed in `ucd/questions.md`, so do not treat them as decided.
- The block position is not assigned: the reference implementation uses a provisional base in the Supplementary Private Use Area-A, and only the offsets inside the block come from the proposal. Do not present the code points as final.

## Cross-repo

`qtng/qatt` (checked out next to this repo) reads `ucd/` and `tools/make_ucd.py` through `qtng/qatt`'s `tools/update_unicode_data.py` to refresh `unicode.html`. Changes here that alter character data therefore also need that update in `qtng/qatt`, and the fonts are rebuilt in the private repository `qtng/chunom-private` (not in this repo).

# qatt-unicode

Working repository for a Unicode encoding proposal for Quốc Âm Tân Tự (QATT), a Vietnamese script found in Han Nôm texts.

Status: draft. Open points are listed in section 9 of the proposal and marked \[TBD\] in the text.

## Contents

| File | Content |
| --- | --- |
| [proposal.md](proposal.md) | Current proposal draft: every combination written with an explicit joiner, components in reading order |
| [ROADMAP.md](ROADMAP.md) | Plan for resolving the open points |
| [evidence/](evidence/) | Evidence catalogue: one row per claim that needs a source citation, with images |
| [ucd/](ucd/) | Draft character data (UnicodeData, properties, names list) and open questions for the Unicode experts |
| [tools/qatt_grammar.py](tools/qatt_grammar.py) | Reference implementation: segmentation and validation of QATT sequences |
| [tools/tests/](tools/tests/) | Unit and property tests for the reference implementation |

The block position is not assigned yet. The reference implementation uses a provisional base in Supplementary Private Use Area-A; only the offsets within the block come from the proposal.

## Generated content

After changing the evidence catalogue or the reference implementation, regenerate:

```
python tools/make_appendix.py   # Appendix B of proposal.md from evidence/catalog.csv
python tools/make_ucd.py        # draft character data in ucd/
```

## Running the tests

```
pip install -r tools/requirements-dev.txt
python -m pytest
```

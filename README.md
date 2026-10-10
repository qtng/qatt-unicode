# qatt-unicode

Working repository for a Unicode encoding proposal for Quốc Âm Tân Tự (QATT), a Vietnamese script found in Han Nôm texts.

Status: draft. Open points are listed in section 9 of the proposal and marked \[TBD\] in the text.

## Contents

| File | Content |
| --- | --- |
| [proposal.md](proposal.md) | Current proposal draft: every combination written with an explicit joiner, components in reading order |
| [qatt_grammar.py](qatt_grammar.py) | Reference implementation: segmentation and validation of QATT sequences |
| [tests/](tests/) | Unit and property tests for the reference implementation |

The block position is not assigned yet. The reference implementation uses a provisional base in Supplementary Private Use Area-A; only the offsets within the block come from the proposal.

## Running the tests

```
pip install -r requirements-dev.txt
python -m pytest
```

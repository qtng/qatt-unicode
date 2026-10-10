# Evidence

`catalog.csv` lists every claim in the proposal that needs a source citation, one row per claim. Appendix B and the \[TBD\] citations in the proposal will be generated from it.

| Field | Content |
| --- | --- |
| id | Stable identifier (E01, E02, …); add a row per further passage, e.g. E12a |
| claim | The statement in the proposal that the passage supports |
| proposal_sections | Sections of `proposal.md` that rely on the claim |
| source | Source 1 or Source 2, or another reference |
| page | Page or folio |
| location | Column and line on the page |
| image | File name in `images/` |
| transcription | Text of the passage; QATT characters as placeholders such as `{CL}` or `{CT}` until a font exists |
| translation | English translation of the passage |
| status | `missing`, `located` (passage known, citation incomplete) or `cited` (all fields filled) |
| notes | Anything else |

Images go in `images/`, named after the row id, for example `E08-1.png`. Publish scans only where the holding institution permits it.

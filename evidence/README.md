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

Cite Source 2, the corrected copy, and add Source 1 only where it differs or where its reading matters. List the source cited first in `source`. The proposal cites by page only, for example (p. 2), and names a source only where it matters.

Images go in `images/`, named after the row id, for example `E08-1.png`. Publish scans only where the holding institution permits it.

## Corrections

`corrections.csv` lists the places where Source 2 differs from Source 1: corrections of characters that are unclear or wrong in Source 1, and local rewrites where the scribe of Source 2 struck out and rewrote his own unclear character.

| Field | Content |
| --- | --- |
| id | Stable identifier (C01, C02, …) |
| page | Page, shared by both sources |
| location | Column and position on the page |
| source_1 | Reading in Source 1 |
| source_2 | Reading in Source 2 |
| type | `correction of Source 1` (character unclear or wrong in Source 1) or `local rewrite in Source 2` (the scribe of Source 2 rewrote his own unclear character; no difference in reading) |
| image | Image file in `images/` |
| notes | Anything else |

A character struck out with three dots is deleted and does not count.

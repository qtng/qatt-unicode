# Evidence

One Markdown file per claim in the proposal that needs a source citation: `E01.md`, `E02.md`, … Each file shows the images of the passage, followed by the transcription, the translation and notes. Appendix B of the proposal and the overview below are generated from these files with `python tools/make_appendix.py`.

## Format

```markdown
---
id: E04
claim: "The statement in the proposal that the passage supports"
sections: [3.2, 4.1]
source: [Source 1]
page: 6
location: "Column and line on the page"
image: [E04-1.png]
status: located
---

![Source 1](images/E04-1.png)

## Transcription
…
## Translation
…
## Notes
…
```

| Field | Content |
| --- | --- |
| id | Stable identifier, also the file name; add `E12a` etc. for further passages |
| claim | The statement in the proposal that the passage supports, in double quotes |
| sections | Sections of `proposal.md` that rely on the claim |
| source | Sources shown, the cited source first |
| page | Page within the manuscript, 1 to 8, shared by both sources (not the folio number of the volume: Source 1 is on folios 3–10, Source 2 on folios 11–18) |
| location | Column and line on the page, in double quotes |
| image | Image files in `images/`, in the order of `source` |
| status | `missing`, `located` (passage known, citation incomplete) or `cited` (all fields filled) |

Transcriptions write QATT characters as placeholders until a font exists: `{CU 翁}` is a standalone unmarked Cán annotated 翁, `{CM 翁}` a standalone marked Cán, `{CH …}` a standalone Chi, `{PT …}` a phản thiết pair, `{QT …}` a QATT character whose class has not been determined.

Cite Source 1, and add Source 2 only where it differs or where its reading matters. Both witnesses share the page numbering and the layout of the columns. The proposal cites by page only, for example (p. 2), and names a source only where it matters.

Full pages are in `pages/`: `S1-p1.jpg` … `S1-p8.jpg` for Source 1 and `S2-p1.jpg` … `S2-p8.jpg` for Source 2, extracted unchanged from the scan of the volume (folios 3–18, 785 × 1525 pixels each). An entry can show a full page by giving its path, for example `image: [pages/S1-p4.jpg]`.

Cut-outs go in `images/`. They are cut from the full pages by `python tools/make_crops.py`, using the page and the pixel box (left, top, right, bottom) listed for each image in `crops.csv`; to change a cut-out, edit its box and run the script again. The optional column `strike` lists boxes (left top right bottom, separated by semicolons) that are not relevant to the evidence; they are framed with a red rectangle and crossed out, so that a full page can be shown with the relevant columns only. Cut-outs are named after the entry id, for example `E08-1.png` (Source 1) and `E08-2.png` (Source 2). Publish scans only where the holding institution permits it.

## Overview

<!-- overview:start -->
| Entry | Claim | Sections | Page | Status |
| --- | --- | --- | --- | --- |
| [E01](E01.md) | The listing under the heading 幹音二十二字 shows 22 forms, the marked Cán, each of three strokes and one short marking stroke | 4.1, 6.4 | 2 | cited |
| [E02](E02.md) | Five Chi per Cán: the marking stroke sits only at stroke ends (six positions); the marked Cán has it at the start position (upper left or upper middle), and moving it counter-clockwise gives the Chi in order | 4.1 | 3 | cited |
| [E04](E04.md) | Components written standalone and side by side when the text explains combination, including a standalone unmarked Cán and two adjacent unmarked Cán | 3.2, 4.1, 5.4 | 6 | located |
| [E05](E05.md) | Phản thiết method described in the section Phản Thiết Hài Âm Pháp (反切諧音法); components of different bases, unmarked Cán first | 3.2, 4.2 | 5 | located |
| [E06](E06.md) | Function in a phản thiết pair: the unmarked Cán gives the initial, the Chi the rhyme | 4.2 | – | located |
| [E07](E07.md) | Hợp Thư: same-base pairs only, Chi first (scope of the term) | 3.2, 4.2, 5.7 | 6 | located |
| [E08](E08.md) | Function in a Hợp Thư: Chi gives the initial, unmarked Cán the rhyme (main argument for the reading order) | 4.2, 5.4 | 6 | located |
| [E09](E09.md) | Omission convention: a same-base phản thiết pair is written as the Chi alone | 3.2, 4.2 | – | missing |
| [E10](E10.md) | Tham Thư rule: the base is a Hợp Thư | 4.3 | 7 | located |
| [E11](E11.md) | Reading of a Tham Thư and function of its components | 4.3 | – | missing |
| [E12](E12.md) | Attested Tham Thư, first example | 4.3, B | – | missing |
| [E13](E13.md) | Attested Tham Thư, second example | 4.3, B | – | missing |
| [E14](E14.md) | Tone marks: circle and semicircle in four corners, eight tones | 4.4 | 4 | located |
| [E15](E15.md) | Tone marks in all four corners, both shapes: the unmarked Cán of đông written with all eight tone marks, annotated 東 董 凍 篤 同 洞 動 獨 | 4.4, B | 5 | located |
| [E16](E16.md) | Semicircle orientation: open side facing the centre in every example | 4.4 | – | missing |
| [E17](E17.md) | Eight tones follow the Chinese yin-yang method | 2.1 | 4 | located |
| [E18](E18.md) | Listing of the 22 base sounds (幹音二十二字) in source order, each shown with its QATT character and annotated with the name of its sound in Chữ Nôm | 6.4, 7.1 | 2 | cited |
| [E19](E19.md) | Script runs with vertical Hán Nôm text, treated like Hán Nôm characters | 3.1, 6.3 | – | missing |
| [E20](E20.md) | Date and provenance of source 1 | 2.1, 3.1 | – | located |
| [E21](E21.md) | Date and provenance of source 2 | 2.1, 3.1 | – | located |
| [E22](E22.md) | Modern use of the script, including written forms in online discussion | 3.3 | – | located |
| [E23](E23.md) | Source 2 has the same content and page numbering as Source 1; whether it was copied from Source 1 or from an earlier original cannot be determined | 1, 3 | – | located |
| [E24](E24.md) | Tone marks are optional: marked and unmarked characters in the same passage | 4.4, 5.6 | 6 | located |
| [E25](E25.md) | The neutral tone (ngang, âm bình) has its own mark, a semicircle in the lower left corner; an unmarked character does not mean the neutral tone | 4.4, 5.6 | 6 | located |
| [E26](E26.md) | Tone marks on standalone components (unmarked Cán and Chi) | 4.4, 5.3 | 6 | located |
| [E27](E27.md) | Round and angular forms of the same tone mark are handwriting variation: Source 1 writes the mark now round, now close to a hook; Source 2 writes all tone marks of the passage angular | 4.4, 8 | 6 | located |
| [E28](E28.md) | The source lists the tones first with the four half circles, then the four full circles, each starting lower left and running clockwise | 7 | 5 | located |
| [E29](E29.md) | Table of the Chi under the heading 枝字一百一十字, 'the 110 Chi'; the table shows 109, one left out by oversight | 4.1, 6.4, 7.1 | 3 | located |
| [E30](E30.md) | Dating: the character 華 lacks its final stroke, a naming taboo for Hồ Thị Hoa, mother of Emperor Thiệu Trị (1841–1847) | 1, 2.1, 3.1 | 1 | cited |
| [E31](E31.md) | Author's signature: Nam Thành cư sĩ Nguyễn Tử (南城居士阮子) | 2.1 | 2 | cited |
| [E32](E32.md) | Classification of the manuscripts as tiểu học (小學) and catalogued as nôm văn thư (喃文書) | 2.1 | – | missing |
| [E33](E33.md) | Name of the script: 國音新字 (Quốc Âm Tân Tự), in the heading of the preface 國音新字序 | 1, 2, 2.1 | 1 | cited |
| [E34](E34.md) | Marked Cán and unmarked Cán both appear standalone, with the same reading, also with tone marks; only the unmarked Cán combines, never the marked Cán | 4.1, 5.3 | 5 | located |
| [E35](E35.md) | The source contains no running text in the script: only single characters given as examples and spelling formulas in the phản thiết manner, within Hán Nôm text | 2.1, 4.1 | – | located |
| [E36](E36.md) | Counts of the characters in the section 音数: 176 single Cán, 880 single characters, 880 合書 with Chi left and Cán right, 18,480 合書 with Cán left and Chi right, each including the tone marks; eight times 22, 110, 110 and 2,310 | 4.1, 4.2, 4.5 | 8 | located |
| [E37](E37.md) | The term Cán (幹): the listing of the 22 Cán is headed 幹音二十二字, 'trunk sounds, twenty-two characters' | 4.1, 6.4 | 2 | cited |
| [E38](E38.md) | The term Cán (幹) also occurs with 字 in 二十二幹字為標, 'the 22 Cán characters as the mark'; with 幹音二十二字 (E37) the source uses 幹 with 音 and with 字 | 4.1 | 7 | cited |
| [E39](E39.md) | Passage on p. 7, first and second column, without heading: a worked example of a phản thiết pair, the unmarked Cán of ONG and the Chi MARKED-5 of CHONG, read yên, and a list of five characters | 4.2 | 7 | located |
<!-- overview:end -->

## Corrections

`corrections.csv` lists the places where Source 2 differs from Source 1: corrections of characters that are unclear or wrong in Source 1, and local rewrites where the scribe of Source 2 struck out and rewrote his own unclear character.

| Field | Content |
| --- | --- |
| id | Stable identifier (C01, C02, …) |
| page | Page within the manuscript, 1 to 8, shared by both sources |
| location | Column and position on the page |
| source_1 | Reading in Source 1 |
| source_2 | Reading in Source 2 |
| type | `correction of Source 1` (character unclear or wrong in Source 1) or `local rewrite in Source 2` (the scribe of Source 2 rewrote his own unclear character; no difference in reading) |
| image | Image file in `images/` |
| notes | Anything else |

A character struck out with three dots is deleted and does not count.

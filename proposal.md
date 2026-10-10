# QATT Unicode Proposal – Draft

Oct 9, 2026 · @Trung

## 1. Summary

This proposal encodes Quốc Âm Tân Tự (QATT), a Vietnamese script used inside Han Nôm texts, as 164 characters in the Supplementary Multilingual Plane.

| Item | Entry |
| --- | --- |
| Script | Quốc Âm Tân Tự (QATT) |
| Proposer | \[TBD: name and affiliation\] |
| Draft date | 2026-10-09 |
| Characters | 164: 154 components, 2 joiners, 8 tone marks |
| Model | Atomic components in reading order; every combination written with an explicit joiner |
| Plane | Supplementary Multilingual Plane \[TBD: block position assigned by the UTC\] |
| Direction | Follows Han Nôm; the source is vertical |
| Attested sources | Two: a vertical Han Nôm text and a handwritten copy of it |
| Official form | \[TBD: complete the UTC Proposal Summary Form\] |

## 2. Introduction

Quốc Âm Tân Tự is a Vietnamese script built from 22 base components, each of three strokes and one short marking stroke. The base components stand alone; forms derived from them stand alone or combine in groups of two or three, and any character may carry a tone mark in one of its corners.

### 2.1 Background

In the source the script appears in running Han Nôm text and is treated exactly like Han Nôm characters. Three-component characters (Tham Thư) record dialectal vowel clusters. Eight tones are marked with circles and semicircles in the corners, following the Chinese yin-yang method. \[TBD: date and provenance of the sources; scholarly literature\]

### 2.2 Reasons for encoding

&#91;TBD: need for digital text, scholarship, user community and interest in the script\]

## 3. Sources and Evidence

Two sources attest the script. Both are vertical Han Nôm texts, and the text describes the methods of combination. Source 2 is a handwritten copy of Source 1 with the same content and the same page numbering. It corrects Quốc Âm Tân Tự characters that are unclear in Source 1 and some obvious scribal errors. The two sources are therefore one text in two witnesses. Page references in this proposal, such as (p. 2), refer to Source 2, the corrected copy; since both witnesses share the page numbering, they apply to Source 1 as well. Source 1 is named only where it differs or where its reading matters. \[TBD: list the places where Source 2 corrects Source 1\]

### 3.1 Attested sources

| Source | Date | Location | Text type | Direction |
| --- | --- | --- | --- | --- |
| Source 1 | \[TBD\] | \[TBD\] | Han Nôm | Vertical |
| Source 2 | \[TBD\] | \[TBD\] | Han Nôm, handwritten copy of Source 1 | Vertical |

### 3.2 Evidence by feature

| Feature | Evidence | Status |
| --- | --- | --- |
| Cán Tự, Chi Tự, Cán Lược | Described in the source; the 22 Cán Tự are listed with their names in the section 幹音二十二字 (p. 2) | \[TBD: cite passages and examples for Chi Tự and Cán Lược\] |
| Phản thiết pairs | Described in the section Phản Thiết Hài Âm Pháp (反切諧音法); components of different bases, Cán Lược first | \[TBD: cite passages and examples; function of the two components\] |
| Hợp Thư | Described in the text; every example is a same-base pair with the Chi Tự first; the Chi Tự gives the initial, the Cán Lược the rhyme | \[TBD: list the examples; cite the passage on the function of the components; confirm that the term covers only same-base pairs\] |
| Tham Thư | Rule described in the text, with a Hợp Thư as the base and the third component extending the rhyme; two examples attested, both on a Hợp Thư | \[TBD: cite both examples\] |
| Standalone and adjacent components | When the text explains how components combine, it writes components on their own and side by side without combining them, including a standalone Cán Lược and two adjacent Cán Lược, in a passage of the form 如{CL}{CT}反切云{CL}{CL}鳥衣是合取衣字也 | \[TBD: exact components, source and page\] |
| Omission of the Cán Lược | Wherever a phản thiết pair of the same base would occur, the source writes the Chi Tự alone | \[TBD: list the places\] |
| Tone marks | Eight tones in four corners; the neutral tone marked with a semicircle lower left; marked and unmarked characters in one passage; round and angular forms of the same mark (p. 6) | \[TBD: passage explaining the tone system; examples for the other corners\] |
| Writing direction | The text is silent; both witnesses are vertical Han Nôm | Assumption: Han Nôm habits |

### 3.3 Modern use

&#91;TBD: current use of the script, for example on chunom.org, and any user community\]

### 3.4 Scans and images

&#91;TBD: scans of the source pages with the relevant passages marked\]

## 4. Structure of the Script

Quốc Âm Tân Tự is built from 22 base components that stand alone. Their derived forms stand alone or combine in groups of two or three, and any character may carry one tone mark in one of its four corners.

### 4.1 Components

Each of the 22 base components (*Cán Tự*) consists of three strokes and one short marking stroke. The marking stroke always sits at the end of a stroke, so the three strokes give six positions. In every attested Cán Tự it sits at the start position, upper left or upper middle depending on the base. Moving it counter-clockwise from one stroke end to the next yields the five variants of the base (*Chi Tự*), in order. \[TBD: cite the passage on the positions\] Omitting it yields one reduced form per base (*Cán Lược*). Because every Chi Tự moves the marking stroke, no Chi Tự coincides with its Cán Tự: each base has six distinct marked forms and one unmarked form. A Cán Lược does not form a character on its own, but the source writes it standalone when it explains how components combine (3.2).

| Component | Count | Derivation | Standalone | In combination |
| --- | --- | --- | --- | --- |
| Cán Tự | 22 | 3 strokes + 1 marking stroke | yes | never |
| Chi Tự | 110 (22 × 5) | marking stroke repositioned | yes | yes |
| Cán Lược | 22 | marking stroke omitted | only when the text discusses components | with a Chi Tự |

### 4.2 Two-component characters: phản thiết and Hợp Thư

A Cán Lược and a Chi Tự combine into one character. The source describes two methods.

- **Phản thiết.** The Cán Lược and the Chi Tự derive from different Cán Tự, and the Cán Lược comes first. The section Phản Thiết Hài Âm Pháp (反切諧音法) describes these pairs; the source gives them no name of its own, and this proposal calls them phản thiết pairs. A phản thiết pair of the same base would add nothing to the Chi Tự, so the source writes the Chi Tự alone instead. \[TBD: function of the two components in a phản thiết pair\]
- **Hợp Thư.** The Chi Tự and the Cán Lược derive from the same Cán Tự, and the Chi Tự comes first. The source describes this arrangement as an exchange of positions. It is not only visual: in reading, the Chi Tự gives the initial consonant and the Cán Lược the rhyme. There are 110 Hợp Thư, one for each Chi Tự.

When the source explains these methods, it also writes components on their own and side by side without combining them (3.2). In a Hợp Thư the written order of the components is also their reading order. \[TBD: cite the source passages for both methods, the function of the components and the attested examples; whether the written order is also the reading order in a phản thiết pair\]

### 4.3 Tham Thư (three components)

A Hợp Thư may carry a third component, a single Chi Tự, above it. The third component extends the rhyme of the Hợp Thư, so in reading order it comes last: initial, rhyme, rhyme extension. The base is always a Hợp Thư; a phản thiết pair or a single Chi Tự is not a base. The third component is otherwise unrestricted. The method records dialectal vowel clusters. This allows 110 bases and 110 × 110 = 12,100 Tham Thư.

The two attested Tham Thư both have a Hợp Thư as the base, as the rule requires. \[TBD: cite the source passage for the base rule, the function of the third component and both examples\]

### 4.4 Tone marks

A tone mark is a circle or a semicircle placed in one of the four corners of the character, giving the eight tones of the Chinese yin-yang system. The corner gives the tone class and the shape gives the register: a semicircle marks âm (陰), a circle dương (陽).

| Corner | Tone class | Semicircle (âm) | Circle (dương) |
| --- | --- | --- | --- |
| Lower left | bình 平 | âm bình (ngang) | dương bình (huyền) |
| Upper left | thượng 上 | âm thượng (hỏi) | dương thượng (ngã) |
| Upper right | khứ 去 | âm khứ (sắc) | dương khứ (nặng) |
| Lower right | nhập 入 | âm nhập (sắc in syllables ending in -p, -t, -c) | dương nhập (nặng in syllables ending in -p, -t, -c) |

The neutral tone ngang has its own mark, a semicircle in the lower left corner (p. 6). A character carries at most one tone mark, and many carry none; on p. 6 a passage marks every Quốc Âm Tân Tự character with the neutral tone except the last two, which carry no mark. An unmarked character therefore leaves the tone unspecified. Standalone components carry tone marks as well (p. 6).

The source does not specify the orientation of the semicircle; every example shows its open side facing the centre of the character. Round and angular forms of the semicircle are handwriting variation, not different marks: Source 1 writes the same mark now round, now close to a hook, while Source 2 writes every tone mark of the passage on p. 6 angular. \[TBD: cite a passage that explains the tone system; examples for the other corners\]

### 4.5 Layout

&#91;TBD: position of the two components within a phản thiết pair and within a Hợp Thư, and of the top component within a Tham Thư\]

## 5. Encoding Model

The script is encoded as 164 atomic characters: 154 components, two joiners and eight tone marks. Components are stored in reading order and drawn in that order; no component is reordered. Every combination is written with an explicit joiner, and components without a joiner are separate characters. Two- and three-component characters are sequences, so every character stays editable and its boundaries are determined locally.

### 5.1 Repertoire

| Group | Characters |
| --- | --- |
| Cán Tự | 22 |
| Cán Lược | 22 |
| Chi Tự | 110 |
| Tham Thư combiner | 1 |
| Component joiner | 1 |
| Tone marks (combining) | 8 |
| **Total** | **164** |

### 5.2 Why not precomposed

A Cán Lược and a Chi Tự allow 2,420 two-component characters (22 Cán Lược × 110 Chi Tự): 2,310 phản thiết pairs and 110 Hợp Thư. Tham Thư allows 110 × 110 = 12,100. Precomposing would need 14,520 code points, most of them for combinations of which only two are attested. Precomposing is neither feasible nor justified.

### 5.3 Sequence grammar

```
Character := Cluster [ToneMark]
Cluster   := CanTu | ChiTu | CanLuoc | PhanThiet | HopThu | ThamThu
PhanThiet := CanLuoc(X) Joiner ChiTu(Y)      X ≠ Y; Cán Lược first
HopThu    := ChiTu(X) Joiner CanLuoc(X)      same Cán Tự X; initial, then rhyme
ThamThu   := HopThu Combiner ChiTu           rhyme extension last
```

The component joiner joins two components into one character, and their order gives the arrangement. Components without a joiner are separate characters; a standalone Cán Lược occurs only where the text discusses components (3.2). The same-base conditions do not affect segmentation; they are checked by validation (6.2).

| Intended character | Sequence |
| --- | --- |
| Standalone Cán Tự | CAN |
| Standalone Chi Tự | CT |
| Standalone Cán Lược (discussion of components) | CL |
| Components side by side, not combined | CL(X) CT(Y) |
| Phản thiết pair | CL(X) JOIN CT(Y) |
| Same-base phản thiết reading (written as the Chi Tự alone) | CT(X) |
| Hợp Thư | CT(X) JOIN CL(X) |
| Tham Thư | CT(X) JOIN CL(X) COMB CT(Z) |
| Any character above with a tone | sequence + TONE |

Sequences outside these patterns are not prohibited. They are not attested, and this proposal does not specify their rendering.

### 5.4 Reading order and the component joiner

In a Hợp Thư the Chi Tự gives the initial and the Cán Lược the rhyme (4.2). Storing the Chi Tự first follows the reading order, which is also the written order, so rendering needs no reordering.

The joiner carries information that the components alone do not. The source writes components side by side without combining them (3.2), so `CL CT` may be two separate components or a phản thiết pair, and `CT CL` may be a Chi Tự followed by a separate Cán Lược or a Hợp Thư. The joiner decides. Every attested two-component character therefore contains it.

### 5.5 Edit stability

Deleting or inserting one character alters at most the cluster at the edit point and its immediate neighbours. An edit can split a cluster, merge two neighbours (for example when the top component of a Tham Thư is deleted and the next Chi Tự takes its place) or attach a tone mark to the preceding cluster. Nothing beyond the neighbours changes.

The guarantee also holds for ill-formed text, because segmentation uses pairwise rules only (6.2): whether a boundary lies between two characters depends on those two characters alone, and there is never a break before or after a joiner. An ill-formed chain such as `CT COMB CT COMB CT` therefore forms one cluster, which a validator reports as ill-formed. Segmentation never pairs up the parts of such a chain, so an edit inside it cannot regroup the text beyond it.

**Why the joiner is needed.** Without the joiner, a Hợp Thư would be the bare sequence Chi Tự, Cán Lược. With B a Chi Tự and A a Cán Lược of the same base, the sequence `BAB` would then read as `[BA][B]` or as `[B][AB]`, and both are valid text. A left-to-right parser takes the first reading, so deleting the first A in `ABABAB` would regroup all following characters from `[AB][AB][AB]` into `[BA][BA][B]`. With the joiner, `B JOIN A B` is `[BA][B]`, `B A JOIN B` is `[B][AB]` and `B A B` is three separate components: each reading has one spelling, and edits stay local.

### 5.6 Tone marks

The eight tone marks are combining characters that follow the complete cluster. Each corner and each mark type is contrastive, so a tone is a character and not a glyph variant. An unmarked cluster leaves the tone unspecified; it does not denote the neutral tone, which has its own mark (4.4). All eight marks are therefore needed. The orientation of the semicircle follows from its corner and is a glyph property. A cluster takes at most one tone mark.

### 5.7 Alternatives considered

- Automatic exchange: a Hợp Thư stored as Cán Lược, Chi Tự, with the font exchanging the components when both share a Cán Tự. Not adopted, because it stores the rhyme before the initial, against the reading order, and relies on a rendering rule that compares bases. It would also fix `CL(X) CT(X)` to the Hợp Thư for good.
- Implicit phản thiết, in which a Cán Lược binds to the following character without a joiner and only a Hợp Thư uses the joiner: not adopted, because the source also writes a Cán Lược standalone and components side by side (3.2). A forward-binding Cán Lược would join them wrongly, for example with a following Han character.
- Joiner that exchanges the components (`CL(X) JOIN CT(X)`, drawn exchanged): not adopted, because it keeps the order against reading.
- Joiner as a suffix (`CT(X) CL(X) JOIN`): not adopted, because it groups preceding characters retroactively, which needs right context in segmentation. Joiners such as U+200D ZERO WIDTH JOINER stand between the parts they join, and so does the Tham Thư combiner.
- One joiner for both two- and three-component characters (163 characters): not adopted, because the structure would follow from position instead of from the joiner, and the decision in 5.8 could no longer be taken for the Tham Thư combiner alone.
- Variation selector: rejected, because the two orders differ in reading, and a variation selector may only select a glyph variant of the same character.
- Separate code points for the Cán Lược of a Hợp Thư: rejected, 22 code points instead of one joiner.
- Broad reading of Hợp Thư, in which the term covers every Cán Lược + Chi Tự pair and a Tham Thư base may be any pair or a single Chi Tự (278,300 Tham Thư): not adopted, because it needs an unattested base and does not match the division of the source into Hợp Thư and Phản Thiết Hài Âm Pháp. \[TBD: cite the passages that support the narrow reading\]
- Two tone marks plus a position selector: rejected, because the corner is contrastive.
- Precomposed Hợp Thư and Tham Thư: rejected for size (5.2).

### 5.8 Open decision

Propose the Tham Thư combiner now, or describe Tham Thư with IDS first and add the combiner once more attestations exist. With two attested examples, the second option lowers the risk of rejection. Without the combiner the repertoire has 163 characters, the component joiner and the tone marks move up by one code point, and the size argument for Tham Thư in 5.2 no longer applies. The component joiner is needed in either case.

## 6. Character Properties

The proposed properties follow from the encoding model: components are letters, the two joiners are format characters, and tone marks are nonspacing marks. Cells marked \[TBD\] depend on evidence from the source or on review by the Unicode text-segmentation experts.

| Characters | General\_Category | Combining class | Grapheme\_Cluster\_Break | Line\_Break | Bidi\_Class |
| --- | --- | --- | --- | --- | --- |
| Cán Tự, Chi Tự | Lo | 0 | Other | ID | L |
| Cán Lược | Lo | 0 | Other | ID | L |
| Tham Thư combiner | Cf | 0 | \[TBD\] | CM | \[TBD\] |
| Component joiner | Cf | 0 | \[TBD\] | CM | \[TBD\] |
| Tone marks (8) | Mn | 0 | Extend | CM | NSM |

### 6.1 Combining class of the tone marks

The corner is part of each tone mark's identity, so no positional combining classes are needed. A cluster takes at most one tone mark, so canonical reordering between marks never occurs. All eight marks therefore take class 0. \[TBD: confirm with current Unicode conventions\]

### 6.2 Grapheme clusters

Segmentation uses pairwise rules only: there is no break directly before or after either joiner and no break before a tone mark; every other boundary is a break. Tone marks match Extend. Components that are not joined, including a standalone Cán Lược, form clusters of their own, so all components behave alike. Whether a cluster is well-formed is left to validation (5.5). \[TBD: decide between existing property values and new ones; compare with the Egyptian hieroglyph format controls; Bidi\_Class of the joiners, since format characters usually take BN\]

### 6.3 Line breaking and direction

The source does not state a writing direction. Both witnesses contain vertical Han Nôm text, and in every case the script is treated exactly like Han Nôm and flows with it: vertical lines, columns running right to left, no spaces between words. No horizontal use is attested. The proposal therefore assumes the writing habits of Han Nôm. The characters behave like ideographs, each occupying one square cell. Proposed for the components: Bidi\_Class L, Line\_Break ID, East\_Asian\_Width W, Vertical\_Orientation U. Tone marks and the joiners never start a line, because they belong to the preceding cluster.

### 6.4 Code point order

The source lists the 22 Cán Tự in the section 幹音二十二字, "the twenty-two characters of the trunk sounds", each annotated with its name in Chữ Nôm (p. 2). The order groups the initials roughly by place of articulation. It has no encoding significance, so code points follow the order of that listing and no collation claim is made. Within each Cán Tự, the five Chi Tự follow the order of the marking-stroke position, counter-clockwise from the position of the Cán Tự (4.1).

## 7. Character Table and Code Chart

The 164 characters fit in a block of 176 code points (11 columns of 16), proposed for the Supplementary Multilingual Plane. \[TBD: block position assigned by the UTC\] Code points follow the source order of the 22 Cán Tự, and the five Chi Tự of each base are consecutive.

| Group | Offset in block | Count |
| --- | --- | --- |
| Cán Tự | +00 to +15 | 22 |
| Cán Lược | +16 to +2B | 22 |
| Chi Tự | +2C to +99 | 110 |
| Tham Thư combiner | +9A | 1 |
| Component joiner | +9B | 1 |
| Tone marks | +9C to +A3 | 8, in the traditional order of the eight tones (see below) |
| Reserved | +A4 to +AF | 12 |

The tone marks follow the traditional order of the eight tones, the numbering 1 to 8 used in Chinese dialectology: âm bình, dương bình, âm thượng, dương thượng, âm khứ, dương khứ, âm nhập, dương nhập, that is by tone class and within each class âm before dương. The first six correspond to the Vietnamese tone order ngang, huyền, hỏi, ngã, sắc, nặng used in dictionaries and in Vietnamese collation. The source lists the marks in a different order, first the four semicircles and then the four circles, each starting lower left and running clockwise; that order presents the marks by shape and is not adopted for the code points. \[TBD: cite the passage that lists the tone marks\]

| Offset | Mark | Tone |
| --- | --- | --- |
| +9C | Semicircle, lower left | âm bình (ngang) |
| +9D | Circle, lower left | dương bình (huyền) |
| +9E | Semicircle, upper left | âm thượng (hỏi) |
| +9F | Circle, upper left | dương thượng (ngã) |
| +A0 | Semicircle, upper right | âm khứ (sắc) |
| +A1 | Circle, upper right | dương khứ (nặng) |
| +A2 | Semicircle, lower right | âm nhập |
| +A3 | Circle, lower right | dương nhập |

### 7.1 Character names

Names use ASCII capitals without diacritics, as Unicode requires. Patterns:

```
QUOC AM TAN TU CAN TU <NAME>
QUOC AM TAN TU CAN LUOC <NAME>
QUOC AM TAN TU CHI TU <NAME>-<N>
QUOC AM TAN TU THAM THU COMBINER
QUOC AM TAN TU COMPONENT JOINER
QUOC AM TAN TU TONE CIRCLE UPPER LEFT
QUOC AM TAN TU TONE SEMICIRCLE LOWER RIGHT
```

The tone marks use the corners UPPER LEFT, UPPER RIGHT, LOWER LEFT and LOWER RIGHT, each for circle and semicircle. The names describe the mark; the tone it denotes is given as an annotation, for example QUOC AM TAN TU TONE SEMICIRCLE LOWER LEFT = âm bình (ngang).

The five Chi Tự of a base are named after their Cán Tự and numbered 1 to 5 in the order of the marking-stroke position, counter-clockwise from the position of the Cán Tự (4.1), for example QUOC AM TAN TU CHI TU ONG-1 to QUOC AM TAN TU CHI TU ONG-5. The positions are relative to the Cán Tự and lie in different places for different bases, so the names number them instead of describing them geometrically.

The names of the 22 Cán Tự come from the source listing (6.4), where each Cán Tự is annotated with a Chữ Nôm character; annotations without an encoded character are given as Ideographic Description Sequences. Each name is the syllable of the initial with the rhyme ông. The source gives the Cán Lược no names of their own and sometimes call them by the name of their Cán Tự, so each Cán Lược takes the name of its Cán Tự. Diacritics are dropped. To keep đông and dông apart, đ is written DD and d is written DZ, following an established convention for Vietnamese: đông → DDONG, dông → DZONG.

| No. | Nôm annotation | Reading | Initial | Name in character names | Cán Tự | Cán Lược |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 翁 | ông | Ɂ | ONG | +00 | +16 |
| 2 | ⿰木禺 | ngông | Ng | NGONG | +01 | +17 |
| 3 | 胸 | hông | H | HONG | +02 | +18 |
| 4 | ⿰木功 | gông | G | GONG | +03 | +19 |
| 5 | 工 | công | C | CONG | +04 | +1A |
| 6 | ⿰竜羽 | lông | L | LONG | +05 | +1B |
| 7 | ⿰竜里 | trông | Tr | TRONG | +06 | +1C |
| 8 | 東 | đông | Đ | DDONG | +07 | +1D |
| 9 | 農 | nông | N | NONG | +08 | +1E |
| 10 | 宗 | tông | T | TONG | +09 | +1F |
| 11 | 通 | thông | Th | THONG | +0A | +20 |
| 12 | ⿰亻戍 | nhông | Nh | NHONG | +0B | +21 |
| 13 | 柊 | chông | Ch | CHONG | +0C | +22 |
| 14 | ⿰月容 | dông | D | DZONG | +0D | +23 |
| 15 | 衝 | xông | X | XONG | +0E | +24 |
| 16 | 空 | không | Kh | KHONG | +0F | +25 |
| 17 | 滝 | sông | S | SONG | +10 | +26 |
| 18 | ⿱山庸 | rông | R | RONG | +11 | +27 |
| 19 | 蒙 | mông | M | MONG | +12 | +28 |
| 20 | 芃 | bông | B | BONG | +13 | +29 |
| 21 | ⿰木芃 | vông | V | VONG | +14 | +2A |
| 22 | ⿰口風 | phông | Ph | PHONG | +15 | +2B |

### 7.2 Code chart

&#91;TBD: reference glyphs from the font, showing every Cán Tự, Chi Tự, Cán Lược, the two joiners and the tone marks in their corners\]

## 8. Font Design Notes

A conforming font draws every cluster in one square cell and composes it with substitution and positioning rules, not with precomposed glyphs.

- **Cell:** Each cluster fills one square cell with the metrics of Han Nôm ideographs, so it sits in vertical or horizontal lines without adjustment.
- **Two-component characters:** The two component glyphs share the cell. \[TBD: positions, see 4.5\]
- **No reordering:** Components are drawn in stored order. The component joiner tells the font to compose the two components in one cell; their order gives the arrangement, Cán Lược first for a phản thiết pair and Chi Tự first for a Hợp Thư. Components without a joiner are drawn as separate characters. \[TBD: positions, see 4.5\]
- **Tham Thư:** After the combiner, the Chi Tự is drawn above the Hợp Thư. The font composes the cluster by contextual substitution and positioning, because 12,100 precomposed glyphs are impractical. The two attested examples serve as test cases for the reference font.
- **Tone marks:** Eight combining glyphs sit in the four corners of the whole cluster cell. The open side of the semicircle faces the centre. Round or angular outlines are a design choice, since the source treats the difference as handwriting variation.
- **Reference font:** \[TBD: designer and licence\]

## 9. Open Points

Thirteen points remain before the proposal can be submitted. The alternatives already weighed are in 5.7.

| Point | Section | What is needed |
| --- | --- | --- |
| Tham Thư combiner now, or IDS first | 5.8 | Decision |
| Scope of the term Hợp Thư (same-base pairs only) | 3.2, 4.2, 5.7 | Source passages for the narrow reading |
| Function of the components: initial and rhyme in phản thiết pairs and Hợp Thư, rhyme extension in Tham Thư | 3.2, 4.2, 4.3 | Source passages; this is the main argument for the reading order (5.4) |
| Proposer and UTC Proposal Summary Form | 1 | Name, affiliation, completed form |
| Date and provenance of the sources, scholarly literature | 2.1, 3.1, D | Source data and references |
| Reasons for encoding and modern use | 2.2, 3.3 | Description of need and user community |
| Source passages and scans for the components, standalone and adjacent components, phản thiết pairs, Hợp Thư, the omission convention, Tham Thư and the tone corners | 3.2, 3.4, 4.1 to 4.4, B, C | Citations and images |
| Layout of the components in two-component characters and Tham Thư | 4.5, 8 | Positions from the source examples |
| Table of the 110 Chi Tự | 4.1, 7.1 | Source passage and image; check of the numbering against it |
| Unicode properties: combining class, grapheme cluster rules, Bidi\_Class of both joiners | 6, 6.1, 6.2 | Review by Unicode experts |
| Block position in the Supplementary Multilingual Plane | 7 | Assignment by the UTC |
| Reference font and code chart glyphs | 7.2, 8 | Designer, licence and glyphs |
| Horizontal use | 6.3 | Not attested, so the proposal assumes Han Nôm habits |

## 10. Appendices

### A. Glossary

| Term | Meaning |
| --- | --- |
| Cán Tự | One of 22 base components; three strokes and one marking stroke; standalone only, never combined |
| Chi Tự | One of five variants per Cán Tự, made by repositioning the marking stroke (110 in total); standalone or combined |
| Cán Lược | The variant without a marking stroke (22 in total); combines with a Chi Tự; written standalone only where the text discusses components |
| Phản thiết pair | Combination of a Cán Lược and a Chi Tự of different Cán Tự, Cán Lược first, joined by the component joiner; described under Phản Thiết Hài Âm Pháp (反切諧音法); 2,310 in total; descriptive term of this proposal, unnamed in the source |
| Hợp Thư | Combination of a Chi Tự and a Cán Lược of the same Cán Tự, joined by the component joiner; the Chi Tự gives the initial, the Cán Lược the rhyme; 110 in total |
| Tham Thư | Hợp Thư with a third component, a Chi Tự, above it that extends the rhyme; 12,100 in total; records dialectal vowel clusters |
| Component joiner | Format character that joins two components into one character; their order gives the arrangement |
| Tham Thư combiner | Format character that places the following Chi Tự above a Hợp Thư |

### B. Attested examples

&#91;TBD: table of every attested Hợp Thư and both Tham Thư with source, page and image\]

### C. Scans of the sources

&#91;TBD: images of the relevant pages\]

### D. References

&#91;TBD: scholarly literature and prior work on the script\]

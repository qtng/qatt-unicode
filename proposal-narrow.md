> **Archived variant (narrow reading, automatic exchange).** Hợp Thư is stored as Cán Lược + Chi Tự and the font exchanges the components when both share a Cán Tự. Superseded; see proposal.md (current) and proposal-3c.md. Kept for reference.

# QATT Unicode Proposal – Draft

Oct 9, 2026 · @Trung

## 1. Summary

This proposal encodes Quốc Âm Tân Tự (QATT), a Vietnamese script used inside Han Nôm texts, as 163 characters in the Supplementary Multilingual Plane.

| Item | Entry |
| --- | --- |
| Script | Quốc Âm Tân Tự (QATT) |
| Proposer | \[TBD: name and affiliation\] |
| Draft date | 2026-10-09 |
| Characters | 163: 154 components, 1 combiner, 8 tone marks |
| Model | Atomic components; two- and three-component characters as sequences |
| Plane | Supplementary Multilingual Plane \[TBD: block position assigned by the UTC\] |
| Direction | Follows Han Nôm; the sources are vertical |
| Attested sources | Two, both vertical Han Nôm texts |
| Official form | \[TBD: complete the UTC Proposal Summary Form\] |

## 2. Introduction

Quốc Âm Tân Tự is a Vietnamese script built from 22 base components, each of three strokes and one short marking stroke. The base components stand alone; forms derived from them stand alone or combine in groups of two or three, and any character may carry a tone mark in one of its corners.

### 2.1 Background

In the attested sources the script appears in running Han Nôm text and is treated exactly like Han Nôm characters. Three-component characters (Tham Thư) record dialectal vowel clusters. Eight tones are marked with circles and semicircles in the corners, following the Chinese yin-yang method. \[TBD: date and provenance of the sources; scholarly literature\]

### 2.2 Reasons for encoding

&#91;TBD: need for digital text, scholarship, user community and interest in the script\]

## 3. Sources and Evidence

Two sources attest the script. Both are vertical Han Nôm texts, and the text of the sources describes the methods of combination.

### 3.1 Attested sources

| Source | Date | Location | Text type | Direction |
| --- | --- | --- | --- | --- |
| Source 1 | \[TBD\] | \[TBD\] | Han Nôm | Vertical |
| Source 2 | \[TBD\] | \[TBD\] | Han Nôm | Vertical |

### 3.2 Evidence by feature

| Feature | Evidence | Status |
| --- | --- | --- |
| Cán Tự, Chi Tự, Cán Lược | Described in the sources | \[TBD: cite passages and examples\] |
| Phản thiết pairs | Described in the section Phản Thiết Hài Âm Pháp (反切諧音法); components of different bases | \[TBD: cite passages and examples\] |
| Hợp Thư | Described in the text; every example is a same-base pair in exchanged arrangement | \[TBD: list the examples; confirm that the term covers only same-base pairs\] |
| Tham Thư | Rule described in the text, with a Hợp Thư as the base; two examples attested, both on a Hợp Thư | \[TBD: cite both examples\] |
| Omission of the Cán Lược | Wherever a phản thiết pair of the same base would occur, the sources write the Chi Tự alone | \[TBD: list the places\] |
| Tone marks | Eight tones in four corners; semicircle orientation visible only in the examples | \[TBD: examples for all four corners\] |
| Writing direction | The text is silent; both sources are vertical Han Nôm | Assumption: Han Nôm habits |

### 3.3 Modern use

&#91;TBD: current use of the script, for example on chunom.org, and any user community\]

### 3.4 Scans and images

&#91;TBD: scans of the source pages with the relevant passages marked\]

## 4. Structure of the Script

Quốc Âm Tân Tự is built from 22 base components that stand alone. Their derived forms stand alone or combine in groups of two or three, and any character may carry one tone mark in one of its four corners.

### 4.1 Components

Each of the 22 base components (*Cán Tự*) consists of three strokes and one short marking stroke. Repositioning the marking stroke yields five variants per base (*Chi Tự*). Omitting it yields one reduced form per base (*Cán Lược*). Because every Chi Tự moves the marking stroke, no Chi Tự coincides with its Cán Tự: each base has six distinct marked forms and one unmarked form.

| Component | Count | Derivation | Standalone | In combination |
| --- | --- | --- | --- | --- |
| Cán Tự | 22 | 3 strokes + 1 marking stroke | yes | never |
| Chi Tự | 110 (22 × 5) | marking stroke repositioned | yes | yes |
| Cán Lược | 22 | marking stroke omitted | no | only with a Chi Tự |

### 4.2 Two-component characters: phản thiết and Hợp Thư

A Cán Lược and a Chi Tự combine into one character. The sources describe two methods.

- **Phản thiết.** The Cán Lược and the Chi Tự derive from different Cán Tự. The section Phản Thiết Hài Âm Pháp (反切諧音法) describes these pairs; the sources give them no name of their own, and this proposal calls them phản thiết pairs. A phản thiết pair of the same base would add nothing to the Chi Tự, so the sources write the Chi Tự alone instead.
- **Hợp Thư.** The Cán Lược and the Chi Tự derive from the same Cán Tự, and their positions are exchanged. There are 110 Hợp Thư, one for each Chi Tự. The non-exchanged arrangement of a same-base pair never occurs in the sources.

Both methods use the same sequence, a Cán Lược followed by a Chi Tự. Whether the bases match decides the method and the arrangement. \[TBD: cite the source passages for both methods and the attested examples\]

### 4.3 Tham Thư (three components)

A Hợp Thư may carry a third component, a single Chi Tự, above it. The base is always a Hợp Thư, that is a same-base pair in exchanged arrangement; a phản thiết pair or a single Chi Tự is not a base. The third component is otherwise unrestricted. The base stays a unit, and the third component stands alone above it. The method records dialectal vowel clusters. This allows 110 bases and 110 × 110 = 12,100 Tham Thư.

The two attested Tham Thư both have a Hợp Thư as the base, as the rule requires. \[TBD: cite the source passage for the base rule and both examples\]

### 4.4 Tone marks

A tone mark is a circle or a semicircle placed in one of the four corners of the character, giving eight tones. The sources do not specify the orientation of the semicircle; every example shows its open side facing the centre of the character. Round versus angular forms of the semicircle are handwriting variation. A character carries at most one tone mark, and many carry none. \[TBD: cite the source passage and examples for all four corners\]

### 4.5 Layout

&#91;TBD: position of the two components within a phản thiết pair and within a Hợp Thư, and of the top component within a Tham Thư\]

## 5. Encoding Model

The script is encoded as 163 atomic characters. Hợp Thư and Tham Thư are sequences, so every character stays editable and its boundaries are determined locally.

### 5.1 Repertoire

| Group | Characters |
| --- | --- |
| Cán Tự | 22 |
| Cán Lược (component only, never standalone) | 22 |
| Chi Tự | 110 |
| Tham Thư combiner | 1 |
| Tone marks (combining) | 8 |
| **Total** | **163** |

### 5.2 Why not precomposed

A Cán Lược and a Chi Tự allow 2,420 two-component characters (22 Cán Lược × 110 Chi Tự): 2,310 phản thiết pairs and 110 Hợp Thư. Tham Thư allows 110 × 110 = 12,100. Precomposing would need 14,520 code points, most of them for combinations of which only two are attested. Precomposing is neither feasible nor justified.

### 5.3 Sequence grammar

```
Character := Cluster [ToneMark]
Cluster   := CanTu | ChiTu | Pair | ThamThu
Pair      := CanLuoc ChiTu               phản thiết or Hợp Thư
ThamThu   := HopThu Combiner ChiTu
HopThu    := CanLuoc(X) ChiTu(X)         same Cán Tự X
```

A Pair whose components share their Cán Tự is a Hợp Thư; otherwise it is a phản thiết pair (4.2). Only a Hợp Thư can be the base of a Tham Thư. A Cán Lược never stands alone and always begins a pair, so cluster boundaries need no lookahead beyond the next character. The same-base condition does not affect segmentation; it is checked by validation (6.2).

| Intended character | Sequence |
| --- | --- |
| Standalone Cán Tự | CAN |
| Standalone Chi Tự | CT |
| Phản thiết pair (different bases) | CL(X) CT(Y) |
| Same-base phản thiết reading (written as the Chi Tự alone) | CT(X) |
| Hợp Thư (same base, rendered exchanged) | CL(X) CT(X) |
| Tham Thư | CL(X) CT(X) COMB CT(Z) |
| Any of the above with a tone | sequence + TONE |

### 5.4 Positional exchange

In a Hợp Thư the two components are exchanged. A same-base pair occurs only as a Hợp Thư, because a same-base phản thiết pair is written as the Chi Tự alone (4.2). The arrangement therefore follows from the sequence: it is a rendering rule, implemented with OpenType substitution, and not encoded. The non-exchanged arrangement of a same-base pair never occurs; if scholarly notation needs it, it can be described with Ideographic Description Sequences. \[TBD: IDS operator depends on the layout in 4.5\]

### 5.5 Edit stability

Deleting or inserting one character alters at most the clusters directly adjacent to the edit point. An edit can split a cluster, merge two neighbours (for example when the top component of a Tham Thư is deleted and the next Chi Tự takes its place) or attach a tone mark to the preceding cluster. Nothing beyond the neighbours changes.

The guarantee also holds for ill-formed text, because segmentation uses local rules only (6.2): there is never a break before or after the combiner. An ill-formed chain such as `CT COMB CT COMB CT` therefore forms one cluster, which a validator reports as ill-formed. Segmentation never pairs up the parts of such a chain, so an edit inside it cannot regroup the text beyond it.

**Hypothetical model, not part of this proposal.** To show why the proposed order matters, consider encoding the exchange by sequence order, with the Chi Tự written before the Cán Lược. This model is rejected, because it fails the test above and is also ambiguous. With B a Chi Tự and A a Cán Lược of the same base, the sequence `BAB` would read as `[BA][B]` or as `[B][AB]`, and both are valid texts. A left-to-right parser takes the first reading, so deleting the first A in `ABABAB` would regroup all following characters from `[AB][AB][AB]` into `[BA][BA][B]`. A parser that binds the Cán Lược forward first avoids that regrouping, but it could no longer express `[BA][B]` at all.

In the proposed model the Cán Lược always comes first, and the exchange is a rendering rule (5.4).

### 5.6 Tone marks

The eight tone marks are combining characters that follow the complete cluster. Each corner and each mark type is contrastive, so a tone is a character and not a glyph variant. The orientation of the semicircle follows from its corner and is a glyph property. A cluster takes at most one tone mark.

### 5.7 Alternatives considered

- Variation selector for the exchange: rejected. The exchanged arrangement distinguishes a Hợp Thư from a phản thiết pair, so the two arrangements differ in reading, and a variation selector may only select a glyph variant of the same character. The non-exchanged arrangement of a same-base pair is also unattested.
- Explicit joiner for the exchange (`CT(X) J CL(X)` for the Hợp Thư): rejected, because it needs a further code point and a same-base restriction, and adds nothing the sequence does not already determine.
- Separate code points for the Cán Lược of a Hợp Thư: rejected for the same reason, at the cost of 22 code points.
- Broad reading of Hợp Thư, in which the term covers every Cán Lược + Chi Tự pair and a Tham Thư base may be any pair or a single Chi Tự (278,300 Tham Thư): not adopted, because it needs an unattested base and does not match the division of the sources into Hợp Thư and Phản Thiết Hài Âm Pháp. \[TBD: cite the passages that support the narrow reading\]
- Exchange by sequence order (hypothetical model with the Chi Tự before the Cán Lược): rejected for ambiguity and edit instability (5.5).
- Two tone marks plus a position selector: rejected, because the corner is contrastive.
- Precomposed Hợp Thư and Tham Thư: rejected for size (5.2).

### 5.8 Open decision

Propose the Tham Thư combiner now, or describe Tham Thư with IDS first and add the combiner once more attestations exist. With two attested examples, the second option lowers the risk of rejection. Without the combiner the repertoire has 162 characters, the tone marks move to +9A to +A1, and the size argument for Tham Thư in 5.2 no longer applies.

## 6. Character Properties

The proposed properties follow from the encoding model: components are letters, the combiner is a format character, and tone marks are nonspacing marks. Cells marked \[TBD\] depend on evidence from the sources or on review by the Unicode text-segmentation experts.

| Characters | General\_Category | Combining class | Grapheme\_Cluster\_Break | Line\_Break | Bidi\_Class |
| --- | --- | --- | --- | --- | --- |
| Cán Tự, Chi Tự | Lo | 0 | Other | ID | L |
| Cán Lược | Lo | 0 | Prepend | ID | L |
| Tham Thư combiner | Cf | 0 | \[TBD\] | CM | \[TBD\] |
| Tone marks (8) | Mn | 0 | Extend | CM | NSM |

### 6.1 Combining class of the tone marks

The corner is part of each tone mark's identity, so no positional combining classes are needed. A cluster takes at most one tone mark, so canonical reordering between marks never occurs. All eight marks therefore take class 0. \[TBD: confirm with current Unicode conventions\]

### 6.2 Grapheme clusters

A Cán Lược always joins the character that follows it. This matches the behaviour of Prepend characters. Tone marks match Extend. The combiner must keep the preceding cluster, itself and the following Chi Tự together, which resembles the conjunct rule for Indic scripts in UAX #29. Segmentation never breaks directly before or after the combiner, whatever the neighbouring characters are; whether the result is well-formed is left to validation (5.5). \[TBD: decide between an existing property value and a new one; Bidi\_Class of the combiner, since format characters usually take BN\]

### 6.3 Line breaking and direction

The sources do not state a writing direction. Both attested sources contain vertical Han Nôm text, and in every case the script is treated exactly like Han Nôm and flows with it: vertical lines, columns running right to left, no spaces between words. No horizontal use is attested. The proposal therefore assumes the writing habits of Han Nôm. The characters behave like ideographs, each occupying one square cell. Proposed for the components: Bidi\_Class L, Line\_Break ID, East\_Asian\_Width W, Vertical\_Orientation U. Tone marks and the combiner never start a line, because they belong to the preceding cluster.

### 6.4 Code point order

The sources list the 22 Cán Tự roughly by place of articulation. \[TBD: cite the listing\] This order has no encoding significance, so code points follow the order of that listing and no collation claim is made. Within each Cán Tự, the five Chi Tự follow one fixed order of the marking-stroke position. \[TBD: define that order of the five positions\]

## 7. Character Table and Code Chart

The 163 characters fit in a block of 176 code points (11 columns of 16), proposed for the Supplementary Multilingual Plane. \[TBD: block position assigned by the UTC\] Code points follow the source order of the 22 Cán Tự, and the five Chi Tự of each base are consecutive.

| Group | Offset in block | Count |
| --- | --- | --- |
| Cán Tự | +00 to +15 | 22 |
| Cán Lược | +16 to +2B | 22 |
| Chi Tự | +2C to +99 | 110 |
| Tham Thư combiner | +9A | 1 |
| Tone marks | +9B to +A2 | 8 |
| Reserved | +A3 to +AF | 13 |

### 7.1 Character names

Names use ASCII capitals without diacritics, as Unicode requires. Patterns:

```
QUOC AM TAN TU CAN TU <NAME>
QUOC AM TAN TU CAN LUOC <NAME>
QUOC AM TAN TU CHI TU <NAME> <POSITION>
QUOC AM TAN TU THAM THU COMBINER
QUOC AM TAN TU TONE CIRCLE UPPER LEFT
QUOC AM TAN TU TONE SEMICIRCLE LOWER RIGHT
```

The tone marks use the corners UPPER LEFT, UPPER RIGHT, LOWER LEFT and LOWER RIGHT, each for circle and semicircle. \[TBD: names of the 22 Cán Tự and of the five marking-stroke positions\]

### 7.2 Code chart

&#91;TBD: reference glyphs from the font, showing every Cán Tự, Chi Tự, Cán Lược, the combiner and the tone marks in their corners\]

## 8. Font Design Notes

A conforming font draws every cluster in one square cell and composes it with substitution and positioning rules, not with precomposed glyphs.

- **Cell:** Each cluster fills one square cell with the metrics of Han Nôm ideographs, so it sits in vertical or horizontal lines without adjustment.
- **Two-component characters:** The two component glyphs share the cell. \[TBD: positions, see 4.5\]
- **Exchange rule:** In a Hợp Thư, a Cán Lược and a Chi Tự of the same Cán Tự (110 pairs), the font swaps the positions of the two components. Phản thiết pairs keep their positions.
- **Tham Thư:** After the combiner, the Chi Tự is drawn above the Hợp Thư. The font composes the cluster by contextual substitution and positioning, because 12,100 precomposed glyphs are impractical. The two attested examples serve as test cases for the reference font.
- **Tone marks:** Eight combining glyphs sit in the four corners of the whole cluster cell. The open side of the semicircle faces the centre. Round or angular outlines are a design choice, since the sources treat the difference as handwriting variation.
- **Reference font:** \[TBD: designer and licence\]

## 9. Open Points

Twelve points remain before the proposal can be submitted. The alternatives already weighed are in 5.7.

| Point | Section | What is needed |
| --- | --- | --- |
| Tham Thư combiner now, or IDS first | 5.8 | Decision |
| Scope of the term Hợp Thư (same-base pairs only) | 3.2, 4.2, 5.7 | Source passages for the narrow reading |
| Proposer and UTC Proposal Summary Form | 1 | Name, affiliation, completed form |
| Date and provenance of the sources, scholarly literature | 2.1, 3.1, D | Source data and references |
| Reasons for encoding and modern use | 2.2, 3.3 | Description of need and user community |
| Source passages and scans for the components, phản thiết pairs, Hợp Thư, the omission convention, Tham Thư and the tone corners | 3.2, 3.4, 4.1 to 4.4, B, C | Citations and images |
| Layout of the components in two-component characters and Tham Thư, and the IDS operator that follows from it | 4.5, 5.4 | Positions from the source examples |
| Names of the 22 Cán Tự, the five marking-stroke positions and their order | 6.4, 7.1 | Names, order and the cited source listing |
| Unicode properties: combining class, grapheme cluster rule and Bidi\_Class of the combiner | 6, 6.1, 6.2 | Review by Unicode experts |
| Block position in the Supplementary Multilingual Plane | 7 | Assignment by the UTC |
| Reference font and code chart glyphs | 7.2, 8 | Designer, licence and glyphs |
| Horizontal use | 6.3 | Not attested, so the proposal assumes Han Nôm habits |

## 10. Appendices

### A. Glossary

| Term | Meaning |
| --- | --- |
| Cán Tự | One of 22 base components; three strokes and one marking stroke; standalone only, never combined |
| Chi Tự | One of five variants per Cán Tự, made by repositioning the marking stroke (110 in total); standalone or combined |
| Cán Lược | The variant without a marking stroke (22 in total); only in combination with a Chi Tự |
| Phản thiết pair | Combination of a Cán Lược and a Chi Tự of different Cán Tự, described under Phản Thiết Hài Âm Pháp (反切諧音法); 2,310 in total; descriptive term of this proposal, unnamed in the sources |
| Hợp Thư | Combination of a Cán Lược and a Chi Tự of the same Cán Tự, drawn with exchanged positions; 110 in total |
| Tham Thư | Hợp Thư with a third component, a Chi Tự, above it; 12,100 in total; records dialectal vowel clusters |

### B. Attested examples

&#91;TBD: table of every attested Hợp Thư and both Tham Thư with source, page and image\]

### C. Scans of the sources

&#91;TBD: images of the relevant pages\]

### D. References

&#91;TBD: scholarly literature and prior work on the script\]

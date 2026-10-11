# QATT Unicode Proposal – Draft

Oct 9, 2026 · Nguyễn Quốc Trung

## 1. Summary

This proposal encodes Quốc Âm Tân Tự (QATT), a Vietnamese script used inside Hán Nôm texts, as 164 characters in the Supplementary Multilingual Plane.

| Item | Entry |
| --- | --- |
| Script | Quốc Âm Tân Tự (國音新字, QATT) |
| Proposer | Nguyễn Quốc Trung, independent researcher |
| Draft date | 2026-10-09 |
| Characters | 164: 154 components, 2 joiners, 8 tone marks |
| Model | Atomic components in reading order; every combination written with an explicit joiner |
| Plane | Supplementary Multilingual Plane \[TBD: block position assigned by the UTC\] |
| Direction | Follows Hán Nôm; the source is vertical |
| Attested sources | Two manuscripts of one text, Institute of Hán Nôm Studies, Hanoi, AB.630; reign of Thiệu Trị (1841–1847) |
| Official form | \[TBD: complete the UTC Proposal Summary Form\] |

## 2. Introduction

Quốc Âm Tân Tự (國音新字, "new script for the sounds of the national language") is a Vietnamese script built from 22 bases, each drawn with three strokes. A base exists in seven forms: one without a marking stroke and six with a short marking stroke at one of the six stroke ends. Every form can stand alone; all but one per base combine in groups of two or three, and any character may carry a tone mark in one of its corners.

### 2.1 Background

The script is known from one text, preserved in two manuscripts at the Institute of Hán Nôm Studies in Hanoi (3.1). The text names the script in the heading of its preface, 國音新字序, "preface to the new script for the sounds of the national language" (p. [1](evidence/pages/S1-p1.jpg)). The text is undated. It can be dated to the reign of Emperor Thiệu Trị (1841–1847), because the character 華 lacks its final stroke, a naming taboo for the emperor's mother, Hồ Thị Hoa (p. [1](evidence/pages/S1-p1.jpg)). \[TBD: reference for the taboo and for Hồ Thị Hoa as the emperor's mother\] The author signs as Nam Thành cư sĩ Nguyễn Tử (南城居士阮子), a lay scholar (cư sĩ) surnamed Nguyễn from Nam Thành, at the end of the preface (p. [2](evidence/pages/S1-p2.jpg)). The manuscripts are classified under tiểu học (小學, philology and elementary learning) and catalogued as nôm văn thư (喃文書, Nôm documents). \[TBD: catalogue reference ([E32](evidence/E32.md))\]

In the source the script appears within Hán Nôm text and is treated exactly like Hán Nôm characters. The source contains no running text written in the script: it gives single characters as examples and spelling formulas in the phản thiết manner (4.1). Three-component characters (Tham Thư) are attested in two examples; their reading is not established (4.3). Eight tones are marked with circles and semicircles in the corners, following the Chinese yin-yang method. \[TBD: scholarly literature\]

### 2.2 Reasons for encoding

&#91;TBD: need for digital text, scholarship, user community and interest in the script\]

## 3. Sources and Evidence

Two sources attest the script. Both are manuscripts of the same vertical Hán Nôm text, which describes the methods of combination. Each has four double pages, numbered as eight pages, with the same content and the same page numbering. Both are bound in one volume with continuous folio numbers, Source 1 on folios 3–10 and Source 2 on folios 11–18; page references in this proposal give the page within each manuscript, 1 to 8. Whether Source 2 was copied from Source 1 or both from an earlier original cannot be determined. The two sources are one text in two witnesses. Page references in this proposal, such as (p. [2](evidence/pages/S1-p2.jpg)), refer to Source 1; since both witnesses share the page numbering and the layout of the columns, they apply to Source 2 as well. Source 2 is named only where it differs or where its reading matters.

### 3.1 Attested sources

| Source | Date | Location | Text type | Direction |
| --- | --- | --- | --- | --- |
| Source 1 | Reign of Thiệu Trị (1841–1847) | Institute of Hán Nôm Studies, Hanoi, AB.630 | Manuscript, Hán Nôm, 4 double pages | Vertical |
| Source 2 | Reign of Thiệu Trị (1841–1847) | Institute of Hán Nôm Studies, Hanoi, AB.630 | Manuscript, Hán Nôm, 4 double pages | Vertical |

Both manuscripts share the shelfmark AB.630. The date is that of the text, from the naming taboo (2.1); the dates of the two copies are not known.

### 3.2 Evidence by feature

The status column names the open items of the evidence catalogue ([E01](evidence/E01.md), [E02](evidence/E02.md), …); Appendix B lists the passages already located.

| Feature | Evidence | Status |
| --- | --- | --- |
| Marked Cán | The 22 marked Cán are listed with the names of their sounds in the section 幹音二十二字 (p. [2](evidence/pages/S1-p2.jpg)) | Cited ([E01](evidence/E01.md), [E18](evidence/E18.md)) |
| Unmarked Cán | Not listed; shown in the combined characters of the examples and standing alone, for example with the eight tones (pp. [5](evidence/pages/S1-p5.jpg)–[7](evidence/pages/S1-p7.jpg)) | Located ([E34](evidence/E34.md)) |
| Chi | Tabulated in the section 枝字一百一十字 in blocks of five per Cán: 109 forms shown against 110 named (pp. [3](evidence/pages/S1-p3.jpg)–[4](evidence/pages/S1-p4.jpg)) | Cited ([E02](evidence/E02.md), [E29](evidence/E29.md)) |
| Phản thiết pairs | Described in the section Phản Thiết Hài Âm Pháp (反切諧音法, from p. [5](evidence/pages/S1-p5.jpg)); components of different bases, unmarked Cán first; the unmarked Cán gives the initial, the Chi the rhyme; pairs in running text (p. [6](evidence/pages/S1-p6.jpg)) | \[TBD: [E05](evidence/E05.md), [E06](evidence/E06.md)\] |
| Hợp Thư | Described in the text; every example is a same-base pair with the Chi first; the Chi gives the initial, the unmarked Cán the rhyme; the count of 880 (110 × 8 tones) covers only same-base pairs (p. [8](evidence/pages/S1-p8.jpg)) | \[TBD: [E08](evidence/E08.md)\] |
| Tham Thư | Rule described in the text, with a Hợp Thư as the base; two examples attested, both on a Hợp Thư; reading not established | \[TBD: [E10](evidence/E10.md), [E12](evidence/E12.md), [E13](evidence/E13.md); deferred\] |
| Standalone and adjacent components | When the text explains how components combine, it writes components on their own and side by side without combining them: a standalone unmarked Cán before a Chi, and two standalone unmarked Cán before a phản thiết pair (p. [6](evidence/pages/S1-p6.jpg)) | Located ([E04](evidence/E04.md)) |
| Omission of the unmarked Cán | Wherever a phản thiết pair of the same base would occur, the source writes the Chi alone | \[TBD: [E09](evidence/E09.md)\] |
| Tone marks | Eight tones in four corners, explained with the corner of each tone class and illustrated on one character (pp. [4](evidence/pages/S1-p4.jpg)–[5](evidence/pages/S1-p5.jpg)); the neutral tone marked with a semicircle lower left; marked and unmarked characters in one passage; round and angular forms of the same mark (p. [6](evidence/pages/S1-p6.jpg)) | \[TBD: [E16](evidence/E16.md)\] |
| Writing direction | The text is silent; both witnesses are vertical Hán Nôm | Assumption: Hán Nôm habits \[TBD: [E19](evidence/E19.md)\] |

### 3.3 Modern use

The script has an online presence of recent date, found by the proposer ([E22](evidence/E22.md)): a website of the proposer (qatt.org), a page on Omniglot (last modified August 2026), a web converter from Quốc Ngữ to the script by an unknown author, a Facebook group named qatt, in which members write tutorials and develop fonts, regular posts on Threads by one person and posts on Reddit, and a YouTube video on the script (Maruhi Academy, about 12,000 views in October 2026). The Omniglot page takes its sample from the Vietnamese Wikipedia. \[TBD: dates of first publication, upload date and sources of the video, size and activity of the group, the existing fonts and how they encode the script, how the converter writes the script, other uses such as chunom.org\]

### 3.4 Scans and images

&#91;TBD: scans of the source pages with the relevant passages marked\]

## 4. Structure of the Script

Quốc Âm Tân Tự is built from 22 bases, each in seven forms. Every form can stand alone; all but one per base combine in groups of two or three, and any character may carry one tone mark in one of its four corners.

### 4.1 Components

The script has 22 bases (*Cán*, 幹; the source writes it with 音 in the heading 幹音二十二字 of the listing, p. [2](evidence/pages/S1-p2.jpg), and with 字 in 二十二幹字為標, p. [7](evidence/pages/S1-p7.jpg)), each drawn with three strokes. The source lists the 22 base sounds (幹音二十二字, p. [2](evidence/pages/S1-p2.jpg)); each is shown with a QATT character, which carries one short marking stroke at the start position, upper left or upper middle depending on the base, and with a Nôm annotation that gives its sound. This form is the *marked Cán*. The marking stroke always sits at the end of a stroke, so the three strokes offer six positions for it, counted counter-clockwise from the start position as 1 to 6. The marked Cán has it at position 1; the five forms with the marking stroke at positions 2 to 6 are the *Chi*, in order. A seventh form has no marking stroke. The source calls it Cán, like the marked Cán; this proposal calls it the *unmarked Cán* to tell it from the marked Cán, whose forms are listed under 幹音 and have no special name either. The unmarked form is shown for ONG ([E07](evidence/E07.md), [E39](evidence/E39.md)) and đông ([E15](evidence/E15.md)); that all 22 Cán occur as unmarked Cán in combinations follows from the counts in the section 音数 (p. [8](evidence/pages/S1-p8.jpg), [E36](evidence/E36.md)), not from a listing ([E34](evidence/E34.md)). In the count section the source calls both the Cán standing alone (單幹書) and the component of a combination, which is always the unmarked form, 幹 (幹体, p. [8](evidence/pages/S1-p8.jpg)). Because the marking stroke of every Chi lies at another position than that of the marked Cán, no Chi coincides with the marked Cán: each base has six distinct marked forms and one unmarked form.

The source lists the 22 Cán by their sounds (p. [2](evidence/pages/S1-p2.jpg)), and the Chi in the section 枝字一百一十字, "the 110 Chi characters", in blocks of five per base (pp. [3](evidence/pages/S1-p3.jpg)–[4](evidence/pages/S1-p4.jpg)); the table shows 109, one having been left out by oversight (KHONG MARKED-4). The source gives the readings of the Chi only through Nôm annotations next to each form; these are ambiguous or not attested in dictionaries, so the readings are not established. The encoding does not depend on them, because the forms differ by the position of the marking stroke. The annotations are not transcribed here.

The three classes have distinct functions. An unmarked Cán gives the initial consonant of its base, and a Chi gives a rhyme; together the 110 Chi form the rhyme table of the script. A marked Cán stands for the whole syllable of its initial with the rhyme ông and names its base; it serves to pronounce the unmarked Cán in the phản thiết method. The unmarked Cán and the Chi also serve as the components of a Tham Thư (4.3). \[TBD: passages for these functions ([E06](evidence/E06.md), [E08](evidence/E08.md))\]

The source contains no running text in the script. Within its Hán Nôm text it gives single characters as examples and spelling formulas in the phản thiết manner, so whether a component may stand alone in running text cannot be decided from it. In these examples the marked Cán, the unmarked Cán and the Chi all appear standalone, also with tone marks. A standalone unmarked Cán has the same reading as the marked Cán of its base: the source illustrates the eight tones on the standalone unmarked Cán of đông (p. [5](evidence/pages/S1-p5.jpg)). Only the unmarked Cán and the Chi combine; the marked Cán never does. Outside the listing of the 22 Cán (p. [2](evidence/pages/S1-p2.jpg)) the marked Cán occurs only twice, both times as a separate character with a reading, in formulas that explain a combined character (p. [6](evidence/pages/S1-p6.jpg), p. [7](evidence/pages/S1-p7.jpg)); the second carries a tone mark.

| Component | Count | Form | Standalone | In combination |
| --- | --- | --- | --- | --- |
| Marked Cán | 22 | marking stroke at position 1 | yes | never |
| Chi | 110 (22 × 5) | marking stroke at position 2 to 6 | yes | yes |
| Unmarked Cán | 22 | no marking stroke | yes, with the reading of the marked Cán | with a Chi |

### 4.2 Two-component characters: phản thiết and Hợp Thư

An unmarked Cán and a Chi combine into one character. The source describes two methods.

- **Phản thiết.** The unmarked Cán and the Chi belong to different Cán, and the unmarked Cán comes first. The unmarked Cán gives the initial and the Chi the rhyme, as in the Chinese fanqie (反切) method of spelling a syllable by the initial of one character and the rhyme of another. The section Phản Thiết Hài Âm Pháp (反切諧音法) describes these pairs; the source gives them no name of its own, and this proposal calls them phản thiết pairs. A phản thiết pair of the same base would add nothing to the Chi, so the source writes the Chi alone instead. \[TBD: [E09](evidence/E09.md)\]
- **Hợp Thư.** The Chi and the unmarked Cán belong to the same Cán, and the Chi comes first. The source describes this arrangement as an exchange of positions. It is not only visual: compared with a phản thiết pair, the components also exchange their functions, so that the Chi gives the initial consonant and the unmarked Cán the rhyme. There are 110 Hợp Thư, one for each Chi.

When the source explains these methods, it also writes components on their own and side by side without combining them (3.2). In both methods the written order of the components is also their reading order: initial, then rhyme.

### 4.3 Tham Thư (three components)

A Hợp Thư may carry a third component, a single Chi, above it. The base is always a Hợp Thư; a phản thiết pair or a single Chi is not a base. The third component is otherwise unrestricted. This allows 110 bases and 110 × 110 = 12,100 Tham Thư. The two attested Tham Thư both have a Hợp Thư as the base, as the rule requires.

Tham Thư is the least certain part of the script. The source describes its structure but not its reading, and with only two examples the function of the three components within a Tham Thư cannot be established. This proposal therefore treats Tham Thư as a structural formation only and makes no claim about its pronunciation. The encoding follows the structure: the Hợp Thư comes first as a complete unit, and the combiner adds the third component to it (5.3).

### 4.4 Tone marks

A tone mark is a circle or a semicircle placed in one of the four corners of the character, giving the eight tones of the Chinese yin-yang system. The source explains the system after the Chi table: "yang uses a full circle, yin a half circle" (陽用全圈，陰用半圈, p. [4](evidence/pages/S1-p4.jpg)), and names the corner for each tone class: the left foot (左足) for bình, the left shoulder (左肩) for thượng, the right shoulder (右肩) for khứ and the right foot (右足) for nhập (p. [5](evidence/pages/S1-p5.jpg)). It illustrates the eight marks on one character, the unmarked Cán of đông, annotated 東 董 凍 篤 for âm and 同 洞 動 獨 for dương (p. [5](evidence/pages/S1-p5.jpg)). The source gives 同 洞 動 獨 explicitly as the level, rising, departing and entering tones (平上去入, p. [4](evidence/pages/S1-p4.jpg)), whereas the rime tradition assigns 動 to the rising and 洞 to the departing tone. 洞 has the readings đỗng and động (Tự điển chữ Nôm trích dẫn, p. 403); by placing 洞 in the rising tone, the source reads it đỗng, so that 同 洞 動 獨 (đồng, đỗng, động, độc) follow the Vietnamese tones huyền, ngã, nặng and the entering nặng. The corner gives the tone class and the shape gives the register: a semicircle marks âm (陰), a circle dương (陽).

| Corner | Tone class | Semicircle (âm) | Circle (dương) |
| --- | --- | --- | --- |
| Lower left | bình 平 | âm bình (ngang) | dương bình (huyền) |
| Upper left | thượng 上 | âm thượng (hỏi) | dương thượng (ngã) |
| Upper right | khứ 去 | âm khứ (sắc) | dương khứ (nặng) |
| Lower right | nhập 入 | âm nhập (sắc in syllables ending in -p, -t, -c) | dương nhập (nặng in syllables ending in -p, -t, -c) |

The neutral tone ngang has its own mark, a semicircle in the lower left corner (p. [6](evidence/pages/S1-p6.jpg)). A character carries at most one tone mark, and many carry none; on p. [6](evidence/pages/S1-p6.jpg) a passage marks every Quốc Âm Tân Tự character with the neutral tone except the last two, which carry no mark. An unmarked character therefore leaves the tone unspecified. Standalone components carry tone marks as well (p. [6](evidence/pages/S1-p6.jpg)).

The source does not specify the orientation of the semicircle; every example shows its open side facing the centre of the character. \[TBD: [E16](evidence/E16.md)\] Round and angular forms of the semicircle are handwriting variation, not different marks: Source 1 writes the same mark now round, now close to a hook, while Source 2 writes every tone mark of the passage on p. [6](evidence/pages/S1-p6.jpg) angular.

### 4.5 Layout

&#91;TBD: position of the two components within a phản thiết pair and within a Hợp Thư, and of the top component within a Tham Thư\]

## 5. Encoding Model

The script is encoded as 164 atomic characters: 154 components, two joiners and eight tone marks. Components are stored in reading order and drawn in that order; no component is reordered. Every combination is written with an explicit joiner, and components without a joiner are separate characters. Two- and three-component characters are sequences, so every character stays editable and its boundaries are determined locally.

### 5.1 Repertoire

| Group | Characters |
| --- | --- |
| Unmarked Cán | 22 |
| Marked Cán | 22 |
| Chi | 110 |
| Tham Thư combiner | 1 |
| Component joiner | 1 |
| Tone marks (combining) | 8 |
| **Total** | **164** |

### 5.2 Why not precomposed

An unmarked Cán and a Chi allow 2,420 two-component characters (22 unmarked Cán × 110 Chi): 2,310 phản thiết pairs and 110 Hợp Thư. The source gives the same counts multiplied by the eight tones: 880 with the Chi left and 18,480 with the Cán left, besides 176 single Cán and 880 single characters (p. [8](evidence/pages/S1-p8.jpg)). Tham Thư allows 110 × 110 = 12,100. Precomposing would need 14,520 code points, most of them for combinations of which only two are attested. Precomposing is neither feasible nor justified.

### 5.3 Sequence grammar

```
Character := Cluster [ToneMark]
Cluster   := MarkedCan | Chi | UnmarkedCan | PhanThiet | HopThu | ThamThu
PhanThiet := UnmarkedCan(X) Joiner Chi(Y)  X ≠ Y; unmarked Cán first
HopThu    := Chi(X) Joiner UnmarkedCan(X)  same Cán X; initial, then rhyme
ThamThu   := HopThu Combiner Chi            third component added to a complete Hợp Thư
```

The component joiner joins two components into one character, and their order gives the arrangement. Components without a joiner are separate characters; a standalone unmarked Cán has the reading of the marked Cán of its base (4.1). The same-base conditions do not affect segmentation; they are checked by validation (5.5).

| Intended character | Sequence |
| --- | --- |
| Standalone marked Cán | CM |
| Standalone Chi | CH |
| Standalone unmarked Cán (reading of the marked Cán) | CU |
| Components side by side, not combined | CU(X) CH(Y) |
| Phản thiết pair | CU(X) JOIN CH(Y) |
| Same-base phản thiết reading (written as the Chi alone) | CH(X) |
| Hợp Thư | CH(X) JOIN CU(X) |
| Tham Thư | CH(X) JOIN CU(X) COMB CH(Z) |
| Any character above with a tone | sequence + TONE |

Sequences outside these patterns are not prohibited. They are not attested, and this proposal does not specify their rendering.

### 5.4 Reading order and the component joiner

In a Hợp Thư the Chi gives the initial and the unmarked Cán the rhyme (4.2). Storing the Chi first follows the reading order, which is also the written order, so rendering needs no reordering.

The joiner carries information that the components alone do not. The source writes components side by side without combining them (3.2), so `CU CH` may be two separate components or a phản thiết pair, and `CH CU` may be a Chi followed by a separate unmarked Cán or a Hợp Thư. The joiner decides. Every attested two-component character therefore contains it.

### 5.5 Edit stability

Deleting or inserting one character alters at most the cluster at the edit point and its immediate neighbours. An edit can split a cluster, merge two neighbours (for example when the top component of a Tham Thư is deleted and the next Chi takes its place) or attach a tone mark to the preceding cluster. Nothing beyond the neighbours changes.

The guarantee also holds for ill-formed text, because segmentation uses pairwise rules only (6.2): whether a boundary lies between two characters depends on those two characters alone, and there is never a break before or after a joiner. An ill-formed chain such as `CH COMB CH COMB CH` therefore forms one cluster, which a validator reports as ill-formed. Segmentation never pairs up the parts of such a chain, so an edit inside it cannot regroup the text beyond it.

**Why the joiner is needed.** Without the joiner, a Hợp Thư would be the bare sequence Chi, unmarked Cán. With B a Chi and A an unmarked Cán of the same base, the sequence `BAB` would then read as `[BA][B]` or as `[B][AB]`, and both are valid text. A left-to-right parser takes the first reading, so deleting the first A in `ABABAB` would regroup all following characters from `[AB][AB][AB]` into `[BA][BA][B]`. With the joiner, `B JOIN A B` is `[BA][B]`, `B A JOIN B` is `[B][AB]` and `B A B` is three separate components: each reading has one spelling, and edits stay local.

### 5.6 Tone marks

The eight tone marks are combining characters that follow the complete cluster. Each corner and each mark type is contrastive, so a tone is a character and not a glyph variant. An unmarked cluster leaves the tone unspecified; it does not denote the neutral tone, which has its own mark (4.4). All eight marks are therefore needed. The orientation of the semicircle follows from its corner and is a glyph property. A cluster takes at most one tone mark.

### 5.7 Alternatives considered

- Automatic exchange: a Hợp Thư stored as unmarked Cán, Chi, with the font exchanging the components when both share a Cán. Not adopted, because it stores the rhyme before the initial, against the reading order, and relies on a rendering rule that compares bases. It would also fix `CU(X) CH(X)` to the Hợp Thư for good.
- Implicit phản thiết, in which an unmarked Cán binds to the following character without a joiner and only a Hợp Thư uses the joiner: not adopted, because the source also writes an unmarked Cán standalone and components side by side (3.2). A forward-binding unmarked Cán would join them wrongly, for example with a following Han character.
- Joiner that exchanges the components (`CU(X) JOIN CH(X)`, drawn exchanged): not adopted, because it keeps the order against reading.
- Joiner as a suffix (`CH(X) CU(X) JOIN`): not adopted, because it groups preceding characters retroactively, which needs right context in segmentation. Joiners such as U+200D ZERO WIDTH JOINER stand between the parts they join, and so does the Tham Thư combiner.
- One joiner for both two- and three-component characters (163 characters): not adopted, because the structure would follow from position instead of from the joiner, and the decision in 5.8 could no longer be taken for the Tham Thư combiner alone.
- Variation selector: rejected, because the two orders differ in reading, and a variation selector may only select a glyph variant of the same character.
- Unification of the marked Cán with the unmarked Cán: not adopted. The marked Cán never combines, and outside the listing of the 22 Cán (p. [2](evidence/pages/S1-p2.jpg)) it occurs only twice, as a separate character (4.1); the unmarked Cán of the same base has the same reading when it stands alone (p. [5](evidence/pages/S1-p5.jpg)). The two forms are nevertheless distinct, differing by the marking stroke, and both are attested, so each has its own code point.
- Separate code points for the unmarked Cán of a Hợp Thư: rejected, 22 code points instead of one joiner.
- Broad reading of Hợp Thư, in which the term covers every unmarked Cán + Chi pair and a Tham Thư base may be any pair or a single Chi (278,300 Tham Thư): not adopted, because it needs an unattested base and does not match the division of the source into Hợp Thư and Phản Thiết Hài Âm Pháp. The count section confirms the narrow reading: the source counts 880 characters with the Chi on the left and the Cán on the right, eight tones on each of the 110 same-base pairs, and no others in this arrangement (p. [8](evidence/pages/S1-p8.jpg)).
- Reuse of U+A700..U+A707 MODIFIER LETTER CHINESE TONE YIN PING to YANG RU: not adopted. These eight characters cover the same eight tones in the same order, but they are spacing modifier letters (General\_Category Sk) written beside a syllable, not combining marks placed in a corner of a character. As separate grapheme clusters they would break the cluster structure, and a font could not place them within the cell. Their forms also differ: they distinguish yin and yang by an underline, Quốc Âm Tân Tự by semicircle and circle.
- Reuse of U+302A..U+302D IDEOGRAPHIC LEVEL, RISING, DEPARTING and ENTERING TONE MARK: not adopted. These combining marks use the same corners for the same four tone classes, but they do not distinguish âm and dương. Using them for one register and new characters for the other would split one set of eight contrastive marks across two blocks, and the existing marks would carry a register they do not denote.
- Two tone marks plus a position selector: rejected, because the corner is contrastive.
- Precomposed Hợp Thư and Tham Thư: rejected for size (5.2).

### 5.8 Open decision

Propose the Tham Thư combiner now, or describe Tham Thư with IDS first and add the combiner once more attestations exist. With two attested examples, the second option lowers the risk of rejection. Without the combiner the repertoire has 163 characters, the component joiner and the tone marks move up by one code point, and the size argument for Tham Thư in 5.2 no longer applies. The component joiner is needed in either case.

## 6. Character Properties

The proposed properties follow from the encoding model: components are letters, the two joiners are format characters, and tone marks are nonspacing marks. Cells marked \[TBD\] depend on evidence from the source or on review by the Unicode text-segmentation experts.

| Characters | General\_Category | Combining class | Grapheme\_Cluster\_Break | Line\_Break | Bidi\_Class |
| --- | --- | --- | --- | --- | --- |
| Marked Cán, unmarked Cán, Chi | Lo | 0 | Other | ID | L |
| Tham Thư combiner, component joiner | Cf | 0 | Extend \[TBD\] | GL \[TBD\] | BN \[TBD\] |
| Tone marks (8) | Mn | 0 | Extend | CM | NSM |

The draft data files list every value, including Indic\_Conjunct\_Break, East\_Asian\_Width and Vertical\_Orientation; the questions on the values marked \[TBD\] are collected for review.

### 6.1 Combining class of the tone marks

The corner is part of each tone mark's identity, so no positional combining classes are needed. A cluster takes at most one tone mark, so canonical reordering between marks never occurs. All eight marks therefore take class 0. The ideographic tone marks U+302A..U+302D, which mark the same corners on Han characters, have positional classes instead (218 lower left, 228 upper left, 232 upper right, 222 lower right); the same classes would also work here, since a cluster never takes two tone marks. \[TBD: confirm with current Unicode conventions which classes to use\]

### 6.2 Grapheme clusters

Segmentation uses pairwise rules only: there is no break directly before or after either joiner and no break before a tone mark; every other boundary is a break. Tone marks match Extend. Components that are not joined, including a standalone unmarked Cán, form clusters of their own, so all components behave alike. Whether a cluster is well-formed is left to validation (5.5). One way to express this with existing properties is Grapheme\_Cluster\_Break=Extend for both joiners, which prevents a break before them, together with the Indic\_Conjunct\_Break mechanism of rule GB9c for the break after them: components as Consonant, joiners as Linker, tone marks as Extend. \[TBD: whether Indic\_Conjunct\_Break may be used for a non-Indic script, or a new value or rule is preferred; compare with the Egyptian hieroglyph format controls\]

### 6.3 Line breaking and direction

The source does not state a writing direction. Both witnesses contain vertical Hán Nôm text, and in every case the script is treated exactly like Hán Nôm and flows with it: vertical lines, columns running right to left, no spaces between words. No horizontal use is attested. The proposal therefore assumes the writing habits of Hán Nôm. The characters behave like ideographs, each occupying one square cell. Proposed for the components: Bidi\_Class L, Line\_Break ID, East\_Asian\_Width W, Vertical\_Orientation U. Tone marks and the joiners never start a line, because they belong to the preceding cluster.

### 6.4 Code point order

The source lists the 22 Cán in the section 幹音二十二字, "trunk sounds, twenty-two characters", each annotated with its name in Chữ Nôm (p. [2](evidence/pages/S1-p2.jpg)). The order groups the initials roughly by place of articulation. It has no encoding significance, so code points follow the order of that listing and no collation claim is made. Within each Cán, the five Chi follow the order of the marking-stroke position, counter-clockwise from the position of the marked Cán (4.1). The unmarked forms come first. The six marked forms of a base follow one another, so that all marked forms form one run of code points (+16 to +99).

## 7. Character Table and Code Chart

The 164 characters fit in a block of 176 code points (11 columns of 16), proposed for the Supplementary Multilingual Plane. \[TBD: block position assigned by the UTC\] Code points follow the source order of the 22 Cán, and the six marked forms of each base are consecutive, the marked Cán first and the five Chi after it. The marked forms form one run (+16 to +99).

| Group | Offset in block | Count |
| --- | --- | --- |
| Unmarked forms | +00 to +15 | 22 |
| Marked forms, six per base: the marked Cán and the five Chi | +16 to +99 | 132 |
| Tham Thư combiner | +9A | 1 |
| Component joiner | +9B | 1 |
| Tone marks | +9C to +A3 | 8, in the traditional order of the eight tones (see below) |
| Reserved | +A4 to +AF | 12 |

The tone marks follow the traditional order of the eight tones, the numbering 1 to 8 used in Chinese dialectology: âm bình, dương bình, âm thượng, dương thượng, âm khứ, dương khứ, âm nhập, dương nhập, that is by tone class and within each class âm before dương. The first six correspond to the Vietnamese tone order ngang, huyền, hỏi, ngã, sắc, nặng used in dictionaries and in Vietnamese collation. The source lists the marks in a different order, first the four semicircles and then the four circles, each starting lower left and running clockwise (p. [5](evidence/pages/S1-p5.jpg)); that order presents the marks by shape and is not adopted for the code points.

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
QUOC AM TAN TU <NAME> UNMARKED
QUOC AM TAN TU <NAME> MARKED-<N>
QUOC AM TAN TU THAM THU COMBINER
QUOC AM TAN TU COMPONENT JOINER
QUOC AM TAN TU TONE CIRCLE UPPER LEFT
QUOC AM TAN TU TONE SEMICIRCLE LOWER RIGHT
```

The tone marks use the corners UPPER LEFT, UPPER RIGHT, LOWER LEFT and LOWER RIGHT, each for circle and semicircle. The names describe the mark; the tone it denotes is given as an annotation, for example QUOC AM TAN TU TONE SEMICIRCLE LOWER LEFT = âm bình (ngang). The names list cross-references the related existing characters: each tone mark refers to the spacing modifier letter for the same tone (U+A700..U+A707) and to the ideographic tone mark for the same corner (U+302A..U+302D).

The names describe the form only and say nothing about its function. A form without marking stroke is UNMARKED. A form with the marking stroke is MARKED-1 to MARKED-6, the number being the position of the marking stroke among the six stroke ends, counted counter-clockwise from the start position of the marked Cán (4.1); MARKED-1 is the marked Cán, MARKED-2 to MARKED-6 are the five Chi, for example QUOC AM TAN TU ONG MARKED-1 to QUOC AM TAN TU ONG MARKED-6. The positions are relative to the marked Cán and lie in different places for different bases, so the names number them instead of describing them geometrically. The names list gives the class as an annotation.

The names of the 22 Cán are the names of their sounds in the source listing (6.4), where each Cán is annotated with a Chữ Nôm character; annotations without an encoded character are given as Ideographic Description Sequences. Each name is the syllable of the initial with the rhyme ông. Every form of a base takes the name of its Cán. Diacritics are dropped. To keep đông and dông apart, đ is written DD and d is written DZ, following an established convention for Vietnamese: đông → DDONG, dông → DZONG.

| No. | Nôm annotation | Reading | Initial | Name in character names | UNMARKED | MARKED-1 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 翁 | ông | Ɂ | ONG | +00 | +16 |
| 2 | ⿰木禺 | ngông | Ng | NGONG | +01 | +1C |
| 3 | 胸 | hông | H | HONG | +02 | +22 |
| 4 | ⿰木功 | gông | G | GONG | +03 | +28 |
| 5 | 工 | công | C | CONG | +04 | +2E |
| 6 | ⿰竜羽 | lông | L | LONG | +05 | +34 |
| 7 | ⿰竜里 | trông | Tr | TRONG | +06 | +3A |
| 8 | 東 | đông | Đ | DDONG | +07 | +40 |
| 9 | 農 | nông | N | NONG | +08 | +46 |
| 10 | 宗 | tông | T | TONG | +09 | +4C |
| 11 | 通 | thông | Th | THONG | +0A | +52 |
| 12 | ⿰亻戍 | nhông | Nh | NHONG | +0B | +58 |
| 13 | 柊 | chông | Ch | CHONG | +0C | +5E |
| 14 | ⿰月容 | dông | D | DZONG | +0D | +64 |
| 15 | 衝 | xông | X | XONG | +0E | +6A |
| 16 | 空 | không | Kh | KHONG | +0F | +70 |
| 17 | 滝 | sông | S | SONG | +10 | +76 |
| 18 | ⿱山庸 | rông | R | RONG | +11 | +7C |
| 19 | 蒙 | mông | M | MONG | +12 | +82 |
| 20 | 芃 | bông | B | BONG | +13 | +88 |
| 21 | ⿰木芃 | vông | V | VONG | +14 | +8E |
| 22 | ⿰口風 | phông | Ph | PHONG | +15 | +94 |

### 7.2 Code chart

&#91;TBD: reference glyphs from the font, showing every marked Cán, unmarked Cán, Chi, the two joiners and the tone marks in their corners\]

## 8. Font Design Notes

A conforming font draws every cluster in one square cell and composes it with substitution and positioning rules, not with precomposed glyphs.

- **Cell:** Each cluster fills one square cell with the metrics of Hán Nôm ideographs, so it sits in vertical or horizontal lines without adjustment.
- **Two-component characters:** The two component glyphs share the cell. \[TBD: positions, see 4.5\]
- **No reordering:** Components are drawn in stored order. The component joiner tells the font to compose the two components in one cell; their order gives the arrangement, unmarked Cán first for a phản thiết pair and Chi first for a Hợp Thư. Components without a joiner are drawn as separate characters. \[TBD: positions, see 4.5\]
- **Tham Thư:** After the combiner, the Chi is drawn above the Hợp Thư. The font composes the cluster by contextual substitution and positioning, because 12,100 precomposed glyphs are impractical. The two attested examples serve as test cases for the reference font.
- **Tone marks:** Eight combining glyphs sit in the four corners of the whole cluster cell. The open side of the semicircle faces the centre. Round or angular outlines are a design choice, since the source treats the difference as handwriting variation.
- **Reference font:** \[TBD: designer and licence\]

## 9. Open Points

Twelve points remain before the proposal can be submitted. The alternatives already weighed are in 5.7.

| Point | Section | What is needed |
| --- | --- | --- |
| Tham Thư combiner now, or IDS first | 4.3, 5.8 | Decision, taken last: the reading of Tham Thư is not established and only two examples exist |
| Function of the components: initial and rhyme in phản thiết pairs and Hợp Thư | 3.2, 4.2 | Source passages; this is the main argument for the reading order (5.4) |
| UTC Proposal Summary Form | 1 | Completed form |
| Scholarly literature | 2.1, D | References |
| Reasons for encoding and modern use | 2.2, 3.3 | Description of need and user community |
| Evidence for the naming taboo, the catalogue classification, the omission convention and the semicircle orientation | 2.1, 4.2, 4.4 | [E32](evidence/E32.md), [E09](evidence/E09.md), [E16](evidence/E16.md); reference for the taboo |
| Open evidence items listed in 3.2 | 3.2, B, C | Passages, pages and images |
| Layout of the components in two-component characters and Tham Thư | 4.5, 8 | Positions from the source examples; the count section names left and right (p. [8](evidence/pages/S1-p8.jpg), [E36](evidence/E36.md)) |
| Unicode properties: combining class, grapheme cluster rules, Bidi\_Class of both joiners | 6, 6.1, 6.2 | Review by Unicode experts |
| Block position in the Supplementary Multilingual Plane | 7 | Assignment by the UTC |
| Reference font and code chart glyphs | 7.2, 8 | Designer, licence and glyphs |
| Horizontal use | 6.3 | Not attested, so the proposal assumes Hán Nôm habits |

## 10. Appendices

### A. Glossary

| Term | Meaning |
| --- | --- |
| Cán | One of the 22 bases, each of three strokes, listed in the section 幹音二十二字 (p. [2](evidence/pages/S1-p2.jpg)); each exists as a marked Cán and as an unmarked Cán |
| Marked Cán | The Cán with the marking stroke at the start position (22 in total); standalone only, never combined; character name MARKED-1 |
| Chi | One of the five forms per Cán with the marking stroke at position 2 to 6 (110 in total); standalone or combined |
| Unmarked Cán | The form of a base without a marking stroke (22 in total); combines with a Chi; standalone, it has the reading of the marked Cán; character name UNMARKED |
| Phản thiết pair | Combination of an unmarked Cán and a Chi of different Cán, unmarked Cán first, joined by the component joiner; described under Phản Thiết Hài Âm Pháp (反切諧音法); 2,310 in total; descriptive term of this proposal, unnamed in the source |
| Hợp Thư | Combination of a Chi and an unmarked Cán of the same Cán, joined by the component joiner; the Chi gives the initial, the unmarked Cán the rhyme; 110 in total |
| Tham Thư | Hợp Thư with a third component, a Chi, above it; 12,100 possible, two attested; reading not established |
| Component joiner | Format character that joins two components into one character; their order gives the arrangement |
| Tham Thư combiner | Format character that places the following Chi above a Hợp Thư |

### B. Attested passages

<!-- appendix-b:start -->
Passages located in the source, by page. Page references are to Source 1 (section 3); images are in the evidence catalogue.

| Page | Passage | Shows | Status |
| --- | --- | --- | --- |
| [1](evidence/pages/S1-p1.jpg) | 我國附於中華日前只 | Dating: the character 華 lacks its final stroke, a naming taboo for Hồ Thị Hoa, mother of Emperor Thiệu Trị (1841–1847) ([E30](evidence/E30.md)) | cited |
| [1](evidence/pages/S1-p1.jpg) | 國音新字序 | Name of the script: 國音新字 (Quốc Âm Tân Tự), in the heading of the preface 國音新字序 ([E33](evidence/E33.md)) | cited |
| [2](evidence/pages/S1-p2.jpg) | 幹音二十二字 | The listing under the heading 幹音二十二字 shows 22 forms, the marked Cán, each of three strokes and one short marking stroke ([E01](evidence/E01.md)) | cited |
| [2](evidence/pages/S1-p2.jpg) | 幹音二十二字 · Nôm annotations in order (IDS where no encoded character is used): 翁 ông · ⿰木禺 ngông · 胸 hông · ⿰木功 gông · 工 công · ⿰竜羽 lông · ⿰竜里 trông · 東 đông · 農 nông · 宗 tông · 通 thông · ⿰亻戍 nhông · 柊 chông · ⿰月容 dông · 衝 xông · 空 không · 滝 sông · ⿱山庸 rông · 蒙 mông · 芃 bông · ⿰木芃 vông · ⿰口風 phông | Listing of the 22 base sounds (幹音二十二字) in source order, each shown with its QATT character and annotated with the name of its sound in Chữ Nôm ([E18](evidence/E18.md)) | cited |
| [2](evidence/pages/S1-p2.jpg) | 五星聚斗南城居士阮子書 | Author's signature: Nam Thành cư sĩ Nguyễn Tử (南城居士阮子) ([E31](evidence/E31.md)) | cited |
| [2](evidence/pages/S1-p2.jpg) | 幹音二十二字 | The term Cán (幹): the listing of the 22 Cán is headed 幹音二十二字, 'trunk sounds, twenty-two characters' ([E37](evidence/E37.md)) | cited |
| [3](evidence/pages/S1-p3.jpg) | 枝字一百一十字 (see [E29](E29.md)) | Five Chi per Cán: the marking stroke sits only at stroke ends (six positions); the marked Cán has it at the start position (upper left or upper middle), and moving it counter-clockwise gives the Chi in order ([E02](evidence/E02.md)) | cited |
| [3](evidence/pages/S1-p3.jpg) | 枝字一百一十字 · 109 Chi, each annotated with a Nôm character | Table of the Chi under the heading 枝字一百一十字, 'the 110 Chi characters'; the table shows 109, one left out by oversight ([E29](evidence/E29.md)) | cited |
| [4](evidence/pages/S1-p4.jpg) | 本字八音識別法。於本字上依陰陽四象識別，每一字各成八字。如同東合一字，惟同音其聲在上為陽，東音其聲在下為陰。以陰陽分配，則東董凍篤四音是陰之平上去入，同洞動獨四音是陽之平上去入。以四象識別，則陽用全圈，陰用半圈。  其同字全識於其字之左足，洞字全識於其字之左肩，動字全識於其字之右肩，獨字全識於其字之右足；東字半識於其字之左足，董字半識於其字之左肩，凍字半識於其字之右肩，篤字半識於其字之右足。如下。他倣此。  {CU 東}{CU 董}{CU 凍}{CU 篤}{CU 同}{CU 洞}{CU 動}{CU 獨} | Tone marks: circle and semicircle in four corners, eight tones ([E14](evidence/E14.md)) | located |
| [4](evidence/pages/S1-p4.jpg) | 本字八音識別法。於本字上依陰陽四象識別，每一字各成八字。如同東合一字，惟同音其聲在上為陽，東音其聲在下為陰。以陰陽分配，則東董凍篤四音是陰之平上去入，同洞動獨四音是陽之平上去入。以四象識別，則陽用全圈，陰用半圈。  其同字全識於其字之左足，洞字全識於其字之左肩，動字全識於其字之右肩，獨字全識於其字之右足；東字半識於其字之左足，董字半識於其字之左肩，凍字半識於其字之右肩，篤字半識於其字之右足。如下。他倣此。  {CU 東}{CU 董}{CU 凍}{CU 篤}{CU 同}{CU 洞}{CU 動}{CU 獨} | Eight tones follow the Chinese yin-yang method ([E17](evidence/E17.md)) | located |
| [5](evidence/pages/S1-p5.jpg) | 反切諧音法 | Phản thiết method described in the section Phản Thiết Hài Âm Pháp (反切諧音法); components of different bases, unmarked Cán first ([E05](evidence/E05.md)) | located |
| [5](evidence/pages/S1-p5.jpg) | {CU 東}{CU 董}{CU 凍}{CU 篤}{CU 同}{CU 洞}{CU 動}{CU 獨} | Tone marks in all four corners, both shapes: the unmarked Cán of đông written with all eight tone marks, annotated 東 董 凍 篤 同 洞 動 獨 ([E15](evidence/E15.md)) | located |
| [5](evidence/pages/S1-p5.jpg) | 其同字全識於其字之左足，洞字全識於其字之左肩，動字全識於其字之右肩，獨字全識於其字之右足；東字半識於其字之左足，董字半識於其字之左肩，凍字半識於其字之右肩，篤字半識於其字之右足。如下。他倣此。 | The source lists the tones first with the four half circles, then the four full circles, each starting lower left and running clockwise ([E28](evidence/E28.md)) | located |
| [5](evidence/pages/S1-p5.jpg) | – | Marked Cán and unmarked Cán both appear standalone, with the same reading, also with tone marks; only the unmarked Cán combines, never the marked Cán ([E34](evidence/E34.md)) | located |
| [6](evidence/pages/S1-p6.jpg) | 如{CU 翁}{CH 宜}{PT 反}反云{CU 翁}{CU 翁}{PT 鳥}{PT 衣}是合取{PT 衣}{PT 字}也 | Components written standalone and side by side when the text explains combination, including a standalone unmarked Cán and two adjacent unmarked Cán ([E04](evidence/E04.md)) | located |
| [6](evidence/pages/S1-p6.jpg) | 合書左從枝体右從幹体畧法  {QT 螉}乃{QT 喊}{CM 翁}{PT 反}法合螉字也他倣此切法亦如之  {QT 癰} {QT 螉} {QT 嗡} {QT ⿰口癰} | Hợp Thư: same-base pairs only, Chi first (scope of the term) ([E07](evidence/E07.md)) | located |
| [6](evidence/pages/S1-p6.jpg) | See [E07](E07.md), the transcription of the whole section. | Function in a Hợp Thư: Chi gives the initial, unmarked Cán the rhyme (main argument for the reading order) ([E08](evidence/E08.md)) | located |
| [6](evidence/pages/S1-p6.jpg) | – | Tone marks are optional: marked and unmarked characters in the same passage ([E24](evidence/E24.md)) | located |
| [6](evidence/pages/S1-p6.jpg) | – | The neutral tone (ngang, âm bình) has its own mark, a semicircle in the lower left corner; an unmarked character does not mean the neutral tone ([E25](evidence/E25.md)) | located |
| [6](evidence/pages/S1-p6.jpg) | – | Tone marks on standalone components (unmarked Cán and Chi) ([E26](evidence/E26.md)) | located |
| [6](evidence/pages/S1-p6.jpg) | – | Round and angular forms of the same tone mark are handwriting variation: Source 1 writes the mark now round, now close to a hook; Source 2 writes all tone marks of the passage angular ([E27](evidence/E27.md)) | located |
| [7](evidence/pages/S1-p7.jpg) | – | Tham Thư rule: the base is a Hợp Thư ([E10](evidence/E10.md)) | located |
| [7](evidence/pages/S1-p7.jpg) | 故二十二幹字為標足以 | The term Cán (幹) also occurs with 字 in 二十二幹字為標, 'the 22 Cán characters as the mark'; with 幹音二十二字 ([E37](evidence/E37.md)) the source uses 幹 with 音 and with 字 ([E38](evidence/E38.md)) | cited |
| [7](evidence/pages/S1-p7.jpg) | {PT 嚥}乃{CM 翁}{CH ⿰口昭}{PT 反}法合嚥字也他倣此切法亦然  {QT ⿰口淵} {QT 馬} {QT 淵} {QT 卬} {QT 喧} | Passage on p. [7](evidence/pages/S1-p7.jpg), first and second column, without heading: a worked example of a phản thiết pair, the unmarked Cán of ONG and the Chi MARKED-5 of CHONG, read yên, and a list of five characters ([E39](evidence/E39.md)) | located |
| [8](evidence/pages/S1-p8.jpg) | 音数  單幹書協契象（即識別也）成一百七十六字。單書協契象成八百八十字（內有喊字等四十六字其八聲稀微置語）。合書左從枝体右從幹体協契象成八百八十字。合書左從幹体右從枝体協契象成一萬八千四百八十字（內有一千九百三十二字其八声稀微置語）。參書倣此。  Text in parentheses: small two-column notes in the manuscript. | Counts of the characters in the section 音数: 176 single Cán, 880 single characters, 880 合書 with Chi left and Cán right, 18,480 合書 with Cán left and Chi right, each including the tone marks; eight times 22, 110, 110 and 2,310 ([E36](evidence/E36.md)) | located |
<!-- appendix-b:end -->

### C. Scans of the sources

All 16 pages of both manuscripts (Source 1, pp. [1](evidence/pages/S1-p1.jpg)–[8](evidence/pages/S1-p8.jpg), folios 3–10; Source 2, pp. [1](evidence/pages/S2-p1.jpg)–[8](evidence/pages/S2-p8.jpg), folios 11–18) are in the evidence catalogue of the working repository. \[TBD: include the pages in the submitted document, subject to permission of the Institute of Hán Nôm Studies\]

### D. References

- Nguyễn Hữu Vinh, Đặng Thế Kiệt, Nguyễn Doãn Vượng, Lê Văn Đặng, Nguyễn Văn Sâm, Nguyễn Ngọc Bích, Trần Uyên Thi. *Tự điển chữ Nôm trích dẫn* (字典𡨸喃摘引) / *Dictionary of Nôm Characters with Excerpts*. USA: Viện Việt-Học (Institute of Vietnamese Studies), 2009. P. 403, entry 洞 đỗng (động, đùng), U+6D1E, with a cross-reference to 洞 động.

&#91;TBD: scholarly literature and prior work on the script\]

# Questions for the Unicode experts

Each question concerns a value marked \[TBD\] in section 6 of the proposal. The draft files contain the value given here as "Draft".

## Segmentation

1. **Grapheme clusters for the two joiners.** Required behaviour: no break directly before or after the component joiner or the Tham Thư combiner; every other boundary between components is a break (proposal 5.5, 6.2).
   Draft: Grapheme_Cluster_Break=Extend for both joiners (no break before them, GB9), and the Indic_Conjunct_Break mechanism of rule GB9c for the break after them: components InCB=Consonant, joiners InCB=Linker, tone marks InCB=Extend.
   Question: may Indic_Conjunct_Break be used for a non-Indic script, or is a new property value or rule preferred? With GB9c a joiner that follows no component (ill-formed text) does not join the next character; the reference implementation joins it. Is that difference acceptable?
2. **Line breaking around the joiners.** Required: no line break before or after a joiner. Line_Break=CM keeps a joiner with the preceding character but allows a break after it.
   Draft: Line_Break=GL. Question: GL, a ZWJ-like class, or a new class?
3. **Default_Ignorable_Code_Point.** If the joiners are default ignorable, software without support shows the components side by side in reading order, which keeps the text readable.
   Draft: not set. Question: should the joiners be Default_Ignorable_Code_Point?

## Other properties

4. **Bidi_Class of the joiners.** Draft: BN, as for most format characters. The earlier draft of the proposal had L.
5. **Canonical_Combining_Class of the tone marks.** Draft: 0. A cluster takes at most one tone mark, so no canonical reordering occurs (proposal 6.1). Please confirm.
6. **Vertical_Orientation and East_Asian_Width of the tone marks and joiners.** Draft: Vertical_Orientation=U, East_Asian_Width=N. The components are W and U like Han ideographs.
7. **Script code.** No ISO 15924 code is known to exist for Quốc Âm Tân Tự. Draft script name: Quoc_Am_Tan_Tu. A code would have to be requested from the ISO 15924 Registration Authority.

## Relation to existing characters

8. **Tone marks and existing characters.** U+A700..U+A707 MODIFIER LETTER CHINESE TONE YIN PING to YANG RU cover the same eight tones but are spacing modifier letters (Sk); U+302A..U+302D IDEOGRAPHIC LEVEL to ENTERING TONE MARK are combining marks for the same corners but without the âm/dương distinction. The draft encodes eight new combining marks and cross-references both sets in the names list (proposal 5.7).
    Question: does the UTC accept eight new marks, or would it prefer unification with U+302A..U+302D for one register? If new marks are accepted, should they take the positional combining classes of U+302A..U+302D (218, 228, 232, 222) instead of 0?

## Names

9. **Name conventions.** đ is written DD and d is written DZ (DDONG, DZONG); the forms are named by the position of the marking stroke, with digits after a hyphen (ONG MARKED-1 to ONG MARKED-6, and ONG UNMARKED); the names describe the form only. The tone marks have descriptive names with the tone as annotation. Are these acceptable?
10. **Block name and position.** Draft block name: Quoc Am Tan Tu, 176 code points in the Supplementary Multilingual Plane.
11. **Order of the groups in the block.** Draft: combiner and joiner (+00, +01), the eight tone marks (+02 to +09) and six reserved code points come first, then the letters (unmarked forms +10 to +25, marked forms +26 to +A9). Precedents for signs and format characters first: Indic blocks (signs before letters) and Mongolian (format characters before the letters). The letters are a fixed set; the marks may grow, so the reserve stands next to them. Question: is this order and the placement of the reserved code points acceptable to the UTC, or is the order letters first, marks last preferred?

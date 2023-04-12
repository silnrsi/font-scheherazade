
### Changes

#### New
- Added Medium and SemiBold weights
- Added Arabic-style (rounded) versions of chevron quotes
- Added Bold calligraphic honorifics (previous ones were the same weight as Regular)
- Added:
  - U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK
  - U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK
  - U+10EFD ARABIC SMALL LOW WORD SAKTA
  - U+10EFE ARABIC SMALL LOW WORD QASR
  - U+10EFF ARABIC SMALL LOW WORD MADDA

#### Improved
- Changed Kurdish language to support a U+06BE Heh Doachashmee alternate rather than U+0647 Heh alternate
- Redesigned
  - U+0616 ARABIC SMALL HIGH LIGATURE ALEF WITH LAM WITH YEH (see https://www.unicode.org/versions/Unicode15.0.0/erratafixed.html)
  - Slight adjustments to:
    - gaf-like characters (such as U+06AF ARABIC LETTER GAF)
    - U+0601 ARABIC SIGN SANAH
    - U+0605 ARABIC NUMBER MARK ABOVE
- Small improvements to kerning

#### Removed
- Removed support for Sindhi-style comma when Sindhi language is selected
- Removed Graphite support

#### Known issues
- Shaping for the newly added characters may not yet occur in applications
- Medial and final high hamza characters may have collisions (these likely do not occur)
- Lam + high hamza alef ligature does not form as it likely does not occur



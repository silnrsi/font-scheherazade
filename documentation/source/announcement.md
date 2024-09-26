---
title: Scheherazade New - Announcement
fontversion: 4.300
---

### Changes

#### New

- Added:
  - U+0897 ARABIC PEPET
  - U+10EC2 ARABIC LETTER DAL WITH TWO DOTS VERTICALLY BELOW
  - U+10EC3 ARABIC LETTER TAH WITH TWO DOTS VERTICALLY BELOW
  - U+10EC4 ARABIC LETTER KAF WITH TWO DOTS VERTICALLY BELOW
  - U+10EFC ARABIC COMBINING ALEF OVERLAY
- Added support for Kashmiri language
- Added facility to override default language behavior through feature selection
- Added support for cv76 (dagger alef) on space, nbspace, and tatweel

#### Improved
- Minor anchor adjustment on U+06D6
- Enhanced positioning of U+06E2 ARABIC SMALL HIGH MEEM ISOLATED FORM next to adjacent vowel marks
- Tweaks to the design of some of the honorifics
- Improved alef+mark positioning to reduce collisions
- Improved madda reordering to comply with UAX #53



#### Known issues
- Shaping for the newly added characters may not yet occur in applications
- Medial and final high hamza characters may have collisions (these likely do not occur)
- Lam + high hamza alef ligature does not form as it likely does not occur



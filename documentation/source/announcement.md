Release 3.200

The only change in this release is to add the new Unicode 14.0 codepoints to the honorifics. At this point either the Private Usa Area (PUA) codepoints, _or_ the Unicode 14.0 codepoints will work. Our intent is to remove the PUA codepoints in about a year. This should give ample time for users to transition to official codepoints.

Both desktop and web fonts are provided in a single, all-platforms package on the [Download Page](https://software.sil.org/scheherazade/download/).

#### Known issues

* Medial and Final high hamza characters may have collisions as these likely do not occur.
* Lam/high hamza alef ligature does not form as it likely does not occur.
* Many OpenType applications do not yet support Unicode 13.0 (or 14.0) and may not correctly handle the characters in ranges U+08BE..U+08C7, U+FD40..U+FD4F, U+FDCF, and U+FDFE..U+FDFF.
* The honorific ligatures that are currently encoded in the Private Use Area (PUA) of Unicode do not have right-to-left properties. In some cases, you can correct reading order problems by inserting a Right-to-Left mark (U+200F) after the honorific ligature. These have also been encoded using Unicode 14.0 codepoints, and because most applications do not support Unicode 14.0 users will still run into some issues in using them.
* The more calligraphic honorifics do not yet have a bold.



---
title: Scheherazade New Font Features
fontversion: 3.100
header-includes:
- |
    ```{=latex}
    %\rowcolors{0}{gray!10}{gray!25}
    ```
---

Scheherazade New is an OpenType and Graphite-enabled font that supports the Arabic script. It includes a number of optional features that may be useful or required for particular uses or languages. These OpenType (and Graphite) features are primarily specified using four-letter tags (e.g. 'cv17'), although some applications may provide a direct way to control certain language features. This document lists all the available features.

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Scheherazade New as a web font see [Scheherazade Webfont Example](../web/ScheherazadeNew-webfont-example.html). See [Using SIL Fonts on Web Pages: OpenType and Graphite feature support](http://scripts.sil.org/using_web_fonts#feat) for more information.

*If this document is not displaying correctly a PDF version is also provided.*

## Complete feature list (in progress)

### Character alternates

#### Dal

<span class='affects'>Affects: U+062F, U+0630, U+0688, U+0689, U+068A, U+068B, U+068C, U+068D, U+068E, U+068F, U+0690, U+06EE, U+0759, U+075A, U+08AE</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard  | <span class='sch-dflt-R normal'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span> | `cv12=0`
Alternate | <span class='sch-cv12-R normal'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span> | `cv12=1`


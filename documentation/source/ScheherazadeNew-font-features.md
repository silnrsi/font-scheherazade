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

| | 
------------- | --------------- 
Check | <span class='sch-rend-R normal'>RenderingUnknown</span>

### Language

<span class='affects'>U+062F, U+0630, U+0688..U+068F, U+0690, U+06EE, U+0759, U+075A, U+08AE, U+0645, U+0765, U+0766, U+08A7, U+0647, U+0626, U+060C, U+061B, U+06F4, U+06F5, U+06F6, U+06F7, U+0650, U+064F, U+064C, U+0657</span>

All of these language features have been implemented in Graphite, OpenType, and TypeTuner rendering*. However, the ability to use them in OpenType applications is dependent on the application allowing the user to select the language. Few applications would allow the user to select Kyrgyz, Rohingya, or Wolof.

Language | Sample | Feature setting
------------- | --------------- | ------------- 
default | <span class='sch-dflt-R normal' >د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ ه ههه  ئ ئئئ ،؛ ۴۵۶۷ ◌ِّ ◌ٌ ◌ُ◌ٗ</span> | 
Kurdish (Northern) | <span class='sch-dflt-R normal' lang="kmr">د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ ه ههه  ئ ئئئ ،؛ ۴۵۶۷ ◌ِّ ◌ٌ ◌ُ◌ٗ</span>| `lang=kmr`
Kyrgyz|<span class='sch-dflt-R normal' lang="ky">د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ ه ههه  ئ ئئئ ،؛ ۴۵۶۷ ◌ِّ ◌ٌ ◌ُ◌ٗ</span>|  `lang=ky`
Rohingya |<span class='sch-dflt-R normal' lang="rhg">د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ ه ههه  ئ ئئئ ،؛ ۴۵۶۷ ◌ِّ ◌ٌ ◌ُ◌ٗ</span>| `lang=rhg`
Sindhi |<span class='sch-dflt-R normal' lang="sd">د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ ه ههه  ئ ئئئ ،؛ ۴۵۶۷ ◌ِّ ◌ٌ ◌ُ◌ٗ</span>| `lang=sd`
Urdu |<span class='sch-dflt-R normal' lang="ur">د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ ه ههه  ئ ئئئ ،؛ ۴۵۶۷ ◌ِّ ◌ٌ ◌ُ◌ٗ</span>| `lang=ur`
Wolof |<span class='sch-dflt-R normal' lang="wo">د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ ه ههه  ئ ئئئ ،؛ ۴۵۶۷ ◌ِّ ◌ٌ ◌ُ◌ٗ</span>|  `lang=wo`

### Character alternates

#### Dal

<span class='affects'>Affects: U+062F, U+0630, U+0688, U+0689, U+068A, U+068B, U+068C, U+068D, U+068E, U+068F, U+0690, U+06EE, U+0759, U+075A, U+08AE</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard  | <span class='sch-dflt-R normal'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span>| G,O,T | `cv12=0`
Alternate | <span class='sch-cv12-R normal'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span>| G,O,T | `cv12=1`


#### Meem 

<span class='affects'>Affects: U+0645, U+0765, U+0766, U+08A7</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard | <span class='sch-dflt-R normal'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span> | G,O,T | cv44=0
Sindhi-style | <span class='sch-cv44-R normal'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span>| G,O,T | cv44=1

#### Heh 

<span class='affects'>Affects: U+0647</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard | <span class='sch-dflt-R normal'> ه ههه </span>| G,O,T | cv48=0
Kurdish-style | <span class='sch-cv48-3-R normal'> ه ههه </span>| G,O,T | cv48=3
Sindhi-style | <span class='sch-cv48-1-R normal'> ه ههه </span>| G,O,T | cv48=1
Urdu-style | <span class='sch-cv48-2-R normal'> ه ههه </span>| G,O,T | cv48=2

#### Kirghiz OE 

<span class='affects'>Affects: U+06C5</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Loop | <span class='sch-dflt-R normal'>ۅ</span> | G,O,T | cv51=0
Bar | <span class='sch-cv51-R normal'>ۅ</span>| G,O,T | cv51=1

#### Yeh Hamza 

<span class='affects'>Affects: U+0626</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard | <span class='sch-dflt-R normal'>ئ ‍ئ</span> | G,O,T | cv54=0
Right hamza| <span class='sch-cv54-R normal'>ئ ‍ئ</span>| G,O,T | cv54=1


### Diacritic and symbol alternates

#### Maddah

<span class='affects'>Affects: U+0622, U+0627, U+0653, U+0653</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Small | <span class='sch-dflt-R normal'> آ آ ◌ٓ </span> | G,O,T | `cv60=0`
Large | <span class='sch-cv60-R normal'>آ آ ◌ٓ </span>| G,O,T | `cv60=1`


#### Shadda+kasra placement

<span class='affects'>Affects: U+064D, U+0650 with U+0651</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Raised  | <span class='sch-dflt-R normal'> بِّ ◌ِّ بٍّ ◌ٍّ </span> | G,O,T | `cv62=0`
Lowered | <span class='sch-cv62-R normal'> بِّ ◌ِّ بٍّ ◌ٍّ </span>| G,O,T | `cv62=1`


#### Damma 

<span class='affects'>Affects: U+064F</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard | <span class='sch-dflt-R normal'> بُ ◌ُ</span>     | G,O,T | `cv70=0`
Filled   | <span class='sch-cv70-1-R normal'>بُ ◌ُ</span>| G,O,T | `cv70=1`
Short    | <span class='sch-cv70-2-R normal'>بُ ◌ُ</span>| G,O,T | `cv70=2`

#### Dammatan 

<span class='affects'>Affects: U+064C</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard | <span class='sch-dflt-R normal'>بٌ ◌ٌ</span> | G,O,T | `cv72=0`
Six-nine | <span class='sch-cv72-R normal'>بٌ ◌ٌ</span>| G,O,T | `cv72=1`

#### Inverted Damma 

<span class='affects'>Affects: U+0657</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard | <span class='sch-dflt-R normal'>بٗ ◌ٗ</span> | G,O,T | `cv74=0`
Hollow | <span class='sch-cv74-R normal'>بٗ ◌ٗ</span>| G,O,T | `cv74=1`


#### Superscript Alef 

<span class='affects'>Affects: U+0670 on all yeh, sad and seen-like characters: 
U+0649 U+064A U+06D0 U+06D1 U+0777 U+06CC U+0635 U+0636 U+069D U+069E U+06FB U+08AF U+0633 U+0634 U+069A U+069B U+069C U+06FA U+075C U+076D U+0770 U+077D U+077E</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Small | <span class='sch-dflt-R normal'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span> | G,O,T | `cv76=0`
Large | <span class='sch-cv76-R normal'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span>| G,O,T | `cv76=1`

#### Sukun 

<span class='affects'>Affects: U+0652</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Closed | <span class='sch-dflt-R normal'>بْ ◌ْ</span> | G,O,T | `cv78=0`
Open down | <span class='sch-cv78-1-R normal'>بْ ◌ْ</span>| G,O,T | `cv78=1`
Open left | <span class='sch-cv78-2-R normal'>بْ ◌ْ</span>| G,O,T | `cv78=2`


#### End of ayah 


<span class='affects'>Affects: U+06DD</span>

Firefox allows you to use U+06DD followed by the digits and proper rendering occurs. Some applications require the following:

* precede the entire sequence (subtending mark plus following digits) with
        202D LEFT-TO-RIGHT OVERRIDE
* follow the entire sequence with U+202C POP DIRECTIONAL FORMATTING.

Surrounding the sequence with U+202D and U+202C seems to give the most reliable results in different browsers. 

<span class='affects'>Sample text below: U+202D U+06DD U+0031 U+0032 U+0033 U+202C / U+202D U+06DD U+0661 U+0662 U+0663 U+202C</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard     | <span class='sch-dflt-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; / &#x202D;&#x6DD;&#x661;&#x662;&#x663;&#x202C;</span> | G,O,T | `cv80=0`
Simplified A | <span class='sch-cv80-1-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; / &#x202D;&#x6DD;&#x661;&#x662;&#x663;&#x202C;</span>| G,O,T | `cv80=1`
Simplified B | <span class='sch-cv80-2-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; / &#x202D;&#x6DD;&#x661;&#x662;&#x663;&#x202C;</span>| G,O,T | `cv80=2`

The new DISPUTED END OF AYAH (U+08E2) is also now available in the font. It works in the same way as End of ayah. It renders properly in Firefox, however, it does not yet work in Chrome or in Internet Explorer/Edge. <span class='sch-dflt-R normal'>&#x202D;&#x8E2;&#x663;&#x664;&#x665;&#x202C;</span>

#### Honorific ligatures 


<span class='affects'>Affects: U+FDFA..U+FDFB, U+FDFD, U+E002..U+E014</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Calligraphic | <span class='sch-dflt-R normal'>&#xFDFA;&#xFDFB;&#xFDFD; &#xE002;&#xE003;&#xE004;&#xE005;&#xE006;&#xE007;&#xE008;&#xE009;&#xE00A;&#xE00B; &#xE00C;&#xE00D;&#xE00E;&#xE00F;&#xE010;&#xE011;&#xE012;&#xE013;&#xE014;</span> | G,O,T | `cv81=0`
Simplified | <span class='sch-cv81-R normal'>&#xFDFA;&#xFDFB;&#xFDFD; &#xE002;&#xE003;&#xE004;&#xE005;&#xE006;&#xE007;&#xE008;&#xE009;&#xE00A;&#xE00B; &#xE00C;&#xE00D;&#xE00E;&#xE00F;&#xE010;&#xE011;&#xE012;&#xE013;&#xE014;</span>| G,O,T | `cv81=1`


#### Eastern digits 


<span class='affects'>Affects: U+06F4, U+06F6, U+06F7</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Standard | <span class='sch-dflt-R normal'>۴۵۶۷</span> | G,O,T | `cv82=0`
Rohingya-style | <span class='sch-cv82-4-R normal'>۴۵۶۷</span>| G,O,T | `cv82=4`
Sindhi-style | <span class='sch-cv82-1-R normal'>۴۵۶۷</span>| G,O,T | `cv82=1`
Urdu-style | <span class='sch-cv82-2-R normal'>۴۵۶۷</span>| G,O,T | `cv82=2`


#### Comma 

<span class='affects'>Affects: U+060C, U+061B</span>

Feature | Sample | Rendering* | Feature setting
------------- | --------------- |------------- | ------------- 
Upward | <span class='sch-dflt-R normal'>، ؛</span> | G,O,T | `cv84=0`
Downward | <span class='sch-cv84-R normal'>، ؛</span>| G,O,T | `cv84=`1

*<b>Legend:</b> G=Implemented in Graphite; O=Implemented in OpenType; T=Implemented in TypeTuner (command line version: [http://scripts.sil.org/TypeTuner](http://scripts.sil.org/TypeTuner) and web-based version: [http://scripts.sil.org/ttw](http://scripts.sil.org/ttw)).


Scheherazade New is a TrueType font with smart font capabilities added using OpenType and Graphite font technologies. The Scheherazade New font includes a number of optional features that provide alternative rendering that might be preferable for use in some contexts. The sections below enumerates the details of these features. Whether these features are available to users will depend on both the application and the rendering technology ([Graphite](http://graphite.sil.org/) or OpenType) being used. Most features are available in both Graphite and OpenType, though there may be minor differences in their implementation. Some applications let the user control certain features such as Character Variants to turn on the rendering of variant characters. However, at this point, most applications do not make use of those features so another solution is needed to show the variant characters. [TypeTuner](http://scripts.sil.org/ttw/fonts2go.cgi) creates tuned fonts that use the variant glyph in place of the standard glyph. TypeTuner also provides the ability to turn on support for the Kurdish, Kyrgyz, Rohingya, Sindhi, Urdu, and Wolof languages variants.

See [Using Font Features](https://software.sil.org/fonts/features/). Although that page is not targeted at Arabic script support, it does provide a comprehensive list of applications that make full use of the OpenType and Graphite font technologies.

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Scheherazade New as a web font see [Scheherazade New Webfont Example](../web/ScheherazadeNew-webfont-example.html). For detailed information see [Using SIL Fonts on Web Pages](http://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*


## Customizing with TypeTuner

For applications that do not make use of Graphite features or the OpenType Character Variants, you can now download fonts customized with the variant glyphs you choose. Read the [Scheherazade New Font Features](https://software.sil.org/scheherazade/support/smart-font-features/#user), visit [TypeTuner Web](http://scripts.sil.org/ttw/fonts2go.cgi), then choose the variants and download your font.



### Test rendering engine choice 

Here is a simple test to see if Graphite is working in your browser. If it is, the following will say "RenderingGraphite". If your browser does not support Graphite it should say "RenderingOpentype". Firefox is currently the only browser that supports Graphite. See the [instructions on how to enable Graphite in Firefox](http://scripts.sil.org/cms/scripts/page.php?site_id=projects&amp;item_id=graphite_firefox#switchon).

| | 
------------- | --------------- 
Check | <span class='scheherazadenew-R normal'>RenderingUnknown</span>

### Language 

<span class='affects'>Affects: U+062F, U+0630, U+0688..U+068F, U+0690, U+06EE, U+0759, U+075A, U+08AE, U+0645, U+0765, U+0766, U+08A7, U+0647, U+0626, U+060C, U+061B, U+06F4, U+06F5, U+06F6, U+06F7, U+0650, U+064F, U+064C, U+0657</span>

Unfortunately, the UI needed to access the language-specific behavior is not yet present in many applications. LibreOffice and Microsoft Word 2016 support language-specific behavior for Kurdish, Sindhi and Urdu (but not Kyrgyz, Rohingya or Wolof). Some Harfbuzz-based apps, e.g., XeTeX, can access language-specific behavior.


Language | Sample | Feature setting
------------- | --------------- | ------------- 
default | <span class='scheherazadenew-R normal'>&#x062F;&#x0020;&#x0630;&#x0020;&#x0688;&#x0020;&#x0689;&#x0020;&#x068A;&#x0020;&#x068B;&#x0020;&#x068C;&#x0020;&#x068D;&#x0020;&#x068E;&#x0020;&#x068F;&#x0020;&#x0690;&#x0020;&#x06EE;&#x0020;&#x0759;&#x0020;&#x075A;&#x0020;&#x08AE;&#x0020;&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;&#x0020;&#x0765;&#x0020;&#x0765;&#x0765;&#x0765;&#x0020;&#x0766;&#x0020;&#x0766;&#x0766;&#x0766;&#x0020; &#x08A7;&#x0020;&#x08A7;&#x08A7;&#x08A7;&#x0020; </br>&#x0647;&#x0020;&#x0647;&#x0647;&#x0647;&#x0020; &#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020; &#x060C; &#x061B; &#x06F4; &#x06F6; &#x06F7; </br>&#x0628;&#x0651;&#x0650; &#x0628;&#x064F; &#x0628;&#x064C; &#x0628;&#x0657;</span>|
Kurdish (Northern) | <span class='scheherazadenew-R normal' lang='kmr'>&#x062F;&#x0020;&#x0630;&#x0020;&#x0688;&#x0020;&#x0689;&#x0020;&#x068A;&#x0020;&#x068B;&#x0020;&#x068C;&#x0020;&#x068D;&#x0020;&#x068E;&#x0020;&#x068F;&#x0020;&#x0690;&#x0020;&#x06EE;&#x0020;&#x0759;&#x0020;&#x075A;&#x0020;&#x08AE;&#x0020;&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;&#x0020;&#x0765;&#x0020;&#x0765;&#x0765;&#x0765;&#x0020;&#x0766;&#x0020;&#x0766;&#x0766;&#x0766;&#x0020; &#x08A7;&#x0020;&#x08A7;&#x08A7;&#x08A7;&#x0020; </br>&#x0647;&#x0020;&#x0647;&#x0647;&#x0647;&#x0020; &#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020; &#x060C; &#x061B; &#x06F4; &#x06F6; &#x06F7; </br>&#x0628;&#x0651;&#x0650; &#x0628;&#x064F; &#x0628;&#x064C; &#x0628;&#x0657;</span>| `lang=kmr`
Kyrgyz|<span class='scheherazadenew-R normal' lang='kir'>&#x062F;&#x0020;&#x0630;&#x0020;&#x0688;&#x0020;&#x0689;&#x0020;&#x068A;&#x0020;&#x068B;&#x0020;&#x068C;&#x0020;&#x068D;&#x0020;&#x068E;&#x0020;&#x068F;&#x0020;&#x0690;&#x0020;&#x06EE;&#x0020;&#x0759;&#x0020;&#x075A;&#x0020;&#x08AE;&#x0020;&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;&#x0020;&#x0765;&#x0020;&#x0765;&#x0765;&#x0765;&#x0020;&#x0766;&#x0020;&#x0766;&#x0766;&#x0766;&#x0020; &#x08A7;&#x0020;&#x08A7;&#x08A7;&#x08A7;&#x0020; </br>&#x0647;&#x0020;&#x0647;&#x0647;&#x0647;&#x0020; &#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020; &#x060C; &#x061B; &#x06F4; &#x06F6; &#x06F7; </br>&#x0628;&#x0651;&#x0650; &#x0628;&#x064F; &#x0628;&#x064C; &#x0628;&#x0657;</span>| `lang=ky`
Rohingya |<span class='scheherazadenew-R normal' lang='rhg'>&#x062F;&#x0020;&#x0630;&#x0020;&#x0688;&#x0020;&#x0689;&#x0020;&#x068A;&#x0020;&#x068B;&#x0020;&#x068C;&#x0020;&#x068D;&#x0020;&#x068E;&#x0020;&#x068F;&#x0020;&#x0690;&#x0020;&#x06EE;&#x0020;&#x0759;&#x0020;&#x075A;&#x0020;&#x08AE;&#x0020;&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;&#x0020;&#x0765;&#x0020;&#x0765;&#x0765;&#x0765;&#x0020;&#x0766;&#x0020;&#x0766;&#x0766;&#x0766;&#x0020; &#x08A7;&#x0020;&#x08A7;&#x08A7;&#x08A7;&#x0020; </br>&#x0647;&#x0020;&#x0647;&#x0647;&#x0647;&#x0020; &#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020; &#x060C; &#x061B; &#x06F4; &#x06F6; &#x06F7; </br>&#x0628;&#x0651;&#x0650; &#x0628;&#x064F; &#x0628;&#x064C; &#x0628;&#x0657;</span>| `lang=rhg`
Sindhi |<span class='scheherazadenew-R normal' lang='sd'>&#x062F;&#x0020;&#x0630;&#x0020;&#x0688;&#x0020;&#x0689;&#x0020;&#x068A;&#x0020;&#x068B;&#x0020;&#x068C;&#x0020;&#x068D;&#x0020;&#x068E;&#x0020;&#x068F;&#x0020;&#x0690;&#x0020;&#x06EE;&#x0020;&#x0759;&#x0020;&#x075A;&#x0020;&#x08AE;&#x0020;&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;&#x0020;&#x0765;&#x0020;&#x0765;&#x0765;&#x0765;&#x0020;&#x0766;&#x0020;&#x0766;&#x0766;&#x0766;&#x0020; &#x08A7;&#x0020;&#x08A7;&#x08A7;&#x08A7;&#x0020; </br>&#x0647;&#x0020;&#x0647;&#x0647;&#x0647;&#x0020; &#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020; &#x060C; &#x061B; &#x06F4; &#x06F6; &#x06F7; </br>&#x0628;&#x0651;&#x0650; &#x0628;&#x064F; &#x0628;&#x064C; &#x0628;&#x0657;</span>| `lang=sd`
Urdu |<span class='scheherazadenew-R normal' lang='ur'>&#x062F;&#x0020;&#x0630;&#x0020;&#x0688;&#x0020;&#x0689;&#x0020;&#x068A;&#x0020;&#x068B;&#x0020;&#x068C;&#x0020;&#x068D;&#x0020;&#x068E;&#x0020;&#x068F;&#x0020;&#x0690;&#x0020;&#x06EE;&#x0020;&#x0759;&#x0020;&#x075A;&#x0020;&#x08AE;&#x0020;&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;&#x0020;&#x0765;&#x0020;&#x0765;&#x0765;&#x0765;&#x0020;&#x0766;&#x0020;&#x0766;&#x0766;&#x0766;&#x0020; &#x08A7;&#x0020;&#x08A7;&#x08A7;&#x08A7;&#x0020; </br>&#x0647;&#x0020;&#x0647;&#x0647;&#x0647;&#x0020; &#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020; &#x060C; &#x061B; &#x06F4; &#x06F6; &#x06F7; </br>&#x0628;&#x0651;&#x0650; &#x0628;&#x064F; &#x0628;&#x064C; &#x0628;&#x0657;</span>| `lang=ur`
Wolof |<span class='scheherazadenew-R normal' lang='wol'>&#x062F;&#x0020;&#x0630;&#x0020;&#x0688;&#x0020;&#x0689;&#x0020;&#x068A;&#x0020;&#x068B;&#x0020;&#x068C;&#x0020;&#x068D;&#x0020;&#x068E;&#x0020;&#x068F;&#x0020;&#x0690;&#x0020;&#x06EE;&#x0020;&#x0759;&#x0020;&#x075A;&#x0020;&#x08AE;&#x0020;&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;&#x0020;&#x0765;&#x0020;&#x0765;&#x0765;&#x0765;&#x0020;&#x0766;&#x0020;&#x0766;&#x0766;&#x0766;&#x0020; &#x08A7;&#x0020;&#x08A7;&#x08A7;&#x08A7;&#x0020; </br>&#x0647;&#x0020;&#x0647;&#x0647;&#x0647;&#x0020; &#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020; &#x060C; &#x061B; &#x06F4; &#x06F6; &#x06F7; </br>&#x0628;&#x0651;&#x0650; &#x0628;&#x064F; &#x0628;&#x064C; &#x0628;&#x0657;</span>| `lang=wo`




### Character variants

There are some character shape differences in different languages which use the Arabic script. These can be accessed by using Graphite features, OpenType Character Variants, or through the language support mentioned above.  

#### Dal 

<span class='affects'>Affects: U+062F, U+0630, U+0688, U+0689, U+068A, U+068B, U+068C, U+068D, U+068E, U+068F, U+0690, U+06EE, U+0759, U+075A, U+08AE</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span>| `cv12=0`
Alternate | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv12" 1'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span>| `cv12=1`

#### Meem 

<span class='affects'>Affects: U+0645, U+0765, U+0766, U+08A7</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span> | `cv44=0`
Sindhi-style | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv44" 1'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span>| `cv44=1`


#### Heh 

<span class='affects'>Affects: U+0647</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'> ه ههه </span>| `cv48=0`
Kurdish-style | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv48" 3'> ه ههه </span>| `cv48=3`
Sindhi-style | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv48" 1'> ه ههه </span>| `cv48=1`
Urdu-style | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv48" 2'> ه ههه </span>| `cv48=2`

#### Kirghiz OE 

<span class='affects'>Affects: U+06C5</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Loop | <span class='scheherazadenew-R normal'>ۅ</span> | `cv51=0`
Bar | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv51" 1'>ۅ</span>| `cv51=1`

#### Yeh Hamza 

<span class='affects'>Affects: U+0626</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'>ئ ‍ئ</span> | `cv54=0`
Right hamza| <span class='scheherazadenew-R normal' style='font-feature-settings: "cv54" 1'>ئ ‍ئ</span>| `cv54=1`

#### Maddah 

<span class='affects'>Affects: U+0622, U+0627, U+0653, U+0653</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Small | <span class='scheherazadenew-R normal'> آ آ ◌ٓ </span> | `cv60=0`
Large | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv60" 1'>آ آ ◌ٓ </span>| `cv60=1`


#### Shadda+kasra placement 

<span class='affects'>Affects: U+064D, U+0650 with U+0651</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Raised | <span class='scheherazadenew-R normal'> بِّ ◌ِّ بٍّ ◌ٍّ </span> | `cv62=0`
Lowered | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv62" 1'> بِّ ◌ِّ بٍّ ◌ٍّ </span>| `cv62=1`

#### Damma 


<span class='affects'>Affects: U+064F</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'> بُ ◌ُ</span> | `cv70=0`
Filled | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv70" 1'>بُ ◌ُ</span>| `cv70=1`
Short| <span class='scheherazadenew-R normal' style='font-feature-settings: "cv70" 2'>بُ ◌ُ</span>| `cv70=2`

#### Dammatan 

<span class='affects'>Affects: U+064C</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'>بٌ ◌ٌ</span> | `cv72=0`
Six-nine | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv72" 1'>بٌ ◌ٌ</span>| `cv72=1`

#### Inverted Damma 

<span class='affects'>Affects: U+0657</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'>بٗ ◌ٗ</span> | `cv74=0`
Hollow | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv74" 1'>بٗ ◌ٗ</span>| `cv74=1`


#### Superscript Alef 

<span class='affects'>Affects: U+0670 on all yeh, sad and seen-like characters 
U+0649 U+064A U+06D0 U+06D1 U+0777 U+06CC U+0635 U+0636 U+069D U+069E U+06FB U+08AF U+0633 U+0634 U+069A U+069B U+069C U+06FA U+075C U+076D U+0770 U+077D U+077E</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Small | <span class='scheherazadenew-R normal'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span> | `cv76=0`
Large | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv76" 1'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span>| `cv76=1`

#### Sukun 

<span class='affects'>Affects: U+0652</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Closed | <span class='scheherazadenew-R normal'>بْ ◌ْ</span> | `cv78=0`
Open down | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv78" 1'>بْ ◌ْ</span>| `cv78=1`
Open left | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv78" 2'>بْ ◌ْ</span>| `cv78=2`

#### End of ayah 


<span class='affects'>Affects: U+06DD</span>

Firefox allows you to use U+06DD followed by the digits and proper rendering occurs. Some applications require the following:

* precede the entire sequence (subtending mark plus following digits) with
        202D LEFT-TO-RIGHT OVERRIDE
* follow the entire sequence with U+202C POP DIRECTIONAL FORMATTING.

Surrounding the sequence with U+202D and U+202C seems to give the most reliable results in different browsers. However, we have not found a solution that works in Internet Explorer/Edge.

In the example below, the following codepoints are used: U+202D U+06DD U+0031 U+0032 U+0033 U+202C U+202D U+06DD U+0611 U+0622 U+0663 U+202C.

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span> | `cv80=0`
Simplified A | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv80" 1'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>| `cv80=1`
Simplified B | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv80" 2'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>| `cv80=2`

The new DISPUTED END OF AYAH (U+08E2) is also now available in the font. It works in the same way as End of ayah. 

<span class='scheherazadenew-R normal'>&#x202D;&#x8E2;&#x663;&#x664;&#x665;&#x202C;</span>

#### Honorific ligatures 


<span class='affects'>Affects: U+FD40..U+FD4F, U+FDCF, U+FDFA..U+FDFB, U+FDFD..U+FDFF</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Calligraphic | <span class='scheherazadenew-R normal'>&#xFD40;&#xFD41;&#xFD42;&#xFD43;&#xFD44;&#xFD45;&#xFD46;&#xFD47;&#xFD48;&#xFD49;&#xFD4A;&#xFD4B;&#xFD4C;&#xFD4D;&#xFD4E;&#xFD4F;</br>&#xFDCF;&#xFDFA;&#xFDFB;&#xFDFD;&#xFDFF;&#xFDFF;</span> | `cv81=0`
Simplified | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'>&#xFD40;&#xFD41;&#xFD42;&#xFD43;&#xFD44;&#xFD45;&#xFD46;&#xFD47;&#xFD48;&#xFD49;&#xFD4A;&#xFD4B;&#xFD4C;&#xFD4D;&#xFD4E;&#xFD4F;</br>&#xFDCF;&#xFDFA;&#xFDFB;&#xFDFD;&#xFDFF;&#xFDFF;</span>| `cv81=1`


#### Eastern digits 


<span class='affects'>Affects: U+06F4, U+06F6, U+06F7</span>

Feature value | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='scheherazadenew-R normal'>&#x06F4;&#x06F6;&#x06F7;</span> | `cv82=0`
Sindhi-style | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv82" 1'>&#x06F4;&#x06F6;&#x06F7;</span>| `cv82=1`
Urdu-style | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv82" 2'>&#x06F4;&#x06F6;&#x06F7;</span>| `cv82=2`
Rohingya-style | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv82" 4'>&#x06F4;&#x06F6;&#x06F7;</span>| `cv82=4`


#### Comma 

<span class='affects'>Affects: U+060C, U+061B</span>

Feature value | Sample |  Feature setting
------------- | --------------- | ------------- 
Upward | <span class='scheherazadenew-R normal'>، ؛</span> | `cv84=0`
Downward | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv84" 1'>، ؛</span>| `cv84=1`

#### Line spacing 

Allows for adjustment of the default line spacing in the font (values shown are ordered in increasing line spacing). This feature is only available with TypeTuner.

Feature Value | 
------------- | ---------------  
Tight | 
Normal | 
Loose |

### Honorific Ligatures

Unicode has a number of honorific ligatures. Recently, more have been approved for release in Unicode 14.0. These are included in this version of the font. As new characters, applications may have problems with rendering them in right-to-left text. In some cases, you can correct reading order problems by inserting a Right-to-Left mark (U+200F) after the honorific ligature.

Unicode Name (ARABIC LIGATURE...) | USV | Glyph | Glyph simplified | Meaning
------------- |------------- |------------- |------------- |------------- 
RAHIMAHU ALLAAH | FD40 | <span class='scheherazadenew-R normal'>﵀</span> |<span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵀</span> | May God have mercy upon him.</br>(Used for companions of the prophet or other widely recognized scholars. Can be for any believer who has passed away.)
RADI ALLAAHU ANH | FD41 | <span class='scheherazadenew-R normal'>﵁ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵁</span> | May God be pleased with him.</br>(Used for companions of the prophet.)
RADI ALLAAHU ANHAA | FD42 | <span class='scheherazadenew-R normal'>﵂ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵂</span> | May God be pleased with her.</br>(Used for companions of the prophet, and in some regions for others such as Mary or Jesus’ apostles.)
RADI ALLAAHU ANHUM | FD43 | <span class='scheherazadenew-R normal'>﵃ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵃</span> | May God be pleased with them (masculine plural, but can be used for a mixed group of men and women).</br>(Used for companions of the prophet.)
RADI ALLAAHU ANHUMAA | FD44 | <span class='scheherazadenew-R normal'>﵄ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵄</span> | May God be pleased with them (both).</br>(Used for companions of the prophet.)
RADI ALLAAHU ANHUNNA | FD45 | <span class='scheherazadenew-R normal'>﵅ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵅</span> | May God be pleased with them (feminine).</br>(Used for companions of the prophet.)
SALLALLAAHU ALAYHI WA-AALIH | FD46 | <span class='scheherazadenew-R normal'>﵆ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵆</span> | Blessings of God be upon him and the people of his household.</br>(Used particularly in Shia Islam for leaders who come from the bloodline of the prophet.)
ALAYHI AS-SALAAM | FD47 | <span class='scheherazadenew-R normal'>﵇ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵇</span> | Peace be upon him.</br>(The normal honorific used after a prophet's or an Archangel's name.)
ALAYHIM AS-SALAAM | FD48 | <span class='scheherazadenew-R normal'>﵈ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵈</span> | Peace be upon them.</br>(Used for two or more prophets.)
ALAYHIMAA AS-SALAAM | FD49 | <span class='scheherazadenew-R normal'>﵉ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵉</span> | Peace be upon them (both).</br>(Used for prophets and angels.)
ALAYHI AS-SALAATU WAS-SALAAM | FD4A | <span class='scheherazadenew-R normal'>﵊ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵊</span> | Blessings and Peace be upon him.</br>(A lesser used honorific used after a prophet's or an Archangel's name.)
QUDDISA SIRRAH | FD4B | <span class='scheherazadenew-R normal'>﵋ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵋</span> | May his secret be sanctified.</br>(Used for Sufi saints, and refers to their shrines where people come to worship.)
SALLALLAHU ALAYHI WA-AALIHEE WA-SALLAM | FD4C | <span class='scheherazadenew-R normal'>﵌ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵌</span> | The blessings of God and peace be upon him and the people of his household.</br>(Used by all Muslims, but particularly in Shia Islam for the prophet Muhammad.)
ALAYHAA AS-SALAAM | FD4D | <span class='scheherazadenew-R normal'>﵍ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵍</span> | Peace be upon her.</br>(Used after the name of a woman who was the mother of a prophet.)
TABAARAKA WA-TAAALAA | FD4E | <span class='scheherazadenew-R normal'>﵎ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵎</span> | May he be blessed and exalted (Blessed and Lofty).</br>(One of the honorifics used only for God himself.)
RAHIMAHUM ALLAAH | FD4F | <span class='scheherazadenew-R normal'>﵏ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﵏</span> | God have mercy upon them (masculine).</br>(Used for widely recognized scholars. Also used for ordinary believers.)
SALAAMUHU ALAYNAA | FDCF | <span class='scheherazadenew-R normal'>﷏ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﷏</span> | His peace be upon us.</br>(Used by some followers of Jesus to give special honor to him.)
SALLALLAHOU ALAYHEWASALLAM  | FDFA | <span class='scheherazadenew-R normal'>ﷺ</span> <| <span
  class='scheherazadenew-R normal'>ﷺ </span> | The blessings and peace of God be upon him. </br>(Used after the name of a major prophet, especially the prophet of Islam.)
JALLAJALALOUHOU | FDFB | <span class='scheherazadenew-R normal'>ﷻ</span> | <span
  class='scheherazadenew-R normal'>ﷻ </span> | May His glory be glorified.</br>(Used after the name of God.)
BISMILLAH AR-RAHMAN AR-RAHEEM | FDFD | <span
  class='scheherazadenew-R normal'>﷽ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'>﷽ </span>| In the name of God, the most merciful, the most compassionate.</br>(Used as the opening of each action in order to receive blessing from God.)
SUBHAANAHU WA TAAALAA | FDFE | <span class='scheherazadenew-R normal'>﷾ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﷾</span> | May He be praised and exalted (Glorified and Lofty).</br>(The most common honorific for God.)
AZZA WA JALL | FDFF | <span class='scheherazadenew-R normal'>﷿ </span> | <span class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'> ﷿</span> | The Glorified/Exalted/Mighty and Sublime (Prestigious and Majestic).</br>(The second most common honorific for God.)



[font id='scheherazadenew' face='ScheherazadeNew-Regular' size='150%' rtl=1]

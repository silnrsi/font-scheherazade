---
title: Scheherazade New - Special rules for rendering Allah
fontversion: 3.300
---


In certain types of literature, the name *Allah* and words related to this name are given unique rendering. Unicode has a *presentation form* character (U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM) that implements this rendering and, while this can work (in some fonts) for the word in isolation, it doesn’t help users obtain special rendering in other contexts where it is desired. 

Starting with v3.300, Scheherazade New provides the special rendering for sequences of Arabic letters that meet specific patterns, giving much more flexibility to document authors. 

* The special Unicode character U+FDF2 will always display the Allah ligature (equivalent to the sequence recommended by Unicode: isolate *alef* + *lam* + *lam* + *shadda* + *superscript-alef* + final *heh*).
* Under certain conditions, a sequence of *lam* + *lam* + *heh* (optionally preceded by other characters) will form an Allah ligature:
  * The *heh* must be final form and may be either the standard *heh* (0647) or the *heh-goal* (06C1) and may have marks.
  * The *lam* must be the standard *lam* (0644).
  * The sequence must include either a preceding isolate *alef* or a *shadda* (0651) on the second *lam*, or both.
  * If *alef* precedes the first *lam*:
    * The *alef* may have marks or be a related character such as *alef-hamza*, *alef-hamza-below*, *alef-madda*, or *alef-wasla* (any character in the `ALEF` joining group).
    * If it is an isolate *alef* but there are no marks on the second *lam*, a *shadda-superscript-alef* will be automatically displayed.
  * The first *lam* may include a *kasra*, but no other marks.
  * The *shadda* may be followed or preceded by either a *superscript-alef* (0670) or a *fatha* (064E). If neither is present, then a *superscript-alef* will be added to the display.



To disable the special ligature, insert a zero-width joiner character (200D) somewhere in the sequence.



Characters | → | Glyph | Comment
---------- | - | ----  | -------
<span class='scheherazadenewL-R normal'>&#x202d;&#x0627; + &#x0644; + &#x0644; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'> الله	</span> | Ligature is formed (U+0647)
<span class='scheherazadenewL-R normal'>&#x202d;&#x0627; + &#x0644; + &#x0644; + &#x06c1;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>اللہ	</span> | Ligature is formed (U+06C1)
<span class='scheherazadenewL-R normal'>&#x202d;&#x0671; + &#x0644; + &#x0644; + &#x0651; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'> ٱللّه </span> | Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0627; + &#x0644; + &#x0644; + &#x0651; + &#x064e; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>اللَّه	</span> | Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0627; + &#x0644; + &#x0644; + &#x0651; + &#x0670; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>اللّٰه</span> | 	Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0644; + &#x0644; + &#x0651; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;&#x0644;&#x0651;&#x0647;</span> | Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0644; + ZWJ + &#x0644; + &#x0651; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;&#x200D;&#x0644;&#x0651;&#x0647;</span> | Ligature is not formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0644; + &#x0644; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;&#x0644;&#x0647;</span> | Ligature is not formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0644; + &#x0650; + &#x0644; + &#x0651; + &#x0647; + &#x0652;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>لِلّهْ	</span> | Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0627; + &#x0644; + &#x0652; + &#x0627; + &#x0644; + &#x0644; + &#x0651; + &#x0647; + &#x0652;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>الْاللّهْ	</span> | Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0628; + &#x0650; + &#x0644; + &#x0644; + &#x0651; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>بِللّه	</span> | Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0641; + &#x0644; + &#x0644; + &#x0651; + &#x064e; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>فللَّه	</span> | Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0641; + &#x0644; + &#x0644; + &#x0651; + &#x064e; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>فللَّه	</span> | Ligature is formed
<span class='scheherazadenewL-R normal'>&#x202d;&#x0641; + &#x0644; + &#x0644; + &#x064e; + &#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>فللَه	</span> | Ligature is not formed





<!-- PRODUCT SITE ONLY
[font id='scheherazadenew' face='ScheherazadeNew-Regular' size='150%' rtl=1]
[font id='scheherazadenewL' face='ScheherazadeNew-Regular' size='150%' ltr=1]
-->

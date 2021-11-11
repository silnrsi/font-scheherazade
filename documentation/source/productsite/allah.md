

In certain types of literature, the name *Allah* and words related to this name are given unique rendering. Unicode has a *presentation form* character (U+FDF2 ARABIC LIGATURE ALLAH ISOLATED FORM) that implements this rendering and, while this can work (in some fonts) for the word in isolation, it doesn’t help users obtain special rendering in other contexts where it is desired. 

Starting with v2.200, Scheherazade New provides the special rendering for sequences of Arabic letters that meet specific patterns, giving much more flexibility to document authors. To obtain the special rendering, all of the following must be true:

* The basic sequence of letters is either:
   * lam-lam-heh 
      * Preceded by some Arabic letter (joining or not, with or without diacritic marks)
      * The second lam *must* be followed (in either order) by shadda and either superscript alef or fatha 
   * alef-lam-lam-heh
      * alef is the *isolate* form (with or without diacritic marks)
      * The second lam *may* be followed (in either order) by shadda and either superscript alef or fatha
* The heh used is the *final* form of either *heh goal* (U+06C1 <span dir="rtl" class='scheherazadenew-R normal'>&#x200d;&#x06c1;</span> ) final OR *heh* (U+0647 <span dir="rtl" class='scheherazadenew-R normal'>&#x200d;&#x0647;</span> ) final
* There are no diacritic marks between the two *lam* characters


feh | + | alef | + | lam | + | lam | + | shadda | + | fatha *or* </br>superscript alef | + | heh | → | Glyph | Comment
--- | - | ---  | - | --- | - | --- | - | ---    | - | ---                              | - | --- | - | ----- | -----
<span dir="rtl" class='scheherazadenew-R normal'> </span>| | <span dir="rtl" class='scheherazadenew-R normal'>&#x0627;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | | | | |<span dir="rtl" class='scheherazadenew-R normal'>&#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>الله </span> | Ligature is formed (U+0647)
<span dir="rtl" class='scheherazadenew-R normal'> </span>| | <span dir="rtl" class='scheherazadenew-R normal'>&#x0627;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | | | | | <span dir="rtl" class='scheherazadenew-R normal'>&#x06c1;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'> اللہ </span>| Ligature is formed (U+06C1)
<span dir="rtl" class='scheherazadenew-R normal'> </span>| | <span dir="rtl" class='scheherazadenew-R normal'>&#x0627;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0651;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'> &#x064e;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0647;</span> | → | <span dir="rtl" class='scheherazadenew-R normal'>  اللَّه </span>| Ligature is formed
<span dir="rtl" class='scheherazadenew-R normal'> </span>| | <span dir="rtl" class='scheherazadenew-R normal'>&#x0627;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0651;</span> | + |  <span dir="rtl" class='scheherazadenew-R normal'> &#x0670;</span>  | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0647;</span> | → |<span dir="rtl" class='scheherazadenew-R normal'> اللّٰه </span>| Ligature is formed
<span dir="rtl" class='scheherazadenew-R normal'>&#x0641;</span>| + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0627;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span>  | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0651;</span> | + |  <span dir="rtl" class='scheherazadenew-R normal'> &#x064e;</span>  | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0647;</span> | → |<span dir="rtl" class='scheherazadenew-R normal'> فللَّه</span> | Ligature is formed
<span dir="rtl" class='scheherazadenew-R normal'>&#x0641;</span>| + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0627;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span> | + | <span dir="rtl" class='scheherazadenew-R normal'>&#x0644;</span>  | + | | | | | <span dir="rtl" class='scheherazadenew-R normal'>&#x0647;</span>  | → | <span dir="rtl" class='scheherazadenew-R normal'>فلله </span>| Ligature is not formed



[font id='scheherazadenew' face='ScheherazadeNew-Regular' size='150%' rtl=1]

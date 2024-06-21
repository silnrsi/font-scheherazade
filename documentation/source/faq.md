---
title: Scheherazade New - Frequently Asked Questions
fontversion: 4.300
---

Many questions can be answered by consulting the following FAQ pages. Here are a few sample questions answered in each FAQ:

- [SIL fonts in general](https://software.sil.org/fonts/faq)
    - *How can I type...?*
    - *How can I use font features?*
    - *Will you add support for character...?*
    - *Will you add support for script...?*
    - *WIll you help me...?*

- [The SIL Open Font License (OFL-FAQ)](https://openfontlicense.org/ofl-faq/)
    - *Can I use this font for...?*
    - *Can I modify the font and then include it in...*
    - *If I use the font on a web page do I have to include an acknowledgement?*
    - The full OFL-FAQ.txt is also included in the font package.

A generic FAQ for all of our Arabic scripts fonts can be found here: [Arabic Fonts - FAQ](https://software.sil.org/arabicfonts/support/faq/). FAQ's specific to Scheherazade New are found below.

### Problems with Bold weights

#### *Why does my application not show the Bold weight in font menus and dialogs?*

Some applications will list all the weights but leave out Bold. To access the Bold you need to choose Regular and turn on Bold using the application's UI controls such as a "B" button.

#### *Why do I sometimes get a fake Bold?*

If you choose a weight other than Regular (such as Medium), then use application controls to turn on Bold, some applications will make a "fake" Bold rather than use one of the real ones in the font (Medium, SemiBold, Bold). This is because only Regular has an associated Bold counterpart. This is a technical limitation with some apps and OSes. If you are using some other weight than Regular for text and want to make a word or phrase stand out you will need to select the text and apply one of the heavier weights manually. 

### *Why the name change? Why is this now called Scheherazade New?*

**Scheherazade** has been around for many years. Over the years people have complained about the small size of the font in comparison to other fonts. We have completely resized the glyphs in **Scheherazade New**. If we had kept the same name, the layout of all existing documents would be affected. Thus, this name change allows users to keep using **Scheherazade** for older documents, but they can begin using **Scheherazade New** for new documents.

### *What characters are included with this release?*

See [Character Set Support](charset.md) for the full listing.

### *I notice that Scheherazade New is missing a number of characters that I would like. Will you add these?*

It is impossible for us to add every glyph that every person desires, but we do place a high priority on adding complete coverage of all the characters defined in Unicode for Arabic script (excluding the Arabic Presentation Forms blocks, which are not recommended for normal use). You can send us your requests, but please understand that we are unlikely to add symbols where the user base is very small, unless they have been accepted into Unicode.

### *What is so special about Scheherazade?*

This font is designed to work with the OpenType font technology. To take advantage of the advanced typographic capabilities of this font, you must be using applications that provide an adequate level of support for OpenType. These advanced capabilities provide access to the variant character forms used in some languages. See [Smart Font Features](features.md).

### *Why is the line spacing in Scheherazade so much looser than earlier versions?*

Our Arabic fonts include characters with multiple stacked diacritics that need a much looser line spacing (for example, U+06D1 ۑ  or U+063A غ with a vowel below would need a lot of space!). We cannot make the line spacing tighter without experiencing “clipping” of those characters. You may be able to overcome this by adjusting the line spacing in the application. In Microsoft Word select **Format / Paragraph** and set the line spacing to use the **Exactly** setting and a value more suited to your needs. For example, if the font size is 12 pt, select line spacing of **Exactly** 13 pt. This will give a tighter line spacing. You can adjust the value up or down depending on how many diacritics you need to stack. With HTML you should also be able to change the line spacing; add the line-height property to your HTML element or CSS style (“<code>line-height: 105%;</code>” or “<code>line-height: 12pt;</code>”) and play around with the value until you get the spacing desired.

We have provided a "Tight" version of our font for download. This is available from [TypeTuner Web](https://scripts.sil.org/ttw/fonts2go.cgi). Just select **Scheherazade New** and choose the Line spacing feature you desire. Then download the font. Be aware that it will have a different font name.


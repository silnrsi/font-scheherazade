
The SIL Arabic script fonts are encoded according to Unicode, so your application must support Unicode text in order to access letters other than the standard ANSI characters. Most applications now provide basic Unicode support. You will, however, need some way of entering Unicode text into your document.

Arabic script is a complex and difficult script, and this complexity is compounded by the fact that Arabic script is used for [many different languages](http://scriptsource.org/scr/Arab) and cultures with variations in acceptable calligraphic style. From a computer perspective at least, the technologies used to implement Arabic script are not yet fully mature. The result is that while a given font might work for one set of languages on a given software platform, the same font might not work for other languages or on other platforms. This means that it is very difficult to give an accurate answer to the question of software requirements. 

## Requirements

This font is supported by all major operating systems (macOS, Windows, Linux-based, iOS, and Android), however the extent of that support depends on the individual OS and application.

## Installation

Install the font by decompressing the .zip archive and installing the font using the standard font installation process for .ttf (TrueType/OpenType) fonts for your platform. For additional tips see the help page on [Font installation](https://software.sil.org/fonts/installation).

## Keyboarding and character set support

The Arabic script font packages do not include any keyboarding helps or utilities. If you cannot use the built-in keyboards of the operating system, you will need to install the appropriate keyboard and input method for the characters of the language you wish to use. If you want to enter characters that are not supported by any system keyboard, the [Keyman program](http://keyman.com/) can be helpful on Windows, macOS, Linux, Android and iOS systems. Also available for Windows is [MSKLC](https://www.microsoft.com/en-us/download/details.aspx?id=102134). For other platforms, [XKB](http://www.x.org/wiki/XKB/) or [Ukelele](https://software.sil.org/ukelele/) can be helpful.

If you want to enter characters that are not supported by any system keyboard, and to access the full Unicode range, we suggest you use gucharmap, kcharselect on Ubuntu or similar software. Another method of entering some symbols is provided by a few applications such as Adobe InDesign. They can display a glyph palette that shows all the glyphs (symbols) in a font and allow you to enter them by clicking on the glyph you want.

Other suggestions are listed here: [Keyboard Systems Overview](http://scriptsource.org/entry/ytr8g8n6sw).

See [Character set support](charset) for details of the Unicode characters supported by this font.

## Rendering and application support

SIL's Arabic script fonts are designed to work with two advanced font technologies, [Graphite](http://graphite.sil.org/) and OpenType. To take advantage of the advanced typographic capabilities of these fonts, you must be using applications that provide an adequate level of support for Graphite or OpenType.

Other suggestions are listed here: [Applications Support](http://software.sil.org/arabicfonts/support/application-support/) and here: [Using Font Features](https://software.sil.org/fonts/features/). 

## Web fonts

Web font versions of this font (in WOFF and WOFF2 formats) are available in the `web` folder. These can be copied to a web server and used as fonts on web pages. A very basic HTML/CSS demo page is also included. For more information on the options and techniques available for using these fonts on web pages see [Using SIL Fonts on Web Pages](http://software.sil.org/fonts/webfonts).

## Text conversion

One common type of data conversion is from Roman script to Arabic script. Cross-script conversion is often very language specific. TECkit is one program that can be used for character encoding conversion. TECkit allows users to write their own custom conversion mappings. The TECkit package is available for download from SIL’s [TECkit](https://software.sil.org/teckit/) Web site. The [SIL Converters](https://software.sil.org/silconverters/) software will be an important tool in data conversion.

One page that may prove helpful is: [Roman Script to Arabic Script Conversion](https://software.sil.org/arabicfonts/rs-to-as-conversion/).

Other suggestions are listed here: [Introduction to Text Conversion and Transliteration](http://scriptsource.org/entry/xlzd6n5aqt).

See also: [Arabic Fonts -- Resources](http://software.sil.org/arabicfonts/resources/).
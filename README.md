# Alkalami

Alkalami is the local word for the Arabic "qalam", a type of sharpened stick used for writing on wooden boards in the Kano region of Nigeria and in Niger, and what gives the style its distinct appearance. The baseline stroke is very thick and solid. The ascenders and other vertical strokes including the teeth are very narrow when compared to the baseline. A generous line height is necessary to allow for deep swashes and descenders, and the overall look of the page is a very black, solid rectangle. Diacritics are much smaller in scale, with very little distance from the main letters.

The source/Alkalami-master.glyphs file contains all the designed glyphs as well as fea files, etc.
The UFOs sources are used for testing, building and releasing the fonts.

## Project status [![Build Status](http://build.palaso.org/app/rest/builds/buildType:Fonts_Alkalami/statusIcon)](http://build.palaso.org/viewType.html?buildTypeId=Fonts_Alkalami&guest=1)

Alkalami v1.200 has been released. 

## About ftml tests

After a successful build, the results/ folder will contain, along with the built ttf and woff fonts, a number of
test files in an xml-based format called FTML. Examples are AllChars-ng.xml, Diac-ng.xml. 
There is an ftml.xsl file that can be used to view these ftml documents directly in Firefox. 

However, in order for Firefox to access the .xsl file, you need to relax its "strict URI" policy by going to about:config and
setting [security.fileuri.strict_origin_policy](http://kb.mozillazine.org/Security.fileuri.strict_origin_policy) to false.

Once you have this setting in effect, you can load the FTML documents directly into Firefox and see the built font rendered.

## License

Alkalami is licensed under the SIL Open Font License. See [OFL.txt](OFL.txt) and [OFL-FAQ.txt](OFL-FAQ.txt) for details.

## See also

For more details about this project, including changelog and acknowledgements see [FONTLOG.txt](FONTLOG.txt).

For further information about this font, including Unicode ranges supported and OpenType font features and how to use them, and licensing, please see the documentation on [software.sil.org/alkalami](http://software.sil.org/alkalami/) or in the documentation/ subfolder.

If you want to contribute to the project let us know.

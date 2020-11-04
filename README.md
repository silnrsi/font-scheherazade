# Scheherazade New

Scheherazade New is a smart open font designed by SIL International. It is designed as a general-purpose Arabic style and is intended to support most of the characters in the Unicode 13.0 Arabic blocks.

### Project status [![Build Status](http://build.palaso.org/app/rest/builds/buildType:Fonts_ScheherazadeNew/statusIcon)](http://build.palaso.org/viewType.html?buildTypeId=Fonts_ScheherazadeNew&guest=1)

Scheherazade New v3.000 has been released. 

Scheherazade New is a mature product with no major changes anticipated. We will be releasing maintenance updates to fix bugs. 


## Copyright and License
For copyright and licensing information - including any Reserved Font Names - see [OFL.txt](OFL.txt).

For practical information about using, modifying and redistributing this font see [OFL-FAQ.txt](OFL-FAQ.txt).

For more details about this project, including its design history and acknowledgements see [FONTLOG.txt](FONTLOG.txt).

## See also
For further information, including Unicode ranges supported, Graphite and OpenType font features
and how to use them, please see the documentation on [software.sil.org/scheherazade](http://software.sil.org/scheherazade/)
or in the documentation subfolder.

# Developer notes

This project uses a UFO-based design and production workflow, with all sources in open formats and a completely open-source build toolkit. For more details see [SIL Font Development Notes](https://silnrsi.github.io/silfontdev/en-US/Introduction.html).

We welcome contributions to this font project, such as new glyphs, enhanced smart font code, or bug fixes. The best way to begin the process is to file an issue in the [Github project](https://github.com/silnrsi/font-scheherazade) or respond to an existing issue and express your interest. Then we can begin to correspond with you regarding what all might be required and discuss how to best submit your contributions.

To enable us to accept contributions in a way that honors your contribution and respects your copyright while preserving long-term flexibility for open source licensing, you would also need to agree to the SIL International Contributor License Agreement for Font Software (v1.0) prior to sending us your contribution. To read more about this requirement and find out how to submit the required form, please visit the [CLA information page](https://software.sil.org/fontcla).

## Building

The Scheherazade New project can be built from source using [smith](https://github.com/silnrsi/smith). This is done via the sequence:
```
    smith distclean
    smith configure
    smith build
    smith alltests
```

Because of the complex kerning logic, builds can take up to 15 minutes or longer, depending on hardware. If the complex kerning is _not_ needed (such as for debugging other font logic), the `--quick` parameter can be supplied: 
```
    smith distclean
    smith configure
    smith build --quick
```
The resulting files will not have functional OpenType kerning, but will be otherwise usable.

### Adding characters

After adding base characters to the font, the `classes.xml` file will need adjustment. The first six
classes relating to right- and dual-link contextual forms are can be generated algorithmically
from `source/glyph_data.csv` using `tools/bin/absgenclasses.py`.

### Generated test files

After adding characters or additional behaviors to the font, test files should be created or enhanced to test the new behaviors. These test files:
- `tests/AllChars.ftml` 
- `tests/ALSorted.ftml`
- `tests/DaggerAlef.ftml`
- `tests/Diac.ftml`
- `tests/Diac-short.ftml`
- `tests/Kern.ftml`
- `tests/SubtendingMarks.ftml`
- `tests/Yehbarree.ftml`

There is, in the tools folder, an ftml.xsl file that can be used to view these ftml documents directly in Firefox (which supports
Graphite rendering). 

However, in order for Firefox to access the .xsl file, you need to relax its "strict URI" policy by going to about:config and
setting [security.fileuri.strict_origin_policy](http://kb.mozillazine.org/Security.fileuri.strict_origin_policy) to false.

Once you have this setting in effect, you can load the FTML documents directly into Firefox and see the built font rendered.

See all the details in the [SIL FontDev guide](https://silnrsi.github.io/silfontdev/).

# Scheherazade New

Scheherazade New is a smart open font designed by SIL International. It is designed as a general-purpose Arabic style and is intended to support most of the characters in the Unicode 13.0 Arabic blocks.

### Project status [![Build Status](http://build.palaso.org/app/rest/builds/buildType:Fonts_ScheherazadeNew/statusIcon)](http://build.palaso.org/viewType.html?buildTypeId=Fonts_ScheherazadeNew&guest=1)

**NOTE: This is a development font. It is not yet ready for wider use or distribution to end-users.**   
Font sources are published in a public repository and a smith open workflow is used for building, testing and releasing.   
You can contribute and report issues but please don't use this in production yet.

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

## Building

The Scheherazade New project can be built from source using [smith](https://github.com/silnrsi/smith). This is done via the sequence:
```
    smith distclean
    smith configure
    smith build
	smith alltests
```
See all the details in the [SIL FontDev guide](https://silnrsi.github.io/silfontdev/).

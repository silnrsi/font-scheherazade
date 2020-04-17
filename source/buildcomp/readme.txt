WHAT THIS FOLDER IS ABOUT

This folder is used to generate glyphs from components. The component definitions are stored in absGlyphList.xslx/csv/txt. Two utility scripts are run to modify the UFO files.

* psfcsv2comp -i glyphs2build.csv compdefns.txt

* psfbuildcomp -i compdefns.txt --preserve "dia[AB]|alef$" --remove "_?(above|below|center|ring|through)$" ../masters/Scheherazade-Regular.ufo

  psfbuildcomp -i compdefns.txt --preserve "dia[AB]|alef$" --remove "_?(above|below|center|ring|through)$" ../masters/Scheherazade-Bold.ufo
  
	 - Use the -a option to do a dry run and see errors before the real thing.
	 
After running these scripts, APs need to be checked and cleaned up on the generated glyphs.

	 
The files are:

* glyphs2build.csv - a subset of absGlyphList.csv containing only the new glyphs to be processed.
* compdefns.txt - the output of psfcsv2comp, the input to psfbuildcomp. The following tweaks must be made to this file:

tehTehabove-ar - _teh@above[shift=0,-200]
tehTehabove-ar.fina - _teh@above[shift=0,-150]
jeemThreedotsabove-ar - _dot3u@above[shift=0,-70]
jeemThreedotsabove.fina-ar - _dot3u@above[shift=0,-40]

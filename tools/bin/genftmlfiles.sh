#!/bin/sh

# This script rebuilds the algorithmically-generated ftml files. See README.md

# Copyright (c) 2020 SIL International  (http://www.sil.org)
# Released under the MIT License (http://opensource.org/licenses/

# Assumes we're in the root folder, i.e., font-scheherazade

set -x
set -e

if [ ! -e OFL.txt ] 
then
	echo "Please cd to root of font project to use this script"
	exit 2
fi

tools/bin/absgenftml.py -t 'AllChars'         source/masters/ScheherazadeNew-Regular.ufo  tests/AllChars.ftml        -l tests/logs/AllChars.log         -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold'
tools/bin/absgenftml.py -t 'AL Sorted'        source/masters/ScheherazadeNew-Regular.ufo  tests/ALsorted.ftml        -l tests/logs/ALsorted.log         -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold'
tools/bin/absgenftml.py -t 'Diac'             source/masters/ScheherazadeNew-Regular.ufo  tests/Diac.ftml            -l tests/logs/DiacTest1.log                                                              --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' 
tools/bin/absgenftml.py -t 'Diac Short'       source/masters/ScheherazadeNew-Regular.ufo  tests/Diac-short.ftml      -l tests/logs/DiacTest1-short.log  -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold'
tools/bin/absgenftml.py -t 'Subtending Marks' source/masters/ScheherazadeNew-Regular.ufo  tests/SubtendingMarks.ftml -l tests/logs/Subtending.log       -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold'
tools/bin/absgenftml.py -t 'DaggerAlef'       source/masters/ScheherazadeNew-Regular.ufo  tests/DaggerAlef.ftml      -l tests/logs/DaggerAlef.log       -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold'
tools/bin/absgenftml.py -t 'Kerning'          source/masters/ScheherazadeNew-Regular.ufo  tests/Kern.ftml            -l tests/logs/Kerning.log          -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold'
tools/bin/absgenftml.py -t 'Yehbarree'        source/masters/ScheherazadeNew-Regular.ufo  tests/Yehbarree.ftml       -l tests/logs/Yehbarree.log        -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold'

#!/bin/sh

# This script rebuilds the algorithmically-generated ftml files. See README.md

# Copyright (c) 2020 SIL International  (http://www.sil.org)
# Released under the MIT License (http://opensource.org/licenses/

# Assumes we're in the root folder, i.e., font-scheherazade

set -e

if [ ! -e OFL.txt ] 
then
	echo "Please cd to root of font project to use this script"
	exit 2
fi

echo "Rebuilding ftml files..."
tools/bin/absgenftml.py -q -t 'AllChars (auto)'         source/masters/ScheherazadeNew-Regular.ufo  tests/AllChars.ftml        -l tests/logs/AllChars.log         -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' &
tools/bin/absgenftml.py -q -t 'AL Sorted (auto)'        source/masters/ScheherazadeNew-Regular.ufo  tests/ALsorted.ftml        -l tests/logs/ALsorted.log         -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' &
tools/bin/absgenftml.py -q -t 'Diac (auto)'             source/masters/ScheherazadeNew-Regular.ufo  tests/Diac.ftml            -l tests/logs/DiacTest1.log                                                              --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' & 
tools/bin/absgenftml.py -q -t 'Diac Short (auto)'       source/masters/ScheherazadeNew-Regular.ufo  tests/Diac-short.ftml      -l tests/logs/DiacTest1-short.log  -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' &
tools/bin/absgenftml.py -q -t 'Subtending Marks (auto)' source/masters/ScheherazadeNew-Regular.ufo  tests/SubtendingMarks.ftml -l tests/logs/Subtending.log       -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' &
tools/bin/absgenftml.py -q -t 'DaggerAlef (auto)'       source/masters/ScheherazadeNew-Regular.ufo  tests/DaggerAlef.ftml      -l tests/logs/DaggerAlef.log       -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' &
tools/bin/absgenftml.py -q -t 'Kerning (auto)'          source/masters/ScheherazadeNew-Regular.ufo  tests/Kern.ftml            -l tests/logs/Kerning.log          -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' &
tools/bin/absgenftml.py -q -t 'Yehbarree (auto)'        source/masters/ScheherazadeNew-Regular.ufo  tests/Yehbarree.ftml       -l tests/logs/Yehbarree.log        -s 'url(../references/Scheherazade-Regular.ttf)=v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,wo,rhg" -s 'url(../results/ScheherazadeNew-Regular.ttf)=Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)=OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)=Bold' &

wait
echo done.

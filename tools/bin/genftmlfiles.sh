#!/bin/sh

# This script rebuilds the algorithmically-generated ftml files. See README.md

# Copyright (c) 2020-2022 SIL International  (http://www.sil.org)
# Released under the MIT License (http://opensource.org/licenses/

# Assumes we're in the root folder, i.e., font-scheherazade

set -e

if [ ! -e OFL.txt ] 
then
	echo "Please cd to root of font project to use this script"
	exit 2
fi

if [ ! -e results/flo_cache/ScheherazadeNew-Regular.woff2 ]
then
	# Cache the Regular font from FLO to use as the "previous font"
	echo "Retrieving FLO woff2 for comparison"
	mkdir -p results/flo_cache/
	wget -nv -P results/flo_cache/ "http://fonts.languagetechnology.org/fonts/sil/scheherazadenew/web/ScheherazadeNew-Regular.woff2"
	echo
fi

echo "Rebuilding ftml files..."
tools/bin/absgenftml.py -q -t 'AllChars (auto)'         source/masters/ScheherazadeNew-Regular.ufo  tests/AllChars-auto.ftml        -l tests/logs/AllChars.log         --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2" -s 'url(../references/Scheherazade-Regular.ttf)|v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/bin/absgenftml.py -q -t 'AL Sorted (auto)'        source/masters/ScheherazadeNew-Regular.ufo  tests/ALsorted-auto.ftml        -l tests/logs/ALsorted.log         --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2" -s 'url(../references/Scheherazade-Regular.ttf)|v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/bin/absgenftml.py -q -t 'Diac (auto)'             source/masters/ScheherazadeNew-Regular.ufo  tests/Diac-auto.ftml            -l tests/logs/DiacTest1.log        --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2"                                                       --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' & 
tools/bin/absgenftml.py -q -t 'Diac Short (auto)'       source/masters/ScheherazadeNew-Regular.ufo  tests/Diac-short-auto.ftml      -l tests/logs/DiacTest1-short.log  --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2" -s 'url(../references/Scheherazade-Regular.ttf)|v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/bin/absgenftml.py -q -t 'Subtending Marks (auto)' source/masters/ScheherazadeNew-Regular.ufo  tests/SubtendingMarks-auto.ftml -l tests/logs/Subtending.log       --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2" -s 'url(../references/Scheherazade-Regular.ttf)|v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/bin/absgenftml.py -q -t 'DaggerAlef (auto)'       source/masters/ScheherazadeNew-Regular.ufo  tests/DaggerAlef-auto.ftml      -l tests/logs/DaggerAlef.log       --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2" -s 'url(../references/Scheherazade-Regular.ttf)|v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/bin/absgenftml.py -q -t 'Kerning (auto)'          source/masters/ScheherazadeNew-Regular.ufo  tests/Kern-auto.ftml            -l tests/logs/Kerning.log          --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2" -s 'url(../references/Scheherazade-Regular.ttf)|v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/bin/absgenftml.py -q -t 'Yehbarree (auto)'        source/masters/ScheherazadeNew-Regular.ufo  tests/Yehbarree-auto.ftml       -l tests/logs/Yehbarree.log        --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2" -s 'url(../references/Scheherazade-Regular.ttf)|v2.1' --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT' -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/bin/absgenftml.py -q -t 'Feature-Language Interactions (auto)' \
                                                		source/masters/ScheherazadeNew-Regular.ufo  tests/FeatLang-auto.ftml        -l tests/logs/FeatLang.log         --prevfont "results/flo_cache/ScheherazadeNew-Regular.woff2"                                                       --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i source/glyph_data.csv --langs "sd,ur,ku,rhg,ky,wo" -w 75% -s 'url(../results/ScheherazadeNew-Regular.ttf)|Graphite' -s 'url(../results/tests/ftml/fonts/ScheherazadeNew-Regular_ot_arab.ttf)|OT'  &

wait
echo done.

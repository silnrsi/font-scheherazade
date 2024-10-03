#!/bin/bash

# This script rebuilds the algorithmically-generated ftml files. See README.md

# Copyright (c) 2020-2024 SIL Global  (https://www.sil.org)
# Released under the MIT License (https://opensource.org/licenses/

# Assumes we're in the root folder, i.e., font-scheherazade

set -e

if [ ! -e OFL.txt ] 
then
	echo "Please cd to root of font project to use this script"
	exit 2
fi

prevfont="references/v4.000/ScheherazadeNew-Regular.ttf"
prevver="4.0"

commonParams=( \
	--prevfont "$prevfont"  \
	-s "url(../$prevfont)|$prevver"  \
	--ap '_?dia[ABO]$'  \
	--xsl ../tools/ftml.xsl  \
	--scale 200  \
	-i source/glyph_data.csv  \
	--langs 'sd,ur,ku,rhg,ks,ky,wo'  \
	-w 75%  \
	--ucdxml source/additional_ucd.xml  \
	-s "url(../references/ScheherazadeNew-Regular.ttf)|ref"  \
	-s "url(../results/ScheherazadeNew-Regular.ttf)|Reg" \
)

echo "Rebuilding ftml files..."
tools/absgenftml.py -q -t 'AllChars (auto)'                      source/masters/ScheherazadeNew-Regular.ufo  tests/AllChars-auto.ftml        -l tests/logs/AllChars.log         "${commonParams[@]}" -s 'url(../results/ScheherazadeNew-Medium.ttf)|Med' -s 'url(../results/ScheherazadeNew-SemiBold.ttf)|SeBld'  -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/absgenftml.py -q -t 'AL Sorted (auto)'                     source/masters/ScheherazadeNew-Regular.ufo  tests/ALsorted-auto.ftml        -l tests/logs/ALsorted.log         "${commonParams[@]}" -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/absgenftml.py -q -t 'Diac (auto)'                          source/masters/ScheherazadeNew-Regular.ufo  tests/Diac-auto.ftml            -l tests/logs/DiacTest1.log        "${commonParams[@]}" -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' & 
tools/absgenftml.py -q -t 'Diac Short (auto)'                    source/masters/ScheherazadeNew-Regular.ufo  tests/Diac-short-auto.ftml      -l tests/logs/DiacTest1-short.log  "${commonParams[@]}" -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/absgenftml.py -q -t 'Subtending Marks (auto)'              source/masters/ScheherazadeNew-Regular.ufo  tests/SubtendingMarks-auto.ftml -l tests/logs/Subtending.log       "${commonParams[@]}" -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/absgenftml.py -q -t 'DaggerAlef (auto)'                    source/masters/ScheherazadeNew-Regular.ufo  tests/DaggerAlef-auto.ftml      -l tests/logs/DaggerAlef.log       "${commonParams[@]}" -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/absgenftml.py -q -t 'Kerning (auto)'                       source/masters/ScheherazadeNew-Regular.ufo  tests/Kern-auto.ftml            -l tests/logs/Kerning.log          "${commonParams[@]}" -s 'url(../results/ScheherazadeNew-Medium.ttf)|Med' -s 'url(../results/ScheherazadeNew-SemiBold.ttf)|SeBld'  -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/absgenftml.py -q -t 'Yehbarree (auto)'                     source/masters/ScheherazadeNew-Regular.ufo  tests/Yehbarree-auto.ftml       -l tests/logs/Yehbarree.log        "${commonParams[@]}" -s 'url(../results/ScheherazadeNew-Bold.ttf)|Bold' &
tools/absgenftml.py -q -t 'Feature-Language Interactions (auto)' source/masters/ScheherazadeNew-Regular.ufo  tests/FeatLang-auto.ftml        -l tests/logs/FeatLang.log         "${commonParams[@]}"  &

wait
echo done.

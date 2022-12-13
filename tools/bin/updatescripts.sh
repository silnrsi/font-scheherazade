#!/bin/sh

# updates tools from ../font-arab-tools/bin

# Copyright (c) 2022 SIL International  (http://www.sil.org)
# Released under the MIT License (http://opensource.org/licenses/

# Requires that we're in the project's root folder, i.e., font-scheherazade
# Assumes the font-arab-tools repo clone is a sibling of font-scheherazade

set -e

if [ ! -e OFL.txt ] 
then
	echo "Please cd to root of font project to use this script"
	exit 2
fi

cp -v ../font-arab-tools/bin/absgen*.py tools/bin
echo done.

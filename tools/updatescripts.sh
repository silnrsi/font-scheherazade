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

for f in absgenftml.py absgenclasses.py
do
	# Update only those scripts that are already in the project:
	[ -e "tools/$f" ] || continue
	if cmp -s "tools/$f" "../font-arab-tools/bin/$f" ; then
		echo "$f is up-to-date"
	else
		echo "Updating $f"
		cp "../font-arab-tools/bin/$f" tools/
		chmod u+x "tools/$f"
	fi
done
echo done.

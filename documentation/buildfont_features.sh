#!/bin/sh

# pandoc -f markdown-smart -s -M testfont="[../results/ScheherazadeNew-Regular.ttf]" -M fontbold="[../results/ScheherazadeNew-Bold.ttf]" -M testsize=12 --metadata-file=source/metadata.yaml --pdf-engine=xelatex -o ScheherazadeNew-font-features.json source/ScheherazadeNew-font-features.md

pandoc -f markdown-smart -F source/pandocfeats.py -s -M testfont="[../results/ScheherazadeNew-Regular.ttf]" -M fontbold="[../results/ScheherazadeNew-Bold.ttf]" -M testsize=12 --metadata-file=source/metadata.yaml --pdf-engine=xelatex -o ScheherazadeNew-font-features.pdf source/ScheherazadeNew-font-features.md

pandoc -f markdown-smart -F source/pandocfeats.py -s -M testfont="ScheherazadeNew-R" -M fontbold="ScheherazadeNew-B" --template=source/template.html -o ScheherazadeNew-font-features.html source/ScheherazadeNew-font-features.md

pandoc -f markdown-smart -F source/pandocfeats.py -s -M testfont="ScheherazadeNew-R" -M fontbold="ScheherazadeNew-B" -o ScheherazadeNew-font-features_mmd.md source/ScheherazadeNew-font-features.md

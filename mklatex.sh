#!/bin/sh

if [ $# -lt 1 ]; then
    echo "Usage: mklatex.sh {latex-file}"
    exit -1
fi

latexmk -e '$pdflatex=q/pdflatex %O -shell-escape %S/' -bibtex -pdf $1

#!/bin/bash

if ! git pull | grep "Already up-to-date." -q; then
  pdflatex -output-directory ~/reason reason.tex
  pdflatex -output-directory ~/reason reason.tex
  pdflatex -output-directory ~/reason reason.tex
fi

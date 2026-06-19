#!/bin/bash
set -e

cd /workspace/CV

pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

ls -la *.pdf

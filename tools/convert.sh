#!/bin/bash

base=$(cd `dirname $0`; pwd)

inp=$1
num=${inp%%.ai}
svg=${num}.svg
svgz=${num}.svgz

echo "$inp -> $svg"

time (
  inkscape ${inp} --export-plain-svg=${num}.orig.svg
  python3 $base/clean.py ${num}.orig.svg > $svg
  inkscape --verb=FitCanvasToDrawing --verb=EditSelectNext --verb=SelectionUnGroup --verb=EditDeselect --verb=EditSelectNext --verb=EditDelete --verb=FileSave --verb=FileQuit $svg
  gzip -9 -c $svg > $svgz
  rm -f ${num}.orig.svg $svg
)


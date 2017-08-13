#!/bin/bash

base=$(cd `dirname $0`; pwd)

for fname in "$@"
do
  out=${fname}.json
  echo "$fname -> $out"
  time $base/get-metadata.py "$fname" > "$out"
done


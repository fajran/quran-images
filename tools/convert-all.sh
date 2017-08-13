#!/bin/bash

base=$(cd `dirname $0`; pwd)

zip=$1
unzip -l $zip | grep ai$ | awk '{ print $4 }' | sort -n > files.txt

cat files.txt | while read file
do
  unzip $zip $file
  $base/convert.sh $file
  rm -v $file
done


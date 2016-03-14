#!/bin/sh
# Lists the n largest directories or files

DFLAGS=""
      
HFLAGS="-10"

while getopts "an:" opt; do
  case $opt in
    a)
      DFLAGS="-a"
      ;;
    n)
      HFLAGS=$OPTARG
      ;;
  esac

done

shift $(($OPTIND -1))

for directory in $@; do
    du -h $DFLAGS $directory 2> /dev/null | sort -hr | head $HFLAGS
done

#!/bin/sh

HFLAGS="10"

while getopts "n:" opt; do
    case $opt in
        n)
          HFLAGS="$OPTARG"
        ;;
        \?) "usage: head.sh
                                    
              -n N Display the first N lines"
              exit 1
        ;;
        esac

done

shift $(($OPTIND -1))

let HFLAGS=$HFLAGS+1

awk "FNR < $HFLAGS"

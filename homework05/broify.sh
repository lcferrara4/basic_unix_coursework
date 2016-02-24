#!/bin/sh
# Get reddit links

DELIM="#"
WFLAGS="off"

ignoreBlank(){
  sed -e "s/[$DELIM].*//" -e 's/[ \t ]*$//' -e 's/^[ \t ]*$//'
}

deleteBlank(){
  sed -e "s/[$DELIM].*//" -e 's/[ \t ]*$//' -e 's/^[ \t ]*$//' -e '/^$/d'
}

while getopts "d:W" opt; do
  case $opt in
    d)
      DELIM=$OPTARG
      ;;
    W)
      WFLAGS="on"
      ;;
    \?)
      echo "usage: broify.sh
              -d DELIM        Use this as the comment delimiter.
               -W              Don't strip empty lines."
      exit 1
      ;;
  esac
done

if [ "$WFLAGS" == "on"  ]; then
  ignoreBlank
elif [ "$WFLAGS" == "off"  ]; then
  deleteBlank
fi

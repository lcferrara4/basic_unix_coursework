#!/bin/sh
# Get reddit links

RFLAGS=""
SFLAGS=""
NFLAGS="-10"

fetchData(){
  curl -s "http://www.reddit.com/r/$subreddit/.json" | python -m json.tool

}


while getopts "rsn:" opt; do
  case $opt in
    r)
      RFLAGS="shuf"
      SFLAGS=""
      ;;
    s)
      SFLAGS="sort -d"
      RFLAGS=""
      ;;
    n)
      NFLAGS="-$OPTARG"
      ;;
  esac
done

shift $(($OPTIND -1))

for subreddit in $@; do

  if [ "$SFLAGS" == "$RFLAGS"  ]
  then
    fetchData | egrep '\"url\": \"http:.*\"' | cut -d"\"" -f4 | head $NFLAGS
  elif [ "$SFLAGS" != "$RFLAGS"  ]
  then
    fetchData | egrep '\"url\": \"http:.*\"' | cut -d"\"" -f4 | $RFLAGS$SFLAGS | head $NFLAGS
  fi  
  
done

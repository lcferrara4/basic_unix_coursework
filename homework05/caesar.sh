#!/bin/sh
# Caesar encryption script

SHIFT=13

CAP='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOW='abcdefghijklmnopqrstuvwxyz'

SET1=$CAP$LOW

makeSet2()
{
  SET2CAP1=$(echo $CAP | cut -b $SHIFT2-26)
  SET2CAP2=$(echo $CAP | cut -b 1-$SHIFT)
  SET2LOW1=$(echo $LOW | cut -b $SHIFT2-26)
  SET2LOW2=$(echo $LOW | cut -b 1-$SHIFT)

  SET2=$SET2CAP1$SET2CAP2$SET2LOW1$SET2LOW2

}


if [ $# -ne 0  ]; then
  shift $((OPTIND-1))
  SHIFT=$@
  if [ "$SHIFT" -gt "26"  ]; then
    let SHIFT=$SHIFT-$SHIFT/26*26;
  fi
fi

let SHIFT2=$SHIFT+1
makeSet2

tr $SET1 $SET2

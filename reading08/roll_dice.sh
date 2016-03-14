#!/bin/sh
#Simulates random dice rolls using shuf

ROLLS="10"
SIDES="6"

while getopts "r:s:" opt; do
  case $opt in
    r)
      ROLLS=$OPTARG
      ;;
    s)
      SIDES=$OPTARG
      ;;
    \?)
      echo "usage: roll_dice.sh
                -r ROLLS        Number of rolls of die (default: 10)
                -s SIDES        Number of sides on die (default: 10)"
      exit 1
      ;;
  esac
done

while [[ $ROLLS -gt 0 ]] ; do
  shuf -i 1-$SIDES | head -1
  let ROLLS=$ROLLS-1
done

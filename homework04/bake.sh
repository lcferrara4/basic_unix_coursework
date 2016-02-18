#!/bin/sh
# Used to compile C files in current directory

SUFFIXES=${SUFFIXES:-".c"}

CC=${CC:-"gcc"}
CFLAGS=${CFLAGS:-"-std=gnu99 -Wall"}

VERBOSE=${VERBOSE:-0}

for X in *$SUFFIXES; do
    
    target=$(basename $X $SUFFIXES)
    $CC $CFLAGS -o $target $X

    if ! $CC $CFLAGS -o $target $X; then
      exit 1
    fi

    if [ $VERBOSE -eq 1 ]; then
      echo ${CC} ${CFLAGS} -o ${target} ${X}
    fi 
done

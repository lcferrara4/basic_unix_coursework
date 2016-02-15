#!/bin/sh
# Prints out what link resolves to

for X in $1/**
  do
    if [ -L $X ] 
      then
        echo $X" links to "$(readlink $X)
    fi
done

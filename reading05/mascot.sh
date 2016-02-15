#!/bin/sh
# Mascot for uname

case $(uname) in
  "Linux" ) echo "Tux"
    ;;
  "Darwin" ) echo "Hexley"
    ;;
  "FreeBSD" ) echo "Beastie"
    ;;
  "NetBSD" ) echo "Beastie"
    ;;
  "OpenBSD" ) echo "Beastie"
esac

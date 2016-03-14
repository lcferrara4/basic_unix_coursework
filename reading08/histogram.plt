#!/bin/sh
# gnuplot script that uses data from results.dat to produce histogram

set terminal png
set output 'results.png'
unset key
set grid
set yrange [0:200]
set xrange [0:7]
set style fill solid 1.00 border 0
set boxwidth 0.95 relative

plot "results.dat" with boxes linecolor rgb "blue"

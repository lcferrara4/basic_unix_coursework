# gnuplot script that uses data from results.dat to produce histogram

set terminal png
set output 'ethnicity.png'
set key left

set grid y
set style data histograms
set style histogram rowstacked
set yrange [0:130]
set xlabel "Year"
set ylabel "# of Students"
set style fill solid 1.00 border -1
set boxwidth 0.75

plot 'ethnicity.dat' using 2 t "Caucasian", '' using 3 t "Oriental", '' using 4 t "Hispanic", '' using 5 t "African American", '' using 6 t "Native American", '' using 7 t "Multiple Selection", '' using 8:xticlabels(1) t "Undeclared"

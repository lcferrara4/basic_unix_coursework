# gnuplot script that uses data from results.dat to produce histogram

set terminal png
set output 'gender.png'
total_box_width_relative=0.6
n=2
set key left
set grid
set xrange [2012.5:2018.75]
set yrange [0:100]
set xlabel "Year"
set ylabel "# of Students"
set style fill solid 1.00 border 100
set boxwidth total_box_width_relative/n relative

plot "gender.dat" u 1:2 w boxes lc rgb "red" title "Female",\
     "gender.dat" u ($1+.3):3 w boxes lc rgb "blue" title "Male"

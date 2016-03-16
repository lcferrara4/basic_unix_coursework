#!/bin/sh
#Get numbers of gender for each year

for i in 1 3 5 7 9 11
do
	let year=i/2+2013;
	echo -n $year
	cut -d',' -f $i demographics.csv | awk '
	BEGIN { F=0; M=0 }
	/F/ { F=F+1 }
	/M/ { M=M+1 }
	END { print "\t"F"\t"M; }
	'
done

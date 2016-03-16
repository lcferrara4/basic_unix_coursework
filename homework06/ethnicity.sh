#!/bin/sh
#Get numbers of ethnicity for each year

for i in 2 4 6 8 10 12
do
        let year=i/2+2012;
        echo -n $year
        cut -d',' -f $i demographics.csv | awk '
        BEGIN { C=0; O=0; S=0; B=0; N=0; T=0; U=0; }
        /C/ { C=C+1 }
        /O/ { O=O+1 }
        /S/ { S=S+1 }
        /B/ { B=B+1 }
        /N/ { N=N+1 }
        /T/ { T=T+1 }
        /U/ { U=U+1 }
        END { print "\t"C"\t"O"\t"S"\t"B"\t"N"\t"T"\t"U; }
        '
done



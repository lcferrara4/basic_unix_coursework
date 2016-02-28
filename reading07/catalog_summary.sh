#!/bin/sh

URL="http://catalog.cse.nd.edu:9097/query.text"

if [ $# -gt 0  ]
then
          URL=$1
fi

curl -s "$URL" | awk '
BEGIN {CPU=0; mach=0; count=0; TYPE=""}
/cpus/ { CPU=CPU+$2  }
/name/ { machines[$2]++  }
/type/ { types[$2]++  }
END {print "Total CPUS: "CPU; 
      
        for (i in machines){
                  mach++

        };
      
      print "Total Machines: "mach;
    
      for (i in types){
        if ( types[i] > count  ){
                          TYPE=i;
                                          count = types[i];
                                                  
        }

      }; 
    
    print "Most Prolific Type: "TYPE}''
        '

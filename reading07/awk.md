TLDR - awk
==========

Overview
--------

awk is a programming language and text processor.



Examples
--------

- Printing specific fields: awk '/field_to_print/'

- Changing FS (the field separator):

sudo awk 'BEGIN { FS=":";  }

{ print $1;  }' /etc/passwd

- Using BEGIN and END, pattern matching, and associative arrays:

awk '

BEGIN {CPU=0; mach=0; count=0; TYPE=""}
/cpus/ { CPU=CPU+$2  } #pattern matching
/name/ { machines[$2]++  } #machines is an associative array
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

print "Most Prolific Type: "TYPE}'

- Using special variables such as NF (number of fields in record) and NR(line number):

awk '{print NR,"->",NF}' student-marks

Resources
---------

- [Awk Guide](https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux)

[git]: https://www.digitalocean.com

- [Manual Page](http://man7.org/linux/man-pages/man1/gawk.1.html)

[git]: http://man7.org

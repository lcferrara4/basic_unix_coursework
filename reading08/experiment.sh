#!/bin/sh
#Simulates 100 dice rolls and uses awk to aggregate output into tsv

./roll_dice.sh -r 1000 | awk '
BEGIN {ONE=0; TWO=0; THREE=0; FOUR=0; FIVE=0; SIX=0}
/1/ { ONE=ONE+1  }
/2/ { TWO=TWO+1  }
/3/ { THREE=THREE+1  }
/4/ { FOUR=FOUR+1  }
/5/ { FIVE=FIVE+1  }
/6/ { SIX=SIX+1  }
END { print "1\t"ONE; }
      print "2\t"TWO;
      print "3\t"THREE;
      print "4\t"FOUR;
      print "5\t"FIVE;
      print "6\t"SIX
      }
' > results.dat

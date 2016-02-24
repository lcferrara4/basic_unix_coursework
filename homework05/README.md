Homework 05
===========

**Activity 1: caesar.sh**

1) SET1 is the same for all inputs. I created a variable called CAP that had all capital letters A-Z.
I also created a variable called LOW that had lower case letters a-z. SET1 is the concatenation of these
two variable, $CAP$LOW.

2) SET2 was constructed using a function called makeSet2(). This was called after all command line arguments
are processed. I made variables SET2CAP1, SET2CAP2, SET2LOW1, and SET2LOW2. These varialbes were constructed using
cut -b and the $SHIFT taken from command line input (default of 13) and then used on $CAP and $LOW. SET2 was 
set equal to the concatenation of these variables.

3) I used the tr (translate) command to do a byte translated from SET1 to SET2 by calling tr $SET1 $SET2.

**Activity 2: reddit.sh**

1) I used egrep to get lines that had url in them. Then I used cut -d with a " delimiter to look at the fourth
section after the double quote. This is where the http started and ended with another ".

2) If either sort or shuffle were set to something other than blank, the egrep, cut commands above were piped into
either sort -d or shuf and then into head. sort -d or shuf were chosen using command line argument and set to
variables called SFLAGS and RFLAGS.

3) Because both -s and -r could be typed into the command line, but only one operation could be performed,
I had to set the other option to "" whenever called. This made it so that the later of the two command line
arguments would be the one chosen. I also had to account for the command line option when neither the -r or -s
flags were given. For this I had to use an if statement that would skip the piping to shuf/sort and go straight to
the piping for head.

**Activity 3: broify.sh**

1) I removed comments using sed -e "s/[$DELIM].\*//". This would remove the text in any lines started with the 
variable $DELIM (comments).

2) I removed empty lines using sed -e '/^$/d'. This would delete the lines starting and ending without anything 
in between.

3) If a -d flag was passed, I simply used $OPTARG to get the new delimiter to set to DELIM. If -W was sent,
I set WFLAGS to "on" instead of "off". The value of WFLAGS was then used in an if statement to call one of two 
different functions. If WFLAGS was on, it would ignore the blank lines so the sed command excluded the argument,
-e '/^$/d'.

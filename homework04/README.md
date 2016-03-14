Homework 04
===========

**bake.sh**

1)

  a) I used parameter expansion to set default values if no command line argument
is given. Otherwise, it sets then equal to the value after the :-. 

  b) Because we are looking through the current directory, I just used 
a for loop that would look for anything matching \*SUFFIXES and do the compiling
for those files.

  c) VERBOSE was set using parameter expansion. As a default, it was set to 0. Using
an if statement I checked to see if VERBOSE was equal to 1. If it was, then I
echoed the compiling statement.

  d) To terminate early if compilation failed I said if the compiling line returned a 0
to exit 1.

2) I prefer make to bake.sh. I like the hierachy/DAG method that make uses to compile
or link all components needed for the compilation process. Using bake was fast and easy
and could help with the ability to change parameters without entering the file though.

**disk_usage.sh**

1)

  a) I parsed the commmand line arguments with getopts using "an:". This took the -a 
flag and set a variable to "-a" if -a was in the command line. It took the argument from 
the -n and set the variable to that number to be used for head.

  b) When there are no line arguments, the default values are taken which is blank for th
a flag and 10 for the nflag.

  c) I moved the command line arguments using shift to where the directories would be 
listed and then had a for loop to go through each directory.

  d) I piped du into sort into head. The du had dflags to specify if files should be
listed. Sort reversed the listing by largest to smallest and head lists only the N items.

2) Using getopts was difficult to figure out. Once I understood how it works, it was okay
but it took a good amount of time and space. This took the most room because of the case
statement, which makes sense.

**taunt.sh**

1)

  a) I handled signals using trap. I would say trap then the function I wanted run
and then the particular signals to trap.

  b) I didn't have long messages but I would've made a variable with the message and then
echoed that with cowsay.

  c) I had a for loop that would count to ten and sleep 1 in each iteration. After this loop,
a function for the timeout was called.

2) Writing shell scripts is easier and faster to execute. C would be more powerful for 
certain things though. I would use shell scripts for things that I needed to run quickly or
to access information about my computer/file system. 

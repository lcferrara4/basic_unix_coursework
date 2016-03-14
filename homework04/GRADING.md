Homework 04 - Grading
=====================

**Score**: 10.25 / 15

Deductions
----------
Activity 1: Task 3:
-1.25	Empty Readme
Activity 2: Task 1:
-0.25 Does not print usage if no arguments given
Activity 2: Task 2:
-1	test_disk_usage.sh does not run successfully
Activity 2: Task 3:
-1.25	Empty Readme
Activity 3: Task 3:
-1	Empty Readme

Comments
--------

test_disk_usage.sh output:
$ test_disk_usage.sh
head: cannot open `10' for reading: No such file or directory
Files - and /tmp/disk_usage.sh.200087/test0 differ
ERROR: ./disk_usage.sh /etc failed

Suggested Fix:
    du ${DFLAGS} ${directory} 2> /dev/null | sort -hr| head -n ${HFLAGS}
For printing usage, add this in the case block
        *)
            echo "usage: $(basename $0) [-n N -a] directory..."
            exit 1
            ;;

And this after shift
if [ $# -eq 0 ]; then
    usage
    exit 1
fi

Correct Readme:
Activity 1: Task 3:
1) a) Should mention either [-z "$VAR"] or parameter expansion
1) b) Should mention loop over glob of $SUFFIXES (ls or find okay) 
1) c) Should mention short circuit evaluation or 'if' check
1) d) Should mention short circuit evaluation or 'if' check
2) bake.sh doesn't require writing anything, make is more flexible and can handle multi-file programs, etc.
Activity 2: Task 3:
1) a) Should mention getopts or some sort of loop
1) b) Should mention checking $# and displaying usage
1) c) Should mention loop and processing pipeline
1) d) Should mention arguments modifying commands in pipeline
2) The command line argument parsing takes up a significant amount of code compared to the actual processing
Activity 3: Task 3:
1) a) Should mention traps and possibly functions
1) b) Should mention here-documents if long messages
1) c) Should mention sleeping multiple times
2) Shell is fast to write, though the language is wonky

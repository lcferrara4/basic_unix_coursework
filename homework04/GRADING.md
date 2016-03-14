Homework 04 - Grading
=====================

**Score**: 13.75 / 15

Deductions
----------
Activity 2: Task 1:
-0.25 Does not print usage if no arguments given
-1	test_disk_usage.sh does not run successfully

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

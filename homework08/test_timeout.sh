#!/bin/bash

FILE="timeout.py"

if ! ( [[ -x "$FILE" ]] ); then
	echo "Im sorry $FILE is not Executable"
	exit 1
fi

if ! ( grep -q "python2.7" $FILE); then
	echo" Sorry that doesnt have the correct she-bang"
	exit 1
fi

var=$( ./timeout.py -h 2>&1 | wc -l)
if ! [ $var -ge 1 ]; then
	echo "No error output!"
	exit 1
fi

for N in 1 2 3 4; do
	./$FILE -t 5 sleep $N 2> /dev/null
	OUT=$?
	if ! [ $OUT -eq 0 ]; then
		echo "Im sorry there is an issue with exiting with sucsess"
		exit 1
	fi
done

for N in 2 3 4 5; do
	./FILE -t 1 sleep $N 2> /dev/null
	OUT1=$?
	if [ $OUT1 -eq 1 ]; then
		echo "Sorry there is an issue with exits if failure"
		exit 1
	fi
done

var1=$( ./timeout.py -v sleep 1 2>&1 | wc -l)
if ! [ $var1 -ge 0 ]; then
	echo "There is a issue with your -v. You arnt printing enough to stderr."
	exit 1
fi

echo "Test Sucessful!"
exit 1

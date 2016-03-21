#!/usr/bin/env python2.7

import sys
import getopt
import os

numbers = False
arg = ""

def usage(status=0):
        print '''usage: uniq.py [-c] files ...

    -c      prefix lines by the number of occurrence'''.format(os.path.basename(sys.argv[0]))
        sys.exit(status)


# Parse command line options

try:
        opts, args = getopt.getopt(sys.argv[1:], "hc")
except getopt.GetoptError as e:
        print e
        usage(1)

for o, a in opts:
        if o == '-c':
                numbers = True
        else:
                usage(2)

if len(args) == 0:
        args.append('-')

previous = ""

uniq = dict()

for path in args:
        if path == '-':
                stream = sys.stdin
        else:
                stream = open(path, "r")

        for line in sorted(stream):
	        if line not in uniq:
        	        uniq[line] = 1
        	else:
                	uniq[line] = uniq[line] + 1
       		previous = line

        stream.close()

for key in uniq:
	if numbers:
		print uniq[key], key,
	else:
		print key,

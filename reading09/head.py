#!/usr/bin/env python2.7

import sys
import getopt
import os

num = 10

def usage(status=0):
        print '''usage: head.py [-n NUM] files ...

    -n NUM  print the first NUM lines instead of the first 10'''.format(os.path.basename(sys.argv[0]))
        sys.exit(status)


# Parse command line options

try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
        print e
        usage(1)

for o, a in opts:
        if o == '-n':
                num = int(a)
        else:
                usage(2)

if len(args) == 0:
        args.append('-')


format = len(args)

for path in args:

        if path == '-':
                stream = sys.stdin
        else:
		if len(args) > 1:
			print "==> %s <==" % path
                stream = open(path, "r")

	count = num

	for line in stream:
		if count > 0:
			print line,
			count = count - 1
		else:
			break


	if format > 1:
		print
		format = format - 1

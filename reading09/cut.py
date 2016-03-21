#!/usr/bin/env python2.7

import getopt
import os
import sys

DELIM = '\t'
FIELDS = None


def usage(status=0):
    	print '''usage: wc.py [-d DELIM -f] files ...

    	-d DELIM  use DELIM instead of TAB for field delimiter
    	-f FIELDS select only these FIELDS'''.format(os.path.basename(sys.argv[0]))
    	sys.exit(status)


# Parse command line options

try:
    	opts, args = getopt.getopt(sys.argv[1:], "hd:f:")
except getopt.GetoptError as e:
    	print e
    	usage(1)

for o, a in opts:
    	if o == '-f':
        	FIELDS = set(a)
		FIELDS.discard(',')
    	elif o == '-d':
		DELIM = a
	else:
        	usage(2)

if len(args) == 0:
    	args.append('-')

if FIELDS == None:
	print "Must have a -f flag"
	usage(4)

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path, "r")

	for line in stream:
		count = 1
		LIST = line.split(DELIM)
		for index in sorted(FIELDS):
			sys.stdout.write(LIST[int(index) - 1])
			if count < len(FIELDS):
				sys.stdout.write(DELIM)
			else:
				print	
			count = count + 1

	stream.close()

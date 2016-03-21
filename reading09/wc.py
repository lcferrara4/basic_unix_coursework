#!/usr/bin/env python2.7

import getopt
import os
import sys

CHARACTERS = False
WORDS = False
LINES = False

def usage(status=0):
    	print '''usage: wc.py [-c -l -w] files ...

    	-c      print the byte/character counts
    	-l      print the newline counts
    	-w      print the word counts'''.format(os.path.basename(sys.argv[0]))
    	sys.exit(status)


# Parse command line options

try:
    	opts, args = getopt.getopt(sys.argv[1:], "hclw")
except getopt.GetoptError as e:
    	print e
    	usage(1)

for o, a in opts:
    	if o == '-c':
        	CHARACTERS = True
    	elif o == '-w':
		WORDS = True
	elif o == '-l':
		LINES = True
	else:
        	usage(2)

if len(args) == 0:
    	args.append('-')

chars = words = lines = 0

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path, "r")
	
	for line in stream:
		lines += 1
		words += len(line.split())
		chars += len(line)

	stream.close()

if CHARACTERS == True:
	print chars
elif WORDS == True:
	print words
elif LINES == True:
	print lines
else:
	usage(3)

#!/usr/bin/env python2.7

import getopt
import os
import sys
import time

# Global Variables

INT = 2

# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)


def usage(status=0):
    	print '''Usage: watch.py [-n INTERVAL] COMMAND

	Options:

    	-n INTERVAL   Specify update interval (in seconds)'''.format(os.path.basename(sys.argv[0]))
    	sys.exit(status)

# Parse command line options

try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
        print e
        usage(1)

count = 1

for o, a in opts:
        if o == '-n':
                try:
			INT = int(a)
		except:
			usage(2)
		count = 3

COMMAND = ' '.join(sys.argv[count:])

while True:
	try:
		print "Every %0.1fs: %s" % (INT, COMMAND)
		print
		os.system(COMMAND)
		print
		time.sleep(INT)
		os.system('clear')
	except KeyboardInterrupt:
		sys.exit(1)

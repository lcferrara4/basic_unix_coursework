#!/usr/bin/env python2.7

import os
import sys
import tempfile
import getopt

# Global Variables

EDITOR = 'vim'


# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)


def usage(status=0):
    	print '''Usage: imv.py FILES...'''.format(os.path.basename(sys.argv[0]))
    	sys.exit(status)

# Parse command line options

try:
        opts, args = getopt.getopt(sys.argv[1:], "h")
except getopt.GetoptError as e:
        print e
        usage(1)

for o, a in opts:
        if o == '-h':
		usage()

temp = tempfile.NamedTemporaryFile(delete=False)

FILES = list(sys.argv[1:])

for item in FILES:
	temp.write(item)
	temp.write('\n')

temp.close()

# Open in EDITOR

try:
	os.system('%s %s' % (EDITOR, temp.name))
except:
	error('Could not open EDITOR')

# Get new names

try:
	newfile = open(temp.name, 'r')
except:
	error('Could not open the temp file.')

NAMES = list()

for line in newfile:
	NAMES.append(line.strip('\n'))

zipped = zip(FILES, NAMES)

for x, y in zipped:
	try:
		os.rename(x, y)
	except:
		exit('Could not rename. Check that files exist.')


os.unlink(temp.name)


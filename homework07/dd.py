#!/usr/bin/env python2.7

import getopt
import os
import sys

# Global Variables

IF = 0
OF = 1

COUNT = sys.maxint
BS = 512
SEEK = 0
SKIP = 0

# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)


def usage(status=0):
    	print '''Unknown argument: -h
	usage: dd.py options...

	Options:

      	if=FILE     Read from FILE instead of stdin
      	of=FILE     Write to FILE instead of stdout

      	count=N     Copy only N input blocks
      	bs=BYTES    Read and write up to BYTES bytes at a time

      	seek=N      Skip N obs-sized blocks at start of output
      	skip=N      Skip N ibs-sized blocks at start of input'''.format(os.path.basename(sys.argv[0]))
    	sys.exit(status)

def open_fd(path, mode):
    try:
        return os.open(path, mode)
    except OSError as e:
        error('Could not open {}: {}'.format(SOURCE, e))

def read_fd(fd, n):
    try:
        return os.read(fd, n)
    except OSError as e:
        error('Could not read {} bytes from FD {}: {}'.format(n, fd, e))

def write_fd(fd, data):
    try:
        return os.write(fd, data)
    except OSError as e:
        error('Could not write {} bytes from FD {}: {}'.format(len(data), fd, e))

# Parse command line options

for command in sys.argv[1:]:
	
	if command.split('=')[0] == 'if':
		IF = command.split('=')[1]
	elif command.split('=')[0] == 'of':
		OF = command.split('=')[1]
	elif command.split('=')[0] == 'count':
		COUNT = int(command.split('=')[1])
	elif command.split('=')[0] == 'bs':
		BS = int(command.split('=')[1])
	elif command.split('=')[0] == 'seek':
		SEEK = int(command.split('=')[1])
	elif command.split('=')[0] == 'skip':
		SKIP = int(command.split('=')[1])
	else:
		usage(1)

# input
if IF != 0:
	      fd = open_fd(IF, os.O_RDONLY)
        os.lseek(fd, SKIP * BS, 0)
else:
	fd = 0

# output
if OF != 1:
        fo = open_fd(OF, os.O_WRONLY|os.O_CREAT)
        os.lseek(fo, SEEK * BS, 0)
else:
        fo = 1

data = read_fd(fd, BS)
counter = 0
while counter != COUNT and data:
	write_fd(fo, data)
	data = read_fd(fd, BS)
	counter += 1

if OF != 1:
	os.close(fo)
if IF != 0:
	os.close(fd)	



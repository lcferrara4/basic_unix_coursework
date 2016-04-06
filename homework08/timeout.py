#!/usr/bin/env python2.7

import os
import sys
import getopt
import time
import signal
import errno

# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)


def usage(status=0):
    	print '''Usage: timeout.py [-t SECONDS] command...

	Options:

      -t SECONDS  Timeout duration before killing command (default is 10 seconds)
      -v          Display verbose debugging output'''.format(os.path.basename(sys.argv[0]))
    	sys.exit(status)

def debug(message, *args):
	if VERBOSE:
		print >>sys.stderr, message.format(*args)

def sigchld_handler(signum, frame):
    debug('Alarm Triggered after {} seconds!', SECONDS)
    try:
        debug('Killing PID {}...', os.getpid() )
        os.kill( pid , signal.SIGTERM)
    except OSError as e:
        error(e)

# Parse command line options

SECONDS = 10
VERBOSE = False

count = 1

try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:v")
except getopt.GetoptError as e:
        print e
        usage(1)

for o, a in opts:
        if o == '-h':
		usage()
	elif o == '-t':
		SECONDS = int(a)
		count = count + 2 
	elif o == '-v':
		VERBOSE = True
		count = count + 1			

COMMAND = sys.argv[count:]
COM = ' '.join(COMMAND)

debug('Executing "{}" for at most {} seconds...', COM, SECONDS)

try:
	debug("Forking...")
    	pid = os.fork()
except OSError as e:# Error
    	error('Unable to fork: {}', e)

if pid == 0:    # Child
    	try:
		debug("Execing...")
        	os.execvp( COMMAND[0], COMMAND) # Alternatively, os.execvp('uname', ['uname', '-a'])
    	except OSError as e:
        	error('Unable to exec: {}', e)
else:           # Parent
    	signal.signal(signal.SIGALRM, sigchld_handler)
    	signal.alarm(SECONDS)
    	debug('Enabling Alarm...')
	
	try:
		debug("Waiting...")
		pid, status = os.wait()
	except OSError as e:
        	if e.errno == errno.EINTR:
            		pid, status = os.wait()
        	else:
            		error(e)

    	debug('Disabling Alarm...')
    	signal.alarm(0)

    	debug('Process {} exited with exit status {}', os.getpid(), status)
    	sys.exit(status)

#!/usr/bin/env python2.7

import os
import sys
import getopt
import time
import signal
import errno
import yaml
import re
import fnmatch

# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)


def usage(status=0):
    	print '''Usage: rorschach.py [-r RULES -t SECONDS] DIRECTORIES...

	Options:

    -r RULES    Path to rules file (default is .rorschach.yml)
    -t SECONDS  Time between scans (default is 2 seconds)
    -v          Display verbose debugging output
    -h          Show this help message'''.format(os.path.basename(sys.argv[0]))
    	sys.exit(status)

def debug(message, *args):
	if VERBOSE:
		print >>sys.stderr, message.format(*args)

def re_match(name, pattern):
	try:
		return re.search(pattern, name)
	except re.error:
		return False

def check_directory(directory, mode):
	for subdir, dirs, files in os.walk(directory):
		for f in files:
			if mode == 0:
				check_file(os.path.join(subdir, f), 0)
			else:
				check_file(os.path.join(subdir, f), 1)	

def check_file(f, mode):
	for p in PATTERN:
		if re_match(f, p):
                        if mode == 0:
                                fill_moddict(f)
                        else:
                                execute_action(f)
		elif fnmatch.fnmatch(f, p):
			if mode == 0:
				fill_moddict(f)
			else:
				execute_action(f)

def fill_moddict(f):
	try:
		statf = os.stat(f)
		mods[f] = statf.st_mtime
	except OSError as e:
		error("Cannot follow path", e)

def execute_action(f):
	if check_newFile(f) or check_moddict(f):
		COMMAND = (ACTION.format(path=f, name=os.path.basename(f))).split()

		try:
        		debug("Forking...")
        		pid = os.fork()
		except OSError as e:# Error
        		error('Unable to fork: {}', e)

		if pid == 0:    # Child
        		try:
                		debug("Execing...")
                		os.execvp( COMMAND[0], COMMAND)
	       		except OSError as e:
                		error('Unable to exec: {}', e)
		else:           # Parent
        		try:
                		debug("Waiting...")
                		pid, status = os.wait()
        		except OSError as e:
                		if e.errno == errno.EINTR:
                        		pid, status = os.wait()
                		else:
                        		error(e)

def check_newFile(f):
	if f in mods.keys():
		return False
	else:
		fill_moddict(f)
		return True

def check_moddict(f):
        try:
                statf = os.stat(f)
		if mods[f] != statf.st_mtime:
			mods[f] = statf.st_mtime
			return True
		else:
			return False
	except OSError as e:
                error("Cannot follow path", e)

# Parse command line options

RULES = '.rorschach.yml'
SECONDS = 2
VERBOSE = False

count = 1
mods = dict()

try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:t:vh")
except getopt.GetoptError as e:
        print e
        usage(1)

for o, a in opts:
        if o == '-h':
		usage()
	elif o == '-r':
		RULES = a
		count = count + 2 
	elif o == '-t':
		SECONDS = int(a)
		count = count + 2			
	elif o == '-v':
		VERBOSE = True
		count = count + 1

DIRECTORIES = sys.argv[count:]
if not DIRECTORIES:
	DIRECTORIES = '.'

# Execution

stream = file(RULES, 'r')
myRules = yaml.load(stream)

for d in myRules:
	PATTERN = d['pattern']
	ACTION = d['action']

for d in DIRECTORIES:
        check_directory(d, 0)

debug('Executing "{}" on new/modified files matching {} every {} seconds...', ACTION, PATTERN, SECONDS)

while True:

	for d in DIRECTORIES:
		check_directory(d, 1)

	try:
		debug('Sleeping...')
		time.sleep(SECONDS)
	except KeyboardInterrupt:
		debug('Exiting program...')
		sys.exit()

Homework 08
===========

**Activity 1 Questions**

1. The parent process had to fork to make the child process and then keeps track of the time with the signal.alarm and wait in order to prevent zombie processes. The child would execute the command specified.

2. The time out method works with signal.signal(signal.SIGALRM, sigchld\_handler) function. This function calls the handler function and checks to see if signal.alarm(SECONDS) has been triggered yet. If it has tries to kill the process. If not, signal.alarm(0) is called and the alarm is disabled, showing that the execution was completed successfully.

3. The test script uses if statements to check that timeout.py is executable, has a she-bang of python2.7, prints the usage message for -h, succeeds when executing ./timeout.py -t 5 sleep N with N=1,2,3,4, succeeds when executing ./timeout.py -t 5 sleep N with N=1,2,3,4, fails when executing ./timeout.py -t 1 sleep N with N=2,3,4,5, and prints debugging information to stderr when -v is sent to the program. This test script explains which if statement fails if and exits if a failure occurs.

4. No you don't always get the same result. I implemented this with a simple shell scripts that would call ./timeout.py -t 2 sleep 2 300 times in a loop. It is not reasonable to expect consistent results, because as shown in class sometimes the parent process forks immediately and sometimes does not.

**Acitivity 2 Questions**

1. I used os.walk in a for loop to go through the directories specified and use os.path.join for the subdirectory and filename. Then these file paths were sent to a separate function check\_file to check each file in the specified directories.

2. I used yaml.load to get a list of dictionaries from the .yaml rule file. Then I went through the dictionaries in this list and set pattern equal to d['pattern'] and action to d['action']. I processed the action in the execute\_action function by using str.format to change {path} to the os.path.join fileName and then {name} to this os.path.basename(path).  

3. I used a dictionary to detect changes to files. The keys were the paths to the files, and the values were the modification times taken from os.stat(path).st\_mtime. I then had a fill this dictionary initially with all the files in the directory and their modification times. Then each time execute\_action was called it would check to see if a new file was created or if a file was modified using two different functions. If they were, these functions would update the modification time dictionary and return True so that the action would be executed. 

4. To execute an action, I would use try/except statements to fork from the parent process. Then if the pid == 0 (it is the child process), I would use os.execvp with COMMAND[0] and the list COMMAND to execute the action specified by the rules.yaml file. If not the child process, the parent would os.wait() to prevent zombie processes.

5. In rorschach.py, I use a while loop that is always True in order to check every however-many seconds. This causes busy waiting. Busy waiting could be avoided by having the program time out after a certain amount of checks. Cache invalidation would come in handy for the storage of modification times. You would have a cache of the modification times and then if a compute node changes a variable, the cached values would be invalidated and then would push new content to a client. 


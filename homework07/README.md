Homework 07
===========

**dd.py**

1. I used a for loop to go through the commands in sys.argv[1:]. I then split the commands at the equal sign. If the first part of this split matched one of the arguments I specified, then I would set the corresponding variable equal to the value of the 2nd part of the split. If the command didn't match any specified, I would call the usage(1) function to return an error message.

2. I opened the input and output files using a function open\_fd. This would try to call os.open(path, mode). If it can't, it prints an error message. For the input file, I used the mode os.O\_RDONLY and for the output file, I used os.O\_WRONLY|os.O\_CREAT to create the file and make it write only. I checked to make sure that I wasn't using stdin or stdout before calling these open\_fd functions.

3. In the same if statements to make sure stdin and then stdout weren't being used, I called os.lseek(fo, SEEK * BS, 0) for the output file to move by SEEK * BS forward in the output file from the beginning and os.lseek(fd, SKIP * BS, 0) to move forward SKIP * BS in the input file before writing to output.

4. To handle bs and count, I had a while loop and a counter. I would call the function read\_fd(fd, BS) to read the number of bytes specified by bs from the input data. I initially set a counter to 0. Then I entered a while loop that would keep going as long as counter doesn't equal the count given in the command line arguments and data isn't empty (meaning it reached the end of the file). In this while loop, it writes the data variable to the output, reads more data to the data variable, and increments counter.
                              
**find.py**

1. I created an empty list. I then had a for loop to go through the arg in sys.arv[2:] to skip the command itself and the directory. I then checked to see if the arg started with a '-'. If it does, I split the arg at the '-' and set the arg to the index 1 field of the split. If this was h, I printed a help usage message. If not, I appended this to the list. If arg[0] does not equal '-', I appended to the list as well.

I then sent a counter equal to 0 and entered a while loop for while count is less than the length of the list. If args[count] matched given fields, I would set the corresponding variable either to true or to args of count+1. If I did the latter, I incremented count. If it did not match anything, I printed an error messaged using usage(). I incremented count at the end of the loop.

2. I used os.walk to walk through the given directory. I set followlinks equal to true to follow symlinks as well. I did this in a for loop that would take root, dirs, and files for each thing in os.walk.

3. Then in the for loop described above, I had another for loop to take the name of dirs + files. I then set a variable called stream to os.path.join(root,name) to combine root, directory, and file names. I passed this value to a function include. If include returns true, I print the filesystems objects path. 

The include function has if statements to check if each of the command line variables have changed from their initial values. If they have changes, the function checks whether the specified path meets the requirements for that condition. If it does not, the function returns false. If it gets to the bottom of the include function, it returns true and the filesystems objects path will be printed.

It begins by setting up a variable called broken and giving it the value False. It then has a try/except statement that tries to set variable statinfo to os.stat(path). If this gives an operating system error, statinfo is set to os.lstat(path) instead and then broken is set to true. The type arguments are handled with os.path.isfile(path) for type f and os.path.isdir(path) for type d. Executable, readable, and writable are handles with os.access with mode os.X\_OK, os.R\_OK, and os.W\_ok respectively. Empty returns false when it is a link and broken is true, when it is a file and statinfo.st\_size is not 0 and when it is a directory with a non-empty os.listdir. The directory option must be handled with a try/except for os.listdir. If calling this function gives an operating system error, it returns false as well. Name and path are handled with fnmatch, except name uses the os.path.basename function. Regex is handled with re.search. Perm, newer, uid, and guid are all handled with information taken from the statinfo variable.

4. There are many more calls to stat by my find.py than by find. I found this by running strace -c ./find.py /etc and strace -c find /etc. And find does not call lstat at all. The strace call on find lists more calls to newfstatat. I could not find how this command works but it seems that maybe find uses this to get file information.

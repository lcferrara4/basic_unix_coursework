Homework 03
===========

**Activity 01: Make It**


1. a.) The shared library is bigger because it needs to be able to be shared with multiple executables so it needs more commands.

b.) gcd-static is much bigger than gcd-dynamic. Static executables are faster for startup but they are much bigger because they must include all libraries.


2. ldd gcd-dynamic shows that gcd-dynamic depends on linux-vdso.so.1, libgcd.so, libc.so.6, and /lib64/ld-linux-x86-64.so.2. Because gcd-static is a static executable, it does not depend on the presence of libraries at runtime. Instead, these are included in the executable itself.


3. No. Had to use setenv LD\_LIBRARY\_PATH . first so that it would know to look in the current directory for the shared library.


4. Static linking is faster but takes more space. Dynamic linking is the default because it is easier to update files made by dynamic linking, because can just update library, not each static link. If I created an application, I would dynamically link the executables so that I could update the application easily.


**Activity 02: Fix It**


1. wget https://www3.nd.edu/~pbui/teaching/cse.20189.sp16/static/tar/is\_palindrome.tar.gz

tar -xzvf is\_palindrome.tar.gz


2. -g -gdwarf-2
These flags increase the size of the executable.
With this flag,
laurens-mbp:is\_palindrome Lauren$ ls -l -h
total 40
-rw-r--r--  1 Lauren  staff   219B Feb  4 20:18 Makefile
-rw-r--r--  1 Lauren  staff   3.9K Feb  4 20:09 is\_palindrome
-rw-r--r--@ 1 Lauren  staff   985B Jan 31 13:35 is\_palindrome.c
-rw-r--r--@ 1 Lauren  staff    27B Jan 31 13:26 is\_palindrome.input
-rw-r--r--@ 1 Lauren  staff    99B Jan 31 13:26 is\_palindrome.output

Without the flags,
laurens-mbp:is\_palindrome Lauren$ make clean
rm -f is\_palindrome \*.o
laurens-mbp:is\_palindrome Lauren$ make
gcc -c -Wall -std=c99 is\_palindrome.c -o is\_palindrome
laurens-mbp:is\_palindrome Lauren$ ls -l -h
total 40
-rw-r--r--  1 Lauren  staff   219B Feb  4 20:18 Makefile
-rw-r--r--  1 Lauren  staff   1.7K Feb  4 20:19 is\_palindrome
-rw-r--r--@ 1 Lauren  staff   985B Jan 31 13:35 is\_palindrome.c
-rw-r--r--@ 1 Lauren  staff    27B Jan 31 13:26 is\_palindrome.input
-rw-r--r--@ 1 Lauren  staff    99B Jan 31 13:26 is\_palindrome.output

Adding these flags makes the executable have more information about the source code (such as line numbers) so that the debugger can give detailed error messages. This makes the executable much bigger.


3. gdb is\_palindrome
r < is\_palindrome.input
I got a segmentation fault.
bt to backtrace to where the segfault occurred. Got line 41 in is\_palindrome.c
The error occurs because buffer tries to access beyond bufsiz with fgets causing an invavlid memory access that makes the program crash. To fix this, I changed the declaration of buffer to char buffer[BUFSIZ] to fix this problem.


This fixed the segmentation fault.


I then used q to exit the gdb, recompiled, and did gdb and ran again.
This time the program ran all the way, but still gave the wrong output.
I then used valgrind --leak-check=yes is\_palindrome < is\_palindrome.input to look for memory leaks. I got a lot of errors saying invalid read, meaning that I was trying to read from memory that doesn't exist.
This was happening at lines 44-45. I changed     const char \*back  = s + strlen(s); to const char \*back  = s + strlen(s) - 1; so that back would point to the last character in the string, not to the null character.


This fixed the invalid memory access.


When running valgrind, I also got a summary saying:
==21013== LEAK SUMMARY:
==21013==    definitely lost: 50 bytes in 8 blocks
I put free(sanitized); at the end of the while loop in the main function to free the memory allocated to sanitized in each iteration. Then running valgrind --leak-check=yes is\_palindrome < is\_palindrome.input said that no leaks were possible because all memory was freed.


This fixed the memory leaks. 

I also added \*writer = \*reader; // adds the null character to the end after the while loop breaks in the function.

4. I had the toughest time debugging the invalid memory access( s + strlen(s) ) pointing to the null character. This was difficult because the error I got was just in the output differing from is\_palindrome.output. The best thing to know here is how C-strings work and to double check when calling to indexes of C-strings. I put breakpoints at each of these calls so I could step through the program and double check by bounds.

**Activity 03: Trace It**

1. Contacting the COURIER:

He said: Did you put the package for the right place?

2. Finding the package location:

strace -e stat /afs/nd.edu/user15/pbui/pub/bin/COURIER

to see what the courier what trying to contact. I saw the following as the last stat call:

stat("/tmp/lferrara.deaddrop", 0x7fff2fcf73b0) = -1 ENOENT (No such file or directory)

3. Creating such a file:

cd /tmp/
vim lferrara.deaddrop

4. Try contacting courier again:

Now he says Whoa whoa... you can't give everyone access to the package! Lock it down!

That makes me think I need to change the permissions.

5. Changing the permissions:

chmod 600 lferrara.deaddrop

Then contact courier and he says, What are you trying to pull here? The package is the wrong size! 

6. Check strace again:

clone(child\_stack=0, flags=CLONE\_PARENT\_SETTID|SIGCHLD, parent\_tidptr=0x7fff6a391da8) = 3411
wait4(3411,  \_\_\_\_\_\_\_\_

7. Type in file to get size to adjust.

8. Check with courier again.

	he got the package and will pass it on.

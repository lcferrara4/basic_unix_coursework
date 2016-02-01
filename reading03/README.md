Reading 03
==========

Part 2:

1. strings -a /bin/ls

2. ldd /bin/ls

3. strace ls

4. gdb hello-debug  // opens GDB with file hello-debug
- r // runs the program
- Can use next or step to run little at a time
- Can set breakpoints or watch points
- q // quits gdb

5. valgrind --leak-check=yes hello-dynamic

6. gprof hello-profile > hello.output
- Look at % of execution time and calls
- Helps to determine bottlenecks (parts of code that take the longest to run

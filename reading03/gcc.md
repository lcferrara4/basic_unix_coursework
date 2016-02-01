TLDR - gcc
==========

Overview
--------

gcc is a C and C++ compiler. It has a 4 step process: preprocessing, compiling, assembling, and linking.

Examples
--------

- Create a dynamic executable: gcc myprogram.c -o myprogram

- Create a static executable: gcc -static myprogram -o myprogram

- Compile but do not link: gcc -c myprogram.c

- Compile with debugging: gcc -g myprogram.c -o myprogram-debug

- Compile with profiling: gcc -pg myprogram.c -o myprogram-profile

Resources
---------

- [GCC and Make](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)

[git]: https://www3.ntu.edu.sg

- [Examples](http://pages.cs.wisc.edu/~beechung/ref/gcc-intro.html)

[git]: https://pages.cs.wisc.edu

- [Manual Page](http://man7.org/linux/man-pages/man1/gcc.1.html)

[git]: http://man7.org

TLDR - make
==========

Overview
--------

make command automates the process of bulding an executable using the makefile.

Examples
--------

- Type make in command line if makefile exists.

- Example makefile:

all: hello

hello: main.o factorial.o hello.o
    g++ main.o factorial.o hello.o -o hello

main.o: main.cpp
    g++ -c main.cpp

factorial.o: factorial.cpp
    g++ -c factorial.cpp

hello.o: hello.cpp
    g++ -c hello.cpp

clean:
    rm *o hello

Resources
---------

- [Makefiles](http://mrbook.org/blog/tutorials/make/)

[git]: https://mrbook.org

- [GCC and Make](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)

[git]: https://www3.ntu.edu.sg

- [Manual Page](http://man7.org/linux/man-pages/man1/make.1.html)

[git]: http://man7.org

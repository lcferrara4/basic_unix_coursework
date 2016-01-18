TLDR - nice
============

Overview
--------

[nice] is used to run a process with adjusted niceness (priority). This changes the scheduling for the process. Niceness ranges from -20 (most favorable to the process) to 19 (least favorable to the process).

Examples
--------

To display the default niceness of a new processes,

nice

To increment the niceness of the pico process on myfile.txt by 13,

nice -n13 pico myfile.txt // This becomes a low priority process, but not the lowest

Resources
---------

- [nice command Tutorial](http://www.computerhope.com/unix/unice.htm)

[git]: https://computerhope.com/

- [Manual Page](https://http://man7.org/linux/man-pages/man1/nice.1.html)

[git]: https://man7.org

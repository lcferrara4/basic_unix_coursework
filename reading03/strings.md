TLDR - strings
==========

Overview
--------

strings displays the printable characters in files (mainly useful for non-text files). By default, it prints sequences that are at least 4 characters long.

Examples
--------

- Show all contents: strings -a myfile

- To search for groups of 2 printable characters instead: strings -n 2 myfile

- To put a file from the local machine into the remote machine:

- To find specific strings in file: strings myfile | grep target

Resources
---------

- [String examples](http://www.thegeekstuff.com/2010/11/strings-command-examples/)

[git]: https://www.thegeekstuff.com

- [Manual Page](http://man7.org/linux/man-pages/man1/strings.1.html)

[git]: http://man7.org

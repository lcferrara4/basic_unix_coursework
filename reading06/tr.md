TLDR - tr
==========

Overview
--------

tr deletes or translates stdin from one form to another using set classes

These classes are:

- alnum - alphanumeric characters
- alpha - alphabetic characters
- blank - whitespace characters
- cntrl - control characters
- digit - numeric characters
- graph - graphic characters
- lower - lower-case alphabetic characters
- print - printable characters
- punct - punctuation characters
- space - space characters
- upper - upper-case characters
- xdigit - hexadecimal characters

Examples
--------

- echo "Who is the standard text editor?" |tr [:lower:] [:upper:]

WHO IS THE STANDARD TEXT EDITOR?

- echo 'ed, of course!' |tr -d aeiou

d, f crs!

Resources
---------

- [Intro to Text Manipulation](http://www.ibm.com/developerworks/aix/library/au-unixtext/)

[git]: https://www.ibm.com

- [Manual Page](http://man7.org/linux/man-pages/man1/tr.1.html)

[git]: http://man7.org

TLDR -  ps                               
============

Overview
--------

[ps] shows a snapshot of active processes. This information includes the PID, TTY, time, and command of each process.

Examples
--------

To show all processes for the same effective user ID,

ps

To print only the name of PID 42,

ps -q 42 -o comm=

Resources
---------

- [How to use ps, kill, and nice to manage processes](https://www.digitalocean.com/community/tutorials/how-to-use-ps-kill-and-nice-to-manage-processes-in-linux)

[git]: https://digitalocean.com/

- [Manual Page](https://http://man7.org/linux/man-pages/man1/ps.1.html)

[git]: https://man7.org

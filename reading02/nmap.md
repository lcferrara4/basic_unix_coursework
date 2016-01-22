TLDR - nmap
============

Overview
--------

nmap is used to identify systems and services of a network.

The syntax is nmap [Scan Type...] [Options] [target specification]

Examples
--------

To scan for open ports,

nmap [IP address] such as nmap 192.168.0.0/24

To identify the operating system of a host,

nmap -O [IP address]

For a verbose scan with insight into what nmap is doing,

nmap -T4 -A -v [IP address]

Resources
---------

- [How to use nmap](https://www.garron.me/en/go2linux/nmap-command-graph-front-end-port-scan.html)

[git]: https://www.garron.me

- [10 important nmap commands](http://bencane.com/2013/02/25/10-nmap-commands-every-sysadmin-should-know/)

[git]: https://bencane.com

- [Manual Page](https://http://man7.org/linux/man-pages/man1/nmap.1.html)

[git]: https://man7.org 

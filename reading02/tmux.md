TLDR - tmux
============

Overview
--------

tmux is a tool to show multiple separate terminal sessions inside a signle window. It also allows the user to execute a persistent shell session to detach/re-attach to.

tmux has the shortcut Ctrl-b

Examples
--------

- To show sessions,

Ctrl-b s or tmux ls

- To create a new session with a name,

tmux new -s session-name

- To reattach to an existing session,

tmux a -t session-name

- To detach,

Ctrl-b d or tmux detach

- To kill a session,

tmux kill-session -t session-name

Resources
---------

- [To learn more about adding windows/panes](https://danielmiessler.com/study/tmux/)

[git]: https://danielmiessler.com

- [Manual Page](https://http://man7.org/linux/man-pages/man1/tmux.1.html)

[git]: https://man7.org 

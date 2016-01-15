TLDR - git
==========

Overview
--------

[Git] is a distributed version control system.

Examples
--------

- **Clone** a remote *repository*:

        $ git clone git@bitbucket.org:CSE-20189-SP16/assignments.git

- **Add** to add any new or modified files to the index

	$ git add *.c
	$ git add LICENSE
	$ git commit -m 'initial project version'

- **Status** to obtain a summary of which files have changes that are staged for the next commit

	$ git status

- **Diff** to see what is still unstaged

	$ git diff

- **Remove** to remove a file from Git and remove the file from your working directory

	$ git rm PROJECTS.md

Resources
---------

- [Pro Git](https://git-scm.com/book/en/v2)

[git]: https://git-scm.com/

- [Code School: Try Git](https://try.github.io/levels/1/challenges/1)

[git]: https://try.github.io/

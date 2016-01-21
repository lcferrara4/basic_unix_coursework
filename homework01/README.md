Homework 01
===========

**Exercise 01: Paths**

1. cd /afs/nd.edu/user14/csesoft

2. cd ../../user14/csesoft

3. cd ~csesoft

4. ln -s /afs/nd.edu/user14/csesoft csesoft

**Exercise 02: Coping, Moving, Removing**

1. cp -a /usr/share/pixmaps/. images

2. *find images -type l -xtype l* tells which symlinks in the images directory are broken. They are broken because the cp command copied all the symlinks that were created but did not copy the files they pointed to. The path to the files are now different. cp -RP would have fixed this problem.

3. time mv images pixmaps

4. time mv pixmaps /tmp/lferrara-pixmaps
Yes, this operation is slower, because the last question simply renames the directory. In this questions, the directly must be removed from one location and put into another.

5. time rm -rf /tmp/lferrara-pixmaps
This is the remove rather than the move command. It takes less time than the move in the previous question.

**Exercise 03: Files and Directories**

1. ls -l -sh /afs/nd.edu/user37/ccl/software

2. ls -lhat /afs/nd.edu/user37/ccl/software

3. 1937 files
cd /afs/nd.edu/user37/ccl/software/cctools/x86\_64
find . -type f | wc -l

4. Yes! 
cd /afs/nd.edu/user37/ccl/software/cctools/x86\_64
find . -name "weaver" -executable -type f

5. 77M	redhat5 
cd /afs/nd.edu/user37/ccl/software/cctools/x86\_64
du -hsx * | sort -n -r 

6. 768
find ./redhat5 -type f | wc -l

7. parrot\_run\_hdfs    18534130 M
find . -printf '%s %p\n'| sort -nr | head -1

8. 1937 files
find /afs/nd.edu/user37/ccl/software/cctools/x86\_64/ -type f -mtime +30 | wc -l

**Exercise 04: Unix Permissions**

1. Who can read from that file? User (me) and group
Who can write to that file? User (me)
Who can execute that file? User (me), group, and world (other)

2. a. chmod 600 data.txt
   b. chmod 770 data.txt
   c. chmod 444 data.txt
   d. chmod 777 data.txt

3. The permissions set on the enclosing directory of the file affect who can delete it, not the permissions on the file itself.

**Exercise 05: AFS Permissions**

1. My home directory:
  	system:administrators rlidwka
  	system:anyuser l
  	lferrara rlidwka

This means that system administrators have all seven standard permissions (read(r), lookup(l), insert(i), delete(d), write(w), lock(k), and administer(a). Any user has permission to lookup, meaning that can call commands ls, ls -ld, and fs listacl. I (lferrara) have all seven standard permissions as well.

My private directory:
	system:administrators rlidwka
	lferrara rlidwka

This means that system administrators and I have all seven standard permissions. Any other user has no permissions.

My public directory:
	system:administrators rlidwka
	system:anyuser rlk
	lferrara rlidwka

This means that system administrators and I have all seven standard permissions. Any other user has permissions to read, lookup, and lock.

2. /afs/nd.edu/commons has Unix permissions drwxrwxrwx, so the owner, groups, and others have Unix permissions to read, write, and execute. However, when I call *touch /afs/nd.edu/common/lferrara.txt*, the following error message occurs:
touch: cannot touch `/afs/nd.edu/common/lferrara.txt': Read-only file system

This occurs because the ACL permissions must be different, making it so that my ACL permissions for this directory are to lookup, but not to insert (add new files).

3. fs setacl <directory> pbui rlidwka system:administrators '' system:anyuser ''
where <directory> is the name of the folder in my home directory

**Exercise 06: Masks**

1. The permissions for world1.txt is rw-rw-rw-, meaning that the owner, groups, and others can all read and write.

2. The permissions for world2.txt is rw-r--r--, meaning that the owner can read and write, while the groups and others can only read.

3. The permissions for world3.txt is rw--w--w-, meaning that the owner can read and write, while the groups and others can only write.

Therefore, the permissions on each of these files is the same for the owner, but different for the groups and others. The umask command defines the default permissions for newly created files. Files have the base permissions of 666, meaning that all users have read and write access. The numbers after a call to umask are the difference between the base permissions and the permissions you want. For example, for world1.txt, nothing was changed so 000 was used, but for world2.txt, 022 reflected that the permissions wanted were 644, with 6 being read and write and 4 being only read. Unless umask is defined in the .bashrc file, they will only apply to the current shell. This can be helpful when creating many files that all need the same permissions.

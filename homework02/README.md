Homework 02
===========

**Activity 01: Transferring Files**

1. Creating workspace, file, and links
# Create workspace on source machine: The ssh command allows me to access the source machine. The mkdir command creates the needed folder.
ssh lferrara@student01.cse.nd.edu
mkdir /tmp/${USER}-workspace

# Generate 10MB file full of random data in the source machine in the directory created, specified by of=/tmp/${USER}-workspace/10MB with 10MB as the file name.
dd if=/dev/urandom of=/tmp/${USER}-workspace/10MB bs=10M count=1

# Create 10 hard links to 10MB file. This can be verified by typing ls -l /tmp/${USER}-workspace -hr to see the file and hard links with sizes in human-readable format.
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data0
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data1
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data2
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data3
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data4
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data5
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data6
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data7
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data8
ln /tmp/${USER}-workspace/10MB /tmp/${USER}-workspace/data9

# Create workspace on target machine. Gives access to a second student machine, the target, and makes the directory here as well.
ssh lferrara@student01.cse.nd.edu
mkdir /tmp/${USER}-workspace

2. Running du -h /tmp/${USER}-workspace shows that the /tmp/${USER}-workspace folder of the source machine has 11M total disk usage. This makes sense because the hard links do not take much space at all, but there is still some overhead for bookkeeping, bringing the disk usage to 1M more than the 10M file of random data.

3. 101M. This is much more than the 11M in the source directory. On the source machine, the hard links are just pointers to the same inode so you have 1 copy of the original random data so that is 10M + some overhead for bookkeeping. When you transfer the files from the source to the target, the target doesn't know anything about the inodes, so it treats each data file as a new file.

4. Transfering data:
# Transfer data files using scp
scp /tmp/${USER}-workspace/data\* lferrara@student03.cse.nd.edu:/tmp/${USER}-workspace

# Transfer data files using sftp
sftp lferrara@student03.cse.nd.edu < transfer.txt

# In transfer.txt,
lcd /tmp/lferrara-workspace
cd /tmp/lferrara-workspace
put data\*
bye

# Transfer data files using rsync
rsync -avz /tmp/${USER}-workspace/data\* lferrara@student03.cse.nd.edu:/tmp/${USER}-workspace

5. scp and sftp transfer every single file. rsync only transfers files with changes. This can make transfers more efficient. It also is a good feature to use when trying to keep files in two directories the same.

6. I like rsync. It is really easy to use (don't have to make a file and the command arguments make sense), and I like the idea of keeping my directories synced. I could imagine this would be useful in a lot of situations. 

**Activity 02: Talk to the Oracle**

1. Scan `xavier.h4x0r.space` for HTTP port:

        nmap -Pn -p 9000-10000 xavier.h4x0r.space
        
Starting Nmap 5.51 ( http://nmap.org ) at 2016-01-27 21:45 EST
Nmap scan report for xavier.h4x0r.space (129.74.161.24)
Host is up (0.00041s latency).
Not shown: 997 closed ports
PORT      STATE    SERVICE
9097/tcp  open     unknown
9111/tcp  open     DragonIDSConsole
9876/tcp  open     sd
10000/tcp filtered snet-sensor-mgmt

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds

    As you can see here, there are 3 open ports in the 9000 - 10000 range.
    To check if the port was a HTTP server, I next used the X command...

2. Access HTTP server:

        curl 129.74.161.24:9097
        Output: The output was an index.html file

	curl 129.74.161.24:9111
	A message with elephant inside an ASCII snake.

		Says name is GET / HTTP/1.1

		Gives message:

		| User-Agent: curl/7.19.7                 |
		| (x86\_64-redhat\-linux\-gnu)               |
		| libcurl/7.19.7 NSS/3.15.3 zlib/1.2.3    |
		| libidn/1.18 libssh2/1.4.2     
	
	wget 129.74.161.24:9111
	--> oddly gets a slightly different message with a dragon.
		
		Says name is GET / HTTP/1.0

		Gives message:

		User-Agent: Wget/1.12 (linux-gnu) 	


	Both redirect you to the SLEEPER or the DOORMAN

	curl 129.74.161.24:9876
	A message from darth vader koala saying:
		If you seek the ORACLE, you must query  |
		| the DOORMAN at /{netid}/{passcode}!     |
		|                                         |
		| To retrieve your passcode you must      |
		| decode the file at                      |
		| ~pbui/pub/oracle/${USER}/code using the |
		| BASE64 command. 

4. Decode the file using BASE64 command:

	base64 -d ~pbui/pub/oracle/${USER}/code

	Output: badda9e106d686273623bc08f2d03271

5. Query the doorman at /{netid}/{passcode}:

	wget xavier.h4x0r.space:9876/lferrara/badda9e106d686273623bc08f2d03271

6. Open new file to see message:

	vim badda9e106d686273623bc08f2d03271

	Output: A message from cow operation saying,

| The ORACLE looks forward to talking to  |
| you, but you must first retrieve a      |
| secret message from the SLEEPER.        |
|                                         |
| He can be found in plain sight at       |
| ~pbui/pub/oracle/SLEEPER... You will    |
| need to wake him up and then signal him |
| to HANGUP his connection. If he         |
| recognizes you, he will give you the    |
| message in coded form.                  |
|                                         |
| Once you have the message, proceed to   |
| port 9111 and deliver the message to    |
| the ORACLE.                             |

7. Move to the proper directory so I can run SLEEPER in the background:

	cd ~pbui/pub/oracle/

8. Run sleeper in background:

	SLEEPER &

9. Find the PID and HANGUP (using kill -1)

	ps
PID TTY          TIME CMD
27468 pts/16   00:00:00 csh
29786 pts/16   00:00:00 SLEEPER
29794 pts/16   00:00:00 sleep
29796 pts/16   00:00:00 ps

	kill -1 29786

	Output:
/ Hmm... I recognize you lferrara...     \
| Here's the message you need to give to |
| the ORACLE:                            |
|                                        |
\ eXNyZWVuZW49MTQ1Mzk1MjAxNg==           /

10. Deliver the message to the oracle:

	telnet xavier.h4x0r.space 9111

Ouput and input:
Name? lferrara
Message? eXNyZWVuZW49MTQ1Mzk1MjAxNg==

Congrats! Lots of fun output!

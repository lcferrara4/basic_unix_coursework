Reading 06
==========

1) tr [:lower:] [:upper:]

2) cat /etc/passwd | grep ^root | cut -d":" -f7

3) echo "monkeys love bananas" | sed -e 's/monkeys/gorillaz/g'

4) cat /etc/passwd | sed -e 's/\/bin\/.\*sh/\/usr\/bin\/python/g' | grep python

5) echo "     monkeys love bananas" | sed 's/^[ \t ]\*//'

6) cat /etc/passwd | grep ':4\w\*7:'

7) tail -f logfile1 logfile2

8) comm -12 file1 file2

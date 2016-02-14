is_palindrome: is_palindrome.o
	gcc -o $@ $^

is_palindrome.o: is_palindrome.c
	gcc -o $@ -c -Wall -std=gnu99 -g -gdwarf-2 $^

test: is_palindrome is_palindrome.input is_palindrome.output
	is_palindrome<is_palindrome.input | diff -s - is_palindrome.output

clean:
	rm -f is_palindrome *.o

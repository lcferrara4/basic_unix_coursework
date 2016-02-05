CC=		gcc
CFLAGS=		-fPIC -Wall -std=c99 -g -gdwarf-2
LD=		gcc
LDFLAGS=	-lgcd
AR=		ar
ARFLAGS=	rcs
TARGETS=	gcd-static gcd-dynamic libgcd.a libgcd.so 

all:	$(TARGETS)

gcd-static: main.o libgcd.a
	$(LD) -static -o $@ -L. $^ $(LDFLAGS)

gcd-dynamic: main.o libgcd.so
	$(LD) -o $@ -L. $^ $(LDFLAGS)

libgcd.a: gcd.o
	$(AR) $(ARFLAGS) $@ $^

libgcd.so: gcd.o
	$(CC) -shared -o $@ $^

%.o: %.c
	$(CC) -c $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGETS) *.o

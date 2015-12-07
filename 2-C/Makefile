ifeq (${CC},)
	CC = gcc
endif

all: main

main: main.o functions.o
	${CC} -o $@ $^ -lm

%.o: %.c functions.h
	${CC} -c -o $@ $<

clean:
	rm -f main.o functions.o

mrproper: clean
	rm -f main

.PHONY: all clean mrproper

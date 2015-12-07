SRC = $(wildcard src/*.c)
OBJ = $(patsubst src/%.c,build/%.o,${SRC})
CFLAGS = -std=c99 -Wall -Wextra

all: main

build:
	mkdir $@

main: ${OBJ}
	${CC} -o $@ $^ ${LDFLAGS}

build/%.o:
	${CC} -c -o $@  ${CPPFLAGS} ${CFLAGS} $<

build/%.d: src/%.c build
	${CC} ${CPPFLAGS} ${CFLAGS} -MM -MT $(patsubst src/%.c,build/%.o,$<) $< > $@

clean:
	rm -rf build

include $(patsubst src/%.c,build/%.d,${SRC})

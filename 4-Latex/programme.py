from __future__ import print_function


def r(a, *b):
    q = lambda t: '"' + t + '"'
    for d in b:
        print("   ", q(d), "->", q(a), ';')


if __name__ == "__main__":
    print("digraph make {")
    r("main.c", "stdio.h", "fonctions.h")
    r("fonctions.c", "math.h", "fonctions.h")
    for obj in ['main', 'fonctions']:
        r(obj+".o", obj+".c")
    r('main', 'main.o', 'fonctions.o')
    print("}")

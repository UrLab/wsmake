from __future__ import print_function


def rule(target, *deps):
    quoted = lambda text: '"' + text + '"'
    for dep in deps:
        print("   ", quoted(dep), "->", quoted(target), ';')


if __name__ == "__main__":
    print("digraph make {")
    rule("main.c", "stdio.h", "fonctions.h")
    rule("fonctions.c", "math.h", "fonctions.h")
    for obj in ['main', 'fonctions']:
        rule(obj+".o", obj+".c")
    rule('main', 'main.o', 'fonctions.o')
    print("}")

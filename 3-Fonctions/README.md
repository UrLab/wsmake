# Fonctions make

## Exercice 1

* Écrire un Makefile pour creer l'exécutable `main`.
* Exécuter main

## Exercice 2

* Rajouter la ligne suivante dans `src/special_letters.h`:

```c
#define ellipsis() dot();dot();dot()
```

* Recompiler avec make. Cela fait-il quelque chose ? _(Si les dépendances de headers sont bien gérées, il devrait se passer quelque chose)_

## Exercice 3

En fait, il est aussi possible de compiler en une seule fois, en utilisant
`gcc src/*.c`.

* Rajouter une règle dans le Makefile, qui tient compte des dépendances, pour compiler un exécutable `main_single` en une seule invocation de `gcc`, et compiler.
* Modifier un des fichiers `.c` (rajouter une ligne vide par exemple) et recompiler. Qu'observe-t-on comme avantage dans la compilation des fichiers séparée ?


# Rappels

* Fonctions make: [documentation Make](https://www.gnu.org/software/make/manual/html_node/Text-Functions.html)
* Création des fichiers de dépendances avec GCC: [documentation GCC](http://gcc.gnu.org/onlinedocs/gcc-4.4.1/gcc/Preprocessor-Options.html#index-dependencies_002c-make-823)

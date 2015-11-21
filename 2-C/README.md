# Introduction à la compilation C/C++
## Exercice 1

* Écrire un Makefile pour creer l'exécutable `main`.
* Exécuter main
* Modifier `functions.c` (ajouter une ligne vide par exemple), recompiler. Que se passe-t-il ? Pourquoi ?
* Même chose avec `functions.h`

## Exercice 2

Rajouter une règle `clean` pour nettoyer les fichiers intermédiaires. Rajouter une règle `mrproper` pour effacer tous les produits de compilation.

## Exercice 3

Créer une règle pour produire l'archive `projet.zip`, qui ne contient que les fichiers nécessaires à la remise du projet (à votre avis: lesquels ?).

# Rappels

* Supprimer un fichier: `rm fichier`. Si on veut forcer la suppression (la commande n'échoue pas si le fichier n'existe pas par exemple), on peut utiliser `rm -f $fichier`


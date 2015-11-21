#include "functions.h"
#include <stdio.h>

int main(int argc, const char **argv)
{
    double base = 3,
           hauteur = 4;
    double diagonale = pythagore(base, hauteur);

    printf("Un triangle rectangle de base %lf et de hauteur %lf "
           "a pour hypotenuse %lf\n", base, hauteur, diagonale);

    return 0;
}

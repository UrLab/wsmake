from fonctions import pythagore

if __name__ == "__main__":
    base, hauteur = 3, 4
    print("Un triangle rectangle de base", base,
          "et hauteur", hauteur,
          "a pour hypotenuse", pythagore(base, hauteur))

def displayMenu():
    toReturn = ""
    print("DOMINO")
    print("1. Jouer")
    print("2. Charger une partie")
    print("3. Règles")
    print("4. Quitter")
    while 1:
        try:
            toReturn = int(input("Que voulez-vous faire ? : "))
            if 0 < toReturn <= 4:
                break
            else:
                print("La valeur saisie n'est pas dans une option")
        except Exception as e:
            print("La valeur saisie ne fonctionne pas")
    return toReturn

print(displayMenu())
def screen_clear():
    for i in range(100):
        print("\n")

def displayMenu():
    screen_clear()
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

def displayRules():
    screen_clear()
    print(f"Les dominos est un jeu dans lequel plusieurs joueurs s'affrontent. Le but est de terminer sa main le plus rapidement possible")
    print(f"\n\nAppuyez sur n'importe quelle touche pour revenir au menu...")
    input()
    displayMenu()


choice = displayMenu()
if choice == 3:
    displayRules()
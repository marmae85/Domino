def clr():
    print("\033[2J")
def pos(x,y):
    print("\033["+str(y)+";"+str(x)+"H", end="")
def printPos(x, y, text):
    print("\033["+str(y)+";"+str(x)+"H"+text)

def screen_clear():
    for i in range(100):
        print("\n")

def displayMenu():
    error = False
    while 1:
        try:
            clr()
            if error:
                pos(25,12)
                print("La valeur saisie ne fonctionne pas")
            toReturn = ""
            printPos(50, 2,"DOMINO")
            printPos(30,4,"1. Jouer")
            printPos(30,5,"2. Charger une partie")
            printPos(30,6,"3. Règles")
            printPos(30,7,"4. Quitter")
            pos(25,10)
            toReturn = int(input("Que voulez-vous faire ? : "))
            if 0 < toReturn <= 4:
                break
            else:
                error = True
        except Exception as e:
            error = True
    return toReturn

def displayRules():
    clr()
    print(f"Les dominos est un jeu dans lequel plusieurs joueurs s'affrontent. Le but est de terminer sa main le plus rapidement possible")
    print(f"\n\nAppuyez sur n'importe quelle touche pour revenir au menu...")
    input()
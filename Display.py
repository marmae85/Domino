import os

from Domino import Domino
def clr():
    print("\033[2J")
def pos(x,y):
    print("\033["+str(y)+";"+str(x)+"H", end="")
def printPos(x, y, text):
    print("\033["+str(y)+";"+str(x)+"H"+text)

def screen_clear():
    #for i in range(100):
    #    print("\n")
    os.system("clear")

def displayMenu():
    error = False
    while 1:
        try:
            clr()
            if error:
                pos(25,12)
                print("La valeur saisie ne fonctionne pas")
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

def displayBoard(boardList):
    clr()
    for i in range(len(boardList)):
        (v1, v2) = boardList[i].getValue()
        if boardList[i].getDirection() == "W":
            printPos(50+(6*i), 15,"["+str(v2) +"|"+str(v1)+"]")
        else:
            printPos(50+(6*i), 15,"["+str(v1) +"|"+str(v2)+"]")


def displayHand(hand):
    for i in range(len(hand)):
        (v1, v2) = hand[i].getValue()
        esp = int(50/len(hand))
        #print(esp)
        printPos(50 + esp*i, 30-1, "[" + str(v2) + "|" + str(v1) + "]")

def displayRules():
    clr()
    print(f"Les dominos est un jeu dans lequel plusieurs joueurs s'affrontent. Le but est de terminer sa main le plus rapidement possible.\n"
          f"Pour poser un domino, une de ses valeurs doit correspondre à celle la plus à gauche ou la plus à droite du plateau. Si aucun domino ne peut être posé,\nle joueur pioche."
          f"Le joueur qui possède le domino dont la somme est la plus haute commence. Si les 2 joueurs ont la même somme,\nc'est celui qui a la plus petite qui commence")
    print(f"\n\nAppuyez sur n'importe quelle touche pour revenir au menu...")
    input()


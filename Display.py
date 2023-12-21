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
            pos(10, 0)
            print(
                f" .------------------------------------.  .------------------------------------.  .-------------------------------------.\n"
                f"          |                  ||                  ||                  ||                  ||                  ||                  |\n"
                f"          |    ________      ||       ____       ||   ____    ____   ||       _____      ||   ____  _____    ||       ____       |\n"
                f"          |   |_   ___ `.    ||     .'    `.     ||  |_   \  /   _|  ||      |_   _|     ||  |_   \|_   _|   ||     .'    `.     |\n"
                f"          |     | |   `. \   ||    /  .--.  \    ||    |   \/   |    ||        | |       ||    |   \ | |     ||    /  .--.  \    |\n"
                f"          |     | |    | |   ||    | |    | |    ||    | |\  /| |    ||        | |       ||    | |\ \| |     ||    | |    | |    |\n"
                f"          |    _| |___.' /   ||    \  `--'  /    ||   _| |_\/_| |_   ||       _| |_      ||   _| |_\   |_    ||    \  `--'  /    |\n"
                f"          |   |________.'    ||     `.____.'     ||  |_____||_____|  ||      |_____|     ||  |_____|\____|   ||     `.____.'     |\n"
                f"          |                  ||                  ||                  ||                  ||                  ||                  |\n"
                f"          |                  ||                  ||                  ||                  ||                  ||                  |\n"
                f"           '------------------------------------'  '------------------------------------'  '------------------------------------'")
            if error:
                pos(25,27)
                print("La valeur saisie ne fonctionne pas")
            printPos(30,20,"1. Jouer")
            printPos(30,21,"2. Charger une partie")
            printPos(30,22,"3. Règles")
            printPos(30,23,"4. Quitter")
            pos(25,26)
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
    curr_x = 50
    curr_y = 15
    seq = ""
    for i in range(len(boardList)):
        seq += str(boardList[i].getDirection())
        if boardList[i].getDirection() == 0:
            curr_y += 4
        if boardList[i].getDirection() == 1:
            curr_x += 6
        if boardList[i].getDirection() == 2:
            curr_y -= 4
        if boardList[i].getDirection() == 3:
            curr_x -= 6
    for i in range(len(seq)):
        #os.system("pause")
        (v1, v2) = boardList[i].getValue()
        if seq[i] == '0':
            printPos(curr_x, curr_y, str(v1))
            curr_y -=1
            printPos(curr_x, curr_y, '-')
            curr_y -=1
            printPos(curr_x, curr_y, str(v2))
            curr_y -=1
        if seq[i] == '1':
            printPos(curr_x, curr_y, "["+str(v1)+"|"+str(v2)+"]")
            curr_x += 6
        if seq[i] == '2':
            printPos(curr_x, curr_y, str(v1))
            curr_y +=1
            printPos(curr_x, curr_y, '-')
            curr_y +=1
            printPos(curr_x, curr_y, str(v2))
            curr_y +=1
        if seq[i] == '3':
            printPos(curr_x, curr_y, "["+str(v2)+"|"+str(v1)+"]")
            curr_x -= 6



def displayHand(hand, extrems):
    count = 0
    index = []
    for i in range(len(hand)):
        (v1, v2) = hand[i].getValue()
        if v1 in extrems or v2 in extrems:
            count += 1
            index.append(i)
    count2 = 0
    count3 = 0
    for i in range(len(hand)):
        (v1, v2) = hand[i].getValue()
        if i in index:
            esp1 = int(50 / count)
            printPos(30,30-1, "Main jouable")
            printPos(50 + esp1 * (i-count3), 30 - 1, "[" + str(v1) + "|" + str(v2) + "]")
            printPos(52 + esp1 * (i-count3), 30, str(i+1))
            count2 += 1
        else:
            esp2 = int(50 / (len(hand)-count))
            printPos(30,33-1, "Dominos implaçables")
            printPos(50 + esp2 * (i-count2), 33 - 1, "[" + str(v1) + "|" + str(v2) + "]")
            printPos(52 + esp2 * (i-count2), 33, str(i+1))
            count3 += 1


def displayRules():
    clr()
    pos(0,5)
    print(f"Les dominos est un jeu dans lequel plusieurs joueurs s'affrontent. Le but est de terminer sa main le plus rapidement possible.\n"
          f"Pour poser un domino, une de ses valeurs doit correspondre à celle la plus à gauche ou la plus à droite du plateau. Si aucun domino ne peut être posé,\nle joueur pioche."
          f"Le joueur qui possède le domino dont la somme est la plus haute commence. Si les 2 joueurs ont la même somme,\nc'est celui qui a la plus petite qui commence")
    print(f"\n\nAppuyez sur n'importe quelle touche pour revenir au menu...")
    input()


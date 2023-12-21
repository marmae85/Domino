import os
import random
from Domino import Domino
from Player import Player
from Display import *



def init(name1,name2):
    #Début du jeu
    bag=bag_dominos()
    a=bag[3].getValue()
    player1=Player(distribution(bag),name1)
    player2=Player(distribution(bag),name2)
    return (player1,player2,bag)

def game(player1,player2,pioche):
    clr()
    start= True
    fin_partie=False
    max1=player1.getMax()
    max2=player2.getMax()
    board = []
    ori_droite = 1
    ori_gauche = 3
    if max2 > max1:# si le joueur 2 à le plus grand il commence directement
        ori = round(player2,board,start,pioche, ori_gauche, ori_droite)
        start = False
    elif max2 < max1:#sinon on rentre dans le while en fin de fonction et J1 commence
        printPos(60,30,"le joueur 2 commence")

    elif max2 == max1:          #cas d'égalité
        min1=player1.getMin()
        min2=player2.getMin()
        if min1 > min2:
            printPos(50,30,"le joueur 1 commence")
            ori = round(player2, board, start, pioche, ori_gauche, ori_droite)
            start = False

        elif min1 < min2:
            printPos(50,30,"le joueur 2 commence")

    while (not fin_partie):
        ori_gauche, ori_droite = round(player1,board,start,pioche, ori_gauche, ori_droite)
        if len(player1.getHand()) == 0:
            print(f"{player1.getUsername} a gagné")
            break
        elif len(player2.getHand()) == 0:
            print(f"{player2.getUsername} a gagné")
            break
        if start == True:
            start=False
        ori_gauche, ori_droite = round(player2,board,start,pioche, ori_gauche, ori_droite)
        print(fin_partie)
        if len(player1.getHand()) == 0:
            print(f"{player1.getUsername} a gagné")
            break
        elif len(player2.getHand()) == 0:
            print(f"{player2.getUsername} a gagné")
            break
    clr()
    os.system("pause")
    exit(0)


def round(player,board,start,pioche, ori_gauche, ori_droite):
    number = -1
    clr()
    tab_extrem = [0,0]
    emplacement_bon=False
    if (start == False):
        displayBoard(board)
        tab_extrem[0], trs = board[0].getValue()
        trs, tab_extrem[1] = board[len(board)-1].getValue()

    while (emplacement_bon == False):
        if start:
            displayHand(player.getHand(),list(range(7)))
        else:
            displayHand(player.getHand(),tab_extrem)
        while number>len(player.getHand()) or number < 0:
            try:
                pos(0, 35)
                number=int(input("\nJoueur "+str(player.getUsername())+", quel domino voulez vous jouer? Entrez 0 pour piocher. Il reste "+str(len(pioche))+" dominos dans la pioche : "))
            except ValueError as e:
                printPos(0,37, "La valeur saisie n'est pas conforme")
        if number == 0:
            if len(pioche)>0:
                player.addDomino(piocher(pioche))
                clr()
                displayBoard(board)
                if start:
                    displayHand(player.getHand(), list(range(7)))
                else:
                    displayHand(player.getHand(), tab_extrem)
                os.system("pause")
                emplacement_bon = True
            else:
                printPos(120,40,"la pioche est vide")

        else:
            number = number - 1
            # while number<0 or number>len(player.getHand())-1:
            #     print(60,30,"Erreur : Veuillez entrer une valeur valide")
            #
            #     pos(60,30)
            #     number = int(input("\nOù voulez-vous jouer votre domino?\nG pour le jouer à gauche\nD pour le jouer à droite\n"))


            #print(player.getHand()[number].getValue())
            clr()
            displayBoard(board)
            if start:
                displayHand(player.getHand(),list(range(7)))
            else:
                displayHand(player.getHand(),tab_extrem)
            rotation = 0
            while rotation != 1 and rotation != 2:
                try:
                    pos(60, 35)
                    rotation=int(input("\nVoulez vous le faire pivoter?\n1 : Oui\n2 : Non\n"))
                except Exception as e:
                    pass
            if rotation == 1:
                player.getHand()[number].reverse()
                #printPos(50, 30, str(player.getHand()[number].getValue()))
            elif rotation==2:
                #printPos(50, 30, str(player.getHand()[number].getValue()))
                pass

            if (start == False):#si on commence, l'emplacement n'importe pas, on ne rentre donc pas dans la boucle
                clr()
                displayBoard(board)
                if start:
                    displayHand(player.getHand(), list(range(7)))
                else:
                    displayHand(player.getHand(), tab_extrem)
                pos(50, 35)
                emplacement=input("\nOù voulez vous jouer votre domino?\nG pour le jouer à gauche\nD pour le jouer à droite\n")

                while emplacement not in ['G', 'g', 'D', 'd']:
                    clr()
                    displayBoard(board)
                    if start:
                        displayHand(player.getHand(), list(range(7)))
                    else:
                        displayHand(player.getHand(), tab_extrem)
                    printPos(50,35,"Erreur : Veuillez entrer une valeur valide (G, g, D, d)")
                    pos(50,35)
                    emplacement = input("\nOù voulez-vous jouer votre domino?\nG pour le jouer à gauche\nD pour le jouer à droite\n")

                clr()
                displayBoard(board)
                if start:
                    displayHand(player.getHand(), list(range(7)))
                else:
                    displayHand(player.getHand(), tab_extrem)
                pos(0, 35)
                changeOrientation = input("Voulez-vous changer la direction ? 1 - Oui, une autre touche non")
                if changeOrientation == "1":
                    print(f"    0     \n"
                          f"    ↑     \n"
                          f"3 ←   → 1 \n"
                          f"    ↓     \n"
                          f"    2     ")
                    new_ori = int(input("Quelle orientation voulez vous ?"))
                    if (emplacement == 'g' or emplacement == 'G') and (ori_gauche != new_ori or (ori_gauche+2)%4 != new_ori):
                        ori_gauche = new_ori
                    elif(emplacement == 'd' or emplacement == 'D') and (ori_droite != new_ori or (ori_droite+2)%4 != new_ori):
                        ori_droite = new_ori

                #print(player.getHand()[number].getValue(), board[0].getValue()[0],board[len(board)-1].getValue()[1])
                if (emplacement=='G' or emplacement == 'g') and board[0].getValue()[0] == player.getHand()[number].getValue()[1]:
                    #deplacer tout le tableau vers la droite et placer le domino a gauche
                    player.getHand()[number].setDirection((ori_gauche+2)%4)
                    board.append(player.getHand()[number])  # ajoute la piece a droite
                    for k in range (len(board)-1,0,-1):
                        board[k],board[k-1] = board[k-1],board[k]
                    player.useDomino(player.getHand()[number].getValue())
                    emplacement_bon=True

                elif (emplacement == 'D' or emplacement == 'd') and board[len(board)-1].getValue()[1] == player.getHand()[number].getValue()[0]:
                    player.getHand()[number].setDirection(ori_droite)
                    board.append(player.getHand()[number])#ajoute la piece a droite
                    player.useDomino(player.getHand()[number].getValue())
                    emplacement_bon=True

                #else :
                #    printPos(50,30,"l'emplacement n'est pas valable")
                #    pos(50,30)
                #    emplacement = str(input("\nOù voulez-vous jouer votre domino?\nG pour le jouer à gauche\nD pour le jouer à droite\n"))

            else:
                board.append(player.getHand()[number])  # ajoute la piece sans vérification étant donné que le plateau est vide
                player.useDomino(player.getHand()[number].getValue())
                emplacement_bon =True #dans le cas du start, l'emplacement est oblligatoirement bon
    return ori_gauche, ori_droite







""" #pour afficher les mains en test 
    j11=[]
    j22=[]
    for i in range(len(bag)):
        if i<len(j1):
            j11.append(j1[i].getValue())
            j22.append(j2[i].getValue())
        bag[i] = bag[i].getValue()
"""

def bag_dominos():
    count= 0
    pioche_obj = []
    liste_coo=[]
    for i in range(7):
        for j in range(i + 1):
            pioche_obj.append(Domino((j,i)))
            liste_coo.append(pioche_obj[count].getValue())
            count=count+1

    return pioche_obj

def piocher(bag):
    piece = random.choice(bag) #pioche un domino random dans le sac
    index=bag.index(piece)
    bag.pop(index)
    return piece

def distribution(bag):
    hand=[]
    for i in range(7):
        domino=piocher(bag)
        hand.append(domino)
    return hand

#hand = distribution()
#print("voilà tes 7 dominos", hand)

"""
def supression_bag(hand):
    for k in range(len(hand)):
        for i in range(len(bag)-1, 0, -1):
            if bag[i] == hand[k]:
             bag.pop(i)
supression_bag(hand)
print("après distribution", bag)
"""



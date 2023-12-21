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

    if max2 > max1:# si le joueur 2 à le plus grand il commence directement
        round(player2,board,start,pioche)
        start = False
    elif max2 < max1:#sinon on rentre dans le while en fin de fonction et J1 commence
        printPos(60,30,"le joueur 2 commence")

    elif max2 == max1:          #cas d'égalité
        min1=player1.getMin()
        min2=player2.getMin()
        if min1 > min2:
            printPos(50,30,"le joueur 1 commence")
            round(player2,board,start,pioche)
            start = False

        elif min1 < min2:
            printPos(50,30,"le joueur 2 commence")

    while (not fin_partie):
        round(player1,board,start,pioche)
        if start == True:
            start=False
        round(player2,board,start,pioche)
        print(fin_partie)

def round(player,board,start,pioche):

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

        number=int(input("\njoueur "+str(player.getUsername())+" quel domino voulez vous jouer? entrez 0 pour piocher. Il reste"+str(len(pioche))+" domino dans la pioche"))
        if number==0:
            if len(pioche)>0:
                player.addDomino(pioche.pop(0))
            else:
                printPos(120,40,"la pioche est vide")

        else:
            number = number - 1
            while number<0 or number>len(player.getHand())-1:
                print(60,30,"Erreur : Veuillez entrer une valeur valide")

                pos(60,30)
                number = int(input("\nOù voulez-vous jouer votre domino?\nG pour le jouer à gauche\nD pour le jouer à droite\n"))


            print(player.getHand()[number].getValue())
            pos(60, 32)
            rotation=int(input("\nvoulez vous le faire pivoter?\n1 : pour le tourner\n2: pour le laisser dans le même sens"))
            if rotation == 1:
                player.getHand()[number].reverse()
                printPos(50, 30, str(player.getHand()[number].getValue()))
            elif rotation==2:
                printPos(50, 30, str(player.getHand()[number].getValue()))

            if (start == False):#si on commence, l'emplacement n'importe pas, on ne rentre donc pas dans la boucle
                emplacement=str(input("\noù voulez vous jouer votre domino?\nG pour le jouer à gauche\nD pour le jouer à droite\n"))

                while emplacement not in ['G', 'g', 'D', 'd']:
                    printPos(50,30,"Erreur : Veuillez entrer une valeur valide (G, g, D, d)")
                    pos(50,30)
                    emplacement = int(input("\nOù voulez-vous jouer votre domino?\nG pour le jouer à gauche\nD pour le jouer à droite\n"))

                #print(player.getHand()[number].getValue(), board[0].getValue()[0],board[len(board)-1].getValue()[1])
                if (emplacement=='G' or emplacement == 'g') and board[0].getValue()[0] == player.getHand()[number].getValue()[1]:
                    #deplacer tout le tableau vers la droite et placer le domino a gauche
                    board.append(player.getHand()[number])  # ajoute la piece a droite
                    for k in range (len(board)-1,0,-1):
                        board[k],board[k-1] = board[k-1],board[k]
                    player.useDomino(player.getHand()[number].getValue())
                    emplacement_bon=True

                elif (emplacement == 'D' or emplacement == 'd') and board[len(board)-1].getValue()[1] == player.getHand()[number].getValue()[0]:
                    board.append(player.getHand()[number])#ajoute la piece a droite
                    player.useDomino(player.getHand()[number].getValue())
                    emplacement_bon=True

                else :
                    printPos(50,30,"l'emplacement n'est pas valable")
                    pos(50,30)
                    emplacement = str(input("\nOù voulez-vous jouer votre domino?\nG pour le jouer à gauche\nD pour le jouer à droite\n"))

            else:
                board.append(player.getHand()[number])  # ajoute la piece sans vérification étant donné que le plateau est vide
                player.useDomino(player.getHand()[number].getValue())
                emplacement_bon =True #dans le cas du start, l'emplacement est oblligatoirement bon







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
    for i in range(3):
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
    for i in range(3):
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



import random
from Domino import Domino
from Player import Player

def init(name1,name2):
    #Début du jeu
    bag=bag_dominos()
    a=bag[3].getValue()
    player1=Player(distribution(bag))
    player1.setUsername(name1)
    player2=Player(distribution(bag))
    player2.setUsername(name2)
    return (player1,player2)

def game(player1,player2):
    fin_partie=False
    max1=player1.getMax()
    max2=player2.getMax()

    if max2 > max1:
        round(player2)
    elif max2 < max1:
        round(player2)

    elif max2 == max1:          #cas d'égalité
        min1=player1.getMin()
        min2=player2.getMin()
        if min1 > min2:
            round(player2)
        elif min1 < min2:
            round(player1)

    while (not fin_partie):
        round(player1)
        round(player2)

def round(player):
    number=int(input("quel domino voulez vous jouer?"))
    rotation=int(input("voulez vous le faire pivoter?\n1 : pour le tourner\n2: pour le laisser dans le même sens"))
    emplacement=int(input("où voulez vous jouer votre domino?\nO pour le jouer à gauche\nE pour le jouer à droite\n"))
    if rotation==1:
        player.getValue[number].reverse()


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









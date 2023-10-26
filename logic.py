import random
from Domino import Domino

def jeu():
    #Début du jeu
    bag=bag_dominos()
    print("1",bag)
    a=bag[3].getValue
    print("2", a)
    j1=distribution(bag)
    j2=distribution(bag)
    print("2",j1)
    print("3",j2)
    print("4",bag)


def bag_dominos():
    pioche_obj = []
    liste_coo=[]
    for i in range(7):
        for j in range(i + 1):
            pioche_obj.append(Domino([j,i]))
            liste_coo.append(pioche_obj[j].getValue())
    print(pioche_obj)


    return pioche_obj

def piocher(bag):
    piece = random.sample(bag, 1) #pioche un domino random dans le sac
    index=bag.index(piece.getValue())
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









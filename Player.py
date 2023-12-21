import os

from Domino import Domino
from Display import pos, printPos

class Player:


    def __init__(self, hand,username):
        self.hand = hand
        self.username = username

    def getMin(self):
        min = 13
        for i in range(len(self.hand)):
            (v1, v2) = self.hand[i].getValue()
            currentvalue = v1 + v2
            if currentvalue < min:
                min = currentvalue
        return min
    def getMax(self):
        max = 0
        for i in range(len(self.hand)):
            (v1, v2) = self.hand[i].getValue()
            currentvalue = v1 + v2
            if currentvalue > max:
                max = currentvalue
        return max
    def useDomino(self, value):
        v0, v1 = value
        printPos(100,50,str(value))
        for i in range(len(self.hand)):
            v2, v3 = self.hand[i].getValue()
            if(v0 == v2 and v1 == v3) or (v0 == v3 and v1 == v2):
                self.hand.pop(i)
                break

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username
    def getHand(self):
        return self.hand

    def getHand(self):
        return self.hand
    def addDomino(self, domino):
        self.hand.append(domino)
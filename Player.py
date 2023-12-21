from Domino import Domino

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
        for i in range(len(self.hand)-1):
            if self.hand[i].getValue() == value:
                self.hand.pop(i)

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def getHand(self):
        return self.hand
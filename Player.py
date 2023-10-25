class Player:
    def __init__(self, game):
        self.game = game

    def getMin(self):
        min = 13
        for i in range(len(self.game)):
            (v1, v2) = self.game[i]#.getValue()
            currentvalue = v1 + v2
            if currentvalue < min:
                min = currentvalue
        return min
    def getMax(self):
        max = 0
        for i in range(len(self.game)):
            (v1, v2) = self.game[i]#.getValue()
            currentvalue = v1 +v2
            if currentvalue > max:
                max = currentvalue
        return max

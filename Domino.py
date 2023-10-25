"""
- creer domino "A", argument: le tableau de valeurs :                D= Domino([7,8])
- établir la direction du domino (N,S,E,O) :                         D.setDirection("N")
- obtenir les valeurs du domino : renvoie un tableau à 2 valeurs     D.getValue()
- définir l'affichage, en parametre la direction :                   D.setAffichage(D.getDirection)
  (appelé automatiquement)
- obtenir l'affichage du domino (renvoie un string                   D.getAffichage()
"""

class Domino :
    value=[0,0]
    direction = ""
    affichage=[str(value[0]),str(value[1])]

    def __init__(self,type):
        self.value = type
        self.direction="E"

    def setValue(self,value):
        self.value=value

    #  changer le sens ----- A FAIRE-----
    def setDirection(self,dir):
        self.direction=dir

    def getValue(self):
        print(self.value)
        return self.value

    def getDirection(self,direction):
        print(self.direction)
        return(self.direction)

    def setAffichage(self):
        self.setAffichage(self.direction)
        return self.affichage

    def setAffichage(self,dir):
        v1=str(self.value[0])
        v2=str(self.value[1])
        if self.direction == "N":
            self.affichage = ["|", v1, "|\n|", v2, "|"]
            self.affichage = "".join(self.affichage)

        elif self.direction == "S":
            self.affichage = ["|", v2, "|\n|", v3, "|"]
            self.affichage = "".join(self.affichage)

        elif self.direction == "E":
            self.affichage = ["|", v1, "|", v2, "|"]
            self.affichage = "".join(self.affichage)

        elif self.direction == "N":
            self.affichage = ["|", v2, "|", v1, "|"]
            self.affichage = "".join(self.affichage)



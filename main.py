import os

from logic import init, game
from Display import displayMenu, displayRules, clr, pos
from Save import loadGame
from Domino import Domino
from Player import Player
def main():
    while 1:
        action = displayMenu()
        if action == 1:
            clr()
            pos(5,20)
            name1 = input("Entrez le nom d'un joueur : ")
            pos(5,21)
            name2 = input("Entrez le nom d'un joueur : ")
            (player1, player2,pioche) = init(name1, name2)
            game(player1, player2, pioche)
        elif action == 2:
            elems = loadGame()
            listMain1 = elems[2].split("+")
            main1 = []
            for i in range(len(listMain1)-1):
                main1.append(dominoString2Domino(listMain1[i]))
            listMain2 = elems[3].split("+")
            main2 = []
            for i in range(len(listMain2)-1):
                main2.append(dominoString2Domino(listMain2[i]))
            player1 = Player(main1, elems[0])
            player2 = Player(main2, elems[1])
            listPioche = elems[5].split("+")
            pioche = []
            for i in range(len(listPioche)-1):
                pioche.append(dominoString2Domino(listPioche[i]))
            boardValueDir = elems[4].split("-")
            board = []
            for i in range(len(boardValueDir)-1):
                domino = boardValueDir[i].split("+")[0]
                dire = int(boardValueDir[i].split("+")[1])
                board.append(dominoString2Domino(domino))
                board[i].setDirection(dire)
            game(player1, player2, pioche, board=board, start=False)
        elif action == 3:
            displayRules()
        else:
            clr()
            exit()
    return 0


def dominoString2Domino(domino):
    v1 = int(domino[1])
    v2 = int(domino[4])
    return Domino((v1, v2))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()





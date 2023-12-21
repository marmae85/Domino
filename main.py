
from logic import init, game
from Display import displayMenu, displayRules, clr, pos
def main():
    while 1:
        action = displayMenu()
        if action == 1:
            clr()
            pos(5,20)
            name1 = input("Entrez le nom d'un joueur : ")
            pos(5,21)
            name2 = input("Entrez le nom d'un joueur : ")
            (player1, player2) = init(name1, name2)
            game(player1, player2)
        elif action == 2:
            loadGame()
        elif action == 3:
            displayRules()
        else:
            clr()
            exit()
    return 0
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()





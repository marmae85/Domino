
from logic import init, game
from Display import displayMenu, displayRules, clr
def main():
    while 1:
        action = displayMenu()
        if action == 1:
            name1 = input("Entrez le nom d'un joueur : ")
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
    return
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()





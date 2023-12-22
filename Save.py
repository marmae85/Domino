#format du fichier sauvegarde : nom1, nom2, main1, main2, plateau, pioche


def saveGame(player1, player2, board, pioche):
    save_file = open("savefile", "w")
    save_file.write(player1.getUsername())
    save_file.write("/")
    save_file.write(player2.getUsername())
    save_file.write("/")
    for i in range(len(player1.getHand())):
        save_file.write(str(player1.getHand()[i].getValue()))
        save_file.write("+")
    save_file.write("/")
    for i in range(len(player2.getHand())):
        save_file.write(str(player2.getHand()[i].getValue()))
        save_file.write("+")
    save_file.write("/")
    for i in range(len(board)):
        save_file.write(str(board[i].getValue()))
        save_file.write("+")
        save_file.write(str(board[i].getDirection()))
        save_file.write("-")
    save_file.write("/")
    for i in range(len(pioche)):
        save_file.write(str(pioche[i].getValue()))
        save_file.write("+")
    save_file.close()
def loadGame():
    try:
        load_file = open("savefile", "r")
        data = load_file.read()
        elems = data.split("/")
        return elems
    except Exception as e:
        return None

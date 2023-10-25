def SaveBoard(list):
    save_file = open("savefile", "w")
    for i in range(len(list)):
        save_file.write(list[i].getValue()+"+")
        save_file.write(list[i].getDirection())
    save_file.write("/")


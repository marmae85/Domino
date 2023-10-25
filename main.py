# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
def bag_dominos():
    list = []
    for i in range(7):
        for j in range(i + 1):
            list.append((j, i))
    return list
bag = bag_dominos() # variable bag est la liste des dominos
#print(bag)

def distribution():
    for i in range(8):
        random_domino = random.randint(0, len(bag) - 1) #pioche un domino random dans le sac
        main = bag.append()
    print("voilà tes 7 dominos batard",main)

distribution()

def main():
    return
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()









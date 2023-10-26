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
print(bag)

def distribution():
    hand = random.sample(bag, 7) #pioche un domino random dans le sac
    return hand
hand = distribution()
print("voilà tes 7 dominos", hand)
def supression_bag(hand):
    for k in range(len(hand)):
        for i in range(len(bag)-1, 0, -1):
            if bag[i] == hand[k]:
             bag.pop(i)
supression_bag(hand)
print("après distribution", bag)

def main():
    return
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()









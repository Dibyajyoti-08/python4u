'''
Create a function that simulates 
rolling two dice and returns their sum.
'''

from random import randrange

def sum_of_dice(dice1, dice2):
    return dice1 + dice2

if __name__ == '__main__':
    dice1 = randrange(1, 6)
    dice2 = randrange(1, 6)
    print(sum_of_dice(dice1, dice2))
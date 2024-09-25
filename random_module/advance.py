'''
Write a program that shuffles a deck of cards 
using the random.shuffle() function.
'''

from random import shuffle
from itertools import product

def deck_card():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = list(product(values, suits))
    shuffle(deck)
    print(deck)

if __name__ == '__main__':
    deck_card()
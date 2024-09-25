'''
Write a script that generates and prints a random number between 1 and 100.
'''

from random import randint

def random_number(num1, num2):
    print(f"Your random number between {num1} and {num2}: {randint(num1, num2)}")

if __name__ == '__main__':
    random_number(1, 100)
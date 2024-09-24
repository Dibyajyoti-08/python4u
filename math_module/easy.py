'''
Write a Python script to calculate 
the square root of a given number.
'''

import math

def square_root(num):
    result = int(math.sqrt(num))
    print(f"The square roor of the {num} is {result}")

if __name__ == '__main__':
    square_root(81)
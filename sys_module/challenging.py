'''
Write a program that accepts multiple command-line arguments 
and prints their sum if they are all numbers.
'''

import sys

def cmd_sum(input):
    if len(input) == 0:
        print("Error: Expected numbers as a argument")
    try:
        return sum(map(float, input))
    except ValueError:
        return "Error: Not all arguments are numbers."
    
if __name__ == '__main__':
    print(cmd_sum(sys.argv[1:]))
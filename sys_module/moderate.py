'''
Create a Python script that takes a filename as a 
command-line argument and prints its content.
'''

import sys

def print_message(messages):
    if len(messages) == 0:
        print("Error: Expected argument")
    else:
        print(" ".join(messages))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_message(sys.argv[1:])
    else:
        print("Error: Expected argument")

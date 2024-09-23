'''
Write a program that reads and prints all arguments passed via the command
line and exits with a custom exit status if no arguments are passed.
'''

import sys

def msg():
    if len(sys.argv[1:]) > 1:
        print(f'Arguments passed: {" ".join(sys.argv[1:])}')
    else:
        print("Error: Argument Expected.")
        sys.exit(1)

if __name__ == '__main__':
    msg()


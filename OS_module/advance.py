'''
Write a program to list all files and 
subdirectories in a given directory, recursively.
'''

import os

path = "/home/dibyajyoti/Work/py_module/"

for root, dirs, files in os.walk(path):
    print(f"Directory: {root}")
    for name in files:
        print(f"File: {name}")
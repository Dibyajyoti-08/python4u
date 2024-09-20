'''
Write a script that renames all .txt files 
in a directory by appending "_backup" to their names
'''

import os

path = '/home/dibyajyoti/Work/py_module/beginner_module_OS'

for filename in os.listdir(path):
    if filename.endswith(".txt"):
        newFile = filename.replace(".txt", ".txt_backup")
        os.rename(os.path.join(path, filename), os.path.join(path, newFile))
        print("Renaming Done")

    else:
        print(".txt extension file is not present!")


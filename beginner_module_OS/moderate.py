'''
Create a new directory named "test_directory"
using the os module
'''

import os

directory_name = 'test_directory'
path = './'

if os.path.exists(directory_name):
    print(f"Directory {directory_name}, is already present")
else:
    os.mkdir(os.path.join(path, directory_name))
    print(f"The directory {directory_name} has been cerated successfully!")
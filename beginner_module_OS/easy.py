'''
Write a python script to print
the current directory
'''
# Import the os module
import os

if __name__ == '__main__':
    print(f"Current directory is {os.getcwd()}")

# Without importing os module
import subprocess

def get_current_dir():
    cur_dir = subprocess.run("pwd", capture_output=True, text=True)
    return cur_dir.stdout.strip()

print(f"Current Directory is {get_current_dir()}")
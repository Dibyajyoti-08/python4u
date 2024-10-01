'''
Write a script that uses a regular expression to check if a string contains the word "Python"
'''

from re import search

def check_str(word, string):
    found_str = search(word, string)
    if found_str:
        print(f"{word} is found in the string '{string}'")
    else:
        print(f"{word} is not found in the string '{string}'")
    
if __name__ == '__main__':
    string = "The best coding language for scipting and manipulation is Python!"
    word = "Python"
    check_str(word, string)
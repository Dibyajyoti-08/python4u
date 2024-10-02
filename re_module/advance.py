'''
 Implement a function that replaces all whitespace characters 
 in a string with a hyphen (-) using a regular expression.
'''

from re import sub

def replace_whitespace(string):
    return sub(r'\s+', '-', string)

if __name__ == '__main__':
    print(replace_whitespace("This is a test string with    multiple whitespaces."))
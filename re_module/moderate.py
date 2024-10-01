'''
Implement a function that finds all occurrences of a digit (0-9) in a string.
'''

from re import findall

def find_digits(string):
    digits = findall(r'\d', string)
    
    return digits

if __name__ == '__main__':
    string = "My phone number is 123-456-7890 and my zip code is 98765."
    digits = find_digits(string)
    print(f"Digits found in the string '{string}' is {digits}")



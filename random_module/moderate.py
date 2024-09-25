'''
Implement a Python function that randomly 
selects an element from a list of strings.
'''

from random import choice

def random_element(element_list):
    print(f"The random element from the string is {choice(element_list)}")

if __name__ == '__main__':
    elements = ["d", "jena", "loves", "coding"]
    random_element(elements)
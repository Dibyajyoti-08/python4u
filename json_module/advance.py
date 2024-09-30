'''
Write a function that reads a JSON file, checks for the 
existence of a specific key, and prints its value if found.
'''

from json import load

def read_json(file_name, json_key):
    with open(file_name, 'r') as json_file:
        data = load(json_file)
    
    if json_key in data:
        result = data[json_key]
        print(f"The value of the {json_key} is {result}")
    else:
        print(f"{json_key} to fetch is not present in the JSON")

if __name__ == '__main__':
    file_name = "output.json"
    json_key = "Age"
    read_json(file_name, 'Age')
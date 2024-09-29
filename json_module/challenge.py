'''
Create a program that reads a JSON file and modifies one of its values, 
then writes the updated JSON back to the file.
'''

from json import load
from json import dump

def read_and_modify_json(file_name, key_to_modify, new_value):
    with open(file_name, 'r') as json_file:
        data = load(json_file)

    if key_to_modify in data:
        data[key_to_modify] = new_value
        print(f"Updated {key_to_modify} to {new_value}")
    else:
        print(f"Key '{key_to_modify}' not found in JSON")
        return
    
    with open(file_name, 'w') as json_file:
        dump(data, json_file, indent=4)
        print(f"Updated JSON has been written back to {file_name}")

if __name__ == '__main__':
    file_name = "output.json"
    read_and_modify_json(file_name, 'Age', 25)
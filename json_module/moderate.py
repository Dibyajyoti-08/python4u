'''
Implement a function that writes a Python 
dictionary to a JSON file.
'''

from json import dump

def write_dict_to_json(python_dict, file_name):
    with open(file_name, 'w') as json_file:
        send = dump(python_dict, json_file, indent=4)
    return send

if __name__ == '__main__':
    example_dict = {
        "Name": "Coder",
        "Age": 24,
        "City": "Jupiter"
    }

    json_dump = write_dict_to_json(example_dict, "output.json")
'''
Write a Python script that loads a JSON string and 
prints its content as a Python dictionary.
'''

from json import loads

def load_json(json_str):
    try:
        return loads(json_str)
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    else:
        return loads(json_str)

if __name__ == '__main__':
    json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
    print(load_json(json_string))
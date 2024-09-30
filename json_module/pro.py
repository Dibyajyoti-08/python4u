'''
Implement a program that merges two JSON files into one and handles any 
conflicts in the keys by appending a suffix to the conflicting key names.
'''

from json import load
from json import dump

def merge_json_file(file1, file2, output_file, suffix1="_file1", suffix2="_file2"):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = load(f1)
        data2 = load(f2)
    
    merge_data = {}

    for key in data1:
        if key in data2:
            merge_data[key + suffix1] = data1[key]
            merge_data[key + suffix2] = data2[key]
        else:
            merge_data[key] = data1[key]
    
    for key in data2:
        if key not in merge_data:
            merge_data[key] = data2[key]

    with open(output_file, 'w') as out_file:
        dump(merge_data, out_file, indent=4)
    
    print(f"Merged data has been written to {output_file}")

if __name__ == '__main__':
    file1 = "output.json"
    file2 = "output2.json"
    output_file = "mergeFile.json"
    merge_json_file(file1, file2, output_file)
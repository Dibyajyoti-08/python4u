'''
Create a function that uses defaultdict to group a 
list of tuples by their first element.
'''

from collections import defaultdict

def group_by_first_element(tuples_list):
    grouped = defaultdict(list)

    for first, second in tuples_list:
        grouped[first].append(second)
    
    return grouped

if __name__ == '__main__':
    tuples_list = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
    grouped_tuples = group_by_first_element(tuples_list)

    for key, values in grouped_tuples.items():
        print(f"{key}: {values}")

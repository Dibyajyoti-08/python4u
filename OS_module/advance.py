'''
Implement a program that measures and prints 
the memory usage of an object (e.g., a list) using the sys module.
'''

import sys

listInput = [1, 4, 3, 5, 6]
total_memory_elements = 0
memory_usage = sys.getsizeof(listInput)

for item in listInput:
    total_memory_elements += sys.getsizeof(item)

total_memory = memory_usage + total_memory_elements

print(f"The memory of the list object itself: {memory_usage} bytes")
print(f"The memory usage of individual element : {total_memory_elements} bytes")
print(f"Total memory usage (list + elements): {total_memory} bytes")

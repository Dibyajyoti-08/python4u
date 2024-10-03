'''
Write a script that creates a Counter object from a list 
of numbers and prints the frequency of each number.
'''

from collections import Counter

def count_frequencies(numbers):
    frequency_counter = Counter(numbers)

    for number, frequency in frequency_counter.items():
        print(f"Number {number} appears {frequency} time(s)")

if __name__ == '__main__':
    numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    count_frequencies(numbers_list)
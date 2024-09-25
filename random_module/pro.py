'''
Implement a program that simulates a lottery draw, 
where 6 unique random numbers are selected from a range of 1 to 49.
'''

from random import randint

def lottery_draw():
    min_num = 1
    max_num = 49
    num_to_select = 6
    numbers = set()
    while len(numbers) < num_to_select:
        numbers.add(randint(min_num, max_num))
        
    print(list(numbers))

if __name__ == '__main__':
    lottery_draw()
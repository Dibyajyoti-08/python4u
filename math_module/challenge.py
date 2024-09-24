'''
Write a function to calculate the sine of a 
given angle (in degrees) using the math module.
'''

import math

def sin_func(angle_degree):
    angle_radians = math.radians(angle_degree)
    print(f"The sine function of the given angle {angle_degree} is {math.sin(angle_radians)}")


if __name__ == '__main__':
    sin_func(90)
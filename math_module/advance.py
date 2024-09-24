'''
Write a program to calculate the area of a circle 
given its radius using the math.pi constant.
'''

import math

def area_circle(radius):
    if radius == 0:
        return 0
    else:
        print(f"The area of the circle is {(math.pi * radius * radius):.2f}")
    
if __name__ == '__main__':
    radius = float(input("Enter the radius of the circle: "))
    area_circle(radius)
'''
Implement a Python function that solves quadratic equations using the quadratic formula, 
making use of the math module for square root operations.
'''

import math

def quadratic_eq(a, b, c):
    discriminant = (b * b) - (4 * a * c)

    if discriminant < 0:
        print("No real solution (discriminant is negative)")

    positive_result = (-b + math.sqrt(discriminant))/ (2*a)
    negative_result = (-b - math.sqrt((b*b)-4*(a*c)))/ (2*a)
    print(f"Quadratic equation: {positive_result, negative_result}")

if __name__ == '__main__':
    quadratic_eq(1, 5, 6)
'''
Implement a function that calculates the greatest 
common divisor (GCD) of two numbers using the math module
'''

import math

def greatest_common_divisor(num1, num2):
    result = math.gcd(num1, num2)
    print(f"The greatest common divisor between {num1} and {num2} is {result}")
    
if __name__ == '__main__':
    greatest_common_divisor(24, 42)
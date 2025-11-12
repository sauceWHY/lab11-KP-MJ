# https://github.com/sauceWHY/lab11-KP-MJ
# Partner 1: Keith Pennock
# Partner 2: Micah Jaffa
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


# First example
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a # raise ZeroDivisionError if a == 0

    
def logarithm(a, b):
    if a <= 0:
        raise ValueError
    else:
        return math.log(b, a)# use math library + raise ValueError
            

def exp(a, b):
    return a ** b


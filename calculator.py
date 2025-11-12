import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def square_root(a):
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a # raise ZeroDivisionError if a == 0
    except:
        raise ZeroDivisionError
    
def log(a, b):
    try:
        return math.log(b, a)# use math library + raise ValueError
    except:
        raise ValueError

def exp(a, b):
    return a ** b


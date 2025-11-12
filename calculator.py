import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# https://github.com/sauceWHY/lab11-KP-MJ
# Partner 1: Keith Pennock
# Partner 2: Micah Jaffa

# First example
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b): 
    return a * b
def div(a, b):  # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    return b/a        
def log(a, b):# use math library + raise ValueError
   if a <= 0:
       raise ValueError
   return math.log(b, a)
def exp(a, b):
    return a**b



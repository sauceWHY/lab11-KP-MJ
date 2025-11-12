import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
<<<<<<< HEAD
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
    try:
        return math.log(b, a)
    except:
        raise ValueError
def exp(a, b):
    return a**b
print(div(0, 5))

=======
def add(a, b): 
    return a + b
>>>>>>> 7c1615079172d39f60d20e0a8aaecadac7fc2dbf

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

print(div(0,6))

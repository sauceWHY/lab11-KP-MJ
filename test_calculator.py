# https://github.com/sauceWHY/lab11-KP-MJ
# Partner 1: Keith Pennock
# Partner 2: Micah Jaffa
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5,3), 8)
        self.assertEqual(add(5,-5), 0)
        self.assertEqual(add(-5,-3), -8)
    #     fill in code

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,3), 2)
        self.assertEqual(sub(5,-5), 10)
        self.assertEqual(sub(-5,-3), -2)
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,3), 15)
        self.assertEqual(mul(6,7), 42)
        self.assertEqual(mul(4,5), 20)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(5,10), 2)
        self.assertEqual(div(5,15), 3)
        self.assertEqual(div(5,20), 4)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
         with self.assertRaises(ZeroDivisionError):
            div(0, 10)
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 10), 1)
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(3, 9), 2)
    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 10)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-3)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(4), 2)
        

# Do not touch this
if __name__ == "__main__":
    unittest.main()

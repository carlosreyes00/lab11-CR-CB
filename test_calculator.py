# https://github.com/carlosreyes00/lab11-CR-CB
# Carlos Reyes
# Christian Boksa

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(2.5, 3), 5.5)
        self.assertEqual(add(0, -5), -5)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(2, 4), -2)
        self.assertEqual(subtract(2.5, 3), -0.5)
        self.assertEqual(subtract(0, -5), 5)

    ##########################

    ####### Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(2, 4), 8)
        self.assertEqual(mul(2.5, 3), 7.5)
        self.assertEqual(mul(0, -5), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(3, 9), 3)
        self.assertEqual(div(-5, 20), -4)

    ##########################

    ####### Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(2, 32), 5)
        self.assertAlmostEqual(logarithm(2, 1), 0)
        self.assertAlmostEqual(logarithm(2, 16), 4)

    def test_log_invalid_base(self):  # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    ##########################

    ####### Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(9, 12), 15)

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(TypeError):
            square_root("abc")
            square_root([2, 4])
            square_root(True)
        # Test basic function
    #########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
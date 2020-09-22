"""
Author:Viktoriia Denys
Program:validation_with_try.py
program validation_with_try.py reads in one person's names, first and last, their age and three scores out of 100.
Taking the three scores and finding the average, storing into a variable.with added input validation using try/except
"""

import unittest

from input_validation import validation_with_try

class MyTestCase(unittest.TestCase):
    def test_average_exception1(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 89, 78)

    def test_average_exception2(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, - 89, 78)

    def test_average_exception3(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, 89, -78)


if __name__ == '__main__':
    unittest.main()

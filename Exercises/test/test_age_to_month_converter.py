import unittest
from AgeToMonthConverter import *


class AgeToMonthConverterTest(unittest.TestCase):

    def test_age_to_month_int_pass(self):
        actual = convert_age_to_month(1)
        expected = float(12)
        self.assertEqual(actual, expected)

    def test_age_to_month_string_as_int_pass(self):
        self.assertEqual(convert_age_to_month("1"), float(12))

    def test_age_to_month_float_pass(self):
        self.assertEqual(convert_age_to_month(1.1), float(13))

    def test_age_to_month_float_less_than_one_pass(self):
        self.assertEqual(convert_age_to_month(0.1), float(1))

    def test_age_to_month_not_number_raise_exception(self):
        self.assertRaises(Exception, convert_age_to_month, "3fd")


"""
Uri's comments:
==============

* It's good to have tests and unittest.TestCase is very common and popular.
  It is used in Django and many other open source projects.
* File names, it's better to write in lowercase (like variable names) and then 
  import from the name in lowercase.
* Sometimes it's useful to import everything from a file ("import *"),
  however in some cases it's better to write specifically what you want
  to import.

"""

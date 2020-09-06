import unittest
from AgeToMounthConverter import *
import decimal

class age_to_mounth_converter_test(unittest.TestCase):

    def test_age_to_mounth_int_pass(self):
        actual = convert_age_to_mounth(1)
        expected = float(12)
        self.assertEqual(actual,expected)

    def test_age_to_mounth_string_as_int_pass(self):
        self.assertEqual(convert_age_to_mounth("1"),float(12))

    def test_age_to_mounth_float_pass(self):
        self.assertEqual(convert_age_to_mounth(1.1),float(13))

    def test_age_to_mounth_float_less_than_one_pass(self):
        self.assertEqual(convert_age_to_mounth(0.1),float(1))

    def test_age_to_mounth_not_number_raise_exception(self):
        self.assertRaises(Exception,convert_age_to_mounth,"3fd")
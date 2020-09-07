import unittest
from DividedBy import *

divided_list = [7.0, 13, 15]
divided_list_not_a_numbers = [7, 13, 15, "ff"]


class DividedByTest(unittest.TestCase):

    def test_divided_by_pass(self):
        self.assertTrue(divided_by(get_common_divided(divided_list), divided_list))

    def test_divided_by_fail(self):
        self.assertFalse(divided_by(get_common_divided(divided_list) - 1, divided_list))

    def test_divided_by_not_a_number_raise_exception(self):
        self.assertRaises(TypeError, divided_by, get_common_divided(divided_list), divided_list_not_a_numbers)

    def test_divided_by_not_a_number_raise_exception2(self):
        self.assertRaises(TypeError, divided_by, "f3", divided_list)

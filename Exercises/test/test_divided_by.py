import unittest
from DividedBy import *
from random import randint

genetated_list = []


class DividedByTest(unittest.TestCase):

    def grnetate_random_list(self, len=5):
        for _ in range(len):
            num1 = randint(1, 100)
            genetated_list.append(num1)

    def setUp(self):
        genetated_list.clear()
        self.grnetate_random_list()

    def test_divided_by_pass(self):
        self.assertTrue(divided_by(get_common_divided(genetated_list), genetated_list))

    def test_divided_by_fail(self):
        self.assertFalse(divided_by(get_common_divided(genetated_list) - 1, genetated_list))

    def test_divided_by_not_a_number_raise_exception2(self):
        self.assertRaises(TypeError, divided_by, "f3", genetated_list)

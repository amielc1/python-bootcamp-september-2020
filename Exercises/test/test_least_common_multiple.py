import unittest
from DividedBy import *
from LeastCommonMultiple import *

input_numbers = [5, 15, 1, 3, 2, 10]


class DividedByTest(unittest.TestCase):

    def test_least_common_multiple_pass(self):
        self.assertEqual(least_common_multiple(input_numbers), 30)

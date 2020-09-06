import unittest
from GetWhileEmpty import *

input_1_6_list = [1,2,3,4,5,6,""]
input_1_3_list = [1,2,3,"",5,6,]
input_empty_list = ["",1,2,3]
class get_while_empty_test(unittest.TestCase):

    def test_get_while_empty_pass(self):
        self.assertEqual(get_while_empty(input_1_6_list),[6,5,4,3,2,1])

    def test_get_while_empty1_pass(self):
        actual = get_while_empty(input_1_3_list)
        expected = [3,2,1]
        self.assertEqual(actual, expected)

    def test_empty_list_pass(self):
        self.assertEqual(get_while_empty(input_empty_list), [])
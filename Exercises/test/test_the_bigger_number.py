import unittest
from TheBiggerNum import the_bigger_number

not_numbers_list = [3, "3", "3r4", 6, 5, 34, 322.3, 22, 100]
int_numbers_list = [3, 3, 34, 6, 5, 34, 322.3, 22, 100, 0]
str_numbers_list = [3, "3", "34", 6, 5, 34, 322.3, "22", 100]


class TheBiggerNumberTest(unittest.TestCase):

    def test_int_list_pass(self):
        my_big_num = the_bigger_number(int_numbers_list)
        py_big_num = max(int_numbers_list)
        self.assertEqual(my_big_num, py_big_num)

    def test_not_numbers_list_raise_exception(self):
        self.assertRaises(ValueError, the_bigger_number, not_numbers_list)

    def test_str_numbers_list_pass(self):
        self.assertEqual(the_bigger_number(str_numbers_list), 322.3)

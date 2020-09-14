import math
from typing import Union, List

Nums = Union[int, float]


def divided_by(input_num: Nums, input_numbers: List[Nums]) -> bool:
    for num in input_numbers:
        if not divmod(input_num, num)[1] == 0:
            return False
        else:
            return True

    # for num in input_numbers:
    #     try:
    #         if not divmod(input_num, num)[1] == 0:
    #             return False
    #     except:
    #         raise TypeError(f"either {input_num} or {num} is not a number ")
    # return True


def get_common_divided(list):
    return math.prod(list)


"""
Uri's comments:
==============

* In Python it's common to use variable names in lowercase. You can use "_" to separate between words.
  For example, use "nums" instead of "Nums".

"""

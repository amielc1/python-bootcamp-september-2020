import math
from typing import Union, List

Nums = Union[int, float]


def divided_by(input_num: Nums, input_numbers: List[Nums]) -> bool:
    for num in input_numbers:
        if not divmod(input_num, num)[1] == 0:
            return False
    return True

def get_common_divided(list):
    return math.prod(list)

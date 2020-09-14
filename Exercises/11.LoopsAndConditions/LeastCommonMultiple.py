from DividedBy import *
from typing import Union, List

Nums = Union[int, float]


def least_common_multiple(input_numbers: List[Nums]) -> Nums:
    for less_mult in range(max(input_numbers), math.prod(input_numbers)):
        if divided_by(less_mult, input_numbers):
            return less_mult

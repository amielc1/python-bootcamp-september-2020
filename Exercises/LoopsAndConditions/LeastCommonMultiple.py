import math
from DividedBy import *


def least_common_multiple(input_numbers):
    for less_mult in range(max(input_numbers), math.prod(input_numbers)):
        if divided_by(less_mult, input_numbers):
            return less_mult

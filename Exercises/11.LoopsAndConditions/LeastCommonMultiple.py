import math
from DividedBy import *

# 1. I can't see a good reason to separate this function from its helper divided_by
# 2. I think you can find a more efficient way to solve this
#    (by checking less numbers)
def least_common_multiple(input_numbers):
    for less_mult in range(max(input_numbers), math.prod(input_numbers)):
        if divided_by(less_mult, input_numbers):
            return less_mult

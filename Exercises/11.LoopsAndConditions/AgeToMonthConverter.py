import math


def convert_age_to_month(age: float) -> int:
    return math.trunc(float(age) * 12)

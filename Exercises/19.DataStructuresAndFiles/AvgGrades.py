import sys
from statistics import mean


def get_above_average_grades(input_grads: list) -> list:
    grades = [int(n) for n in input_grads]
    average = mean(grades)
    above_average = [n for n in grades if n > average]
    return above_average


print(get_above_average_grades(sys.argv[1:]))

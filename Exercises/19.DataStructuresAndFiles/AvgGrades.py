import sys
from statistics import mean


def get_above_average_grades(input_grads: list) -> list:
    grades = [int(n) for n in input_grads]
    average = mean(grades)
    above_average = [n for n in grades if n > average]
    return above_average


print(get_above_average_grades(sys.argv[1:]))

"""
Uri's comments:
==============

* Very good! This code works.
* You might want to display an error message if the user ran the program without
  parameters instead of raising an exception. Also, write how to use the program
  in the error message.

"""

import math


def convert_age_to_month(age: float) -> int:
    return math.trunc(float(age) * 12)


"""
Uri's comments:
==============

* The input part of the assignment is missing. You should ask the user for input
  and then print the result. I can't run your exercises without it.
  This is relevant to all your exercises.
* It's better to use .gitignore to not commit .idea files to the repository
  (PyCharm internal files).

"""

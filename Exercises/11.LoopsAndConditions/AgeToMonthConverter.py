"""
Ynon's Comments (general)

1. Hi :) So I see you used functions and I assume the goal was to make this code easier to test. That's awesome.
   I did send you the pytest webinar to watch - using pytest you would have been able to test even normal input
   calls without a problem.

2. In python when you see a function that has __ around its name (like __trunc__()) it means this function
   should be called through some special syntax of the language.

   For example: a string in python has the method __len__, but to get the actual length we normally write:
   print(len("hello"))

   And not
   print("hello".__len__())
   
   (though the second also works)

   Same goes for __trunc__. In this case __trunc__ is called by using math.trunc such as:

   import math
   math.trunc(2.5) # returns 2

   A full list of these functions is available here:
   https://rszalski.github.io/magicmethods/
"""

def convert_age_to_month(age):
    # I personally don't use this structure to force types but use type hints instead
    # please watch the lesson on them here:
    # https://www.tocode.co.il/bundles/advanced-python3/lessons/type-hints
    try:
        val = (float(age) * 12).__trunc__()
    except TypeError:
        raise (f"{age} is not a number")
    return val



# Indentation is huge here, I think 2 spaces would suffice
# Also when you use variable names such as input_num and input_numbers
# it's highly recommended to add type hints (because the name doesn't mean anything)
def divided_by(input_num, input_numbers):
    """ Finally a function in python has a docstring,
    you write it using 3 quotes at the beginning, and it helps
    everyone understand what the function do.
    You can read more about docstring best practices here:
    https://www.python.org/dev/peps/pep-0257/
    """
    for num in input_numbers:
        try:
            # see previous comment on __trunc__
            # can you figure out how to reformat this code to not use the __ version of the function?
            if not input_num.__divmod__(num)[1] == 0:
                return False
        except:
            raise TypeError(f"either {input_num} or {num} is not a number ")
    return True

def get_common_divided(list):
    t = 1
    for n in list:
        t *= n
    return t

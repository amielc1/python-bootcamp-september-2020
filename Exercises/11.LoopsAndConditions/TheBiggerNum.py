def the_bigger_number(list_of_numbers):
    # Why -1 ? What if all the numbers would actually be smaller than this value?
    # In python you can use float("-inf") to create the smallest possible value,
    # so I would write:
    big = float("-inf")
    for num in list_of_numbers:
        try:
            num = float(num)
            if num > big:
                big = num
        except ValueError:
            raise ValueError(f"{num} is not a number")
    return big

# As a side not - python has a build-in function called max()
# that is useful for questions like this. You can find a list of all
# python's built-in functions here:
# https://docs.python.org/3/library/functions.html

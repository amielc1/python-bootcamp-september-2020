def the_bigger_number(list_of_numbers):
    big = -1
    for num in list_of_numbers:
        try:
            num = float(num)
            if num > big:
                big = num
        except ValueError:
            raise ValueError(f"{num} is not a number")
    return big

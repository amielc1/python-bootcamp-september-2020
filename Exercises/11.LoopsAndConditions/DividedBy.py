def divided_by(input_num, input_numbers):
    for num in input_numbers:
        try:
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

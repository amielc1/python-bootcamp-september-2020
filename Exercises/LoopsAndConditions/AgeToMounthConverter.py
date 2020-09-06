def convert_age_to_mounth(age):
    try:
        val = (float(age) * 12).__trunc__()
    except TypeError:
        raise(f"{age} is not a number")
    return  val
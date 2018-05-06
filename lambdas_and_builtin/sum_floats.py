def sum_floats(*args):
    floats = [num for num in args if type(num) == float]
    return sum(floats)

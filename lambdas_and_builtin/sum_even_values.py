def sum_even_values(*args):
    even_values = [num for num in args if num % 2 == 0]
    return sum(even_values)

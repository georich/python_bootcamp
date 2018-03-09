def number_compare(a, b):
    """
    >>> number_compare(1, 1)
    'Numbers are equal'
    >>> number_compare(2, 1)
    'First is greater'
    >>> number_compare(1, 2)
    'Second is greater'
    """
    if a == b:
        return "Numbers are equal"
    elif a > b:
        return "First is greater"
    return "Second is greater"

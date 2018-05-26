def compact(li):
    """
    >>> compact([1, 0, [], -1])
    [1, -1]
    """
    return [value for value in li if value]

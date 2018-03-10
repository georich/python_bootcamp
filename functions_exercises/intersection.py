def intersection(li1, li2):
    """
    >>> intersection([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    return [value for value in set(li1) & set(li2)]

def frequency(li, search_term):
    """
    >>> frequency([1, 2, 3, 4, 4, 4], 4)
    3
    >>> frequency([1, 2, 3, 4], 5)
    0
    """
    return li.count(search_term)

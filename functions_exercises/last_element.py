def last_element(values):
    """
    >>> last_element([]) is None
    True
    >>> last_element([1, 2, 3, 4])
    4
    >>> last_element([1])
    1
    >>> last_element([1, 2, 3, '4'])
    '4'
    """
    if len(values) == 0:
        return None
    return values[-1]


def return_day(num):
    """
    >>> return_day(1)
    'Sunday'
    >>> return_day(7)
    'Saturday'
    >>> return_day(10) is None
    True
    """
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(num)

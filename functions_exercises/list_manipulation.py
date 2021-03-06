def list_manipulation(li, command, location, value = None):
    """
    >>> list_manipulation([1,2,3], 'add', 'beginning', 20)
    [20, 1, 2, 3]
    >>> list_manipulation([1,2,3], 'remove', 'end')
    3
    """
    if command == "remove":
        if location == "end":
            return li.pop()
        if location == "beginning":
            return li.pop(0)
    elif command == "add":
        if location == "beginning":
            li.insert(0, value)
            return li
        if location == "end":
            li.append(value)
            return li

print(list_manipulation([1,2,3], "add", "beginning", 20))

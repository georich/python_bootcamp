def partition(li, fn):
    trues = []
    falses = []
    for value in li:
        if fn(value):
            trues.append(value)
        else:
            falses.append(value)
    return [trues, falses]

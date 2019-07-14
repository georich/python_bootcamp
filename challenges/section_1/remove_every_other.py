def remove_every_other(list_in):
    if len(list_in) > 1:
        new_list = []
        index = 1
        for item in list_in:
            if index % 2 != 0:
                new_list.append(item)
            index += 1
        return new_list
    return list_in

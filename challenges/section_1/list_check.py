def list_check(list_in):
    for item in list_in:
        if type(item) != list:
            return False
    return True

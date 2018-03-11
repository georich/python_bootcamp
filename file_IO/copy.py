def copy(first_file, second_file):
    with open(first_file) as original:
        with open(second_file, "w") as to_copy:
            to_copy.write(original.read())

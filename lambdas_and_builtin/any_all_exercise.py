def is_all_strings(string_iter):
    return all(type(item) == str for item in string_iter)


print(is_all_strings(["a", "b", "c"]))
print(is_all_strings(["a", "b", "c", 4]))
print(is_all_strings(["a", "b", "c", "def"]))

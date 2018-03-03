def interleave(string1, string2):
    zipped_strings = list(zip(string1, string2))
    joined2 = ["".join(part) for part in zipped_strings]
    final_string = "".join(joined2)
    return final_string

print(interleave("hi", "ha"))
print(interleave("sna", "udy"))

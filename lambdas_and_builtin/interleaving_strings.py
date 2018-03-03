def interleave(string1, string2):
    return "".join("".join(part) for part in zip(string1, string2))

print(interleave("hi", "ha"))
print(interleave("sna", "udy"))

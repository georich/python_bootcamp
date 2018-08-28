cat = {"name": "Minnie", "age": 8, "fat": True}

# cat.clear() # will clear dictionary
feline = cat.copy()  # will copy dictionary
user = {}.fromkeys(
    ["email", "phone", "address"], "unknown"
)  # will make a dictionary with all keys assigned value unknown

print(cat.get("name"))
print(cat.get("colour"))  # will print None instead of KeyError

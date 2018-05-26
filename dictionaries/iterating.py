cat = {
    "name": "Minnie",
    "age": 8,
    "fat": True
}

for value in cat.values():
    print(value)

for key in cat.keys():
    print(key)

for key, value in cat.items(): # tuple comprehension?
    print(f"key is {key}, value is {value}")

cat = {
    "name": "Minnie",
    "age": 8,
    "fat": True
}

cat.pop("fat") # removes key-value pair, will give KeyError if key doesn't exist, also returns value
cat.popitem() # removes random key-value pair, returns key-value pair

cat = {
    "name": "Minnie",
    "age": 8,
    "fat": True
}

feline = {"mammal": True}
feline.update(cat) # will update keys and values with another set of pairs
print(feline) # similar to extend for lists then?

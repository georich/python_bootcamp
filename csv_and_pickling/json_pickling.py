import json
import jsonpickle


class Cat():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat("Minnie", "Ginger Tabby")

# j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
j = json.dumps(c.__dict__)
with open("cat.json", "w") as file:
    frozen = jsonpickle.encode(c)
    print(frozen)
    file.write(frozen)

print(j)

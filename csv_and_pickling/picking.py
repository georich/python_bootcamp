import pickle


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


minnie = Cat("Minnie", "Ginger Tabby", "Mouse")
with open("pets.pickle", "wb") as file:
    pickle.dump(minnie, file)

with open("pets.pickle", "rb") as file:
    returned_minnie = pickle.load(file)
    print(returned_minnie)
    print(returned_minnie.play())

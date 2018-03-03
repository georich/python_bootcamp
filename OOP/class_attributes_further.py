class Pet:
    allowed = ["cat", "dog", "fish", "parrot"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.species = species

cat = Pet("Minnie", "cat")
dog = Pet("Lucky", "dog")
#tiger = Pet("Tony", "Tiger")
#cat.set_species("tiger")

Pet.allowed.append("pig")
pig = Pet("Percy", "pig")

cat.allowed = ["cat", "tiger"]
print(cat.allowed)
print(Pet.allowed)
print(dog.allowed)

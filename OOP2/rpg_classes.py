class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        print(f"{self.name} says: 'I heard there were monsters running around last night!'")

villager = NPC("Bob", 10, 12)
villager.name
villager.hp
villager.level
villager.speak()

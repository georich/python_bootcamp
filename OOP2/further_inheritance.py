class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

    @classmethod
    def display_active_user(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_total_mods(cls):
        return f"There are currently {cls.total_mods} total mods"

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"

# user4 = User.from_string("Tom,Jones,89")
# print(user4)
jasmine = Moderator("Jasmine", "O'Connor", 51, "Piano")
print(jasmine.full_name())
print(jasmine.community)

user1 = User("Tom", "Garcia", 21)
print(user1.full_name())
print(User.display_active_user())
print(Moderator.display_total_mods())

class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
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

user1 = User("Joe", "Bloggs", 52)
user2 = User("George", "Richards", 23)
print(User.display_active_user())
user3 = User("Alice", "Purcell", 21)
print(User.display_active_user())

user4 = User.from_string("Tom,Jones,89")
print(user4.first)
print(user4.full_name())
print(user4.age)
print(user4.birthday())

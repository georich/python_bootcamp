class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
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

print(User.active_users)

user1 = User("Joe", "Bloggs", 52)
user2 = User("George", "Richards", 23)
print(user2.full_name())
print(user2.initials())
print(user2.likes("cats"))
print(user2.birthday())
print(user2.age)

print(User.active_users)

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

user4 = User.from_string("Tom,Jones,89")
print(user4)

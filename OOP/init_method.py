class User:
    def __init__(self, first, last, age):
        #print("A new user has been created")
        self.first = first
        self.last = last
        self.age = age

user1 = User("Joe", "Bloggs", 52)
user2 = User("George", "Richards", 23)
print(user2.first, user2.last)

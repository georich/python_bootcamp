# class Human:
#     def __init__(self, height):
#         self.height = height
    
#     def __len__(self):
#         return self.height

# george = Human(67)
# print(len(george))

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last}, age {self.age}"
    
    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Jeb", last=self.last, age=0)
        return "You can't add that!"

g = Human("George", "Richards", 23)
print(g)
print(len(g))

a = Human("Alice", "Purcell", 21)

print(g + a)

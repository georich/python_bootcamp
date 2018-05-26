class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        # self.age = age
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    
    # def get_age(self):
    #     return self._age
    
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

george = Human("George", "Richards", 23)
# print(george.age)
# print(george.get_age())
# george.age = -100 # nothing currently stopping us from writing this
print(george.age)
george.age = 24
print(george.age)
print(george.full_name)

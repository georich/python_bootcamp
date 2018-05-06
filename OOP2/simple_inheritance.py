class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    pass

minnie = Cat()
minnie.make_sound("meow!")
# print(minnie.cool)
# print(Cat.cool)
# print(Animal.cool)

print(isinstance(minnie, Cat))
print(isinstance(minnie, Animal))
print(isinstance(minnie, object))

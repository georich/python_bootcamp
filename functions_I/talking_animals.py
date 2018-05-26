def speak(animal = "dog"):
    """Returns the noise a specified animal should make"""
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

print(speak())
print(speak.__doc__)

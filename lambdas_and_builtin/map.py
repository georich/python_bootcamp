nums = [2, 4, 6, 8, 10]

doubles = map(lambda x: x * 2, nums)
doubles = list(doubles) # need to convert to list
print(doubles)

people = ["Darcy", "Christina", "Dana", "Annabel"]
peeps = map(lambda name: name.upper(), people)
peeps = list(peeps)
print(peeps)

# list comprehensions can provide similar results

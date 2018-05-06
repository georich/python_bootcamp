# returns only values which return true to the lambda

l = [1, 2, 3, 4]

evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)

# combining filter and map

names = ["Lassie", "Colt", "Rusty"]

#return a list with the string "Your instructor is "
# + each value in array, only if less than 5 characters
# sends filtered names into the map function

filtered_names = list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) < 5, names)))
print(filtered_names)

# list comprehension solution, much more pythonic solution

filtered_list_comp_names = [f"Your instructor is {name}" for name in names if len(name) < 5]
print(filtered_list_comp_names)

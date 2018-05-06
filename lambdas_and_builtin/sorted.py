# returns a new sorted list from the items in the iterable
numbers = [6, 1, 8, 2]
print(sorted(numbers))
print(numbers) # original list unchanged, as opposed to .sort()
print(sorted(numbers, reverse=True))

# if sorting a dict will need to add extra parameters
# i.e. sorted(dictionary, key=len)

songs = [
    {"title": "Happy Birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(sorted(songs, key=lambda s: s["playcount"]))

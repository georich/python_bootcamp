songs = [
    {"title": "Happy Birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(min(songs, key=lambda s: s["playcount"]))
print(max(songs, key=lambda s: s["playcount"]))
print(max(songs, key=lambda s: s["playcount"])["title"])

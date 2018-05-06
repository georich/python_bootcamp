def make_song(count=99, beverage="soda"):
    for num in range(count, -1, -1):
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall."
        elif num == 1:
            yield f"Only 1 bottle of {beverage} left!"
        else:
            yield f"No more {beverage}!"

default_song = make_song()
for line in default_song:
    print(line)

coke_song = make_song(20, "coke")
for line in coke_song:
    print(line)

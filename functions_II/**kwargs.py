# gathers remaining keyword arguments as a dictionary

def fav_colors(**kwargs):
    #print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favourite colour is {color}")

fav_colors(colt = "purple", ruby="red", ethel="teal")

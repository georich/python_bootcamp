# try:
#     something
# except NameError:
#     print("You tried to use a variable that hasn't been declared")

d = {"name": "George"}
#d["city"] # key error

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(d, "name"))
print(get(d, "city"))

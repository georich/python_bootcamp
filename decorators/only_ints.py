from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if all(type(item) == int for item in args):
            return fn(*args, **kwargs)
        return "Please only invoke with integers."
    return wrapper

@only_ints
def add(x, y):
    return x + y

print(add(1, 2))
print(add("1", "2"))

from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # print(args)
        value = fn(*args, **kwargs)
        return [value, value]
    # print(wrapper)
    return wrapper

@double_return
def add(x, y):
    return x + y

print(add(1, 2))

from functools import wraps
from time import sleep

def delay(wait):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Waiting {wait}s before running {fn.__name__}")
            sleep(wait)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi())

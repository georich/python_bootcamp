def log_function_data(fn):
    def wrapper(*args, **kwargs):
        """wrapper function"""
        print(f"You are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    """adds two numbers together"""
    return x + y

print(add(10, 20))

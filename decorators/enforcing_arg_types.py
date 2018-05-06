def enforce(*types):
    def decorator(fn):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return fn(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg("hello", "3") # 3 will be converted to an int

@enforce(float, float)
def divide(a, b):
    print(a / b)

divide(1, 2)
divide("5", 2.0)

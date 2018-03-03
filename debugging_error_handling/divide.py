def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You are dividing by zero...")
    except TypeError as err:
        print("a and b must both be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

divide(1, 2)
divide(1, 0)
divide(1, "a")

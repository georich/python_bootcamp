# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y

# print(add_positive_numbers(1, 2))
# print(add_positive_numbers(1, -1))

def eat_junk(food):
    assert food in [
        "pizza",
        "ice cream",
        "candy",
        "fried butter"
    ], "food must be junk!"
    return f"I am eating {food}!"

food = input("Enter a food to eat please: ")
print(eat_junk(food))

# assertions will be ignored if -O flag is used to run the python file

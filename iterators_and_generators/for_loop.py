def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
            func(thing)
        except StopIteration:
            print("End of iterator.")
            break

def square(x):
    print(x * x)

# my_for("hello")
my_for([1, 2, 3, 4], print)
my_for([1, 2, 3, 4], square)

def square(a):
    return a * a

square2 = lambda a: a * a # similar to anon function

print(square(9))
print(square2(9))

add = lambda a, b: a + b

print(add(3, 10))

# useful for passing a function into another function that will only be used one time

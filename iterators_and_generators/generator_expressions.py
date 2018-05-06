def nums():
    for num in range(1, 10):
        yield num

g = nums()
print(g)
print(list(g))

h = (num for num in range(1, 10))
print(h) # <genexpr>
print(list(h))

print(sum([num for num in range(1, 10)]))
print(sum((num for num in range(1, 10))))

from random import randint

x = randint(-100, 100)
while x == 0:
    x = randint(-100, 100)

y = randint(-100, 100)
while y == 0:
    y = randint(-100, 100)

check_x = x > 0
check_y = y > 0
if check_x and check_y:
    print("both positive")
elif not check_x and not check_y:
    print("both negative")
elif check_x and not check_y:
    print("x is positive and y is negative")
else:
    print("y is posiive and x is negative")

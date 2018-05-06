def get_multiples(num=1, count=10):
    value = num
    iterations = 1
    while iterations <= count:
        yield value
        value += num
        iterations += 1

default_multiples = get_multiples()
print(list(default_multiples))

def get_unlimited_multiples(num=1):
    value = num
    while True:
        yield value
        value += num

ones = get_unlimited_multiples()
print([next(ones) for i in range(20)])

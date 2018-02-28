def multiply_even_numbers(li):
    product = 1
    for num in li:
        if num % 2 == 0:
            product *= num
    return product

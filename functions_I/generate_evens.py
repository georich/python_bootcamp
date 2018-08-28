def generate_evens():
    return [num for num in range(1, 50) if num % 2 == 0]


evens = generate_evens()
print(evens)

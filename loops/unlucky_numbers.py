for num in range(1,21):
    if num == 4 or num == 13:
        result = "unlucky"
    elif num % 2 == 0:
        result = "even"
    else:
        result = "odd"
    print(f"{num} is an {result} number.")

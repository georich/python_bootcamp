# *arg, special operator to pass to functions
# will gather remaining arguments as a tuple

#def sum_all_nums(num1, num2, num3):
#    return num1 + num2 + num3

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(4, 6, 9))
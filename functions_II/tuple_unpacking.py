def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

#sum_all_values(1, 30, 2, 5, 6)
nums = [1, 2, 3, 4, 5, 6] # need to unpack this into single elements
sum_all_values(*nums) # adding the asterik will pass each element in as seperate argument

numbers = (1, 2, 3, 4, 5, 6) # also works for tuples
sum_all_values(*numbers) 

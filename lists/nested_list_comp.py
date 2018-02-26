nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#for l in nested_list:
#    for val in l:
#        print(val)

[[print(val) for val in l] for l in nested_list]

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# answer = {}
# for i in range(0, 3):
#    answer[list1[i]] = list2[i]
# print(answer)
answer = {list1[i]: list2[i] for i in range(0, 3)}

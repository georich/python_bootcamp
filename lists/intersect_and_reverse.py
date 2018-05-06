numbers1 = [1, 2, 3, 4]
numbers2 = [3, 4, 5, 6]
answer = [num for num in numbers1 if num in numbers2]
print(answer)

names = ["Elie", "Tim", "Matt"]
answer2 = [name[::-1].lower() for name in names]
print(answer2)

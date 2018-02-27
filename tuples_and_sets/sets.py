# will not contain duplicate values
# will not be ordered
# cannot access via index

s = {1, 4, 5}
print(4 in s)

s2 = set({1, 2, 3, 4, 4, 4})
print(s2)
s2.add(4) # will not do anything due to duplicate
s2.remove(4) # reports KeyError if it doesn't find value
s3 = s2.copy()
s3.clear()

# Union
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
students = math_students | biology_students
taking_both_classes = math_students & biology_students
print(students)
print(taking_both_classes)

nums = [1, 2, 3]
nums2 = [x * 10 for x in nums]
print(nums2)

name = "george"
upper_name = [char.upper() for char in name]
print(upper_name)

with_vowels = "This is so much fun!"
without_vowels = "".join(char for char in with_vowels if char not in "aeiou")
print(without_vowels)

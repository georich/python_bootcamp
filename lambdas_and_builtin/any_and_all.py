# all will return true if iterable is empty

all([0, 1, 2, 3]) # False

all([char for char in "eio" if char in "aeiou"]) # True

people = ["Charlie", "Casey", "Cody", "Charlie"]
print(all([name[0] == "C" for name in people]))

# any will return false if iterable is empty

any([0, 1, 2, 3]) # True

nums = [2, 3, 4, 5]
any([num % 2 == 0 for num in nums]) # True
any(num % 2 == 0 for num in nums) # True
# code in brackets acts as a generator, don't need list as 
# it is a middleman

import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List comprehension: {list_comp} bytes")
print(f"Generator expression: {gen_exp} bytes")

import re

# define out phone number regex
pattern = re.compile(r"\d{3} \d{3}-\d{4}")  # only compiled once

# search a string with our regex
result = pattern.search("Call me at 543 666-9876!")
# .search() only finds first match
# .findall() finds all matches in a list

res = re.search(
    r"\d{3} \d{3}-\d{4}", "Call me at 655 222-4563"
)  # shorter way, but regex object is compiled EVERY time
print(res.group())

grouping = result.group()
print(grouping)

# capturing match groups
regex_capture = re.compile(r"(?P<areacode>\d{3}) (\d{3}-\d{4})")
matches = regex_capture.search("Call me at 444 333-2222")
print(matches.groups())
print(matches.group(0))
print(matches.group("areacode"))
print(matches.group(1))
print(matches.group(2))

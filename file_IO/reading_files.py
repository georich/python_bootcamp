file = open("story.txt")
print(file.read())

print(file.read())
file.seek(0) # will send cursor back to beginning

print(file.read())

file.seek(0)
print(file.readlines()) # puts each line in a seperate string in a list
file.close()
print(file.closed)

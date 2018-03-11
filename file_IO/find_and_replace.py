def find_and_replace(file_name, word_find, replace):
    with open(file_name, "r") as file:
        text = file.read()
    
    new_text = text.replace(word_find, replace)
    
    with open(file_name, "w") as file:
        file.write(new_text)

print(find_and_replace("alice.txt", "Alice", "George"))

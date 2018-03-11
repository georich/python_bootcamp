def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        file.seek(0)
        text = file.read()
    
    number_of_lines = len(lines)
    list_of_words = text.replace('\n', ' ').split(' ')
    number_of_words = len(list_of_words)
    blob_words = ''.join(text)
    character_count = len(blob_words)
    
    return {"lines": number_of_lines, "words": number_of_words, "characters": character_count}

print(statistics("alice.txt"))

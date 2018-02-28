def multiple_letter_count(phrase):
    return {phrase[i]: phrase.count(phrase[i]) for i in range(0, len(phrase))}

print(multiple_letter_count("awesome"))

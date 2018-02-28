def multiple_letter_count(phrase):
    return {letter: phrase.count(letter) for letter in phrase}

print(multiple_letter_count("awesome"))

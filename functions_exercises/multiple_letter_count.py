def multiple_letter_count(phrase):
    """
    >>> multiple_letter_count('awesome')
    {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}
    >>> multiple_letter_count('AAAAAAH!')
    {'A': 6, 'H': 1, '!': 1}
    """
    return {letter: phrase.count(letter) for letter in phrase}

print(multiple_letter_count("awesome"))

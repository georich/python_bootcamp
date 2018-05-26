def single_letter_count(phrase, letter):
    """
    >>> single_letter_count('Hello', 'l')
    2
    >>> single_letter_count('aeiou', 'm')
    0
    >>> single_letter_count('Capital', 'c')
    1
    """
    return phrase.lower().count(letter.lower())

def capitalize(word):
    """
    >>> capitalize("george")
    'George'
    >>> capitalize("George")
    'George'
    """
    return f"{word[0].upper()}{word[1::]}"

print(capitalize("george"))

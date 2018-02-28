def is_palindrome(word):
    reduced = word.lower().replace(" ", "")
    return reduced == reduced[::-1]

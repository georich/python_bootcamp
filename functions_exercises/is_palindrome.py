def is_palindrome(word):
    """
    >>> is_palindrome("")
    False
    >>> is_palindrome("a")
    True
    >>> is_palindrome("aabaa")
    True
    >>> is_palindrome("abbaa")
    False
    """
    if len(word) == 0:
        return False
    reduced = word.lower().replace(" ", "")
    return reduced == reduced[::-1]

import keyword

def contains_keyword(*args):
    return any(keyword.iskeyword(word) for word in args)

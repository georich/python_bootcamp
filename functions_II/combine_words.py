def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return f"{kwargs['prefix']}{word}"
    elif "suffix" in kwargs:
        return f"{word}{kwargs['suffix']}"
    return word

print(combine_words("child"))
print(combine_words("child", prefix = "man"))
print(combine_words("child", suffix = "ish"))

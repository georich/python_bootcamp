from random import choice

def greet(person):
    def get_mood():
        message = choice(["Hello there", "Go away", "I love you"])
        return message
    
    # return get_mood() + person
    return "{} {}".format(get_mood(), person)

print(greet("George"))

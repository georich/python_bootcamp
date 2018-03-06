def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is George.")

def rage():
    print("I AM REALLY MAD!")

# greet is wrapped in the be_polite function
# being decorated
greet = be_polite(greet)
greet()

polite_rage = be_polite(rage)
polite_rage()

from random import randint

number = randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Correct!")
    elif guess < number:
        print("You guessed too low, try again!")
    else:
        print("You guessed too high, try again!")

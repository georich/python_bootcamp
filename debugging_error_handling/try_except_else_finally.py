while True:
    try:
        num = int(input("Please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("This is the else, number correctly entered")
        break # finally still runs
    finally:
        print("This appears no matter what")
print("Rest of code...")

from csv import reader

def print_users():
    with open("users.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)
        for row in csv_reader:
            print(" ".join(row))
            
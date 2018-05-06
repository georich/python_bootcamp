from csv import reader


def find_user(first_name, last_name):
    with open("users.csv", "r") as file:
        csv_reader = reader(file)
        next(csv_reader)
        count = 1
        for row in csv_reader:
            if row == [first_name, last_name]:
                return count
            count += 1
        return f"{first_name} {last_name} not found."

from csv import reader

with open("trees.csv") as file:
    csv_reader = reader(file) # this is an iterator
    next(csv_reader) # this moves the cursor passed the headers
    for row in csv_reader:
        print(row)

from csv import DictReader

with open("trees.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # print(row)
        print(row[" \"Height (ft)\""])

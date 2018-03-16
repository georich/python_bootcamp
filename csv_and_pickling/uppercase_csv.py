from csv import reader, writer

with open("writing_test.csv") as file:
    csv_reader = reader(file)
    cats = [[s.upper() for s in row] for row in csv_reader]
    for row in csv_reader:
        print(row)

with open("uppercase_cats.csv", "w") as file:
    csv_writer = writer(file)
    for cat in cats:
        csv_writer.writerow(cat)

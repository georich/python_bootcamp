from csv import writer

with open("writing_test.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Colour"])
    csv_writer.writerow(["Minnie", "Ginger"])
    csv_writer.writerow(["Alex", "Black and White"])
    csv_writer.writerow(["TJ", "Ginger"])

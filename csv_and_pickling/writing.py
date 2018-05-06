from csv import writer, DictWriter

# with open("writing_test.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Colour"])
#     csv_writer.writerow(["Minnie", "Ginger"])
#     csv_writer.writerow(["Alex", "Black and White"])
#     csv_writer.writerow(["TJ", "Ginger"])

with open("cats.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Minnie",
        "Breed": "Orange Tabby",
        "Age": 9
    })

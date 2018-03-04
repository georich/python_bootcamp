def yes_or_no():
    while True:
        yield "yes"
        yield "no"

for answer in yes_or_no():
    print(answer)

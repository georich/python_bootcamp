person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# answer = {person[i][0]: person[i][1] for i in range(0, 3)}
answer = dict(person)
print(answer)

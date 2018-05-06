midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["dan", "ang", "kate"]

final_grades = [max(pair) for pair in zip(midterms, finals)]
print(final_grades)

final_grades_dict = {value[0]: max(value[1], value[2]) for value in zip(students, midterms, finals)}
print(final_grades_dict)

scores = map(
    lambda pair: max(pair),
    zip(midterms, finals)
)
print(list(scores))

scores_extra = zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)
print(dict(scores_extra))

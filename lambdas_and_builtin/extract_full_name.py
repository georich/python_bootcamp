def extract_full_name(entries):
    return list(map(lambda name: f"{name['first']} {name['last']}", entries))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))

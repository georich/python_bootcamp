import sqlite3

conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()

# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = "INSERT INTO friends VALUES ('Alice', 'Purcell', 10);"

# BAD WAY
# form_first = "Minnie"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}');"
# c.execute(query)

# BETTER WAY
# form_first = "Alex"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query)

# EVEN BETTER WAY
# data = ("Steve", "Irwin", 9)
# query = "INSERT INTO friends VALUES (?,?,?)"
# c.execute(query, data)

# people = [
#     ("Roald", "Amundsen", 5),
#     ("Rosa", "Parks", 8),
#     ("Henry", "Hudson", 7),
#     ("Neil", "Armstrong", 7),
#     ("Daniel", "Boone", 3),
# ]

# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#     print("INSERTING NOW")  # could be something else just example

c.execute("SELECT * FROM friends")
# for result in c:
    # print(result) # prints each tuple
print(c.fetchall()) # prints a list containing the tuple values

# commit changes
conn.commit()

conn.close()

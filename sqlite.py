# import sqlite3

# conn = sqlite3.connect('mydatabase1.db')
# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                   (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", ("Alice", 25))
# cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", ("Bob", 30))

# conn.commit()


# cursor.execute("SELECT * FROM users")
# result = cursor.fetchone()
# print(f'User: {result[1]}, age : {result[2]}')

# import sqlite3
# conn = sqlite3.connect('memory')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)''')
# cursor.execute("INSERT INTO users VALUES ('Tobias', 28)")
# conn.commit()

# cursor.execute('SELECT * FROM users')
# print(cursor.fetchall())
# result = cursor.fetchone()
# print(f'User: {result[0]}, Age: {result[1]}')



import sqlite3
conn = sqlite3.connect('new_database.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users( 
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER)''')
conn.commit()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)",("Alice",25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob",30))
cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", ("George",38))
cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", ("Zoi", 31))

conn.commit()

users = [("Charlie",22), ("Diana",28)]

conn.commit()
cursor.execute("SELECT * FROM users")
row = cursor.fetchall()
while row:
    print(row)
    row = cursor.fetchone()
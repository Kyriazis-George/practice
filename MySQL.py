# import sqlite3

# conn = sqlite3.connect("example.db")
# cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY,
#             name TEXT NOT NULL,
#             age INTEGER
# )
# ''')

# cur.execute('''CREATE TABLE IF NOT EXISTS user_jobs (
#             id INTEGER PRIMARY KEY,
#             user_id INTEGER,
#             name TEXT NOT NULL,
#             job TEXT,
#             income REAL,
#             FOREIGN KEY (user_id) REFERENCES user (id))
#             ''')

# cur.execute('INSERT INTO users (name, age) VALUES (?,?)', ('George', 38))
# cur.execute('INSERT INTO users (name, age) VALUES (?,?)', ('John',33))
# conn.executemany("INSERT INTO users (name, age) VALUES (?,?)",[("Bob",24),("Carol",29)])
# conn.executemany("INSERT INTO users (name, age) VALUES (?,?)", [("Zoi", 31),("Athina", 30)])
# conn.commit()

# cur.execute("select * from users")
# users = cur.fetchall()
# # cur.execute("SELECT name from users")
# # users = cur.fetchall()




# job_data = {
#     "George": ("Engineer", 72000),
#     "John": ("Designer", 58000),
#     "Bob": ("Technician", 45000),
#     "Carol": ("Manager", 63000),
#     "Zoi": ("Analyst", 52000),
#     "Athina": ("Teacher", 49000)
# }

# cur.execute("select id, name, age from users")
# users = cur.fetchall()


# for user_id, name, age in users:
#     job, income = job_data.get(name, ("Unknown", 0))
#     cur.execute(
#         'INSERT INTO user_jobs (user_id, name, age, job, income) VALUES (?, ?, ?, ?, ?)',
#         (user_id, name, age, job, income)
#     )
# conn.commit()
    
# cur.execute("select id, name from users")
# users = cur.fetchall()









# cur.execute("SELECT * FROM users")
# rows = cur.fetchall()
# names = ",".join([row[1] for row in rows])
# print(names)


# cur.execute("SELECT DISTINCT name FROM users WHERE age >= 31")
# rows = cur.fetchall()
# names = ",".join([row[0] for row in rows])
# print(names)

# cur.execute("SELECT DISTINCT name, age FROM users")
# rows = cur.fetchall()
# formatted = [f"{row[0]} ({row[1]})" for row in rows]
# output = ", ".join(formatted)
# print(output)

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # replace with your real password
)

print("Connected!", connection)
connection.close()
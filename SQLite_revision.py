import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# cursor.execute("""
#                create table if not exists students (
#                ig integer primary key autoincrement,
#                name text not null,
#              grate real)
#                """)
# conn.commit()

# # cursor.execute("insert into students (name, grate) values (?,?)",("Maria", 18.6))
# # cursor.execute("insert into students (name, grate) values (?,?)",("Nikos",15.0))
# # conn.commit()

# cursor.execute("select * from students")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# cursor.execute("delete from students where name = ?",("Nikos",))
# conn.commit()    

cursor.execute("Select * from students")
rows = cursor.fetchall()

for row in rows:
    print(row)
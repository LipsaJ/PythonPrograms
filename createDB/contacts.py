import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('Lipsa', 6578901, 'lipsa@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Hanz', 12345, 'hanz@gmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone()) # as there nothing more to fetch so its none

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("--"*20)

db.commit()
db.close()

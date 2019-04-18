import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Please enter the name: ")
#
# select_sql = "SELECT * FROM contacts WHERE name = ?"
# select_cursor = db.cursor()  # we have used the cursor to update so that we can see how many rows were updated
# select_cursor.execute(select_sql, name)
# print("{} rows got selected".format(select_cursor.rowcount))

for rows in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
    print(rows)
db.close()

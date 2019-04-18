import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = 'updatenew@gmail.com'
phone = input("Please enter the phone number:")

# update_sql = "UPDATE contacts SET email = 'updatenew@gmail.com' WHERE phone = {}".format(phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
update_cursor = db.cursor()  # we have used the cursor to update so that we can see how many rows were updated
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows got updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-'*20)

# we didn't commit the changes in previous, that is why now we are not getting anything
# rollback done

db.close()

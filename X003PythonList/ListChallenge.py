
menu = []
menu.append(["eggs", "Meat", "Bacon", "Sausage"])
menu.append(["eggs", "Meat", "Spam", "Sausage"])
menu.append(["eggs", "Spam", "Bacon", "Sausage"])
menu.append(["Spam", "Meat", "Bacon", "Sausage"])
menu.append(["Spam", "Spam", "Bacon", "Sausage"])
menu.append(["eggs", "Meat", "Spam", "Spam"])
menu.append(["Spam", "Meat", "Spam", "Sausage"])
menu.append(["Spam", "Meat", "Bacon", "Spam"])
menu.append(["eggs", "Spam", "Spam", "Sausage"])
menu.append(["eggs", "Spam", "Bacon", "Spam"])
menu.append(["eggs", "Spam", "Spam", "Spam"])

# print(menu)

for meals in menu:
    if "Spam" not in meals:
        print(meals)
        for food in meals:
            print(food)


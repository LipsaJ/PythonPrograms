Shopping_List = ["Eggs", "Milk", "Meat", "Spam", "Butter"]
item: str
for item in Shopping_List:
    if item == "Spam":
        continue
    print("Buy "+item)

nasty_food = ""
Meals = ["Eggs", "Milk", "Meat", "Spam", "Butter"]
for item in Meals:
    if item == "Spam":
        nasty_food = item
        break
else:
    print("I'll have a plate of this...")
    # so here we need to run the else condition only once which gets run
    # after break condition

if nasty_food:
    print("Please give me something else!")

# As you can see in case of first example you can just skip and continue
# shopping but in second example you need can have meal with bad things
# so you have to ditch it then and there, that is the difference in
# continue and break

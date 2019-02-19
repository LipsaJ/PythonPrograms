# List are ordered sequences, both dictionary and set are unordered,
# set is unordered so indexes doesnt make sense. Dictionary are key value paired.

fruits = {"Orange": "a sweet sour orange coloured fruit",
          "Lime": "a green coloured sour fruit",
          "Apple": "Keeps doctor away",
          "Lime": "A sour fruit, green in colour",  # so now Lime is value updated as key in the
          # dictionary are unique
          "Pear": "An odd shaped apple"
          }

# As we dont have indexes here we can access it by key
print(fruits)
print(fruits["Lime"])

# In case you want to add something
fruits["Banana"] = "A tasty fruit"
print(fruits)

fruits["Pear"] = "Its amazing with Tequilla"
print(fruits)  # the above line has updated the pear key value

# in case of deletion:
del fruits["Lime"]
print(fruits)

# del fruits  # this deletes everything and throws error
# print(fruits)

# fruits.clear()  # this keeps the empty dictionary but all values are gone
# print(fruits)


# if a key doesnt exist in that case it will throw an error for print(fruits["tomato"]

while True:
    dict_key = input("Please enter the name of your fruit: ")
    if dict_key in fruits:
        desc = fruits.get(dict_key)
        print(desc)
    elif dict_key == "Quit":
        print("Bye Bye!")
        break
    else:
        print("Sorry! We dont have a {}".format(dict_key))

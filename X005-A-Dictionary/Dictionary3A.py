fruits = {"Orange": "A sweet, sour and tasty fruit",
          "Apple": "A red colour fruits, comes in various sizes and colours",
          "Lime": "A green coloured citrus fruits",
          "Lemon": "Small in size and yellow in colour citrus fruit",
          "Pineapple": "Not at all like apple"}

print(fruits)

print("=" * 30)

fruits_keys = fruits.keys()  # this is a view.
print(fruits_keys)
fruits["Tomato"] = "good with Pizzas"  # this updates the fruits_keys as well.
print("=" * 30)
print(fruits_keys)  # this is the only way in which view objects are updated, we can convert them to list and perform
# the operation of add and delete

# another view object - dynamic, that consists of key and tuples

print("=" * 30)
print(fruits)
print(fruits.items())  # this looks very similar to a tuple

# this can change it to tuple
f_tuple = tuple(fruits.items())
print("=" * 30)
print(f_tuple)  # regular tuple

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)  # as you can see its taking key and value from the tuple and printing it

# you can create a dictionary from tuple as well
print("=" * 30)
# in python there are lot of interaction between lists, tuple and dictionary
print(dict(f_tuple))

# joinstring.py
# another string method called joined, strings are immutable so even augmented assignment cant help it
# so join method produces a string from sequences

myList = ["a", "b", "c"]

newString = ', '.join(myList)
print(newString)
print("=" * 30)
letters = "abcdefghijklmnopqrstuvwxyz"  # above its used in list and here its used in strings
newString1 = ', '.join(letters)
print(newString1)
print("=" * 30)
numbers = "123456789"  # above its used in list and here its used in strings
newString2 = ' misissippi '.join(numbers)
print(newString2)

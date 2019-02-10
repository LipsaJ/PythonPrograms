# Tuples are ordered set of data
# Tuples are similar to list but they are immutable, that means cant be changed
# so appending them throws and error
# tuples acn use paranthesis or even without them they are fine, but advised to use for syntactic
# ambiguity.

t = "a", "b", "c"  # this is tuple
print(t)

print("a", "b", "c")
print({"a", "b", "c"})  # this is tuple

fruits = "apple", "banana", "pinapple", 23
veges = "Potatao", "Tomato", 345
meals = "McD", "KFC", 1971

print(fruits)  # print entire tuple
print(fruits[0])  # gives first element

# fruits[2] = "Orange" # it does not support to change like this

# Now, the good thing now is tuples actually support indexing and
# slicing, which is sort of a sneaky way of actually correcting any problems or
# updating particular entries.

meals = meals[0], "Sangam", meals[2]
print(meals)

# Firstly, a type being immutable means that you can't change the contents of an object
# once you've created it.But, it doesn't mean that your variable Can't be assigned
# a new object of that type, so that's an important clarification here.

meal2 = ["BBq", "KFC", 1975, "Biryani"]
print(meal2)
meal2[1] = "McD"
print(meal2)

# Basic difference between list and tuple, list allows to change
# expression on the right side are evaluated first
# so in the tupple example,
# meals = meals[0],"Sangam",meals[2]
# It created the new object and then pointed the vaibale meals toward the new object

# Why tuples??, In case of dictionary it forces to use immutable object
# List even though not mandatory but enforce to use same kind of data type
# Lik a real world list,
# tuples are basically to hold hetrogeneous objects unlike list which is homogeneous
# Mostly fixed items are not changed , for example album, once released the album name never changes

# unpacking the tupple example:
fav_place, ok_ok_place, hungry_since = meals
print(fav_place)
print(ok_ok_place)
print(hungry_since)

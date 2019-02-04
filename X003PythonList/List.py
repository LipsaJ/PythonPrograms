parrot_list = ["Blue", "Green", "Very beautiful", "is annoying"]
parrot_list.append("Red at the beak")

for state in parrot_list:
    print("Parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
# numbers.sort is a method which applies on the object it never creates it
# Below are two ways to sort but look at them carefully

# numbers.sort() #this has changed the actual object
# print(numbers)

# see the difference below if you run print(numbers.sort()),o/p is none

# print(numbers.sort())

print(sorted(numbers))  # this sorted(numbers)) create a new list

sorted_numbers_list = sorted(numbers)

print(sorted_numbers_list == numbers)
print(sorted_numbers_list == sorted(numbers))

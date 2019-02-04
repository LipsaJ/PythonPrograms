# different ways to create a list using constructors
list_1 = []
list_2 = list()

if list_1 == list_2:
    print("They are same!!")

print(list("They are same!!"))
# here as you can see it created list with each character!
# In python iterable is an object which is capable of returning
# values one by one.

even = [2, 4, 6, 8]
another_even = even

another_even.sort(reverse=True)

print(another_even)
print(even)

# Here another_even and even both are pointing to same object.
# thats hwy even is sort in reverse

if another_even is even:
    print("'another_even is even' is true")  # this proves they are same

odd = [1, 3, 5, 7]
another_odd = list(odd)

another_odd.sort(reverse=True)

print(another_odd)
print(odd)

# Here another_even and even both are pointing to same object.
# thats why even is sort in reverse

if another_odd is odd:
    print("'another_odd is odd' is true")  # this proves they are same
else:
    print("No they are not the same!")

# Here another_odd and odd both are pointing to different object.

numbers = (even, odd)
print(numbers) #list contaning two list

for number in numbers:
    print(number)
    for value in number:
        print(value)

# here to iterate through lists inside list
my_list = list(range(10, 20, 2))
print(my_list)

# Now ranges don't support all the operations that you can perform on sequences.
# The reason for that is largely because they represent sequences that follow a defined pattern.
# And so for example the multiplication operator to repeat a range is not allowed,
# nor is concatenation, pending in other words.
# Other than that you can perform all the usual sequence operations or ranges.

# index

My_letters = "abcdefghijklmnopqrstuvwxyz"
print(My_letters.index('e'))
print(My_letters[18])

small_decimals = range(0, 100)
print(small_decimals.index(30))
print(small_decimals[6])
print(small_decimals)

# for num in small_decimals:
#     print(num)

my_range = small_decimals[0:50:3]
print(my_range)

for i in my_range:
    print(i)

print("=" * 20)

for i in range(0, 50, 3):
    print(i)
print(my_range == range(0, 50, 3))

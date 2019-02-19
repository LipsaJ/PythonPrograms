fruits = {"Orange": "A sweet, sour and tasty fruit",
          "Apple": "A red colour fruits, comes in various sizes and colours",
          "Lime": "A green coloured citrus fruits",
          "Lemon": "Small in size and yellow in colour citrus fruit",
          "Pineapple": "Not at all like apple"}

print(fruits)

print("=" * 30)

# desc = fruits.get("BAnana", "We dont have it!")
# print(desc)

del fruits["Lemon"]
print(fruits)

print("=" * 30)

for i in fruits:
    print(i)

print("=" * 30)
# there's more work for python to keep in an order.
# its better to keep the dictionary as it is unordered

# ordered_keys = list(fruits.keys())
# ordered_keys.sort()

# you can use only one line instead of two

# ordered_keys = sorted(list(fruits.keys()))
# for f in ordered_keys:
#    print(f + "-" +fruits[f])

# If list is just used once in that case no need to keep the variable for list instead we can do like this

for f in sorted(fruits.keys()):
    print(f + " - " + fruits[f])

print("=" * 30)

for value in fruits.values():
    print(value)

# the above is less sufficient
print("=" * 30)

for k in fruits:
    print(fruits[k])

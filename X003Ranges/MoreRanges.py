decimal = range(0, 100)
my_range = decimal[3:40:3]
print(my_range)
print(my_range == range(3, 40, 3))
print(range(0, 5, 2) == range(0, 6, 2))
print(decimal[::-10])

decimal_sm = range(0, 10)

for i in decimal_sm[::-2]:
    print(i)

print("==============================")

for i in range(9, 0, -2):
    print(i)

print("=============As you can see both are the same=============")

print(range(0, 10)[::-2] == range(9, 0, -2))

print(range(0, 100, -2))  # this wont publish any thing reason mentioned below

# [::-2] this thing is called slice
# We don't actually get any output from that.
# The reason is because in the negative slice example, --range(0,100,-2)
# a negative step causes a slice to be reversed. --[::-2]
# Now, the same effect is obtained by specifying a negative step in the range, --(9,0,-2)
# But the start and end values must also be reversed,otherwise it doesnt work

backstring = "!etuc yrev si aspiL"
print(backstring[::-1])  # this is very useful you can do backstring and read,
# simple way to process in reverse range


print("----------Challenge-----------")

o = range(0, 100, 4)
print(o)
p = o[::3]
print(p)

for i in p:
    print(i)

# this multiplies these two values 4 * 3 and p actually become (0,100,12)

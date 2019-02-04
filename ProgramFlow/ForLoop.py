for i in range(1, 9):
    print(i)

a = "987,2673,82973,786,2763,92873,009"
for char in range(1, len(a)):
    print(a[char])

for char in range(1, len(a)):
    if a[char] in "0123456789":
        print(a[char], end='')  # this prints in one line
print("\n")
print("Clean number is: ")
cleanNumber = ''
for char in range(1, len(a)):
    if a[char] in "0123456789":
        cleanNumber = cleanNumber + a[char]

print(int(cleanNumber))

# ######################################
# for noe list is just a sequence of thing

for state in ["cute", "Adorable", "Green", "Talkative"]:
    print("Parrot is " + state)

for i in range(0, 10, 2):
    print(i)  # steps, it doesnt take 10 the last value runs till 9

for i in range(1,13):
    print("================Table of {}================".format(i))
    for j in range (1,11):
        print("{} times {} is equal to {}".format(i,j,i*j))


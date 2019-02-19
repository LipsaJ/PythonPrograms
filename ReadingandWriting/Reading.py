jabber = open("sample.txt", "r")  # this is read mode
# jabber = open("C:\\desktop\\sample.txt")
for line in jabber:
    # print(line)
    # this is wat is pythonic
    if "jabberwock" in line.lower():
        print(line, end='')  # stops from printing another line

jabber.close()  # close the file after reading

# ---------------------you need not close the file specifically

with open("sample.txt", "r") as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end="")

# Without using with, if there was an error in reading the file, The with stopping the file may not be closed,
# which, in a especially could mean that it can't be deleted or moved. So programs often have to areas and
# ensure that things like files are closed if an error in fact does occur.Now we're going to be looking at error soon.
# But using width here means that it's not something we need to worry about.
# If there's an error reading from the file, then the width statement will the exception,
# and close the file before the error terminates the program, and that's pretty cool that's handling all that for us.

with open("sample.txt", "r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end="")
        line = jabber.readline()

# the above is like any other programming langauges

with open("sample.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines)

# the above returns a list

for line in lines:
    print(line, end="")

for line in lines[::-1]:
    print(line, end="")

with open("sample.txt", "r") as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end="")

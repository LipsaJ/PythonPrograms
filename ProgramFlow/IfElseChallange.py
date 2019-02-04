name = input("Please tell me your name? ")
age = int(input("Whats your age, {}? ".format(name)))

if 17 < age < 31:
    print("Welcome to the holidays, {}".format(name))
else:
    print("Sorry {}, this is only for cool people".format(name))


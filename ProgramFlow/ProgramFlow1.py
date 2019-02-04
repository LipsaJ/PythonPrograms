name = input("Please tell me your name: ")
age = int(input("Hi {}, What's your age? ".format(name)))
if age > 18:
    print("You are eligible to vote!")
    print("Put an X in Ballot!")
else:
    print("Please wait for {} years!".format(18 - age))

# #################guess a number###################

number = int(input("Guess a number between 1 and 10: "))

if number < 5:
    print("Please enter higher value!")
    number = int(input())
    if number == 5:
        print("Second time lucky!")
    else:
        print("Wrong guess this time as well")
elif number > 5:
    print("Please enter a lower value!")
    number = int(input())
    if number == 5:
        print("Second time lucky!")
    else:
        print("Wrong guess this time as well")
else:
    print("Got it correct in the first time !")

# #################guess six this time###################
# in the above block you can see we are repeating the code
# lets look at in a different way!

guess = int(input("Guess a number between 1 and 10: "))

if guess != 6:
    if guess > 6:
        print("Please guess a lower number!")
    else:
        print("Please guess a higher number!")
    guess = int(input())
    if guess == 6:
        print("Correct guess second time!")
    else:
        print("Sorry! better luck next time")

else:
    print("Correct in first time!!")


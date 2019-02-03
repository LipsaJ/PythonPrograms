# for i in range(10):
#    print("Current value is {}".format(i))
# j = 0
# while j < 10:
#     print("Current value is {}".format(j))
#     j += 1
#
# available_exit = ["East", "West", "South"]
# select_exit = ""
# while select_exit not in available_exit:
#     select_exit = input("Please select a direction: ")
#     if select_exit == "quit":
#         print("Game Over!!!")
#
# else:
#     print("you are out of the loop! now party...")
#
# import random
#
# highest: int = 100
# answer = random.randint(1, highest)
# chance = 0
# print("Guess a number between 1 and {}:".format(highest))
#
# while chance < 4:
#     guess = int(input())
#     if guess == 0:
#         print("Game Over")
#         break
#     elif guess != answer:
#         if guess > answer:
#             print("Insert a lower values")
#         else:
#             print("Insert a higher value")
#     else:
#         print("You got it correct!")
#     chance += 1
    # guess = int(input())
    # if guess != answer:
    #     if guess > answer:
    #         print("Enter a lower number")
    #     else:
    #         print("Enter a higher number")
    #     guess = int(input())
    #     if guess == answer:
    #         print("Its correct this time!!")
    #     else:
    #         print("Better luck next time!!")
    # else:
    #     print("Congratulations you got it correct in the first guess!!")
    #     break
    # chance += 1


value = 8
answer = 0

for x in range (1,13):
    answer = value * x
print("{} times {} is {}".format(x,value,answer))
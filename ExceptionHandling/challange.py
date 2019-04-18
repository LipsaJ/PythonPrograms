import sys


def inp_number(prp_value):
    while True:
        try:
            number = int(input(prp_value))
            return number
        except ValueError:
            print("Invalid number")
        except EOFError:
            print("Exiting!")
            sys.exit(0)
        finally:
            print("The finally clause always execute")


first_n = inp_number("Please enter first value: ")
second_n = inp_number("Please enter second value: ")

try:
    print("{} / {} = {}".format(first_n, second_n, first_n/second_n))
except ZeroDivisionError:
    print("You cannot divide by Zero")
else:
    print("Code successfully run!")  # else only runs when it diesnt get through exception (unlike finally),
    # so its more like if else

# we have two type of errors: syntax error and exceptions

# x = 8 = 5  # this wont run -- sybtax erro as python is able to detect it
x = 8 - 5

# y = x/0 zero division exceptions it comes at runtime


def factorial(n):

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(998))  # this is the last number 998 , 999 onwards it gives RecursionError exception
except RecursionError:
    print("This program can not calculate factorial that large")
except ZeroDivisionError:
    print("Don't do that!")
# we can hanld it in same except as well
# except (RecursionError, ZeroDivisionError):
#     print("Cant calculate because of stupid error!")
print("Program Terminating!!!!!!")

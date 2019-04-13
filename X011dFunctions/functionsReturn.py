def python_food():
    width = 80
    text = "Spams and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# call the function
python_food()

# to create a file with output
# print(centre_text("Spams and eggs"))
# print(centre_text("Spams and eggs and eggs"))
# print(centre_text(12))
# print(centre_text("Spams and spam and spam and eggs"))
# print(centre_text("first", "Second", 3, 4, "V", sep=':'))

s1=centre_text("Spams and eggs")
s2=centre_text("Spams and eggs and eggs")
s3=centre_text(12)
s4=centre_text("Spams and spam and spam and eggs")
s5=centre_text("first", "Second", 3, 4, "V", sep=':')

with open("menu", mode='w') as menu:
    print(s1, file=menu)
    print(s2, file=menu)
    print(s3, file=menu)
    print(s4, file=menu)
    print(s5, file=menu)

def python_food():
    width = 80
    text = "Spams and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' ', end= '\n', file=None, flush=False):
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


# call the function
python_food()

# to create a file with output

with open("centered", mode='w') as centered_file:  # see the first code to check output normally functions code

    centre_text("Spams and eggs", file=centered_file)
    # argument is the value which we pass to function in this example spams and eggs
    centre_text("Spams and eggs and eggs", file=centered_file)  # parameter is general term like text
    centre_text(12, file=centered_file)  # thats why we have added line two in the function we are converting to string
    centre_text("Spams and spam and spam and eggs", file=centered_file)

    centre_text("first", "Second", 3, 4, "V", sep=':', file=centered_file)

def python_food():
    width = 80
    text = "Spams and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
python_food()
centre_text("Spams and eggs")  # argument is the value which we pass to function in this example spams and eggs
centre_text("Spams and eggs and eggs")  # parameter is general term like text
centre_text(12)  # thats why we have added line two in the function we are converting to string
centre_text("Spams and spam and spam and eggs")

print("first", "Second", 3, 4, "V")
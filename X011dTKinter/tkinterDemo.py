import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainwindow = tkinter.Tk()

mainwindow.title("Hello Lipsa")
mainwindow.geometry('400x400+800+400')  # 800 and 400 repesent the widget placement on screen
mainwindow.mainloop()

import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello Liff")
mainWindow.geometry('520x410+20+30')

label = tkinter.Label(mainWindow, text="Hello World!")
label.pack(side='top')

# this is widget
# canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=2)
# canvas.pack(side='left', fill=tkinter.Y)
# # canvas.pack(side='left', fill=tkinter.X, expand='TRUE')   # this expands
# # canvas.pack(side='left', fill=tkinter.Y, expand='TRUE')   # this expands
#
# button1 = tkinter.Button(mainWindow, text='Button')  # tells the direction of buttor
# button2 = tkinter.Button(mainWindow, text='Button')
# button3 = tkinter.Button(mainWindow, text='Button')
#
# button1.pack(side='left', anchor='n')
# button2.pack(side='left', anchor='s')
# button3.pack(side='left', anchor='e')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand='False')

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=2)
canvas.pack(side='left', fill=tkinter.Y)
# canvas.pack(side='left', fill=tkinter.X, expand='TRUE')   # this expands
# canvas.pack(side='left', fill=tkinter.Y, expand='TRUE')   # this expands

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', fill=tkinter.Y, expand='False')

button1 = tkinter.Button(rightFrame, text='Button')  # tells the direction of buttor
button2 = tkinter.Button(rightFrame, text='Button')
button3 = tkinter.Button(rightFrame, text='Button')

# button1.pack(side='left', anchor='n')
# button2.pack(side='left', anchor='s')
# button3.pack(side='left', anchor='e')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
mainWindow.mainloop()

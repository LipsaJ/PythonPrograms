import tkinter


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")


def parabola(a):
    b = a*a / 100
    return b


def plot(page, a, b):
    page.create_line(a, b, a+1, b+1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="pink")
canvas2.grid(row=0, column=1)

draw_axes(canvas)
draw_axes(canvas2)

for x in range(-100, 100):
    y = parabola(x)
    plot(canvas, x, -y)

mainWindow.mainloop()

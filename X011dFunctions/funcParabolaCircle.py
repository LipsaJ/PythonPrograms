import tkinter
import math

def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")


def parabola(page, size):
    for a in range(-size, size):
        b = a * a / size
        plot(page, a, b)


def circle(page, radius, g, h, colour="red"):
    # for x in range(g*100, (g + radius)*100):
    #     x /= 100
    #     y = h + (math.sqrt(radius**2 - ((x-g) **2)))
    #     plot(page, x, y)  # plots 1/4th , one quadrant
    #     plot(page, 2*g-x, 2*h-y)
    #     plot(page, x, 2*h-y)
    #     plot(page, 2*g-x, y)

    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
    # we have this function

    # class functions are called methods thats why page.create_oval method of class canvas


def plot(page, a, b):
    page.create_line(a, -b, a+1, -b+1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)


draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100, "blue")
circle(canvas, 100, 100, -100, "green")

circle(canvas, 200, 60, 30)

mainWindow.mainloop()

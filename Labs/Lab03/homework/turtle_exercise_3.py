import turtle
def draw_square(length, square_color):
    screen_show = turtle.Screen()
    screen_show.title("Turtle Exercises 1")
    drawing_pen = turtle.Turtle()
    drawing_pen.speed(-1)
    drawing_pen.color(square_color)
    for i in range(4):
        drawing_pen.forward(length)
        drawing_pen.left(90)
    screen_show.mainloop()
draw_square(100, "red")

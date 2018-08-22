import turtle
screen_show = turtle.Screen()
screen_show.title("Turtle Exercises 4")
drawing_pen = turtle.Turtle()
drawing_pen.speed(2)

def draw_star(x, y, length):
    drawing_pen.penup()
    drawing_pen.setpos(x, y)
    drawing_pen.pendown()
    for i in range(5):
        drawing_pen.right(144)
        drawing_pen.forward(length)

draw_star(100, 30, 200)

screen_show.mainloop()
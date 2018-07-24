import turtle
screen_show = turtle.Screen()
screen_show.title("Turtle Exercises 4")
drawing_pen_1 = turtle.Turtle()
drawing_pen_1.speed(-1)
drawing_pen_2 = turtle.Turtle()
drawing_pen_2.speed(-1)

def draw_square(length, square_color):
    drawing_pen_2.color(square_color)
    for i in range(4):
        drawing_pen_2.forward(length)
        drawing_pen_2.left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    drawing_pen_1.left(17)
    drawing_pen_1.penup()
    drawing_pen_1.forward(i * 2)
    drawing_pen_1.pendown()

screen_show.mainloop()
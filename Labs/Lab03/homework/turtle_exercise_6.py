import turtle
screen_show = turtle.Screen()
screen_show.title("Turtle Exercises 6")
drawing_pen = turtle.Turtle()
drawing_pen.speed(-1)
drawing_pen.color('blue')

def draw_star(x, y, length):
    drawing_pen.penup()
    drawing_pen.setpos(x, y)
    drawing_pen.pendown()
    for i in range(5):
        drawing_pen.right(144)
        drawing_pen.forward(length)

for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

screen_show.mainloop()
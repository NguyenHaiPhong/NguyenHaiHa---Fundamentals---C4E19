import turtle
screen_show = turtle.Screen()
screen_show.title("Draw a triangle")
exp_1 = turtle.Turtle()
exp_1.color("green","yellow")
exp_1.begin_fill()
for i in range(3):
    exp_1.forward(250)
    exp_1.left(120)
exp_1.end_fill()
screen_show.mainloop()
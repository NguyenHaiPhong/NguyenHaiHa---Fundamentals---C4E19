for i in range(100, 0, -2):
    print(i)
import turtle
screen_show = turtle.Screen()
screen_show.title("Draw a cube")
exp_1 = turtle.Turtle()
exp_1.color("green","yellow")
exp_1.begin_fill()
for i in range(4):
    exp_1.forward(250)
    exp_1.left(90)
exp_1.end_fill()
screen_show.mainloop()
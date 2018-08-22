import turtle
screen_show = turtle.Screen()
screen_show.title("Draw a maze")
exp_1 = turtle.Turtle()
exp_1.speed(-1)
for i in range (0, 500, 3):
    exp_1.forward(i)
    exp_1.left(90)
screen_show.mainloop()    

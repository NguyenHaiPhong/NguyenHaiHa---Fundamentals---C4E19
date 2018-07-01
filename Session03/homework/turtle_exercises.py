import turtle
screen_show = turtle.Screen()
screen_show.title("Turtle Exercises")
exp_1 = turtle.Turtle()
exp_1.speed(-1)
list_color = ["red", "blue", "brown", "yellow", "grey"]
a = int(3)
for index in list_color:
    exp_1.color(index)
    for i in range(len(list_color)):
        for j in range(a):
            exp_1.forward(100)
            exp_1.left(360/a)
    a = a + 1
screen_show.mainloop()

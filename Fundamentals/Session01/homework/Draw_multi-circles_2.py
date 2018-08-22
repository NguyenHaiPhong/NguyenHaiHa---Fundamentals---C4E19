import turtle
print("Enter number of cirles:")
number_of_circles = int(input())
screen_show = turtle.Screen()
screen_show.title("Draw a circle")
exp_1 = turtle.Turtle()
exp_1.color("green","yellow")
exp_1.speed(-1)
for i in range(number_of_circles):
    exp_1.circle(100)
    exp_1.left(13)
screen_show.mainloop()

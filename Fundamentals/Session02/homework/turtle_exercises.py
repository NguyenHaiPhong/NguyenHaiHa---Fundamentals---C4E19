import turtle
number_of_rhombuses = int(input("Enter the number of rhombuses: "))
screen_show = turtle.Screen()
screen_show.title("Turtle Exercises")
exp_1 = turtle.Turtle()
exp_1.color("red")
exp_1.right(25)
exp_1.speed(-1)
for i in range(number_of_rhombuses):
    for j in range(2):
        exp_1.forward(100)
        exp_1.left(50)
        exp_1.forward(100)
        exp_1.left(130)
    exp_1.left(90)
screen_show.mainloop()

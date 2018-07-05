import turtle 
screen_show = turtle.Screen()
screen_show.title("Turtle Exercises")
drawing_pen = turtle.Turtle()
drawing_pen.speed(-1)
drawing_pen.color("blue")
for i in range(40):
    for j in range(4):
        drawing_pen.forward(100)
        drawing_pen.left(90)
    drawing_pen.left(10)    
screen_show.mainloop()
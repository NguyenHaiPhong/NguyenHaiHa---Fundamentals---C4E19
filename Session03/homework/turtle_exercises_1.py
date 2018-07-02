# count = 0
# loop = True

# while loop:
#     print("running...")
#     count += 1
#     if count == 3:
#         # loop = False
#         break
#     print("stop")

# list_color = ["red", "blue", "brown", "yellow", "grey"]
# for index in enumerate(list_color):
#     print(index)

# for item in enumerate(list_color):
#     print(item)
# for index in list_color:
#     print(index)

import turtle
screen_show = turtle.Screen()
screen_show.title("Turtle Exercises")
drawing_pen = turtle.Turtle()
drawing_pen.speed(-1)
length = int(50)
list_color = ["red", "blue", "brown", "yellow", "grey"]
for index in list_color:
    drawing_pen.color(index, index)
    drawing_pen.begin_fill()
    drawing_pen.pendown()
    for j in range(2):
        drawing_pen.forward(50)
        drawing_pen.left(90)
        drawing_pen.forward(100)
        drawing_pen.left(90)       
    drawing_pen.end_fill()
    drawing_pen.penup()
    drawing_pen.forward(length)
screen_show.mainloop()


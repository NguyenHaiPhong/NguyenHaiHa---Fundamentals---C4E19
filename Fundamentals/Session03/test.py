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
exp_1 = turtle.Turtle()
exp_1.speed(-1)
index_in_list = int(0)
length = int(50)
list_color = ["red", "blue", "brown", "yellow", "grey"]
for i in range(len(list_color)):
    for index in list_color:
        exp_1.color(index, index)
        exp_1.begin_fill()
        exp_1.pendown()
        for j in range(2):
            exp_1.forward(length)
            exp_1.left(90)
            exp_1.forward(100)
            exp_1.left(90)       
        exp_1.penup()
        exp_1.end_fill()
    length = length + 50
screen_show.mainloop()


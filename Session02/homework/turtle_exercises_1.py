import turtle
so_canh = int(input(print("Nhap so canh da giac bao trum ngoai cung: ")))
a = int(3)
screen_show = turtle.Screen()
screen_show.title("Turtle Exercises 1")
exp_1 = turtle.Turtle()
exp_1.speed(-1)
for i in range(so_canh):  
    for j in range(a):
        if (a % 2 == 0):
            exp_1.color("red")
        else:
            exp_1.color("blue")
        exp_1.forward(100)
        exp_1.left(360/a)
    a = a + 1
screen_show.mainloop()

from turtle import *
print("Nhap so canh:")
so_canh = int(input())
print("Hinh ve la: ")
shape("turtle")
color("blue")
for i in range(so_canh):
    forward(100)
    left(360/so_canh)
mainloop()

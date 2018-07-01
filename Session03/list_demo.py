# menu = ["Dota 2", "CS: GO", "Doki-Doki"]
# print("Games that i like:")
# print(*menu, sep = ", ")
# print("Name game(s) you  want to add?")
# a = input("")
# menu.append(a)
# print(*menu, sep = ", ")
# print("Games that i like:")
# print("*"*20)
# for index, item in enumerate(menu):
#     print(index + 1, item, sep = ". ")
# print("*"*20)
# position = int(input("Position you want to update? "))
# your_replacing = input("Your replacing: ")
# menu[position - 1] = your_replacing
# print("*"*20)
# print("Games that i like:")
# for index, item in enumerate(menu):
#     print(index + 1, item, sep = ". ")
# print("*"*20)
# list_color = ["red", "blue", "brown", "yellow", "grey"]
# for i in range(4):
#     for index in (list_color):
#         print(index)
# for i in enumerate(list_color):
#     print (i)
# a = list_color.index("red")
# print(a)
# for i in [0, 1, 2, 3]:
#     print(list_color[i])
# for i in list_color:
    # print(i)
# list_length = len(list_color)
# print(list_length)
# list_copy = list_color.copy()
# print(list_copy)
# d = {k: k**2 for k in range(1, 21) if k % 3 == 0}
# print(d)
list_ship_size = [5, 7, 300, 90, 24, 50, 75]
print(list_ship_size)

# list_ship_size = {list_ship_size[i] + 50 for i in range(len(list_ship_size))}
# print(list_ship_size)
# for idx, val in enumerate(list_ship_size):
#     list_ship_size[idx] = val + 50
# print(list_ship_size)
total = sum(list_ship_size)
print(total)
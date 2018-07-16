food1 = "Kem"
food2 = "Xoi"
food3 = "Pho"
food4 = "Thit"
food5 = "Tao Pho"

menu = ["Kem", "Xoi", "Pho", "Thit", "Tao Pho"]
# print(*menu, sep =", ")
# print(len(menu))
# menu.append("Banh my xuc xich 2 trung")
# print(*menu, sep =", ")
# print(len(menu))
# item = menu[2]
# print(item)

# for i in range(len(menu)):
#     print(menu[i])

# for index, item in enumerate(menu):
#     print(index, item)

# for item in menu:
#     print(item)

menu[1] = "Haha"
print(*menu, sep =", ")
# menu.remove("Pho")
# print(*menu, sep =", ")
# menu.clear()
# print(*menu, sep =", ")

pop = menu.pop(1)
print(pop)
print(*menu, sep =", ")

menu.reverse()
print(*menu, sep =", ")

del menu[1]
print(*menu, sep =", ")



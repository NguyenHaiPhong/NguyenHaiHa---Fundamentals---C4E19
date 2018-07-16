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
# list_ship_size = [5, 7, 300, 90, 24, 50, 75]
# print(list_ship_size)

# list_ship_size = {list_ship_size[i] + 50 for i in range(len(list_ship_size))}
# print(list_ship_size)
# for idx, val in enumerate(list_ship_size):
#     list_ship_size[idx] = val + 50
# print(list_ship_size)
# total = sum(list_ship_size)
# print(total)
# guess_word = "champion"
# import random
# list_charater = list(guess_word)
# random_charater = random.choice(list_charater)
# print(random_charater)
# for index in list_charater:
#     print(index)
# print(list_charater)
# a = list_charater[0]
# print(a)
# b = list_charater.upper(0)
# print(b)
# name = input("Enter your name: ")
# list_character = list(name)
# changed_charater = []
# index = 0
# loop_append = True
# loop_change = True
# while loop_append:
#     detect_charater = list_character.pop(index)
#     changed_charater.append(detect_charater)
#     if index == len(list_character):
#         loop_append = False
# print(changed_charater)
# a = "helLo"
# b = list(a)
# c = []
# loop = True
# while loop:
# for i in range(len(b)):
    # d = b.pop(index)
    # if i == 0 and d == " ":
    #     b.remove(d)
    # if index == len(b):
    #     loop = False
    # elif index == 0:
    #     d.upper()
    # elif d == " ":
    #     b[i + 1].upper()
#     else:
#         d.lower()
#     c.append(d)
# print(c)
# for index,item in enumerate(b):
#     d = b.pop(index)
#     if index == 0 and item == " ":
#         b.pop(index)
#     elif index == 0:
#         item.upper()
#     elif item == " " and  item + 1 == " ":
#         b.remove(item)
#     else:
#         item.lower()
#     c.append(d)
# print(b)
# print(c)
# # c = b.pop(0)
# # print(c)
# # d = b.pop(0)
# # print(d)
# e = b[0]
# e = b[2]
# b.remove(e)
# print(b)
# print(e)
# print(b)
# c = b.pop(0)
# print(b)
# print(c)

# name = input("Enter your name: ")
# list_character = list(name)
# changed_character = []
# length_list = len(list_character)
# loop_append = True
# while loop_append:
#     detect_character = list_character[0]
#     if index == len(list_character):
#         loop_append = False
#     elif == 0:
#         detect_character.upper()
#     elif list_character[index] == 0 and list_character[index] == " ":
#         changed_character.pop(index)
#         detect_character.upper(index + 1)
#     elif list_character[index] == " " and list_character[index + 1] == " ":
#         list_character.pop(index)
#     elif list_character[index] == " ":
# 	    list_character[index + 1].upper()
#     else:
#         detect_character.lower()
#     append_character = detect_character   
#     changed_character.append(append_character)

# print("Updated: ", sep = "")
# print(changed_character, sep = "")

# number = int(input("Enter your balance: "))
# print("Your updated balance: ${:0,}".format(number))

# from random_list import image_list_link, description_list
# from random import sample as sp
# for key, value in enumerate(image_list_link):
#     print(key)
#     print(type(key))
#     print(value)
#     print(type(value))
# # a_list = []
# a_list = sp(description_list, 5)
# print(a_list)

session = {}
session["admin log in"] = True
print(session)
a = session["admin log in"]
print(a)
print(type(a))
del session["admin log in"]
print(session)
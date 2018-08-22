# list_words = {
#     "hc": "Học",
#     "ng": "Người",
#     "pt": "Phát triển",
#     "eny": "Em người yêu",
#     "any": "Anh người yêu",
#     "ns": "Nói",
#     "ngta": "Người ta",
# }
# loop = True
# while loop:
#     for key in list_words.keys():
#         print(key, end = "\t")
#     your_code = input("\nYour code? ")
#     print("* "*25)
#     if your_code in list_words:
#         print("Code: ", your_code)
#         print("Translation:", list_words[your_code])
#     else: 
#         answer = input("We don't have that word. Do you want to contribute? (Y/N) ").upper()
#         if answer == "Y":
#             new_word = input("Your code: ")
#             meaning_new_word = input("Meaning: ")
#             list_words[new_word] = meaning_new_word
#             print("Updated")
#             print("* "*25)
#         elif answer == "N":
#             print("You dence motherfucker. !!!!")
#             loop = False
#         else:
#             print("We don't have that kind of action. Please re-enter: ")
# a = input()
# print(a)
from random import choice, sample
from demo import a_list
for i in a_list:
    print(i)
random_list = []
random_list = sample(a_list, 2)
print(random_list)
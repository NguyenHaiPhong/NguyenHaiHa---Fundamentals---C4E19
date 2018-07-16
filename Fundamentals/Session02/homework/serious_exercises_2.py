# number = int(input(print("Enter a number: n = ")))
# product = 1
# for i in range(1, number + 1):
#     product = product * i
# print("The product from 1 to n =",product)
from math import factorial
number = int(input("Enter a number: n = "))
product = factorial(number)
print("The product from 1 to {0} = {1}".format(number, product))

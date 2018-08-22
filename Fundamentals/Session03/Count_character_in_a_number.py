count = 0
loop = True
number = int(input("Enter a number?: "))
second_number = number
while loop:
    number = number // 10
    count += 1
    if (number // 10) == 0:
        count += 1
        loop = False
        break
# print(second_number, "has", count, "digit(s).")
print("{0} has {1} digits".format(second_number, count))
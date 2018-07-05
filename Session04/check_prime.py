number = int(input("Enter a number: "))
# list_1_to_number = []
count = 0
# for i in range(2, number - 1):
#     a = i
#     list_1_to_number.append(a)
#     i= i + 1 
for i in range(2, int(number ** 0.5)):
    if (number % i == 0):
        count += 1
if count == 0:
    print("{0} is a prime".format(number))
else: 
    print("{0} is not a prime".format(number))
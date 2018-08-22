list_number = []
loop = True
print("Enter a list of number. Press E to 'E'nd.")
while loop:
    your_number = input("Enter a number: ")
    if your_number == "E" or your_number == "e":
        loop = False
    elif your_number.isdigit() == True:
        append_number = int(your_number)
        list_number.append(append_number)
    else: 
        print("We don't have that kind of action. Pleas re-enter.")
print("Your list number: ", list_number)

count = 0
find_number = int(input("Enter your number? "))
for var in list_number:
    if var == find_number:
        count += 1
print("{0} appears {1} time(s) in list".format(find_number, count))
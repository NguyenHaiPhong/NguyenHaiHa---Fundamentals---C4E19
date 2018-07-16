# i.
print("The first pattern: 9 x 9 numbers (multiplication table).")
print()
for i in range(1, 10):
    for j in range (1, 10):
        print(i * j, " ", end = " ")
    print()
# ii.
print("The second pattern: Ask user to enter a number n, then print n x n numbers, following multiplication table pattern.")
print()
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    for j in range (1, number + 1):
        print(i * j, " ",end = " ")
    print()
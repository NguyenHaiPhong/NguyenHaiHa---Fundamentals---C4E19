# i.
print("The first pattern: 10 x 10 1’s and 0’s, consecutively.")
a = int(10)
for i in range(0, a):
    for j in range(i + 1, a + 1):
        if (j % 2 == 0):
            print("0", " ", end = " ")
        else: 
            print("1"," ", end = " ")
    print()
    a = a + 1
# ii.
print("The second pattern: Ask users to enter a number n, then print n x n 1’s and 0’s, consecutively.")
b = int(input(print("Enter a nubmer: ")))
for i in range(b):
    for j in range(i + 1, b + 1):
        if (j % 2 == 0):
            print("0", " ", end = " ")
        else: 
            print("1"," ", end = " ")
    print()
    b = b + 1 

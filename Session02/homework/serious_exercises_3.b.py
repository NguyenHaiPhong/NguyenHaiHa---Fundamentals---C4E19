# i.
print("The first pattern: 1’s and 0’s, consecutively.")
for i in range(0, 21):
    if i % 2 == 0:
        print("1", end =" ")
    else: 
        print("0", end =" ")
# ii.
print("\nAsk users to enter a number n, then print n 1’s and 0’s in total consecutively.")
number = int(input("Enter a number: "))
for j in range(0, number):
    if j % 2 == 0:
        print("1", end =" ")
    else: 
        print("0", end =" ")
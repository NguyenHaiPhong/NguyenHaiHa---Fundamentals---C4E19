# i.
print("The first pattern: 9 x 9 numbers (multiplication table).")
print()
a = int(10)
for i in range(1, a):
    for j in range (i + 1, a + 1):
        print(j, "", end = " ")   
        print(i)
    print()
# for i in range(1, 10):
#     print(i, " ", end = "")
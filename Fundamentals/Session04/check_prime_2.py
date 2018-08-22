numb = int(input("Enter a number: "))
is_prime = True
i = 2
while i <= (numb ** 0,5):
    if numb % i == 0:
        is_prime = False
        break
if is_prime:
    print("{0} is a prime".format(numb))
else:
    print("{0} is  not a prime".format(numb))


prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

print("Our stores:")
for what_we_have in prices.keys():
        print(what_we_have)

checking = True
while checking:
    have_fruit = input("What kind of fruits would you like to know? (Press 'E' to 'E'nd) ").lower()
    if have_fruit in prices:
        print(have_fruit)
        print("price:", prices[have_fruit])
        print("stock:", stock[have_fruit])
    elif have_fruit == "e":
        print("Bye.")
        checking = False
    else:
        print("We don't have that kind of action. Please re-enter.")

total = 0
for kind_of_fruit in prices:
    total = total + (prices[kind_of_fruit] * stock[kind_of_fruit])
print("Total: $", total)
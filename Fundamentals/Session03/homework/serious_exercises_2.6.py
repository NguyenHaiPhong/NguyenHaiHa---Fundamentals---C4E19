list_ship_size = [5, 7, 300, 90, 24, 50, 75]
number_of_month = int(input("Enter number of months: "))
money_earned = int(0)
for i in range(number_of_month):
    print("MONTH {0} :".format(i + 1))
    print("Hello, my name is Phong and here is my flock.")
    print(list_ship_size)
    highest = max(list_ship_size)
    print("Now my biggest sheep has size {0} let's share it".format(highest))
    default_size = list_ship_size.index(highest)
    list_ship_size[default_size] = 8
    print("After sheering, here is my flock")
    print(list_ship_size)
    print("One month hass passed, now here is my flock")
    for idx, val in enumerate(list_ship_size):
        list_ship_size[idx] = val + 50
    print(list_ship_size)
    print("-"*50)
total_size = sum(list_ship_size)
money_earned = money_earned + total_size * 2
print("My flock has size in total: {0}".format(total_size))
print("I would get {0}* 2$ = {1}".format(total_size, money_earned))


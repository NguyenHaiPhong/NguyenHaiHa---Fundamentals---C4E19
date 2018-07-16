list_ship_size = [5, 7, 300, 90, 24, 50, 75]
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
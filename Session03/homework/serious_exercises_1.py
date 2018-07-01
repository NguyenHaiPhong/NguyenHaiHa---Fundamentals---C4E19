list_action = ["C: Create", "R: Read", "U: Update", "D: Delete", "E: End"]
list_items = ["T-Shirt", "Sweater"]
print("Menu: ")
list_length = len(list_items)
for index, item in enumerate(list_action):
    print(index + 1, item, sep = ". ")
loop = True
loop_update = True
loop_delete = True
while loop:
    action = input("Welcome to our shop, what do you want to do? (C, R, U, D, E)? (Uppercase and lowercase are allowed) ")
    if action == "R" or action == "r":
        print("Our items:", end = " ") 
        print(*list_items, sep =", ")
    elif action == "C" or action == "c":
        new_item = input("Enter new item: ")
        list_items.append(new_item)
        print("Our items:", end = " ") 
        print(*list_items, sep =", ")
    elif action == "U" or action == "u":
        while loop_update:
            update_position = int(input("Update position? "))
            if (update_position - 1 < 0) or (update_position > list_length):
                print("Your chosen position is incorrect. Please re-enter.")               
            else:
                update_item = input("New item: ")
                list_items[update_position - 1] = update_item
                print("Our items:", end = " ") 
                print(*list_items, sep =", ")
                break
    elif action == "D" or action == "d":
        while loop_delete:
            delete_position = int(input("Delete position? "))
            if (delete_position - 1 < 0) or (delete_position > list_length):
                print("Your chosen position is incorrect. Please re-enter.")
            else:
                delete_item = list_items.pop(delete_position - 1)
                print("Our items:", end = " ") 
                print(*list_items, sep =", ")
                break
    elif action == "E" or action == "e":
        print("Good bye.")
        loop = False
        break
    else:
        print("We don't have that kind of action. Please select one of these action: C, R, U, D, E.")



map = {
    "size_x": 5,
    "size_y": 5
}

player = {
    "x": 3,
    "y": 4
}

boxes = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},
]

destinations = [
    {"x": 2, "y": 1},
    {"x": 3, "y": 2},
    {"x": 4, "y": 3},
]

playing = True
while playing:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False
            if x == player["x"] and y == player["y"]:
                player_is_here = True
            box_is_here = False
            for box in boxes:
                if x == box["x"] and y == box["y"]:
                    box_is_here = True
            dest_is_here = False
            for destination in destinations:
                if x == destination["x"] and y == destination["y"]:
                    dest_is_here = True
            
            if player_is_here:
                print("P ", end = "")
            elif box_is_here:
                print("B ", end = "")
            elif dest_is_here:
                print("D ", end = "")
            else:
                print("- ", end = "")
        print()
    dx = 0
    dy = 0
    move = input("Your move: ").upper()
    if move == "W":
        dy = -1
    elif move == "A":
        dx = -1
    elif move == "S":
        dy = 1
    elif move == "D":
        dx = 1     
    else:
        print("Wrong move sucker. Try again fucker.")
    if (0 <= player["x"] + dx < map["size_x"]) \
    and (0 <= player["y"] + dy < map["size_y"]):
        player["x"] += dx
        player["y"] += dy
    else: 
        print("YOU CAN'T GO THERE")
    for box in boxes:
        if (player["x"] == box["x"]) \
        and (player["y"] == box["y"]):
            box["x"] += dx
            box["y"] += dy
    check_box = 0    
        # for destination in destinations:
        #     if (box["x"] == destination["x"]) and (box["y"] == destination["y"]):
        #         print("Hura")
        #         playing = False
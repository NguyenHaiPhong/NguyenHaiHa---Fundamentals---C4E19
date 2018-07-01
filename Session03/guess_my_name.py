from random import randint
number = randint(0, 100)
loop = True
try_time = 0
while loop == False:
    guess = int(input("Guess my number (1-100)? "))
    if number < guess:
        print("A little too large :(.")
    elif number > guess:
        print("Too small :3.")
    else: 
        print("Bingo :D.")
        loop = False
        break
    try_time += 1
if try_time == 7:
    print("You fucking lose, sucker. xDDD")
    loop = False



    
    
    
print("Guess my number game")
print("Now think of a number from 0 to 100, then press 'Enter'")
input()
loop = True
first = 0
end = 100
print("""
    All you have to do is answer to my guess
    'c' if my guess is 'C'orrect
    "s' if my guess is 'S'maller than your number
    'h' if my guess is 'H'ihger than your number
    'e' if you want to 'E'nd
    """)
while loop:
    middle = (first + end) // 2
    if (end - first <= 2) and (() or ())
        # print("All you have to do is answer to my guess")
        # print("'c' if my guess is 'C'orrect")
        # print("'s' if my guess is 'S'maller than your number")
        # print("'h' if my guess is 'h'ihger than your number")
        # print("E if you want to 'E'nd")
    print("Is {0} your number?".format(middle))
    answer = input()
    if answer == "C" or answer == "c":
        print("I knew it. Ez pz. xD")
        loop = False
    elif answer == "S" or answer == "s":
        end = middle
    elif answer == "H" or answer == "h":
        first = middle
    elif answer == "E" or answer == "e":
        print("I beat your ass. xD")
        loop = False
    else: 
        print("I don't have that. :(")


    
    
  


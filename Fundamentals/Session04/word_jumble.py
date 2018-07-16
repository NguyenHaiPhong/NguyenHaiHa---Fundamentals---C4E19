import random
guess_word = "champion"
list_charater = list(guess_word)
list_length = len(list_charater)
loop_print = True
loop_guess = True
while loop_print:
    if list_length == 0:
        loop = False
    for i in range(list_length):
        random_charater = random.choice(list_charater)
        print(random_charater, end = " ")
        list_charater.remove(random_charater)
answer = input("Your answer: ")
while loop_guess:
    if answer == guess_word:
        print("Hura")
        break
    else:
        print("Too bad: :(")
        break

        

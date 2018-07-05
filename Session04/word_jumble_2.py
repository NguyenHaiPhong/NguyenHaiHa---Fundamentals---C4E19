from random import choice
word = "champion"
list_charater = list(guess_word)
changed_charater = []
loop = True
while loop:
    random_charater = choice(list_charater)
    changed_charater.append(random_charater)
    list_charater.remove(random_charater)
    if len(list_charater) == 0:
        loop = False

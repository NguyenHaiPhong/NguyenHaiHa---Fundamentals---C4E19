your_string = input("Enter your string. Press Enter to finish: ").lower()
remove_blankspace_from_string = your_string.replace(" ","")
letter_counts = {}
storage_letter = {}

for letter in remove_blankspace_from_string:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.items())
letter_items.sort()
storage_letter = dict(letter_items)
for key, value in storage_letter.items():
    print("{0}  {1}".format(key, value))


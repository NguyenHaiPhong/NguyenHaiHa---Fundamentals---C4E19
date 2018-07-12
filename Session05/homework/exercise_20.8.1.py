your_string = input("Enter your string. Press Enter to finish: ").lower()
letter_counts = {}
storage_letter = {}

for letter in your_string:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.items())
letter_items.sort()
del letter_items[0]
storage_letter = dict(letter_items)
for key, value in storage_letter.items():
    print("{0}  {1}".format(key, value))


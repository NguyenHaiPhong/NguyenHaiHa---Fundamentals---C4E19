number_of_pair = 0
list_number_of_pair = []
for month in range(5):
    if month == 0:
        number_of_pair = 1
        list_number_of_pair.append(number_of_pair)
    elif month == 1:
        number_of_pair = 2
        list_number_of_pair.append(number_of_pair)
    else:
        number_of_pair = list_number_of_pair[month - 1] + list_number_of_pair[month - 2]
        list_number_of_pair.append(number_of_pair)
for index, value in enumerate(list_number_of_pair):
    print("Month {0}: {1} pair(s) of rabit".format(index, value))
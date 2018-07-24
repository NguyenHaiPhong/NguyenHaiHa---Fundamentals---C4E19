def get_even_list(l):
    new_list = []
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    new_list = l
    print(new_list)
    return new_list

get_even_list([1, 2, 3, 4, 5, 6, 7, 8, 9])


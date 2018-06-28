chieu_cao = int(input("h = "))
for i in range(chieu_cao):
    for j in range(chieu_cao):
        if (j < chieu_cao - i - 1):
            print("  ", end = "")
        else:
             print("* ", end = "")
    print()
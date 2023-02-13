mylist = [1, 2, 3, 4, 5, 1, 2, 3]

unqlist = []

for i in mylist:
    if i not in unqlist:
        unqlist.append(i)

print(unqlist)

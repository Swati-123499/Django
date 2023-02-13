mylist = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(mylist[0][0])
for i in mylist:
    print(i)
    for j in i:
        print(j)


# another

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        print(mylist[i][j])

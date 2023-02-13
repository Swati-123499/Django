def linearsearch(mylist, val):
    for i in mylist:
        if i == val:
            return True
    return False


mylist = [1, 2, 3, 4, 5]
print(linearsearch(mylist, 6))

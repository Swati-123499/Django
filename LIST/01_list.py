"""
mylist = [4, "a", True]
#mylist = []

# print(mylist)

# indexing

for i in range(len(mylist)):
    print(i, mylist[i])


# iterate
for i in mylist:
    print(i)


# reverse
for i in mylist[::-1]:
    print(i)


# slicing
print(mylist[0:3])

# type of list
mylist = [4, "a", True, 1, "b", "k"]
print(mylist, type(mylist))


mylist = []
print(mylist)

mylist.append(True)
print(mylist)

"""
mylist = []
n = int(input("Enter the size of list:"))
for i in range(n):
    mylist.append(input())
print(mylist)

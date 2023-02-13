string = "abcd"

#print(string, len(string), type(string))

# for i in string:
# print(i)


# for i in range(len(string))
# print(string[i])

# if we start from begining then it willl start with 0 and if we will start from end then it will be -1

for i in range(len(string), -1):
    print(string[i])

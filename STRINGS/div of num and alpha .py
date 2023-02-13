string = "a1b2c3d4e5"

num = " "
alpha = " "
for i in string:
    #print(i, i.isdigit())
    if i.isdigit():
        num += i
    else:
        alpha += i
print(num, alpha)
# string typecasting
number = int(num)
print(type(num), number, type(number))

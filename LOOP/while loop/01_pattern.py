n = int(input())

i = 1
while n > 0:
    print(i)
    i += 1
    n -= 1
    j = i
    while j > 0:
        print("*", end=" ")
        j = -1
    print()
    i += 1
    n -= 1

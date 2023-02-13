

n = int(input())

for i in range(n):
    # upperloop/leftloop
    for j in range(n-i-1):
        print(" ", end=" ")
        # lower/right loop
    for k in range(i+1):
        print("*", end=" ")
    print()

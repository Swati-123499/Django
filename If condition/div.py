n = int(input())

if (n % 3 == 0 and n % 5 == 0):
    print("Both are divisble by 3 and 5")
elif (n % 3 == 0):
    print("divisble by 3")
elif (n % 5 == 0):
    print("Divisble by 5")
else:
    print("both are not divisble by 3 or 5")

n = int(input("Enter a number to check prime number or not: "))
count = 0

for i in range(1, n):
    if n % i == 0:
        count += 1

if (count == 1):
    print("It is a prime number")

else:
    print("It is not a prime")

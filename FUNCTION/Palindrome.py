n = int(input())
temp = n
sum = 0

while n > 0:
    rem = n % 10
    sum = sum*10+rem
    n = int(n/10)

if temp == sum:
    print(f"{sum} is palindrome")
else:
    print(f"{sum} is not a palindrome")

n = int(input())
count = 0

for i in range(1, 100):
    if (n % i == 0):
        count += 1

if (count == 1):
    print(i)

n = int(input())

sum = 0
count = 0
while n > 0:
    rem = n % 10
    sum += rem
    count += 1
    # print(rem)
    n = int(n/10)
print(sum)
print(count)

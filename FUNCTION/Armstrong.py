def findlength(n):
    count = 0
    while n > 0:
        count += 1
        n = int(n/10)
    return count


def findsum(n, length):
    sum = 0
    while n > 0:
        rem = n % 10
        sum += (rem**length)
        n = int(n/10)
    return sum


def isArmstrong(n, sum):
    if n == sum:
        return True
    else:
        return False


def armstrongInCertainRange(_range):
    for i in range(_range):
        n = i
        length = findlength(n)
        sum = findsum(n, length)
        if isArmstrong(n, sum):
            print(i)


_range = int(input())
armstrongInCertainRange(_range)
